import z3
z3.set_param("opt.elim_01", "false")
from . import demo
from .compute_indmin import compute_indmin





class Kappa:

    def __init__(self, etas_list, ckb):
        self.etas_list=etas_list
        self.conditionals=ckb.conditionals
        self.ckb = ckb
        self.k0= 0


    def rank_world(self, model):
        s = self.k0 +z3.Sum([z3.If(self.conditionals[c].make_A_then_not_B(), e,0) for c,e in enumerate(self.eta_list, start=1)])

        return model.eval(s,model_completion=True)


    def conditional_rank(self, cond):
        opt = z3.Optimize()
        opt.add(cond.make_A_then_B())
        s=opt.minimize(z3.Sum([z3.If(self.conditionals[c].make_A_then_not_B(), e,0) for c,e in enumerate(self.eta_list, start=1)]))
        opt.check()
        v = s.value()

        opt = z3.Optimize()
        opt.add(cond.make_A_then_not_B())
        s=opt.minimize(z3.Sum([z3.If(self.conditionals[c].make_A_then_not_B(), e,0) for c,e in enumerate(self.eta_list, start=1)]))
        opt.check()
        f = s.value()
        return v,f


    def min_world(self, cond):
        opt = z3.Optimize()
        opt.add(cond.make_A_then_B())
        s=opt.minimize(z3.Sum([z3.If(self.conditionals[c].make_A_then_not_B(), e,0) for c,e in enumerate(self.eta_list, start=1)]))
        s.check()
        return s.model()


    def rank_from_logits(self, logits):
        return min([z3.Sum([e*l for e,l in zip(etas,logits)]) for etas in self.etas_list])

        

    def prepare_rank_formula(self, formula):
        opt = z3.Optimize()
        opt.set(priority='pareto')
        obj = {i:opt.add_soft(c.make_A_then_not_B()==False, id=i) for i,c in self.conditionals.items()}
        opt.add(formula)
        ranks=[]
        while opt.check() ==z3.sat:
            m =opt.model()
            ranks.append([v.value().as_long() for i,v in obj.items()])
        return (ranks)

    def rank_formula(self, formula):
        ranks = self.prepare_rank_formula(formula)
        ''' the i-th element of ssums will contain the rank belonging to the i-th eta in self.etas_list '''
        ssums = []
        for etas in self.etas_list:
            temp =[]
            for rank in ranks:
                temp.append(sum([e*r for e,r in zip(etas, rank)]))
            #print(temp)
            ssums.append(min(temp))
        return ssums



    def rank_conditional(self, conditional):
        v =self.rank_formula(conditional.make_A_then_B())
        f =self.rank_formula(conditional.make_A_then_not_B())
        return v,f


    def infer(self, conditional, mode):

        v,f = self.rank_conditional(conditional)
        print(v,f)
        #raise ValueError(v,f)
        #print(v,f)
        s=z3.Solver()
        if mode == 'SKEPTICAL':
            return all((s.check(i < j) == z3.sat) for i,j in zip(v,f))

        if mode == 'CREDULOUS':
            return any((s.check(i < j)==z3.sat) for i,j in zip(v,f))

        if mode == 'WEAKLY_SKEPTICAL':
            return any((s.check(i < j)==z3.sat) for i,j in zip(v,f)) and not any((s.check(i < j)==z3.sat) for i,j in zip(f,v))





class KappaAll:

    def __init__(self, base_csp, ckb):
        self.base_csp = base_csp
        self.ckb = ckb

    def infer(self, conditional, mode):
        s = z3.Solver()
        s.add(self.base_csp)

        if mode == 'SKEPTICAL':
            query = self.ckb.compile_and_encode_query(conditional)
            return s.check(query) == z3.unsat

        if mode == 'CREDULOUS':
            query = self.ckb.compile_and_encode_query_credulous(conditional)
            return s.check(query) == z3.sat

        if mode == 'WEAKLY_SKEPTICAL':
            query = self.ckb.compile_and_encode_query_credulous(conditional)
            if s.check(query) == z3.sat:
                query = self.ckb.compile_translate_query_finegrained(conditional.antecedence, conditional.consequence)
                return s.check(query) == z3.unsat
            return False


def makeKappa(mode, base_csp, ckb):
    if mode == 'CREP_ALL':
        return KappaAll(base_csp, ckb)
    if mode == 'CREP_CW':
        etas = demo.evaluateCSP(ckb, base_csp)
        return Kappa(etas, ckb)
    if mode == 'CREP_SUM':
        etas = demo.evaluateCSP(ckb, base_csp)
        minima = min([sum(i) for i in etas])
        etas = [i for i in etas if sum(i) == minima]
        return Kappa(etas, ckb)
    if mode == 'CREP_IND':
        etas = demo.evaluateCSP(ckb, base_csp)
        minima = compute_indmin(ckb, etas)
        return Kappa(minima, ckb)
