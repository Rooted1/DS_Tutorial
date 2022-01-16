from create_node import Node

class DoublyLinkedList:
    def __init__(self, value=None):
        self.head_node = Node(value)
        self.tail_node = Node(value)

    # get head node 
    def get_head_node(self):
        return self.head_node

    # get tail node 
    def get_tail_node(self):
        return self.tail_node 


