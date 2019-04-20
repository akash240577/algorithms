from linked_list.ListNode import ListNode
from linked_list.UnorderedList import UnorderedList


def sum_list_stored_in_reverse_order(head1, head2):
    """
    You have two numbers represented by a linked list, where each node contains a single
    digit. The digits are stored in reverse order, such that the last digit is at the head of the list. Write a
    function that adds the two numbers and returns the sum as a linked list.
    EXAMPLE
    Input: ( 7 - > 1 -> 6) + (5 -> 9 -> 2).That is,617 + 295.
    Output: 2 -> 1 -> 9. That is, 912.

    :param head1:
    :param head2:
    :return: result
    """
    result = UnorderedList()

    start1 = head1
    start2 = head2

    carry = 0
    result_head = None
    last = None
    while start1 is not None or start2 is not None:
        data1 = data2 = 0
        if start1 is not None:
            data1 = start1.data

        if start2 is not None:
            data2 = start2.data

        tmp = data1 + data2 + carry
        if tmp >= 10:
            tmp = tmp - 10
            carry = 1

        else:
            carry = 0

        node = ListNode(tmp)
        if result_head is None:
            result_head = node
            last = node

        last.next_node = node
        last = node

        if start1 is not None:
            start1 = start1.next_node

        if start2 is not None:
            start2 = start2.next_node

    if carry == 1:
        # create a new node for carry 1
        node = ListNode(1)
        # insert this node after last node
        last.next_node = node

    result.head = result_head

    return result


list1 = UnorderedList(7, 3)
list2 = UnorderedList(8, 9, 5, 2)
result = sum_list_stored_in_reverse_order(list1.head, list2.head)
result.print()
print("Sum {}".format(37 + 2598))
