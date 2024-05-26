from z3 import *
from time import time as time
from .Conditional import *



def makeOptimizer():
    opt = z3.Optimize()
    opt.set(priority='pareto')
    opt.set(elim_01= False)
    opt.add_soft(BoolVal(True),id=-1)
    opt.add_soft(BoolVal(True),id=-2)
    opt.add_soft(BoolVal(True),id=-3)

    #z3.set_param(verbose=1)
    return opt


def makeAB(conditional):
    """
    actually makes A(not B), can't think of a better name for now
    """
    return And(conditional.antecedence, Not(conditional.consequence))



def simplyfy(d):
    return [a for a,b in d.items() if b==1]



class CKB:
    """
    currently only supports strong conditionals
    several functionalities currently exist as multiple implementation within this class.
    The inferior one, that uses if-then-then encoding, will moved somewhere else some day.
    """

    def __init__(self, signature, conditionals, name):
        self.signature=signature
        self.conditionals=conditionals
        self.name = name
        self.eta = dict()
        self.vMin = dict()
        self.fMin = dict()






    #replaces every items in the argument by it's sum representation
    def makeSummation(self,minima):
        results=dict()
        for index, summ in minima.items():
            interim= []
            for subsum in summ:
                if subsum is None:
                    interim.append(0)
                    print('its none')
                    continue
                interim.append(Sum([Int('eta_%i' %i) for i in subsum]))
            results[index] = interim
        #print(results)
        return results



    def freshVars(self,i):
        return Int('mv_%i' %i), Int('mf_%i'%i)




    def minima_encoding(self,mv, ssums):
        ands = [(mv <= i)  for i in ssums]
        ors = z3.Not(z3.And([mv < i for i in ssums]))
        ands.append(ors)
        #print(ands)
        return ands


    def encoding(self, etas, vSums, fSums):
        csp = []
        for index, eta in etas.items():
            mv, mf = self.freshVars(index)
            vMin = self.minima_encoding(mv, vSums[index])
            fMin = self.minima_encoding(mf, fSums[index])
            csp.extend(vMin)
            csp.extend(fMin)
            csp.append(eta  >mv - mf )

        return csp



    def translate_experimental(self):
        """
        takes the compiled database from fmin and vmin and translates it into CR(R) in z3.
        uses inequality - encoding.
        """
        eta = {i:z3.Int('eta_%i' % i) for i,_ in enumerate(self.conditionals, start =1)}
        gteZeros = [e >= 0 for e in eta.values()]
        vSums = self.makeSummation(self.vMin)
        fSums = self.makeSummation(self.fMin)
        csp = self.encoding(eta, vSums, fSums)
        csp.extend(gteZeros)
        #[print(i) for i in csp]
        return csp

    """
    def translate(self):
        #takes the compiled database from fmin and vmin and translates it into CR(R) in z3.
        #uses if-then-else encoding.
        eta = {i:z3.Int('eta_%i' % i) for i,_ in enumerate(self.conditionals, start =1)}
        gteZeros = [e >= 0 for e in eta.values()]
        vSums = self.makeSummation(self.vMin)
        fSums = self.makeSummation(self.fMin)
        vMins = self.makeMinima(vSums)
        fMins = self.makeMinima(fSums)
        csp = [neta  > (vMins[index] - fMins[index]) for index, neta in eta.items()]
        csp.extend(gteZeros)
        return csp
    """

    """
    ## this method uses the assumption stack, is roughly 1% faster
    def compile_constraint_tt(self):
        opt = makeOptimizer()
        objectives = {j:opt.add_soft(makeAB(c) == False, id=j) for j,c in self.conditionals.items()}    #setting id's for easier bookkeeping
        V,F = dict(), dict()
        for i,c in enumerate(self.conditionals, start=1):
            t1 = time()
            cond = self.conditionals[i]
            antecedence = cond.antecedence
            consequence = cond.consequence
            opt.push()
            opt.add(antecedence)
            vMin, fMin = [], []
            opt.push() 
            while opt.check() == sat:
                if z3.solve(opt.model().evaluate(consequence==True)) is None:
                    vMin.append(simplyfy({j:k.value() for j,k in objectives.items() if i != j}))
                if z3.solve(opt.model().evaluate(consequence==False)) is not None:
                    fMin.append(simplyfy({j:k.value() for j,k in objectives.items() if i != j}))
            opt.pop()
            opt.pop()
            t2 = time()
            V[i] = vMin
            F[i]= fMin
        self.vMin, self.fMin = V,F
        return V,F
    """

    



    def compile_constraint_test(self):

        """
        because the constraint for the falsifying case is almost the same as for the verifying case,
        this method uses the assumption stack, which is roughly 1% faster than not using the assumption stack
        """
        opt = makeOptimizer()
        objectives = {j:opt.add_soft(makeAB(c) == False, id=j) for j,c in self.conditionals.items()}    #setting id's for easier bookkeeping
        V,F = dict(), dict()
        

        for i,c in enumerate(self.conditionals, start=1):
            t1 = time()
            cond = self.conditionals[i]
            antecedence = cond.antecedence
            consequence = cond.consequence
            opt.push()
            opt.add(antecedence)
            vMin, fMin = [], []
            opt.push() 
            opt.add(consequence)
            while opt.check() == sat:
                vMin.append(simplyfy({j:k.value() for j,k in objectives.items() if i!=j}))

            opt.pop()
            opt.add(Not(consequence))
            while opt.check() == sat:
                fMin.append(simplyfy({j:k.value() for j,k in objectives.items() if i!=j}))
            opt.pop()
            V[i] = vMin
            F[i]= fMin
        self.vMin, self.fMin = V,F
        return V,F



    def compile_and_translate_query(self, query):
        """
        uses if-then-else encoding to encode the query. Slower than the inequality encoding.

        """
        opt = makeOptimizer()
        objectives = {j:opt.add_soft(makeAB(c) == False, id=j) for j,c in self.conditionals.items()}    #setting id's for easier bookkeeping
        antecedence = query.antecedence
        consequence = query.consequence
        opt.push()
        opt.add(antecedence)
        opt.push() 
        opt.add(consequence)
        vMin, fMin = [], []
        while opt.check() == sat:
            vMin.append(simplyfy({j:k.value() for j,k in objectives.items()}))
        opt.pop()
        opt.add(Not(consequence))
        while opt.check() == sat:
            fMin.append(simplyfy({j:k.value() for j,k in objectives.items()}))
        vSum = self.makeSummation({0:vMin})
        fSum = self.makeSummation({0:fMin})
        v,f = self.freshVars(0)
        vM = self.minima_encoding(v,vSum[0])
        fM = self.minima_encoding(f,fSum[0])
        csp = vM >= fM 
        return csp

    def compile_translate_query_finegrained(self, antecedence, consequence):
        return self.compile_and_encode_query_credulous(Conditional(antecedence,consequence, "", False))


    def compile_and_encode_query(self, query):
        """
        uses inequality encoding to encode the query. 
        """
        opt = makeOptimizer()
        objectives = {j:opt.add_soft(makeAB(c) == False, id=j) for j,c in self.conditionals.items()}    #setting id's for easier bookkeeping
        antecedence = query.antecedence
        consequence = query.consequence
        opt.push()
        opt.add(antecedence)
        opt.push() 
        opt.add(consequence)
        vMin, fMin = [], []
        while opt.check() == sat:
            vMin.append(simplyfy({j:k.value() for j,k in objectives.items()}))
        opt.pop()
        opt.add(Not(consequence))
        while opt.check() == sat:
            fMin.append(simplyfy({j:k.value() for j,k in objectives.items()}))
        vSum = self.makeSummation({0:vMin})
        fSum = self.makeSummation({0:fMin})
        v, f = self.freshVars(0)
        vM = self.minima_encoding(v, vSum[0])
        fM = self.minima_encoding(f, fSum[0])
        csp = vM + fM + [mv >= mf]
        #print(len(csp))
        return csp


    def compile_and_encode_query_credulous(self, query):
        """
        uses inequality encoding to encode the query. 
        """
        opt = makeOptimizer()
        objectives = {j:opt.add_soft(makeAB(c) == False, id=j) for j,c in self.conditionals.items()}    #setting id's for easier bookkeeping
        antecedence = query.antecedence
        consequence = query.consequence
        opt.push()
        opt.add(antecedence)
        opt.push() 
        opt.add(consequence)
        vMin, fMin = [], []
        while opt.check() == sat:
            vMin.append(simplyfy({j:k.value() for j,k in objectives.items()}))
        opt.pop()
        opt.add(Not(consequence))
        while opt.check() == sat:
            fMin.append(simplyfy({j:k.value() for j,k in objectives.items()}))
        vSum = self.makeSummation({0:vMin})
        fSum = self.makeSummation({0:fMin})
        v, f = self.freshVars(0)
        vM = self.minima_encoding(v, vSum[0])
        fM = self.minima_encoding(f, fSum[0])
        csp = vM + fM + [mv < mf]
        #print(len(csp))
        return csp




