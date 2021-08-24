from block import Block

class Blockchain():
  #<--------------- Starts Constructor --------------->
    def __init__(self):
        self.blocks = []                              #Initializes empty blockchain.
        self.generate_genesis_block()                 #Starts genesis block.
  #<--------------- Ends Constructor --------------->

    def get_last_block_hash(self):                    # Gets last block hash from the blockchain.
        lastBlock = self.blocks[-1]                   # Gets last element from list (Blockchain).
        lastBlockHash = lastBlock.hash                #Gets hash from the last block in blockchain.
        return lastBlockHash
    
    def get_blockchain(self):                         # Gets full blockchain.
        
        return self.blocks

    def add_new_block(self,data):                     #Generates a new block, receives the data you want to store as a string.
        previousHash = self.get_last_block_hash()     #Calls a function to get last block hash.
        newBlock = Block(data,previousHash)           #Generates a new block sending data as string and the hash of the last block.
        self.blocks.append(newBlock)                  #Adds new block to the blockchain.
    
    def generate_genesis_block(self):                 #Generates the genesis block.
        data = "Genesis\t"                            #Defines the genesis data predefined as "Genesis".
        PREVIOUS_HASH = '0' * 64                      #Defines a full zero 64 element as hash.
        genesisBlock = Block(data,PREVIOUS_HASH)      #Generates the block with the data and hash.
        self.blocks.append(genesisBlock)              #Incorporates the gensis block in the blockchain.
