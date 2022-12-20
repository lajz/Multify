

from .models import Model

registry : list[Model] = []

def register(model : Model):
    if model not in registry:
        registry.append(model)
        