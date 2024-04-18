
from time import time_ns as time
from z3 import *
from antlr4 import *

from .CKBparser.CKBLexer import CKBLexer
from .CKBparser.CKBParser import CKBParser
from .CKBparser.CKBVisitor import CKBVisitor
from .CKBparser.CKB import CKB,makeOptimizer
from .CKBparser.Conditional import Conditional
from .CKBparser.myVisitor import myVisitor

from .Queryparser.QUERYLexer import QUERYLexer
from .Queryparser.QUERYParser import QUERYParser
from .Queryparser.QUERYVisitor import QUERYVisitor
from .Queryparser.myQueryVisitor import myQueryVisitor

import multiprocessing
#from parallelCompiler import compileParallel
import sys
from collections import namedtuple
import pickle

#from mop_solver import solve


Result = namedtuple(
        'Result',
        ['name', 'conditionals', 'signature', 'minima', 'compiletime', 'solvetime']
        )



mymax = []
### i'm sure there's a built in method to do this, will find out later
def bench_function(f):
    t1 = time()
    result = f()
    t2 = time()
    return result, (t2-t1)/1000/1000/1000


def find_cw_min(solver, etas):
    i = 0
    cw =[]
    while z3.sat == solver.check():
        i +=1
        m1 = solver.model()
        
        cw.append([(m1.eval(Int('eta_%i'%i))).as_long() for i in range(1,etas+1)])
        #cw.append([(m1.eval(Int('eta_%i'%j))) for j in range(1,etas+1)])
        #print(cw[-1])
    #print(i)
    return cw


def parseCKB(ckbs_string, ):
    stream = InputStream(ckbs_string)
    lexer = CKBLexer(stream)
    stream = CommonTokenStream(lexer)
    parser = CKBParser(stream)
    visitor = myVisitor()
    ckbs = visitor.visit(parser.ckbs())
    ckb = list(ckbs.values())[0]
    return ckb

        



def parseQuery(querystring):
    stream = InputStream(querystring)
    lexer = QUERYLexer(stream)
    stream = CommonTokenStream(lexer)
    parser = QUERYParser(stream)
    visitor = myQueryVisitor()
    query = visitor.visit(parser.query())
    #print(query)
    return query



def evaluateQueries(ckbs_string, query_string):

    #print(ckbs_string)
    #parse the ckb
    #with open(filename) as f:
        #ckbs_string = f.read() 
    stream = InputStream(ckbs_string)
    lexer = CKBLexer(stream)
    stream = CommonTokenStream(lexer)
    parser = CKBParser(stream)
    visitor = myVisitor()
    ckbs = visitor.visit(parser.ckbs())
    #print(list(ckbs.items())[0])
    #print(ckbs)
    #print(ckbs.items())
    # assume ckb names are equal to filename
    #name = os.path.basename(filename).split('.')[0]
    #name = "abcd"
    ckb = list(ckbs.values())[0]
    queries = parseQuery(query_string)
    _, compile_time = bench_function(lambda : ckb.compile_constraint_test())
    base_csp = ckb.translate_experimental()
    #base_csp = ckb.translate()
    #solver = z3.Solver()
    solver = makeOptimizer()
    #z3.set_param(verbose=2)
    solver.add(base_csp)
    #[solver.add(z3.Int('eta_%i' % i) <= 2**len(ckb.conditionals)) for i in range(1, len(ckb.conditionals)+1)]
    #[solver.add(z3.Int('eta_%i' % i) <= len(ckb.conditionals)) for i in range(1, len(ckb.conditionals)+1)]
    #[solver.add(z3.Int('eta_%i' % i) <= 4) for i in range(1, len(ckb.conditionals)+1)]
    #o2 = [solver.minimize(z3.Int('eta_%i' % i)) for i in range(1, len(ckb.conditionals)+1)]
    #print(base_csp)
    results = []
    #print("base-compilation-time", compile_time)
    etas = len(ckb.conditionals)
    #cw, time = bench_function(lambda: find_cw_min(solver, etas))
    #return cw
    #print(queries)
    for _,q in queries.items():
        query_csp, compilation_time = bench_function(lambda : ckb.compile_and_encode_query(q))
        solver.push()
        solver.add(query_csp)
        solution, solve_time = bench_function(lambda : solver.check())
        solver.pop()
        results.append("no" if solution == z3.sat else "yes" if solution == z3.unsat else "unknown")
        #results.append({'query':str(q), 'solution': solution, 'seconds': solve_time})
        #print(solution, solve_time)
    #print(results)
    return results[0]



