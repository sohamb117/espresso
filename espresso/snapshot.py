from espresso.block import *
import json

class Snapshot(Block):
	def summarize(self, blockdata):
		final = len(blockdata) - 1
		if(final < 0):
			return;
		while(final > 0 and not blockdata[final].isSnapshot):
			final -= 1;

		blockdata = blockdata[(final):]
		datadict = {};

		for block in blockdata:
			for datapoint in block.data:
				if("sender" in datapoint.keys() and "recipient" in datapoint.keys() and "amount" in datapoint.keys()):
					sender = datapoint["sender"];
					recipient = datapoint["recipient"];
					amount = int(datapoint["amount"]);
					if(sender in datadict.keys()):
						datadict[sender] -= amount;
					else:
						datadict[sender] = 0 - amount;
					if(recipient in datadict.keys()):
						datadict[recipient] += amount;
					else:
						datadict[recipient] = amount;

		self.data = datadict;
		self.isSnapshot = True;
		self.hash = self.calculate_hash()