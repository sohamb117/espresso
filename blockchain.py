import time
from block import *
from data import *
from snapshot import *
import json

class Blockchain(object):

	def gen_chain(chain):
		blockchain = Blockchain()
		blockchain.chain = []
		for i in chain["chain"]:
			blockchain.chain.append(Block(**i));
		return blockchain

	def __init__(self):
		self.chain = []
		self.genesis_block()
		self.current_data = []
	
	def generate_block(self):
		return Block(
			len(self.chain),
			time.time(),
			self.last_block().hash if len(self.chain)>0 else 0
		)

	def add_snapshot(self):
		block = Snapshot(len(self.chain), time.time(), self.last_block().hash)
		block.summarize(self.chain)
		block.index = len(self.chain)
		self.chain.append(block)
		return(block.__dict__)


	def add_block(self):
		block = self.generate_block()
		block.add_data(self.current_data)
		print(self.current_data)
		block.write_block()
		self.chain.append(block)
		self.current_data = [];
		if(len(self.chain) > 0 and len(self.chain)%10 == 0):
			self.add_snapshot()
		return(block.__dict__)

	def genesis_block(self):
		block = self.generate_block()
		block.add_transaction("Genesis", "Genesis", "0", "Genesis Block")
		block.write_block()
		self.chain.append(block)
		return(block.__dict__)

	def add_data(self, data):
		self.current_data.append(data)

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