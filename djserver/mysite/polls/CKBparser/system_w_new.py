from inference import Inference
from belief_base import BeliefBase
from Parser.Conditional import Conditional
from consistencySAT import consistency
from warnings import warn
from z3 import z3, unsat, sat, Not, Or, And, Bool, is_true
import copy


def makeOptimizer():
    opt = z3.Optimize()
    opt.set(priority='pareto')

    #z3.set_param(verbose=1)
    return opt

class SystemW(Inference):
    _partition: list | bool 



    def _preprocess_belief_base(self) -> None:
        partition, _ = consistency(self.belief_base)
        if not partition: warn('belief base inconsistent')
        self._partition = partition


    def _inference(self, query: Conditional) -> bool:
         
        assert type(self._partition) == list, "Knowledge base is inconsistent."
        #print('\n\n') 
        #print(f"query {query}")
        #print(f'partition {self._partition}')
        opt = makeOptimizer()
        return self._rec_inference(opt, len(self._partition) -1, query)
        

    def _rec_inference(self, opt, partition_index, query):
        #print(f"\nrec inf called: {partition_index}, {query}")
        #print('objectives')
        assert type(self._partition) == list
        part = self._partition[partition_index]
        opt.push()
        opt.add(query.make_A_then_B())
        xi_i_set = get_all_xi_i(opt, part)
        opt.pop()
        opt.push()
        opt.add(query.make_A_then_not_B())
        xi_i_prime_set = get_all_xi_i(opt, part)
        opt.pop()
        #print(f"xi_i_set {xi_i_set}")
        #print(f"xi_i_prime_set {xi_i_prime_set}")
        if not any_subset_of_all(xi_i_set, xi_i_prime_set):
            return False
        for xi_i in xi_i_set & xi_i_prime_set:
            #print(f"set in instersection: {xi_i}")
            if partition_index == 0:
                return False
            opt.push()
            [opt.add(c.make_A_then_not_B()) for c in xi_i]
            [opt.add(c.make_A_then_not_B() == False) for c in part if c not in xi_i]
            result = self._rec_inference(opt, partition_index -1, query)
            opt.pop()
            if result == False:
                return False
        return True

# Function to extract 
def get_all_xi_i(opt, part: list[Conditional]):
    #print("get_all_xi_i called")

    xi_i_set = set() 
    for conditional in part:
        opt.add_soft(conditional.make_A_then_not_B() == False)
    while True:
        if opt.check() == unsat:
           return xi_i_set
        m = opt.model()
        xi_i = frozenset([c for c in part if is_true(m.eval(c.make_A_then_not_B()))])
        xi_i_set.add(xi_i)
        if xi_i == frozenset(): 
            return xi_i_set
        opt.add(Or([c.make_A_then_not_B() == False for c in xi_i]))
 
def any_subset_of_all(A, B):
    return all(any(a.issubset(b) for a in A) for b in B)

