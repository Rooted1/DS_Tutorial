from create_ll import LinkedList 

ll = LinkedList(23)
print(ll.get_head_node().get_value())

ll.add_to_beginning(35)

# prints value of new head node --> should print 35
print(ll.get_head_node().get_value())

# print ll --> should ouptput 35 23
ll.printll()
