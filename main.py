from blockchain import *

espresso = Blockchain();

espresso.add_block(espresso.generate_block())
espresso.add_block(espresso.generate_block())
espresso.add_block(espresso.generate_block())
espresso.add_block(espresso.generate_block())
espresso.add_block(espresso.generate_block())

for i in espresso.chain:
	print("Index:", i.index)
	print("Time:",i.timestamp)
	print("Data:",i.data)
	print("Previous Hash:",i.previous_hash)
	print("Hash:",i.hash)
	print()

print(espresso.check_validity())