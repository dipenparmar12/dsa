class ListNode:
    def __init__(self, val, _next=None):
        self.val = val
        self.next = _next


class SinglyLinkedList:
    head = None

    def __str__(self):
        output = ''
        current = self.head
        while current.next:
            output +=  str(current.val) + ' -> '
            current = current.next

        output += str(current.val)
        return output

    def push(self, val):
        if self.head is None:
            self.head = ListNode(val)
            return self.head

        current = self.head
        while current.next:  # is not None
            current = current.next

        current.next = ListNode(val)


sl = SinglyLinkedList()

sl.push(1)
sl.push(22)
sl.push(3)
sl.push(44)
sl.push(55)

print(f"SinglyList.py::37 sl: ", sl)
