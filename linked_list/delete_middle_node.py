from linked_list.ListNode import ListNode
from linked_list.UnorderedList import UnorderedList


def delete_middle_node(node):
    """
    Delete the middle (any node except first and last), given access to only that node, no head access is give,
    Solution is to copy  the data from the next node to this node and delete the next node!
    Input is node to be deleted
    """
    if (node is not None and node.next_node is not None):
        node.data = node.next_node.data
        node.next_node = node.next_node.next_node


node5 = ListNode(8)
node4 = ListNode(7, node5)
node3 = ListNode(4, node4)
node2 = ListNode(1, node3)
node1 = ListNode(3, node2)

list = UnorderedList()
list.head = node1
list.print()

delete_middle_node(node2)

print("\nAfter deleting node with value {}".format(node2.data))
list.print()
