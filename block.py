from hashlib import sha256
from datetime import datetime

class Block():
    def __init__(self, data, previousBlockHash):

        self.data = data
        self.previousBlockHash = previousBlockHash
        self.compute_valid_hash()

    def is_hash_valid(self,hash):

        return (hash.startswith('0' * 4))
    
    def convert_into_hash(self,preHash):

        encodedPreHash = preHash.encode()
        hash256 = sha256(encodedPreHash)
        return (hash256.hexdigest())
        

    def compute_valid_hash(self):

        hash = ''
        nonce = 0

        while (not self.is_hash_valid(hash)):
            preHash = self.to_string() + str(nonce)
            hash = self.convert_into_hash(preHash)
            nonce += 1

        self.hash = hash



    def to_string(self):
        return (f"{self.data}\t{self.previousBlockHash}")