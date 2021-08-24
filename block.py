class Block():
  #<--------------- Starts Constructor --------------->
    def __init__(self, data, previousBlockHash):
        self.dateAndTime = datetime.now(timezone(timedelta(hours = -5)))  #When called, takes current data & time in UTC-5.
        self.hash = ""                                                    #Defines an empty hash.
        self.data = data                                                  #Defines the sent data as the block data.
        self.previousBlockHash = previousBlockHash                        # Defines the sent previous hash as the previous block hash.
        self.compute_valid_hash()                                         #Computes the current block hash for the requirements specified for this blockchain.
  #<--------------- Ends Constructor --------------->

    def is_hash_valid(self,possibleHash):                                 #Checks if the hash sent is valid for this blockchain.

        return (possibleHash.startswith('0' * 4))
    
    def convert_into_hash(self,preHash):                                  #Hashes the string sent into sha256.
        encodedPreHash = preHash.encode()                                 #Encodes the string into utf-8.
        hash256 = sha256(encodedPreHash)                                  #Turns string into sha256.
        
        return (hash256.hexdigest())
        

    def compute_valid_hash(self):                                         #Iterator that builds the hash until it accomplishes the requirements for a hash block in this blockchain.
        nonce = 0

        while (not self.is_hash_valid(self.hash)):                        #Repeats until is a valid hash.
            preHash = self.to_string() + str(nonce)                       #Builds a string with the all the data that we want the block to have plus a nonce for getting a specific hash format.
            self.hash = self.convert_into_hash(preHash)                   #Converts the data string into a hash sha256.
            nonce += 1                                                    #Increases the nonce plus one in case that the previous hash didn't accomplished the blockchain hash requirements.




    def to_string(self):                                                  #Transforms the data of the block into a formated string.

        return (f"{self.hash}\t{self.data}\t{self.dateAndTime}\t{self.previousBlockHash}\n")
