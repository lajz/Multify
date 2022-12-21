

from multify.models import Model

class Registry:
    """Registry holds a list of models for runs"""
    
    def __init__(self):
        """__init__ registry"""
        self.models : list[Model] = []

    def register(self, model : Model):
        """register add model to registry

        Args:
            model (Model): model to add to registry
        """
        if model not in self.models:
            self.models.append(model)
        