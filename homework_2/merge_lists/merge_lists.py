class Node:
    def __init__(self, value=None):
        self.next = None
        self.value = value

    def __str__(self):
        return str(self.value)


def merge_dummy(list1, list2):
    if not list1:
        return list2
    if not list2:
        return list1

    dummy = Node()
    tail = dummy
    while list1 and list2:
        if list1.value < list2.value:
            tail.next = list1
            list1 = list1.next
        else:
            tail.next = list2
            list2 = list2.next
        tail = tail.next

    tail.next = list1 if list1 else list2

    return dummy.next


def merge_no_dummy(list1, list2):
    if not list1:
        return list2
    if not list2:
        return list1

    if list1.value < list2.value:
        head = list1
        list1 = list1.next
    else:
        head = list2
        list2 = list2.next

    tail = head

    while list1 and list2:
        if list1.value < list2.value:
            tail.next = list1
            list1 = list1.next
        else:
            tail.next = list2
            list2 = list2.next
        tail = tail.next

    tail.next = list1 if list1 else list2

    return head
