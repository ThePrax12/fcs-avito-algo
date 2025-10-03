class Node:
    def __init__(self, value):
        self.next = None
        self.value = value

    def __str__(self):
        return str(self.value)


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def append_right(self, value):
        node = Node(value)
        if self.head is None:
            self.tail = node
            self.head = node

        else:
            self.tail.next = node
            self.tail = node
        self.size += 1

    def append_left(self, value):
        node = Node(value)
        if self.head is None:
            self.tail = node
            self.head = node
        else:
            node.next = self.head
            self.head = node
        self.size += 1

    def pop_left(self):
        to_pop = None
        if self.head is not None:
            to_pop = self.head.value
            self.head = self.head.next
            self.size -= 1
        if self.head is None:
            self.tail = None
        return to_pop

    def is_empty(self):
        return self.head is None

    def __str__(self):
        node = self.head
        ans = []
        while node is not None:
            ans.append(str(node.value))
            node = node.next
        return ",".join(ans)

    def __len__(self):
        return self.size

    def peek_left(self):
        return None if self.head is None else self.head.value
