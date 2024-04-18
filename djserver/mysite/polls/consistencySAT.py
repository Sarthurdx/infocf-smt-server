
import z3
from .CKBparser.Conditional import *


def toImplicit(conditionals):

    """
    accepts a list of conditionals
    returns a list of implications
    """
    return [z3.Implies(i.antecedence, i.consequence) for i in conditionals]




def consistency(ckb):
    conditionals = [i for i in ckb.conditionals.values()]
    #partition is a list of lists
    partition = []
    ### We use the solver here, not the optimizer
    calls = 0
    levels = 0
    while True:
        s = z3.Solver()
        #if no conditionals remain, the ckb is consistent 
        if len(conditionals) == 0:
            #print(calls, levels, [len(i) for i in partition], 'consistent')
            return partition, ([len(p) for p in partition],calls, levels)
        levels +=1
        #print(levels)
        s.push()
        knowledge = toImplicit(conditionals)
        [s.add(k) for k in knowledge]
        R = []
        C = []
        for c in conditionals:
            calls+=1
            if z3.sat ==s.check(c.make_A_then_B()):
                R.append(c)
            else:
                C.append(c)
        if R == []:
            #we found no parition, the ckb is inconsistent
            #Maybe throw an error instead?
            #print(calls, levels, 'False')
            return False, ([len(p) for p in partition], calls, levels)
        partition.append(R)
        conditionals = C
        #reset the solver sothat it wont consider the currently found partition anymore
        s.pop()

def set_core_minimize(s):
    s.set("sat.core.minimize",True)  # For Bit-vector theories
    #s.set("smt.core.minimize",True)  # For general SMT 



class dummyCKB: ...

def inferenceP(ckb, query):
    dummy = dummyCKB()
    dummy.conditionals = {i:c for i,c in ckb.conditionals.items()}
    query_AnotB = Conditional(z3.Not(query.consequence), query.antecedence, None, None)
    dummy.conditionals[0] = query_AnotB
    return 'yes' if (consistency(dummy)[0] == False) else 'no'






"""
from Parser.Wrappers import *
#with open('../../bench/test5.cl') as f:
with open('exp10.cl') as f:
    exp = f.read()

myckb = parseCKB(exp)
part = inferenceP(myckb, myckb.conditionals[1])
"""


