
from abc import ABCMeta, abstractmethod

class Model(ABCMeta):
    
    @abstractmethod
    def generate(self, **kwargs):
        pass


# Text model
class TextCompletionModel(Model):
    
    @abstractmethod
    def generate(self, prompt: str, **kwargs):
        pass