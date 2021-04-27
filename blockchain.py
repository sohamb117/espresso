import time
from block import *
import json

class Blockchain(object):
	def __init__(self):
		self.chain = [self.genesis_block()]
		self.current_data = []
	
	def generate_block(self):
		return Block(
			len(self.chain),
			time.time(),
			self.last_block().hash
		)

	def add_block(self, new_block=None):
		if new_block == None:
			new_block = self.generate_block()
		new_block.index = len(self.chain)
		new_block.data = self.current_data
		new_block.hash = new_block.calculate_hash()
		self.chain.append(new_block)
		self.current_data = []

	def add_data(self, data):
		self.current_data.append(data)

	def genesis_block(self):
		gen_block = Block(0, time.time(), "0")
		gen_block.add_transaction("Genesis", "Genesis", "0", "Genesis Block")
		gen_block.hash = gen_block.calculate_hash()
		return(gen_block)

	def last_block(self):
		return(self.chain[-1])

	def check_validity(self):
		for i in range(1, len(self.chain)):
			current = self.chain[i]
			prev = self.chain[i-1]

			if current.hash != current.calculate_hash():
				return False

			if prev.hash != prev.calculate_hash():
				return False

			if current.previous_hash != prev.hash:
				return False

		return True

	def get_json(obj):
		return json.dumps(obj, default=lambda o: getattr(o, '__dict__', str(o)))
	
	def get_chain(self):
		return json.dumps([obj.__dict__ for obj in self.chain])