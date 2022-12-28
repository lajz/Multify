
import cohere
from typing import Union


from multify.models.model import TextCompletionModel

def validate_api_key(func):
    def wrapper():
        if cohere.api_key is None:
            raise ValueError("API key not set")
        func()
    return wrapper

class Cohere():
    
    co = None
    
    @staticmethod
    def setup(api_key):
        Cohere.co = cohere.Client('{api_key}')
    
    class TextCompletion(TextCompletionModel):    
        
        def __init__(self, **kwargs):
            self.model_args = {**kwargs}
            
        @validate_api_key
        def run(self, prompt: str, **kwargs) -> tuple[Union[str, list[str]], tuple[TextCompletionModel, any]]:
            response = Cohere.co.generate(
				prompt=prompt, **self.model_args, **kwargs
			)
            return [generation.text for generation in response.generations], (self, response)