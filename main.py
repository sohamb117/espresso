from blockchain import *
from data import *
import json
from flask import Flask, request, jsonify, abort
from shortuuid import uuid

node_uuid = uuid()
app = Flask("Node-"+node_uuid)

espresso = Blockchain();

''' espresso.add_block()
espresso.add_data({"sender":"soham", "recipient": "soham", "amount": "10", "memo": "testing"})
espresso.add_data({"sender":"soham", "recipient": "soham", "amount": "10", "memo": "testing"})
espresso.add_block()
espresso.add_block()
espresso.add_block()
espresso.add_block()
espresso.add_data({"sender":"soham", "recipient": "soham", "amount": "10", "memo": "testing"})
espresso.add_data({"sender":"soham", "recipient": "soham", "amount": "10", "memo": "testing"})
espresso.add_block()
espresso.add_block()
espresso.add_block()
espresso.add_data({"sender":"soham", "recipient": "soham", "amount": "10", "memo": "testing"})
espresso.add_data({"sender":"soham", "recipient": "soham", "amount": "10", "memo": "testing"})
espresso.add_block()
espresso.add_block()
espresso.add_data({"sender":"soham", "recipient": "soham", "amount": "10", "memo": "testing"})
espresso.add_data({"sender":"soham", "recipient": "soham", "amount": "10", "memo": "testing"})
espresso.add_data({"sender":"soham", "recipient": "soham", "amount": "10", "memo": "testing"})
espresso.add_block()
espresso.add_block()
espresso.add_block() '''

@app.route("/mine", methods=["GET"])
def mine():
	block = espresso.add_block()
	return(block)

@app.route("/chaindump", methods=['GET'])
def chaindump():
	return(espresso.get_json())

@app.route("/chain", methods=['GET'])
def chain():
	return(espresso.get_chain())

@app.route("/data", methods=['POST'])
def add_data():
	data = Data(request.json, False)
	if(data.data == None):
		abort(403)

	espresso.add_data(data.getJson())
	return(data.__dict__)
		

@app.route("/transact", methods=['POST'])
def add_transaction():
	data = Data(request.json, True)
	if(data.data == None):
		abort(403)

	espresso.add_data(data.getJson())
	return(data.__dict__)

@app.route("/merge", methods=['POST']) # WIP
def merge():
	chain = Blockchain.gen_chain(request.json)
	if(not chain.check_validity()):
		return("Invalid chain")
	return(chain.get_chain())

for i in espresso.chain:
	print("Index:", i.index)
	print("Time:",i.timestamp)
	print("Data:", str(i.data))
	print("Previous Hash:",i.previous_hash)
	print("Hash:",i.hash)
	print("isSnapshot:",i.isSnapshot)
	print()

print(espresso.check_validity())

app.run(host='0.0.0.0',port=8080)