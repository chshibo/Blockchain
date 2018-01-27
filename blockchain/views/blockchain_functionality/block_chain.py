"""
class Blockchain

Created by Shibo Chen, Data:1/26/2018
University of Michigan, class of 2019
email: chshibo@umich.edu
"""

import hashlib
import base64
import blockchain
from .block import Block
from .transaction import Transaction

class Blockchain(object):
	"""Blockchain class"""
	def __init__(self, difficulty=1):
		"""
		Initialize the chain and set the difficulty

		Parameters
		----------
		difficulty : int (default : 1)
			difficulty of calculating blocks
		"""

	@staticmethod
	def hash(block):
		"""
		Hash a block
		
		Parameters
		----------
		block : Block
			the block to hash

		Returns
		-------
		hash_str : String
			the hex digest of the sha256 hash of block
		"""
		block_str = block.__str__()
		block_base64 = base64.b64encode(block_str.encode())
		hash_obj = hashlib.sha256(block_base64)
		return hash_obj.hexdigest()	
	
	@staticmethod
	def get_block(index=-1):
		"""
		Get the block at index
		
		Parameters
		----------
		index : Int (default = -1 (the last block))
			The index where the block located

		Returns
		-------
		block: Block
			The block at index
		"""
		conn = blockchain.model.get_db()
		cur = conn.cursor()
		block = Block()
		if index == -1:
			cur.execute("SELECT * FROM 	blocks WHERE identity =" 
						"(SELECT MAX(identity) FROM blocks)")
			rows = cur.fetchall()
			if len(rows) == 0:
				Blockchain.create_block(index=1)
				cur.execute("SELECT * FROM 	blocks WHERE identity =" +
						"(SELECT MAX(identity) FROM blocks)")
				rows = cur.fetchall()
			block_data = rows[0]
			block = Block(
				identity=block_data['identity'],
				timestamp=block_data['timestamps'],
				proof=block_data['proof'],
				previous_block_hash=block_data['previous_block_hash']
			)
		else:
			cur.execute("SELECT * FROM 	blocks WHERE identity =" 
						+str(index))
			block_data = cur.fetchall()[0]
			block = Block(
				identity=block_data['identity'],
				timestamp=block_data['timestamps'],
				proof=block_data['proof'],
				previous_block_hash=block_data['previous_block_hash']
			)
		cur.execute("SELECT * FROM 	transactions WHERE blockid =" 
			+str(index))
		rows = cur.fetchall()
		for line in rows:
			transaction = Transaction(
				sender=line['sender'],
				receiver=line['receiver'],
				value=line['value']
			)
			block.transactions.append(transaction)
		return	block

	@staticmethod
	def is_proof_valid(tentative_block):
		"""
		Determine whether this is a valid proof
		If the hash of a block has difficulty number of 0s in the end.
		then the proof is valid or it's not

		Parameters
		----------
		tentative_block : Block
			The potential block with potential proof number

		Returns
		-------
		isValid : Boolean
			whether this is a valid proof value or not
		"""
		result = Blockchain.hash(tentative_block)
		return result[len(result)-blockchain.app.config['DIFFICULTY']:] ==\
				 '0'*blockchain.app.config['DIFFICULTY']

	@staticmethod
	def mine_proof(tentative_block):
		"""
		Iterate different proof values until we get a valid value
		
		Parameters
		----------
		tentative_block : Block
			The block for which we need to find a valid proof value
		"""
		while not Blockchain.is_proof_valid(tentative_block):
			tentative_block.proof += 1

	@staticmethod
	def create_block(index=None):
		"""
		Create a block
		The initial proof is set to 0, which may be an invalid proof,
		thus we need to mineProof ourselves

		Returns
		-------
		block : Block
			New mined block
		"""
		block = Block()
		if index is None:
			last_block = Blockchain.get_block()
			block = Block(identity=last_block.identity+1, proof=0,
				previous_block_hash=Blockchain.hash(last_block))
		else:
			block = Block(0, proof=0, previous_block_hash=0)
		Blockchain.mine_proof(block)
		conn = blockchain.model.get_db()
		cur = conn.cursor()
		cur.execute("INSERT INTO blocks(identity,timestamps,proof,previous_block_hash) "
					"VALUES("+
					str(block.identity)+","+
					str(block.timestamp)+","+
					str(block.proof)+", '"+
					str(block.previous_block_hash)+
					"')")
		conn.commit()
		return block

	@staticmethod
	def create_transaction(sender, receiver, value):
		"""
		Create a transaction and push it to the back of blockchain

		Parameters
		----------
		sender : String
			Name of the sender
		receiver : String
			Name of the receiver
		value : Double
			Value of this transaction

		Returns
		-------
		Id : Int
			Id of the last block
		"""
		block = Blockchain.get_block()
		conn = blockchain.model.get_db()
		cur = conn.cursor()
		cur.execute("INSERT INTO transactions(blockid, sender,receiver,value) VALUES "+
					"(" +
					str(block.identity) + "," +
					"'" + sender + "'," +
					"'" + receiver + "'," +
					str(value)
					+")")
		conn.commit()
		return block.identity
