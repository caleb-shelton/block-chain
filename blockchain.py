import hashlib


class Block:
    def __init__(self, data, h, prev_hash=None):
        self.data = data
        h.update(data.encode("utf-8"))
        self.hash = h.hexdigest()
        self.prev_hash = prev_hash

    def __str__(self):
        return str(self.hash)


class BlockChain:
    def __init__(self, data):
        self.chain = []
        self.h = hashlib.new("sha256")

        if self.chain == []:
            # generate Genesis block
            self.chain.append(Block(data=data, h=self.h))

    def add_block(self, data):
        self.chain.append(Block(prev_hash=self.chain[-1].hash, data=data, h=self.h))
        self.data = data
        self.hash = 0
        self.prev_hash = 0

    def __str__(self):
        lines = ""
        hash = ""
        result = ""
        count = 1
        for block in self.chain:
            lines += "----------   "
            hash += "| 0x" + block.hash[:4] + " |"
            if count != len(self.chain):
                hash += "<->"
            count += 1
        result = lines + "\n" + hash + "\n" + lines
        return result


block_chain = BlockChain(data="hello")
block_chain.add_block(data="hello")
block_chain.add_block(data="hello")
print(block_chain)
