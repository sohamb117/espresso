from espresso import app, espresso
from espresso.data import *
from flask import request, abort

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