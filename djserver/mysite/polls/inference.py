from abc import ABC, abstractmethod
from .CKBparser.Conditional import Conditional
from .belief_base import BeliefBase
from time import time_ns


class Inference(ABC):
    belief_base: BeliefBase
    preprocessing_done: bool
   

    def __init__(self, belief_base: BeliefBase)-> None:
        self.belief_base = belief_base
        self.preprocessing_done = False    


    def preprocess_belief_base(self) -> float:
        start_time = time_ns()
        #print("preprocess_belief_base in inference_operator")
        self._preprocess_belief_base()
        self.preprocessing_done = True
        time = (time_ns() - start_time) / 1e+6 # type: ignore
        return time


    def inference(self, query: Conditional) -> bool:

        assert self.belief_base, "belief base needed"

        if not self.preprocessing_done: self.preprocess_belief_base()
        results = self._inference(query)
        return results
   

    @abstractmethod
    def _preprocess_belief_base(self) -> None:
        pass
   

    @abstractmethod
    def _inference(self, query: Conditional) -> bool:
        pass
