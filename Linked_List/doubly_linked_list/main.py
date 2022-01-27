from create_dll import DoublyLinkedList 

dll = DoublyLinkedList()

dll.add_to_beginning(14)
dll.add_to_beginning(23)
dll.add_to_beginning(58)
dll.add_to_beginning(94)
dll.print_dll()

print()

dll.add_to_end(78)
dll.add_to_end(84)
dll.add_to_end(45)
dll.add_to_end(18)
dll.print_dll()

print()

print(dll.remove_head())
dll.print_dll()

print()

print(dll.remove_tail())
dll.print_dll()

print()

print(dll.remove_by_value(78))

dll.print_dll() 