# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.data = x
        self.next = None
        self.maxNext = 50

    def __str__(self, x=19):
        if self is None:
            return None
        # return str(self.data)
        current = self
        string = ''
        i = 0
        while current:
            i += 1
            # print(current.data, end=' ')
            string += str(current.data) + ', '
            current = current.next
            if self.maxNext == i:
                break
        return string


def CreateToSinglyList(items):
    singlyList = None
    temp = None

    for i, item in enumerate(items):
        if i == 0:
            singlyList = ListNode(item)
            temp = singlyList
        else:
            temp.next = ListNode(item)
            temp = temp.next

    return singlyList

# nodeItems = [-11, 22, 33, 44,  55, 66]
# node = CreateToSinglyList(nodeItems)
# print("CreateToSinglyList:-> ", node)


def singlyListToArr(head):
    if head is None:
        return None
    current = head
    items = []
    while current:
        items.append(current.data)
        current = current.next

    return items


# print(singlyListToArr(CreateToSinglyList([])))
# print(singlyListToArr(CreateToSinglyList([1, ])))
# print(singlyListToArr(CreateToSinglyList([1, 2, 3, 4, 5])))
