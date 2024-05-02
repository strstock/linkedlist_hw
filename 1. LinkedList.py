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

    def add_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            last_node = self.head
            while last_node.next is not None:
                last_node = last_node.next
            last_node.next_node = new_node

    def add_node(self, data, prev_node):
        if not self.head:
            return
        new_node = Node(data)
        new_node.next = prev_node.next
        prev_node.next = new_node

    def delete_node(self, node):
        if node == self.head:
            self.head = node.next
        else:
            curr_node = self.head
            while curr_node is not None:
                curr_node = curr_node.next
            curr_node.next = node.next

    def search(self, data):
        curr_node = self.head
        while curr_node is not None:
            if curr_node.data == data:
                return True
            curr_node = curr_node.next
        return False

    def print_list(self):
        curr_node = self.head
        while curr_node is not None:
            print(curr_node.data, end=" ")
            curr_node = curr_node.next

if __name__ == '__main__':
    lst = LinkedList()
    lst.add_start(1)
    lst.add_end(2)
    lst.add_node(3, lst.head)
    lst.print_list()
    print(lst.search(1))
    print(lst.search(4))
    lst.delete_node(lst.head)
    lst.print_list()
