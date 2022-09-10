import hashlib

class NeuralCoinBlock:

   def __init__(self, previous_block_hash, transaction_list):
      self.previous_block_hash = previous_block_hash
      self.transaction_list = transaction_list

      self.block_data = "-".join(transaction_list) + "-" + previous_block_hash
      self.block_hash = hashlib.sha256(self.block_data.encode()).hexdigest()

t1 = "Luke sends 2 BTC to Lindsy "
t2 = "Megan sends 4.1 BTC to Lindsy "
t3 = "Lindsy sends 3.2 BTC to Megan "
t4 = "Robert sends 0.3 BTC to Luke "
t5 = "Lindsy sends 1 BTC to Ben "
t6 = "Lindsy sends 5.4 BTC to Robert "

initial_block = NeuralCoinBlock("Initial String", [t1,t2])

print(initial_block.block_data)
print(initial_block.block_hash)

second_block = NeuralCoinBlock(initial_block.block_hash, [t3,t4])

print(second_block.block_data)
print(second_block.block_hash)

third_block = NeuralCoinBlock(second_block.block_hash, [t5,t6])

print(third_block.block_data)
print(third_block.block_hash)