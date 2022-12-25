
from abc import ABCMeta, abstractmethod
from typing import Union


class Model(ABCMeta):
    
    @abstractmethod
    def run(self, **kwargs) -> tuple[any, tuple['Model', any]]:
        pass


# Text model
class TextCompletionModel(Model):
    
    @abstractmethod
    def run(self, prompt: str, **kwargs) -> tuple[Union[str, list[str]], tuple['TextCompletionModel', any]]:
        pass
    
class ImageCreationModel(Model):
    
    @abstractmethod
    def run(self, prompt: str, **kwargs)  -> tuple[Union[str, list[str]], tuple['ImageCreationModel', any]]:
        pass