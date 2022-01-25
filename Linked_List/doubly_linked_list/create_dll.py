from platform import node
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

    # add new node to end of dll
    def add_to_end(self, value):
        new_node = Node(value)
        if self.tail_node.get_value() == None:
            self.tail_node = self.head_node = new_node
        current_tail = self.tail_node
        current_tail.set_next_node(new_node)
        new_node.set_prev_node(current_tail)
        self.tail_node = new_node
            
    # remove head node
    def remove_head(self):
        head_to_remove = self.head_node
        if head_to_remove == None:
            return None
        self.head_node = head_to_remove.get_next_node()
        if self.head_node != None:
            self.head_node.set_prev_node(None)
        if head_to_remove == self.tail_node:
            self.remove_tail()
        return head_to_remove.get_value()

    # remove tail node
    def remove_tail(self):
        tail_to_remove = self.tail_node 
        if tail_to_remove == None:
            return None
        self.tail_node = tail_to_remove.get_prev_node()
        if self.tail_node != None:
            self.tail_node.set_next_node(None)
        if tail_to_remove == self.head_node:
            self.remove_head() 
        return tail_to_remove.get_value()

    def remove_by_value(self, value_to_remove):
        node_to_remove = None 
        current_node = self.head_node
        while current_node != None:
            if current_node.get_value() == value_to_remove:
                node_to_remove = current_node 
                break 
            current_node = current_node.get_next_node()
        if node_to_remove == None:
            return None 
        if node_to_remove == self.head_node:
            self.remove_head()
        elif node_to_remove == self.tail_node:
            self.remove_tail()
        else:
            next_node = node_to_remove.get_next_node()
            prev_node = node_to_remove.get_prev_node()
            next_node.set_prev_node(prev_node)
            prev_node.set_next_node(next_node)
        return node_to_remove