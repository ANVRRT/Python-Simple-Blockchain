from block import Block

class Blockchain():
    def __init__(self):
        self.blocks = []
        self.generate_genesis_block()

    def get_last_block_hash(self):
        lastBlock = self.blocks[-1]
        lastBlockHash = lastBlock.hash
        return lastBlockHash
    
    def get_blockchain(self):
        
        return self.blocks

    def add_new_block(self,data):
        previousHash = self.get_last_block_hash()
        newBlock = Block(data,previousHash)
        self.blocks.append(newBlock)
    
    def generate_genesis_block(self):
        data = "Genesis\t"
        PREVIOUS_HASH = '0' * 64
        genesisBlock = Block(data,PREVIOUS_HASH)
        self.blocks.append(genesisBlock)

    

