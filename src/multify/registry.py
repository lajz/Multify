
from typing import TypeVar, Generic

from multify.models import Model

T = TypeVar('T', bound=Model)

class Registry(Generic[T]):
    """
    Registry holds a list of models for runs
    
    Generic type should be a type of Model, such as TextGenerationModel
    """
    
    def __init__(self):
        """__init__ registry"""
        self.models : list[T] = []

    def register(self, model : T):
        """register add model to registry

        Args:
            model (Model): model to add to registry
        """
        if model not in self.models:
            self.models.append(model)
    
    # TODO: set typing of parameters and return to be typing of parameters of T.generate
    # TODO: issue is that will not give type hints
    def generate(self, **kwargs):
        
        if len(self.models) == 0:
            raise ValueError("No models available")
        
        model = self.select_model()
        
        # TODO: check that paramater types match
        return model.generate(**kwargs)
        
    
    def select_model(self) -> T:
        # TODO: implement
        return self.models[0]
        