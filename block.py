from blake3 import blake3
import json

class Block:
	def __init__(self, index, timestamp, data, previous_hash=""):
		self.index = index
		self.timestamp = timestamp
		self.data = data
		self.previous_hash = previous_hash
		self.hash = ""
	
	def calculate_hash(self):
		hash = bytes(str(self.index) + str(self.timestamp) + str(self.previous_hash) + self.data, 'utf-8')
		return(blake3(hash).digest())