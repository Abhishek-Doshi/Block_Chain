import hashlib
from time import time

class transaction:
	def __init__(self, amount, from_address, to_address):
		self.amount = amount
		self.from_address = from_address
		self.to_address = to_address

class block:
		
	def __init__(self, timestamp, data, previous_hash):
		self.nonce = 0
		self.timestamp = time()
		self.data = data
		self.previous_hash = previous_hash
		self.hash = self.generate_hash()		
		
	def generate_hash(self):
		return hashlib.sha256((str(self.previous_hash) + str(self.timestamp) + str(self.data) + str(self.nonce)).encode('utf-8')).hexdigest()	
		
	def mine_block(self, difficulty):
		print('Mining Block...')
		difficulty_string = '0'
		for index in range(0,difficulty-1):
			difficulty_string += '0'    		
		while (self.hash[:difficulty] != difficulty_string):
			self.nonce += 1
			self.hash = self.generate_hash()
		print('Block Mined Successfully!')
		
class block_chain:

	def __init__(self):	
		self.length = 0
		self.difficulty = 6
		self.chain = []
		self.chain.append(self.create_genesis_block())
		self.length += 1
		
	def create_genesis_block(self):
		return block("24/09/2019", "Genesis Block", "0")
	
	def get_latest_block(self):
		return self.chain[self.length-1]	
	
	def add_block(self, new_block):
		new_block.previous_hash = self.get_latest_block().hash
		new_block.mine_block(self.difficulty)
		self.chain.append(new_block)
		self.length += 1
	
	def is_chain_valid(self):
		for block_index in range(1, self.length-1):
			current_block = self.chain[block_index]
			previous_block = self.chain[block_index-1]
			if current_block.hash != current_block.generate_hash():
				return False
			if current_block.previous_hash != previous_block.hash:
				return False 	 
		return True
			
bitcoin = block_chain()
for i in range(0,10):
	bitcoin.add_block(block("24/09/2019", transaction(100, str("24A6FC8C"), str("BA7DF88E")), bitcoin.chain[i].hash))
print(bitcoin.length)
print(bitcoin.is_chain_valid())
