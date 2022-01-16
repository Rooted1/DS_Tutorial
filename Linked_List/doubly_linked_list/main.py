from create_dll import DoublyLinkedList 

dll = DoublyLinkedList(85)

# print values of head and tail nodes
print(dll.get_head_node().get_value())
print(dll.get_tail_node().get_value())

print("New head and tail values: ")

dll.add_to_beginning(14)
# print values of head and tail nodes --> outputs 14 85
print(dll.get_head_node().get_value())
print(dll.get_tail_node().get_value())