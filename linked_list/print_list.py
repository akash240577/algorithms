# prints all nodes in a linked list
from linked_list.UnorderedList import UnorderedList

my_list = UnorderedList()
# my_list.add(1)
# my_list.add(3)
# my_list.add(4)

my_list.add(5)
my_list.add(4)
my_list.add(7)
my_list.add(4)
my_list.add(10)
my_list.add(20)

# my_list.remove_duplicates()

# print
my_list.print()

print("\nkth last element")

# print(my_list.kth_to_last_recursive(7))

print(my_list.kth_to_last_iterative(2))
