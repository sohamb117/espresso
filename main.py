from blake3 import blake3
import json
import time

class Blockchain(object):
	def __init__(self):
		self.chain = []
		self.current_transactions = []
	
	def new_block(self):
		pass
	
	def new_transaction(self):
		pass
    
	@staticmethod
	def hash(block):
		pass

	@property
	def last_block(self):
		pass

class Block:
	def __init(self, index, timestamp, data, previousHash = ''):
		self.index = index;
		self.timestamp = timestamp;
		self.data = data;
		self.previousHash = previousHash;
		self.hash = self.calculateHash();
	
	def calculateHash(self):
		hash = str(self.index + self.previousHash + self.timestamp + self.data + json.dumps(self.data))
		return(blake3(hash).digest())
		
