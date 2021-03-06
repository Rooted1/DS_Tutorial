from create_ll import LinkedList 

ll = LinkedList(23)
print(ll.get_head_node().get_value())

ll.add_to_beginning(35)

# prints value of new head node --> should print 35
print(ll.get_head_node().get_value())

# print ll --> should ouptput 35 23
ll.printll()

print()

# add new node to end of ll and print ll --> outputs 35 23 45
ll.add_to_end(45)
ll.printll()

print()

# add new node btw nodes and print ll --> outputs 35 20 23 45
ll.add_in_btw(35, 20)
ll.printll()

print() 

# update node value and print ll --> outputs 16 20 23 45
ll.update_node(35, 16)
ll.printll()

print() 

# remove node and print ll --> outputs 16 20 23
ll.remove_node(45)
ll.printll() 

print()

print(ll.traverse_ll())