from create_dll import DoublyLinkedList 

dll = DoublyLinkedList()

# print values of head and tail nodes
# print(dll.get_head_node().get_value())
# print(dll.get_tail_node().get_value())

# print("Add new head node: ")

dll.add_to_beginning(14)
# print values of head and tail nodes --> outputs 14 85
# print(dll.get_head_node().get_value())
# print(dll.get_tail_node().get_value())

# print("Add new tail node: ")

dll.add_to_end(78)
dll.add_to_end(84)
# print values of head and tail nodes --> outputs 14 85
# print(dll.get_head_node().get_value())
# print(dll.get_tail_node().get_value())

# print("remove head and print new head: ")

# print(dll.remove_head())

# print("remove tail node twice and print new head: ")
# print(dll.remove_tail())
# print(dll.remove_tail())


# print("remove head node and print its value: ")

# print(dll.remove_head())

# print("remove tail node twice and print its value: ")
# print(dll.remove_tail())
# print(dll.remove_tail())

# print(dll.remove_by_value(78))

dll.print_dll()