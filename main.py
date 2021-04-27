from blockchain import *
import json
from flask import Flask, request, jsonify, Response
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

@app.route("/mine", methods=["GET"])
def mine():
	espresso.add_block()
	return("Generated block")
	

@app.route("/chaindump", methods=['GET'])
def chaindump():
	return(espresso.get_json())

@app.route("/chain", methods=['GET'])
def chain():
	return(espresso.get_chain())

@app.route("/data", methods=['POST'])
def add_data():
	try:
		request.json["key"]
		request.json["hash"]
		espresso.add_data(request.json)
	except:
		return(Response(jsonify("Please provide a key and hash"), 403))

	return(request.json)
		

@app.route("/transact", methods=['POST'])
def add_transaction():
	try:
		memo = request.json["memo"]
	except:
		memo = ""
	transaction = {
		"sender": request.json["sender"],
		"recipient": request.json["recipient"],
		"amount": request.json["amount"],
		"memo": memo
		}
	espresso.add_data(transaction)
	return(transaction)

for i in espresso.chain:
	print("Index:", i.index)
	print("Time:",i.timestamp)
	print("Data:", str(i.data))
	print("Previous Hash:",i.previous_hash)
	print("Hash:",i.hash)
	print()

print(espresso.check_validity())

app.run(host='0.0.0.0',port=8080)