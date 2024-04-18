
import z3


def flatten(l):
    f = []
    [f.extend(i) for i in l]
    #print(f)
    return f


def z_kappa(partition, query):
    k = 0
    s = z3.Solver()
    s.add(query)
    zero = z3.And([(p.make_A_then_not_B() == False) for p in flatten(partition)])
    if s.check(zero) == z3.sat:
        return 0

    while True:
        if len(partition) == 0: ##can this happen? 
            return k
        if len(partition) == 1:
            result = s.check(z3.Or([(p.make_A_then_not_B()==True) for p in flatten(partition)])) 
            if result == z3.unsat:
                print("Always zero?", k)
                return k  ## always 0??
            if result == z3.sat:
                return k+1 
        pointer = len(partition) // 2
        ors_left = z3.Or([p.make_A_then_not_B() == True for p in flatten(partition[:pointer])])
        ands_right = z3.And([(p.make_A_then_not_B() == False) for p in flatten(partition[pointer:])])
        #result = s.check(ands_right)
        result = s.check([ors_left,ands_right])

        if result == z3.sat:
            s.add(ands_right)
            partition = partition[:pointer]
        if result == z3.unsat:
            k = k + len(partition[:pointer])
            partition = partition[pointer:]

def has_lower(partition, query, k):
    #some cheap heuristics first
    if k == 0:
        return False

    s = z3.Solver()
    s.add(query)
    #ors_left = z3.Or([p.make_A_then_Not_B() == True for p in partition[:k]])
    ands_right = z3.And([(p.make_A_then_not_B()) == False for p in flatten(partition[k-1:])])
    s.add(ands_right)
    if s.check() == z3.sat:
        return True
    #if s.check(z3.And([p.make_A_then_Not_B() == False for p in partition])):
    #    return True
    return False


def naiv_system_Z(partition, query):
    s = z3.Solver()
    s.add(query==True)
    zero = z3.And([(p.make_A_then_not_B() == False) for p in flatten(partition)])
    if s.check(zero) == z3.sat:
        return 0

    for k in range(0,len(partition)):
        #print('left:')
        ors_left = z3.Or([(p.make_A_then_not_B() == True) for p in flatten(partition[:k+1])])
        #print('right:')
        ands_right = z3.And([(p.make_A_then_not_B() == False) for p in flatten(partition[k+1:])])
        s.push()
        s.add(ors_left)
        s.add(ands_right)
        if s.check() == z3.sat:
            return k+1
        s.pop()
        #print(k)
    raise ValueError("Something went wrong") ## even possible?

def inference_system_z(partition, query):
    AB = query.make_A_then_B()
    AnotB = query.make_A_then_not_B()
    kab = naiv_system_Z(partition, AB)
    kanotb = naiv_system_Z(partition, AnotB)
    return kab < kanotb


import math

def logsum_objectives(obj):
    w=obj[0].value().as_long()
    #print([o.value().as_long() for o in obj])
    if w == 0:
        return 0
    return math.floor(math.log2(w))+1

def weighted_z(partition, formula):
    opt = z3.Optimize()
    opt.add(formula)
    obj =[]
    for w,part in enumerate(partition):
        constraint = (z3.Not(z3.Or([(p.make_A_then_not_B()) for p in part])))
        #constraint = z3.And(([z3.Not(p.make_A_then_not_B()) for p in part]))
        obj.append(opt.add_soft(constraint,weight=2**w))
    opt.check()
    #print(opt.objectives())
    return logsum_objectives(obj)

def zWeightedOpimizer(partition):
    opt = z3.Optimize()
    obj =[]
    for w,part in enumerate(partition):
        constraint = (z3.Not(z3.Or([(p.make_A_then_not_B()) for p in part])))
        #constraint = z3.And(([z3.Not(p.make_A_then_not_B()) for p in part]))
        obj.append(opt.add_soft(constraint,weight=2**w))
    #print(opt.objectives())
    return opt,obj

def indicator_z(partition, formula):
    opt = z3.Optimize()
    opt.add(formula)
    rank = z3.Int('r')
    opt.add(z3.Int('r')>=0)
    obj =[]
    for w,part in enumerate(partition):
        constraint = z3.Implies(z3.Or([p.make_A_then_not_B() for p in part]),rank>=2**w)
        opt.add(constraint)
        #constraint = z3.And(([z3.Not(p.make_A_then_not_B()) for p in part]))
    obj=opt.minimize(rank)
    opt.check()
    #print(opt.objectives())
    return logsum_objectives([obj])

def zIndicatorOptimizer(partition):
    opt = z3.Optimize()
    rank = z3.Int('r')
    opt.add(z3.Int('r')>=0)
    obj =[]
    for w,part in enumerate(partition):
        constraint = z3.Implies(z3.Or([p.make_A_then_not_B() for p in part]),rank>=2**w)
        opt.add(constraint)
        #constraint = z3.And(([z3.Not(p.make_A_then_not_B()) for p in part]))
    obj=opt.minimize(rank)
    #print(opt.objectives())
    return opt,obj
        
    
def zIndicatorLinear(partition):
    opt = z3.Optimize()
    rank = z3.Int('r')
    opt.add(z3.Int('r')>=0)
    obj =[]
    for w,part in enumerate(partition):
        constraint = z3.Implies(z3.Or([p.make_A_then_not_B() for p in part]),rank>=1+w)
        opt.add(constraint)
        #constraint = z3.And(([z3.Not(p.make_A_then_not_B()) for p in part]))
    obj=opt.minimize(rank)
    #print(opt.objectives())
    return opt,obj






from .consistencySAT import consistency
def inferZ(ckb, query):
    partition, _ = consistency(ckb)
    opt,obj = zIndicatorOptimizer(partition)
    AB = query.make_A_then_B()
    AnB = query.make_A_then_B()
    opt.check(AB)
    ab = obj.value().as_long()
    opt.check(AnB)
    aNb = obj.value().as_long()
    return 'yes' if ab < aNb else 'no'





def z_kappa_on_world(ckb, bitvector,formula):
    partition, _ = consistency(ckb)
    var = [z3.Bool(v) for v in ckb.signature]
    conf = [True if b == '1' else False for b in bitvector]
    conf = bitvector
    world = [v == c for v,c  in zip(var,conf)]
    s=z3.Solver()
    s.add(world)
    s.add(formula)
    if s.check()!=z3.sat:
        return -1
    m = s.model()
    for level in range(len(partition)-1,-1, -1):
        for c in partition[level]:
            if m.eval(c.make_A_then_not_B()):
                return level + 1
    return 0



def evalPartition(ckb, bitvector):
    partition, _ = consistency(ckb)
    var = [z3.Bool(v) for v in ckb.signature]
    conf = [True if b == '1' else False for b in bitvector]
    world = [v == c for v,c  in zip(var,conf)]
    s=z3.Solver()
    s.add(world)
    s.check()
    m = s.model()
    for level in (partition):
        vals = [m.eval(c.make_A_then_not_B()) for c in level]
        print(vals)

