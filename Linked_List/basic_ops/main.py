from create_ll import LinkedList 

ll = LinkedList()
print(ll.get_head_node().get_value())

ll.add_to_beginning(35)

# prints value of new head node --> should print 35
print(ll.get_head_node().get_value())