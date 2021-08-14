from block import Block
from blockchain import Blockchain

class BlockchainUtilities():

    def __init__(self,blockchain) -> None:
        self.blocks = blockchain.get_blockchain()

    def show_blockchain(self) -> None:

        for block in self.blocks:
            print(block.to_string())



if __name__ == "__main__":

    blockchain = Blockchain()


    blockchain.add_new_block("Wallet 1")

    blockchain.add_new_block("Wallet 2")

    blockchain.add_new_block("Wallet 3")

    blockchain.add_new_block("Wallet 4")

    blockchain.add_new_block("Wallet 5")

    blockchain.add_new_block("Wallet 6")

    blockchain.add_new_block("Wallet 7")

    blockchain.add_new_block("Wallet 8")


    utilities = BlockchainUtilities(blockchain)
    utilities.show_blockchain()



