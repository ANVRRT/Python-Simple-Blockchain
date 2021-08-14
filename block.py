from hashlib import sha256
from datetime import *

class Block():

    def __init__(self, data, previousBlockHash):
        self.dateAndTime = datetime.now(timezone(timedelta(hours = -5)))
        self.hash = ""
        self.data = data
        self.previousBlockHash = previousBlockHash
        self.compute_valid_hash()

    def is_hash_valid(self,possibleHash):

        return (possibleHash.startswith('0' * 4))
    
    def convert_into_hash(self,preHash):
        encodedPreHash = preHash.encode()
        hash256 = sha256(encodedPreHash)
        
        return (hash256.hexdigest())
        

    def compute_valid_hash(self):
        nonce = 0

        while (not self.is_hash_valid(self.hash)):
            preHash = self.to_string() + str(nonce)
            self.hash = self.convert_into_hash(preHash)
            nonce += 1




    def to_string(self):

        return (f"{self.hash}\t{self.data}\t{self.dateAndTime}\t{self.previousBlockHash}\n")