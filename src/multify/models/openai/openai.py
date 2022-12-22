
from multify.models.model import TextCompletionModel

import openai


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
        # TODO: turn engine, model_type into ENUM
        # model_type refers to code generations, text generation, or image generation <-- could alternately implement as subclasses
        def __init__(self, engine: str, model_type: str):
            self.engine = engine
            self.model_type = model_type

        def generate(prompt: str, engine: str, **kwargs):
            completion = openai.Completion.create(prompt=prompt, engine=engine, **kwargs)
            return completion.choices[0].text
