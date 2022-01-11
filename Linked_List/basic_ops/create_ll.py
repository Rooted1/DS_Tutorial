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

    # add new node to end of ll - append
    def add_to_end(self, value):
        if self.head_node.get_value() == None:
            self.head_node.set_value(value)
        else:
            new_node = Node(value)
            current_node = self.head_node
            while current_node.get_next_node() != None:
                current_node = current_node.get_next_node()
            current_node.set_next_node(new_node)

    # add new node in between nodes in ll - insert
    def add_in_btw(self, lookup_value, value_to_add):
        if self.head_node.get_value() == None:
            self.head_node.set_value(value_to_add)
        else:
            new_node = Node(value_to_add)
            current_node = self.head_node
            while current_node.get_value() != lookup_value:
                current_node = current_node.get_next_node()
            new_node.set_next_node(current_node.get_next_node())
            current_node.set_next_node(new_node)

    # update a node value
    def update_node(self, value_to_update, new_value):
        if self.head_node.get_value() == value_to_update:
            self.head_node.set_value(new_value)
        else:
            current_node = self.head_node.get_next_node()
            while current_node:
                if current_node.get_value() != value_to_update:
                    current_node = current_node.get_next_node()
                current_node.set_value(new_value)
                current_node = None

    # remove node
    def remove_node(self, value_to_remove):
        if self.head_node.get_value() == value_to_remove:
            self.head_node = self.head_node.get_next_node()
        else:
            previous_node = self.head_node
            current_node = previous_node.get_next_node()
            while current_node:
                if current_node.get_value() != value_to_remove:
                    previous_node = current_node
                    current_node = current_node.get_next_node()
                else:
                    previous_node.set_next_node(current_node.get_next_node())
                    current_node = None

    # traverse ll and count how many nodes
    def traverse_ll(self):
        count = 0
        current_node = self.head_node
        while current_node != None:
            count += 1
            current_node = current_node.get_next_node()
        return count