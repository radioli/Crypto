from CoolCoinBlock import CoolCoinBlock


class CoolCoinBlockChain:

    def __init__(self):
     # constructor method
        self.chain = []
        self.current_data = []
        self.nodes = set()
        self.construct_genesis()


    def construct_genesis(self):
        # constructs the initial block
        self.construct_block(prev_hash=0)


    def construct_block(self,prev_hash):
        # constructs a new block and adds it to the chain
        block = CoolCoinBlock(
            index=len(self.chain),
            prev_hash=prev_hash,
            data=self.current_data)
        self.current_data = []
        self.chain.append(block)
        return block

    @staticmethod
    def check_validity(block, prev_block):
        print(f"For transaction: {prev_block.index} Hash is: {prev_block.calculate_hash()}")
        print(f"For transaction: {block.index} Previous Hash is: {block.prev_hash}")
        if prev_block.index + 1 != block.index:
            return False

        elif prev_block.calculate_hash() != block.prev_hash:
            return False

        return True


    def get_previous_block(self):
        return self.chain[-1]

    def add_new_data(self, sender, recipient):
        # adds a new transaction to the data of the transactions
        self.current_data.append({
            'sender': sender,
            'recipient': recipient
        })
        return True