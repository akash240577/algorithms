# An unordered linked list
from linked_list.ListNode import ListNode


class UnorderedList:

    def __init__(self, *args):
        self.head = None

        for item in args:
            node = ListNode(item)
            if self.head is None:
                self.head = node
                last = self.head

            last.next_node = node
            last = node

    def add(self, data):
        node = ListNode(data, self.head)
        self.head = node

    def print(self):
        current_node = self.head
        while current_node is not None:
            print(current_node.data, end='->')
            current_node = current_node.next_node

    def remove_duplicates(self):
        """
            Removes duplicates data nodes from the list.
            E.g. a list 10->15->20->15->20->2 will become 10->15->20->2
            It will compare current node with any node down the list, if found remove that other node.
            Will take O(1) space but O(N*N) time.
        """
        current_node = self.head
        while current_node is not None:
            previous = current_node
            runner = current_node.next_node
            while runner is not None:
                if current_node.data == runner.data:  # remove runner node, and move runner to next node
                    previous.next_node = runner.next_node
                else:
                    previous = previous.next_node

                runner = runner.next_node

            current_node = current_node.next_node

    def kth_to_last_recursive(self, k):
        """
            Returns kth element from the last node.
            Uses recursion
        """
        node_count, found = self.__recursive_count_backward(self.head, k, 0)
        return found

    def __recursive_count_backward(self, current_node, k, count_backward):
        """
            Helper function for self.kth_to_last_recursive
        """

        if current_node is None:
            return 0, None

        node_count, found = self.__recursive_count_backward(current_node.next_node, k, count_backward)
        node_count = node_count + 1

        if node_count == k:
            return node_count, current_node.data
        else:
            return node_count, found

    def kth_to_last_iterative(self, k):
        """
            Returns kth element from the last node.
            Uses iterative approach

            Begin with/keep two pointers p2 and p1, k elements apart, then move both of them until p1 reaches the end of the list,
            so that p1 will move LENGTH - k and p2 also moves LENGTH - k from the beginning, hence p2 will be the kth element from the last
        """

        p1 = p2 = self.head

        #  make p2 and p1, k elements apart
        count = 0
        while count < k and p1 is not None:
            p1 = p1.next_node
            count = count + 1

        if count < k:
            return None  # list length is less than k

        # now move both p1,p2 until p1 reaches end of the list
        while p1 is not None:
            p1 = p1.next_node
            p2 = p2.next_node

        return None if p2 is None else p2.data

    def partition(self, pivot):
        """
        partition the list such that all element < pivot will be on the left side, and all elements >= pivot will be on the right side.
        If pivot element, if in the list can be on the right side.
        Algorithm: keep two pointer, compare first node pointer data with pivot, if greater than pivot, swap nodes data.
        E.g. Input:  3 -> 5 -> 8 -> 5 -> 10 -> 2 -> 1 [pivot = 5]
             Output: 3 -> 1 -> 2 -> 10 -> 5 -> 5 -> 8

        :param pivot: the data to be used to partition the list.
        :return: None
        """

        p1 = self.head
        p2 = p1.next_node

        while p2 is not None:
            if p1.data >= pivot:
                pass
            p1 = p2
            p2 = p2.next_node

    def add_1(self):
        """
        Add the given number to the number represented as a list e.g. list for number 1999 is 1 - 9 - 9 - 9,
        adding one will modify it as 2 - 0 - 0 - 0
        Algorithm: User recursion to reach to the last element, add one to last and propagate carry backward!
        :return: None, list will be modified
        """

        self.__add_1_recursive(self.head)

        # need to add a new node if head now >= 10
        if self.head.data == 0:
            node = ListNode(1, self.head)
            self.head = node

    def __add_1_recursive(self, node):
        if node.next_node is None:  # if we reached to the end node
            tmp = node.data + 1
        else:
            tmp = node.data + self.__add_1_recursive(node.next_node)

        carry = 0
        if tmp >= 10:
            tmp = tmp - 10
            carry = 1
        node.data = tmp

        return carry
