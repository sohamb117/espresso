from blockchain import *
import json
from flask import Flask, request
from shortuuid import uuid

node_uuid = uuid()
app = Flask("Node-"+node_uuid)

espresso = Blockchain();

espresso.add_block(espresso.generate_block())
espresso.add_data('{"sender":"soham", "recipient": "soham", "amount": "0", "memo": "testing"}')
espresso.add_data('{"sender":"soham", "recipient": "soham", "amount": "0", "memo": "testing"}')
espresso.add_block(espresso.generate_block())
espresso.add_block(espresso.generate_block())
espresso.add_block(espresso.generate_block())
espresso.add_block(espresso.generate_block())

#@app.route("/mine", method=["GET"])
#def mine():
	

@app.route("/chain", methods=['GET'])
def chain():
	return(espresso)

for i in espresso.chain:
	print("Index:", i.index)
	print("Time:",i.timestamp)
	print("Data:", str(i.data))
	print("Previous Hash:",i.previous_hash)
	print("Hash:",i.hash)
	print()

print(espresso.check_validity())

app.run()