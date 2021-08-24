from block import Block
from blockchain import Blockchain

class BlockchainUtilities():

    def __init__(self,blockchain) -> None:                                          #Gets all the blocks of the blockchain sent as parameter.
        self.blocks = blockchain.get_blockchain()

    def show_blockchain(self) -> None:
        #<--------------- Starts defining format tags for the "table" showing blocks data -------------->
        bHashT = "Block Hash" 
        bDataT = "Block Data" 
        bDateTimeT = "Date&Time"
        bPrevHashT = "Block Previous Hash"
        sHash =((64 - len(bHashT))*" ")
        sDate = ((32 - len(bDateTimeT))* " ")
        #<--------------- Ends defining format tags for the "table" showing blocks data -------------->
        print(f"{bHashT} {sHash}\t{bDataT}\t{bDateTimeT}\t{sDate}\t{bPrevHashT}"  ) #Prints "table" header.
        for block in self.blocks:
            print(block.to_string())                                                #Prints each block data as a string.

if __name__ == "__main__":

    blockchain = Blockchain()                                   #Initializes blockchain


    blockchain.add_new_block("Wallet 1")                        #Adds new block

    blockchain.add_new_block("Wallet 2")                        #Adds new block

    blockchain.add_new_block("Wallet 3")                        #Adds new block

    blockchain.add_new_block("Wallet 4")                        #Adds new block

    blockchain.add_new_block("Wallet 5")                        #Adds new block

    blockchain.add_new_block("Wallet 6")                        #Adds new block

    blockchain.add_new_block("Wallet 7")                        #Adds new block

    blockchain.add_new_block("Wallet 8")                        #Adds new block
    
    blockchain.add_new_block("Wallet 8")                        #Adds new block


    utilities = BlockchainUtilities(blockchain)                 #Initializes utilities for the sent blockchain
    utilities.show_blockchain()                                 #Shows all data of blocks in the blockchain
