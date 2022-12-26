
from typing import TypeVar, Generic, Callable
from random import choice

from multify.models import Model
from multify.verification import verify_manually

T = TypeVar('T', bound=Model)

class Registry(Generic[T]):
    """
    Registry holds a list of models for runs
    
    Generic type should be a type of Model, such as TextGenerationModel
    """
    
    def __init__(self):
        """__init__ registry"""
        self.models : set[T] = set()

    def register(self, model : T):
        """register add model to registry

        Args:
            model (Model): model to add to registry
        """
        if model in self.models:
            raise ValueError("Model already added.")
        
        self.models.add(model)
    
    def remove(self, model: T) -> bool:
        if model in self.models:
            self.models.remove(model)
            return True
        else:
            return False
        
    # TODO: set typing of parameters and return to be typing of parameters of T.generate
    # TODO: issue is that will not give type hints
    def run(self, model_selector : Callable[[set[T]], T] = None, **kwargs) -> tuple[any, tuple[T, any]]:
        
        model = model_selector(self.models) if model_selector is not None else self.select_model()
        
        # TODO: check that paramater types match
        result : tuple[any, tuple[T, any]] = model.run(**kwargs)
       
        # TODO: make verification optional
        success, info = verify_manually(kwargs, result)
        
        return result
    
    def select_model(self) -> T:
        
        if len(self.models) == 0:
            raise ValueError("No models available")
        
        # TODO: implement
        return choice(list(self.models))
        