from create_node import Node

class LinkedList:
    def __init__(self, value=None):
        self.head_node = Node(value) 

    # get head node
    def get_head_node(self):
        return self.head_node

    # add node to beginning of ll - prepend
    def add_to_beginning(self, value):
        if self.head_node.get_value() == None:
            self.head_node.set_value(value)
        else:
            new_node = Node(value)
            new_node.set_next_node(self.head_node)
            self.head_node = new_node

    # print ll
    def printll(self):
        if self.head_node.get_value() == None:
            print("Linked list is empty!")
        else:
            current_node = self.head_node
            while current_node:
                if current_node.get_value() != None:
                    print(current_node.get_value(), end=" ")
                current_node = current_node.get_next_node()

    # add new node to end of ll
    def add_to_end(self, value):
        if self.head_node.get_value() == None:
            self.head_node.set_value(value)
        else:
            new_node = Node(value)
            current_node = self.head_node
            while current_node.get_next_node() != None:
                current_node = current_node.get_next_node()
            current_node.set_next_node(new_node)