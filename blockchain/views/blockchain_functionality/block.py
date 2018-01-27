"""
class Block

Created by Shibo Chen, Data:1/26/2018
University of Michigan, class of 2019
email: chshibo@umich.edu
"""

import time

class Block(object):
	"""Block class"""
	def __init__(self, identity=None, proof=None, previous_block_hash=None, timestamp=None):
		"""
		Constructor for block

		Parameters
		----------
		timestamp : Int
			timestamp for new block (Unix epoch)
		id : Int
			id for current block
		proof : Int
			proof for validity of current block
		previousBlockHash : Int
			Hash value of previous block in the chain
		"""
		if timestamp is None:
			self.timestamp = int(time.time())
		else:
			self.timestamp = timestamp
		if identity is None:
			self.identity = -1
		else:
			self.identity = identity
		if proof is None:
			self.proof = -1
		else:
			self.proof = proof
		if previous_block_hash is None:
			self.previous_block_hash = -1
		else:
			self.previous_block_hash = previous_block_hash
		self.transactions = []
	
	def __str__(self):
		"""
		Return a block instance to string

		Returns
		-------
		Block_str : String
			Block string of this functions
		"""
		block_dict = {}
		block_dict['timestamp'] = self.timestamp
		block_dict['identity'] = self.identity
		block_dict['proof'] = self.proof
		block_dict['previous_block_hash'] = self.previous_block_hash
		block_dict['transactions'] = self.transactions
		return block_dict.__str__()
