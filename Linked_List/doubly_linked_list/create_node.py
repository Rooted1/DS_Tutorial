class Node:
    def __init__(self, value, prev_node=None, next_node=None):
        self.value = value 
        self.prev_node = prev_node
        self.next_node = next_node

    # get node value
    def get_value(self):
        return self.value 

    # get node previous pointer
    def get_prev_node(self):
        return self.prev_node 

    # get node next pointer
    def get_next_node(self):
        return self.next_node 

    # set node previous pointer
    def set_prev_node(self, prev_node):
        self.prev_node = prev_node 

    # set node next pointer
    def set_next_nmode(self, next_node):
        self.next_node = next_node 