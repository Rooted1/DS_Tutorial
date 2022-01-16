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

    # add new node to beginning of dll
    def add_to_beginning(self, value):
        new_node = Node(value)
        if self.head_node.get_value() == None:
            self.head_node = self.tail_node = new_node
        current_head = self.head_node 
        new_node.set_next_node(current_head)
        current_head.set_prev_node(new_node)
        self.head_node = new_node
