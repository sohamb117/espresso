import json
from blake3 import blake3


class Data():
	def __init__(self, content: dict, isTransaction: bool):
		if(content["hash"]!=None and content["key"]!=None):
			self.data = content
			self.data["transaction"] = isTransaction
		else:
			self.data = None
			self.data["transaction"] = isTransaction
	
	def validate(self):
		pass

	def getJson(self):
		return(self.data)