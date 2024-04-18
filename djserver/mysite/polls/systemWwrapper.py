
from .system_w_new import SystemW
from .belief_base import BeliefBase


# minimal example of new system w usage (please note that designed to work in color2 - fingers crossed that everything will work)

def inferW(ckb, query):
    ckb_dict = ckb.__dict__
    belief_base = BeliefBase(ckb_dict['signature'], ckb_dict['conditionals'], ckb_dict['name'])
    sysw = SystemW(belief_base)
    result = sysw.inference(query)
    return 'yes' if result else 'no'

