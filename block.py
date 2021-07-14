from blake3 import blake3
from data import *
import json

class Block:
	def __init__(self, index, timestamp, previous_hash="", data=[], hash=""):
		self.index = index
		self.timestamp = timestamp
		self.data = data
		self.previous_hash = previous_hash
		self.hash = hash

	def add_transaction(self, sender, recipient, amount, memo=""):
		self.data.append({"sender": sender, "recipient": recipient, "amount": amount, "memo": memo})
		self.hash = self.calculate_hash()

	def calculate_hash(self):
		hash = bytes(str(self.index) + str(self.timestamp) + str(self.previous_hash) + str(self.data), 'utf-8')
		return(blake3(hash).hexdigest())

	def write_block(self):
		filename = "block-"+str(self.index)+".json"
		with open("chain/"+filename, 'w') as f:
			json.dump(self.__dict__, f, indent=2)