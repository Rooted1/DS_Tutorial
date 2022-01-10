from create_node import Node

class LinkedList:
    def __init__(self, value=None):
        self.head_node = Node(value) 

    # get head node
    def get_head_node(self):
        return self.head_node

    # add node to beginning of ll
    def add_to_beginning(self, value):
        if self.head_node.get_value() == None:
            self.head_node.set_value(value)
        else:
            new_node = Node(value)
            new_node.set_next_node(self.head_node)
            self.head_node = new_node