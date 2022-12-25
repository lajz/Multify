
from typing import Union
from multify.models.model import TextCompletionModel, ImageCreationModel

import openai

def validate_api_key(func):
    def wrapper():
        if openai.api_key is None:
            raise ValueError("API key not set")
        func()
    return wrapper

class OpenAI():
    
    @staticmethod
    def setup(api_key, organization = None, api_type = None, api_base = None, api_version = None):
        openai.api_key = api_key
        
        if organization is not None:
            openai.organization = organization
        
        if api_type is not None:
            openai.api_type = api_type
        if api_base is not None:
            openai.api_base = api_base
        if api_version is not None:
            openai.api_version = api_version
    
    def list_engines():
            return openai.Engine.list()
    
    class TextCompletion(TextCompletionModel):    
        
        def __init__(self, model: str, **kwargs):
            self.model_args = {model: model, **kwargs}
            
        @validate_api_key
        def run(self, prompt: str, **kwargs) -> tuple[Union[str, list[str]], tuple[TextCompletionModel, any]]:
            completion = openai.Completion.create(prompt=prompt, **self.model_args, **kwargs)
            return [choice.text for choice in completion.choices], (self, completion)
    
    class ImageCreation(ImageCreationModel):    
        
        def __init__(self, **kwargs):
            self.model_args = {**kwargs}
            
        @validate_api_key
        def run(self, prompt: str, **kwargs) -> tuple[Union[str, list[str]], tuple[ImageCreationModel, any]]:
            completion = openai.Image.create(prompt=prompt, **self.model_args, **kwargs)
            return [image_data.url for image_data in completion.data], (self, completion)
