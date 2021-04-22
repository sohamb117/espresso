import time
from block import *

class Blockchain(object):
	def __init__(self):
		self.chain = [self.genesis_block()]
		self.current_transactions = []
	
	def generate_block(self):
		return Block(
			len(self.chain),
			time.time(),
			self.last_block().hash
		)

	def add_block(self, new_block):
		new_block.index = len(self.chain)
		new_block.hash = new_block.calculate_hash()
		self.chain.append(new_block)

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