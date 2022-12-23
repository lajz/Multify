
from abc import ABCMeta, abstractmethod

class Model(ABCMeta):
    
    @abstractmethod
    def run(self, **kwargs):
        pass


# Text model
class TextCompletionModel(Model):
    
    @abstractmethod
    def run(self, prompt: str, **kwargs):
        pass
    
class ImageCreationModel(Model):
    
    @abstractmethod
    def run(self, prompt: str, **kwargs):
        pass