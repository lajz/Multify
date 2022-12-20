

from .models import Model

registry : list[Model] = []

def register(model : Model):
    registry.append(model)