from Parser.CKB import *
from pysat.examples.rc2 import RC2
from pysat.formula import WCNF, IDPool 



"""
Inherits from CKB and implements compilation and inference using maxsat RC2. 
Overwrites compile_constraint and compile_and_encode_query.
Usage identical to CKB exept that makeCNFs has to be called before compile_constraint or 
compile_and_encode_query can be called.
"""
class CKB_RC2(CKB):
    def __init__(self, signature: list[str], conditionals: dict[int, Conditional], name: str) -> None:
        super().__init__(signature, conditionals, name)
        self.pool = IDPool()
        self.ABs = {}
        self.AnotBs = {}
        self.notAorBs = {}

    
    """
    Uses z3's logical operators, tseitin transformation and local helper methods to fill the dicts 
    self.ABs, self.AnotBs and self.notAorBs with int/id CNFs equivalent to the name-giving logical 
    operations applied to the conditionals in self.conditionals at the same dict index

    Context:
        This method has to be called before compile_constraint or compile_and_encode_query can be 
        called since both of these methods depend on the dicts of CNFs being filled

    Returns:
        Execution time in ms
    """
    def makeCNFs(self) -> float:
        start_time = time_ns()
        t = Tactic('tseitin-cnf')
        
        for index, conditional in self.conditionals.items():
            g1 = t(And(conditional.antecedence, conditional.consequence))
            g2 = t(And(conditional.antecedence, Not(conditional.consequence)))
            g3 = t(Or(Not(conditional.antecedence), conditional.consequence))
            self.ABs[index] = self.goal2intcnf(g1[0])
            self.AnotBs[index] = self.goal2intcnf(g2[0])
            self.notAorBs[index] = self.goal2intcnf(g3[0])
        return (time_ns() - start_time) / (1e+6) 
    

    """
    Takes z3 goal in CNF and turns it to CNF of ints. The absolute values of those ints 
    function as unique IDs of the z3 expressions in the goal.

    Context:
        Helper function called by makeCNFs and compile_and_encode_query.

    Parameters: 
        z3 goal as CNF

    Returns:
        CNF of ints (which are signed IDs of z3 expressions in goal)
    """
    def goal2intcnf(self, goal: z3.Goal) -> list[list[int]]:
        cnf = []
        for expr in goal:
            if is_or(expr):
                cnf.append([self.expr_to_signed_id(x) for x in expr.children()])
            else:
                cnf.append([self.expr_to_signed_id(expr)])
        return cnf
    

    """
    Takes z3 expression and creates or retrieves unique ID of expression using pysat.formula.IDPool
    and signs it (with a minus or nothing) depending on whether the expression is negated by being 
    wrappend in a "Not()"

    Context:
        Helper function called by goal2intcnf 

    Parameters: 
        z3 expression

    Returns:
        int serving as signed ID of input expression
    """
    def expr_to_signed_id(self, expr: ExprRef) -> int:
        sign = 1
        if is_not(expr):
            sign = -1
            expr = expr.children()[0]
        expr_id = self.pool.id(expr)
        return sign * expr_id


    """
    Compiles KB by filling the dicts vMin and fMin with lists of lists of ints. Each inner list 
    corresponds to a possible world while the ints represent indices in notAorBs of unsatisfied CNFs. 
    The index of vMin/fMin equals the index of the CNF in ABs/notABs that has been used as a hard
    constrain before checking what CNFs in notAorBs can be satisfied in different possible worlds.

    Context:
        This Method is called to compile a KB based on conditionals in self.conditionals

    Returns:
        Execution time in ms
    """
    def compile_constraint(self) -> float:
        start_time = time_ns() / (1e+6)

        for leading_conditional in [self.ABs, self.AnotBs]:
            for i, conditional in leading_conditional.items():
                xMins = []
                wcnf = WCNF()
                [wcnf.append(c) for c in conditional]
                [wcnf.append(s, weight=1) for j, softc in self.notAorBs.items() if i != j for s in softc]
                
                with RC2(wcnf) as rc2:
                    while True:
                        model = rc2.compute()
                        
                        if model == None:
                            break
                        
                        cost = rc2.cost
                        
                        violated = self.get_violated_conditional(model, cost, i)
                        
                        if not violated:
                            xMins.append(violated)
                            break
                        
                        xMins.append(violated)
                        clauses_to_add = self.exclude_violated(violated)

                        [rc2.add_clause(clause) for clause in clauses_to_add]
                
                xMins_lst = remove_supersets(xMins)

                if leading_conditional is self.ABs:
                    self.vMin[i] = xMins_lst
                else: 
                    self.fMin[i] = xMins_lst

        return (time_ns()/(1e+6))-start_time
    

    """
    Compiles query using RC2 and encodes it using minima_encoding.

    Context:
        This method is used to query the KB and do actual inference.

    Parameters:
        The Query in form of a conditional

    Returns:
        Constraint satisfaction problem that can be fed into the z3 solver;
        Execution time
    """
    def compile_and_encode_query(self, query: Conditional) -> tuple[list[z3.BoolRef], float]:
        start_time = time_ns() / 1e+6
        t = Tactic("tseitin-cnf")
        AB = self.goal2intcnf(t(And(query.antecedence, query.consequence))[0])
        AnotB = self.goal2intcnf(t(And(query.antecedence, Not(query.consequence)))[0])
        vMin, fMin = [], []
        
        for conditional in [AB, AnotB]:
            xMins = []
            wcnf = WCNF()
            [wcnf.append(c) for c in conditional]
            [wcnf.append(s, weight=1) for j, softc in self.notAorBs.items() for s in softc]
            
            with RC2(wcnf) as rc2:
                while True:
                    model = rc2.compute()
                    
                    if model == None:
                        break
                    
                    cost = rc2.cost
                    
                    violated = self.get_violated_conditional(model, cost, 0)
                    
                    if not violated:
                        xMins.append(violated)
                        break
                    
                    xMins.append(violated)
                    clauses_to_add = self.exclude_violated(violated)

                    [rc2.add_clause(clause) for clause in clauses_to_add]
            
            xMins_lst = remove_supersets(xMins)
            if conditional is AB:
                vMin = xMins_lst
            else: 
                fMin = xMins_lst

        vSum = self.makeSummation({0:vMin})
        fSum = self.makeSummation({0:fMin})
        mv, mf = self.freshVars(0)
        vM = self.minima_encoding(mv, vSum[0])
        fM = self.minima_encoding(mf, fSum[0])
        csp = vM + fM + [mv >= mf]
        return csp ,(time_ns()/(1e+6)-start_time)

    
    """
    Takes model and returns all IDs of CNFs in notAorBs (i.e. Not(A, Not(B))) that are not satisfied 
    by the model

    Context:
        Helper function called by compile_constraint and compile_and_encode_query

    Parameters:
        RC2 model; cost of the model; ID of CNF in notAorBs to be ignored (important to implement 
        the 'i!=j, AB[i]/notAB[i], notAorB[j]' requirement in compile_constraint)

    Returns:
        Set of IDs
    """
    def get_violated_conditional(self, model: list[int], cost: int, ignore: int) -> set[int]:
        violated = set()
        if cost > 0:
            counter = 0
            for index, conditional in self.notAorBs.items():
                if index == ignore:
                    continue
                for clause in conditional:
                    if not any(x in clause for x in model):
                        counter += 1
                        violated.add(index)
                    if counter == cost:
                        return violated
        return violated

    """
    Takes indices of violated CNFs and creates new CNF that can be added as hard constraint to the 
    solver. Based on the idea of restraining the solver from violating the same conjuction of CNFs 
    again.

    Context:
        Helper function called by compile_constraint in order to add new hard constraint to solver
        and make solver solve for different possible world

    Parameters:
        set of indices of unsatisfied CNFs in notAorBs

    Returns:
        int CNF equivalent to disjunction of all CNFs referred to by input indices
    """ 
    def exclude_violated(self, violated: set[int]) -> list[list[int]]:
        return_constraints = []
        helper_variables_clause = []

        for index in violated:
            id = self.pool.id(index)
            for clause in self.notAorBs[index]:
                new_clause = clause[:]
                new_clause.append(id * (-1))
                return_constraints.append(new_clause)
        
            helper_variables_clause.append(id)
        return_constraints.append(helper_variables_clause)
        return return_constraints


"""
Removes supersets and converts sets to lists

Context:
    Helper function called by compile_constraint 

Parameters:
    list of sets (some sets might be supersets of other sets)

Returns:
    lists of lists (none of the inner lists will be a superset of other inner list)
"""
def remove_supersets(lst_of_sets: list[set[int]]) -> list[list[int]]:
    lst_of_sets = sorted(lst_of_sets, key=len)
    filtered = []

    for a in lst_of_sets:
        is_superset = False
        for b in filtered:
            if b.issubset(a):
                is_superset = True
                break
        if not is_superset:
            filtered.append(a)

    return [list(s) for s in filtered]
