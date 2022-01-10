from create_node import Node

class LinkedList:
    def __init__(self, value=None):
        self.head_node = Node(value) 

    # get head node
    def get_head_node(self):
        return self.head_node