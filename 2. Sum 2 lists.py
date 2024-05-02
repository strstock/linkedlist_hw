class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def add_start(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def add_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            last_node = self.head
            while last_node.next is not None:
                last_node = last_node.next
            last_node.next = new_node

    def add_node(self, data, prev_node):
        if not self.head:
            return
        new_node = Node(data)
        new_node.next = prev_node.next
        prev_node.next = new_node

    def add_two_numbers(self, l1, l2):
        dummy = Node(0)
        curr_node = dummy
        carry = 0
        while l1 or l2 or carry:
            val1 = l1.data if l1 else 0
            val2 = l2.data if l2 else 0
            sum = val1 + val2 + carry
            carry = sum // 10
            curr_node.next = Node(sum % 10)
            curr_node = curr_node.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        if not carry:
            return dummy.next
        else:
            return None


if __name__ == "__main__":
    l1 = LinkedList()
    l1.add_start(3)
    l1.add_start(4)
    l1.add_start(2)
    l2 = LinkedList()
    l2.add_start(4)
    l2.add_start(6)
    l2.add_start(5)
    result_list = l1.add_two_numbers(l1.head, l2.head)

    curr_node = result_list
    while curr_node is not None:
        print(curr_node.data, end=" ")
        curr_node = curr_node.next