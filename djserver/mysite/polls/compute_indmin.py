
import z3

def make_kappa(ckb, etas):
    impact = [z3.If(c.make_A_then_not_B(), etas[i-1], 0) for i,c in ckb.conditionals.items()]
    return z3.Sum(impact)


def isSmaller(k1,k2):
    s=z3.Solver()
    s.add(k1>k2)
    return s.check() == z3.unsat


def compute_indmin(ckb, etas_lists):
    kappas = [make_kappa(ckb, e) for e in etas_lists]
    #indmins = []
    ignore = set()
    for i,k1 in enumerate(kappas):
        for j,k2 in enumerate(kappas):
            if i == j or (i in ignore) or (j in ignore):
                continue
            if isSmaller(k1,k2):
                #if (isSmaller(k2,k1)):
                #    print(f'{i} == {j} happend')
                #    continue
                ignore.add(j)
    return [e for i,e in enumerate(etas_lists) if (i not in ignore)]


    
