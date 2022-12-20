
from abc import ABCMeta, abstractmethod

class Model(ABCMeta):
    
    @abstractmethod
    def generate(prompt: str):
        pass
    