def evaluateCKB(ckbs_string):

    #print(ckbs_string)
    ckb = parseCKB(ckbs_string)
    #print(len(ckb.conditionals))
    #print(ckb)
    _, compile_time = bench_function(lambda : ckb.compile_constraint_test())
    print(compile_time)
    base_csp = ckb.translate_experimental()
    solver = makeOptimizer()
    #solver.set(priority='box')
    #solver.set(priority='lex')
    solver.add(base_csp)
    [solver.add(z3.Int('eta_%i' % i) < 2**(len(ckb.conditionals))) for i in range(1, len(ckb.conditionals)+1)]
    #solver.add(z3.Sum([Int('eta_%i' % i) for i in range(1, len(ckb.conditionals)+1)]) <= 2**len(ckb.conditionals))

    #o1 = [solver.minimize(z3.Int('mf_%i' % i)) for i in range(1, len(ckb.conditionals)+1)]
    #o2 = [solver.minimize(z3.Int('mv_%i' % i)) for i in range(1, len(ckb.conditionals)+1)]
    #o3 = [solver.minimize(z3.Int('mv_%i' % i)+z3.Int('mf_%i'%i)) for i in range(1, len(ckb.conditionals)+1)]
    #o3 = [solver.minimize(z3.Int('mv_%i' % i)+z3.Int('mf_%i'%i)) for i in range(1, len(ckb.conditionals)+1)]
    #o3 = [solver.minimize(z3.Int('mv_%i' % i)+z3.Int('mf_%i'%i) + z3.Int('s_%i'%i)) for i in range(1, len(ckb.conditionals)+1)]
    #z3.set_param(verbose=1000)
    #z3.set_param('parallel.enable', True)
    #z3.set_param('smt.arith.solver', 3)
    o3 = [solver.minimize(z3.Int('eta_%i' % i)) for i in range(1, len(ckb.conditionals)+1)]
    #o3 = [solver.minimize(z3.Int('s_%i' % i)) for i in range(1, len(ckb.conditionals)+1)]


    results = []
    etas = len(ckb.conditionals)
    #z3.set_param(verbose=3)
    cw, time = bench_function(lambda: find_cw_min(solver, etas))
    #print(solver.statistics())
    print(time)
    return cw




def evaluateCSP(ckb, base_csp):

    solver = makeOptimizer()
    solver.add(base_csp)
    [solver.add(z3.Int('eta_%i' % i) <= 2**(len(ckb.conditionals))) for i in range(1, len(ckb.conditionals)+1)]
    o3 = [solver.minimize(z3.Int('eta_%i' % i)) for i in range(1, len(ckb.conditionals)+1)]
    results = []
    etas = len(ckb.conditionals)
    #z3.set_param(verbose=10)
    cw, time = bench_function(lambda: find_cw_min(solver, etas))
    return cw



def benchCKB(ckbs_string, j, i):

    #print(ckbs_string)
    ckb = parseCKB(ckbs_string)
    _, compile_time = bench_function(lambda : ckb.compile_constraint_test())
    #print(compile_time)
    base_csp = ckb.translate_experimental()
    solver = makeOptimizer()
    #solver.set(priority='box')
    #solver.set(priority='lex')
    solver.add(base_csp)
    [solver.add(z3.Int('eta_%i' % i) < 2**(len(ckb.conditionals))) for i in range(1, len(ckb.conditionals)+1)]
    #solver.add(z3.Sum([Int('eta_%i' % i) for i in range(1, len(ckb.conditionals)+1)]) <= 2**len(ckb.conditionals))

    #o1 = [solver.minimize(z3.Int('mf_%i' % i)) for i in range(1, len(ckb.conditionals)+1)]
    #o2 = [solver.minimize(z3.Int('mv_%i' % i)) for i in range(1, len(ckb.conditionals)+1)]
    #o3 = [solver.minimize(z3.Int('mv_%i' % i)+z3.Int('mf_%i'%i)) for i in range(1, len(ckb.conditionals)+1)]
    #o3 = [solver.minimize(z3.Int('mv_%i' % i)+z3.Int('mf_%i'%i)) for i in range(1, len(ckb.conditionals)+1)]
    #o3 = [solver.minimize(z3.Int('mv_%i' % i)+z3.Int('mf_%i'%i) + z3.Int('s_%i'%i)) for i in range(1, len(ckb.conditionals)+1)]
    #z3.set_param('parallel.enable', True)
    #z3.set_param('smt.arith.solver', 3)
    o3 = [solver.minimize(z3.Int('eta_%i' % i)) for i in range(1, len(ckb.conditionals)+1)]
    #o3 = [solver.minimize(z3.Int('s_%i' % i)) for i in range(1, len(ckb.conditionals)+1)]


    results = []
    etas = len(ckb.conditionals)
    #z3.set_param(verbose=3)
    cw, solve_time = bench_function(lambda: find_cw_min(solver, etas))

    results =Result(ckb.name, len(ckb.conditionals), len(ckb.signature), len(cw), compile_time, solve_time)
    with open('results_%i_%i.pickle'%(j,i), 'wb') as f:
            pickle.dump(results, f)
    print(results)
    return results



if __name__ == "__main__":
    res = []
    for j in [4,6,8,10,12,14,20,30,40,50,60,70,80,90,100]:
        for i in range(0,10):
            tester = '../../bench/bases/randomTest_%i_%i.cl' %(j,i)

            #tester = "../../bench/test25cwMinima.cl"
            #tester = "../../bench/birds.cl"
            #tester = "../../bench/abcd.cl"
            #tester = "../../bench/thirdRandomTest%i.cl" % (i)
            #tester =  "../../bench/randomTest%i.cl" %i
            #tester =  "../../bench/test100.cl"
            
            with open(tester) as f:
                ckbs_string = f.read()
            #print(ckbs_string)
            p = multiprocessing.Process(target=benchCKB, name='bench', args=(ckbs_string,j,i))
            p.start()
            p.join(30 * 60)
            p.terminate()
            #r  = benchCKB(ckbs_string) #, "(a|b), (c|d)")
            #r  = benchCKB(ckbs_string) #, "(a|b), (c|d)")
            #print(tester, ':', t)
