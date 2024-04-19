from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render

from .forms import NameForm

import sys
#sys.path.append("/home/chroom/Documents/InfOCF-Lib2/src/infocf/CKBparser/")
#sys.path.append("/home/chroom/Documents/InfOCF-Lib2/src/infocf/Queryparser/")
#sys.path.append("/home/chroom/Documents/InfOCF-Lib2/src/infocf/")
from . import demo
from . import kappa
import z3

from dataclasses import dataclass
from . import consistencySAT
from .compute_indmin import compute_indmin
from .system_Z import inferZ
from .systemWwrapper import inferW


@dataclass
class Result:
    query1:str 
    query2:str 
    mode:str 
    crep_cw:str = '-'
    crep_sum:str = '-'
    crep_ind:str = '-'
    crep_all:str = '-'
    mi:str = 'unbounded'


@dataclass
class SystemsResults:
    P: '-'
    Z: '-'
    W: '-'


@dataclass
class CW:
    length: int
    minima: list[int]


def makeResult(query1, query2, query, mode, kappas,mi):
    yesno ={True:'Yes', False:'No'}
    creps = kappas.keys()
    crep_cw:str = yesno[kappas['CREP_CW'].infer(query,mode)] if 'CREP_CW' in creps  else'-'
    crep_sum:str = yesno[kappas['CREP_SUM'].infer(query,mode)] if 'CREP_SUM' in creps  else'-'
    crep_ind:str = yesno[kappas['CREP_IND'].infer(query,mode)] if 'CREP_IND' in creps  else'-'
    crep_all:str = yesno[kappas['CREP_ALL'].infer(query,mode)] if 'CREP_ALL' in creps  else'-'
    result = Result(query1, query2, mode,crep_cw, crep_sum, crep_ind, crep_all, mi)
    return result
    

def makeMI(mi, nr, n):
    if mi == 0:
        return 'unbounded'
    s = {1:n, 2:2**n, 3:nr}
    return s[mi]


def index(request):
    return render(request, 'InfOCF.html')

def partition(request):
    if request.method == 'GET':
        knowledgebase = request.GET.get("knowledgebase")
        ckb = demo.parseCKB(knowledgebase)
        part, _ = consistencySAT.consistency(ckb)
        return render(request, 'partition.html', {"part":part})

def evalSystems(ckb, query, systems):
    p = consistencySAT.inferenceP(ckb,query) if ('SYSTEM_P' in systems) else '-'

    z = inferZ(ckb, query) if ('SYSTEM_Z' in systems) else '-'
    
    w = inferW(ckb, query) if ('SYSTEM_W' in systems) else '-'

    return SystemsResults(p,z,w)


def inference(request):
    # if this is a POST request we need to process the form data
    print(request.method)
    if request.method == 'GET':
        knowledgebase = request.GET.get("knowledgebase")
        crep = request.GET.get("knowledgebase")
        query2=request.GET.get("query2")
        query1=request.GET.get("query1")
        mode=request.GET.get("mode")
        mode=mode.split(';')
        crep=request.GET.get("crep")
        crep=crep.split(';')
        maximpact = int(request.GET.get("maximalimpact"))
        maximpactnr = int(request.GET.get("maximalimpactnr"))
        systems = request.GET.get("system").split(';')
        query =demo.parseQuery( f'({query1}|{query2})' )[1]
        ckb = demo.parseCKB(knowledgebase)
        mi = makeMI(maximpact, maximpactnr, len(ckb.conditionals))
        ckb.compile_constraint_test()
        print('compiled')
        base_csp = ckb.translate_experimental()
        if mi != 'unbounded':
            [base_csp.append(z3.Int(f'eta_{i}') <= mi) for i in ckb.conditionals.keys()]
        kappas = {c:kappa.makeKappa(c, base_csp, ckb) for c in crep}
        print('made kappas')
        #crep_all = demo.evaluateQueries(knowledgebase,query)
        result = [makeResult(query1, query2, query, m, kappas, mi) for m in mode]
        print('results made')
        sysResults = evalSystems(ckb, query, systems)
        return render(request, 'name.html', {'results':result, 'system':sysResults})


def cw(request):
    z3.set_param("opt.elim_01", "false")
    # if this is a POST request we need to process the form data
    if request.method == 'GET':
        knowledgebase = request.GET.get("knowledgebase")
        model = request.GET.get("modelkind")
        maximalimpact = int(request.GET.get("maximalimpact"))
        maximalimpactnr = int(request.GET.get("maximalimpactnr"))
        if model == "SYSTEM_Z":
            result = CW(1, [['dummy']])
            return render(request, 'cw.html', {'cw':result})
        crep_cw = demo.evaluateCKB(knowledgebase)
        mi = makeMI(maximalimpact, maximalimpactnr, len(crep_cw[0]))

        if model == "CREP_SUM":
            minima = min(sum(i) for i in crep_cw)
            crep_cw = [i for i in crep_cw if sum(i) == minima]
        if model == "CREP_IND":
            crep_cw = compute_indmin(crep_cw)
        if mi != 'unbounded':
            crep_cw = [i for i in crep_cw if (all((j <= mi) for j in i))]
        result = CW(len(crep_cw), crep_cw)
        return render(request, 'cw.html', {'cw':result})

def consistency(request):
    if request.method == 'GET':
        knowledgebase = request.GET.get("knowledgebase")
        try:
            ckb = demo.parseCKB(knowledgebase)
            part, _ = consistencySAT.consistency(ckb)
            if part == False:
                raise ValueError("CKB inconsistent")
        except ValueError as ve:
            return str(ve)

        return render(request,'consistency.html',{})
