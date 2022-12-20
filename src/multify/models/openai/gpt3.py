
import openai

from .. import Model

class GPT3(Model):
	
	# TODO: enforce singleton
	def __init__(self, api_key, organization = None):
		openai.api_key = api_key
		openai.organization = organization
		
	