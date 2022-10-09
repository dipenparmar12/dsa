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
            output += str(current.val) + ' -> '
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

    def reverseRecursive_(self, node=None, reverseList=None):
        if self.head is not None and reverseList is None:
            node = self.head
            reverseList = SinglyLinkedList()
        #
        if node is None:
            return None

        self.reverseRecursive_(node.next, reverseList)

        reverseList.push(node.val)

        return reverseList

    def reverseRec(self, node=None):
        if node is None or node.next is None:
            return node

        next_ = node.next
        lastNode = self.reverseRec(next_)
        next_.next = node
        node.next = None

        return lastNode

    def reverseIterative(self):
        prev = None
        i_curr = self.head

        """
         List = 1 -> 2 -> 3 -> 4 -> null

         if i not None
         i=1
            tempNext    =  next -> 2
            i.next(2)   =  Pre  -> None
            pre         =  i    -> 1
            i           =  tempNext -> 2
            -----
            prevList: 1 -> 
            CurrentList: 2 -> 3 -> 4 -> 5 ->     
        i=2
            tempNext    =  next -> 3
            i.next(2)   =  Pre  -> None
            pre         =  i    -> 2
            i           =  tempNext -> 3
            -----
            prevList: 2 -> 1 -> 
            CurrentList: 3 -> 4 -> 5 -> 
        i=3
            tempNext    =  next -> 4
            i.next(3)   =  Pre  -> None
            pre         =  i    -> 3
            i           =  tempNext -> 4
            -----
            prevList: 3 -> 2 -> 1 -> 
            CurrentList: 4 -> 5 -> 
        i=4
            tempNext    =  next -> null
            i.next(4)   =  Pre  -> 3
            pre         =  i    -> 4
            i           =  tempNext -> null
            -----
            prevList: 4 -> 3 -> 2 -> 1 -> 
            CurrentList: 5 -> 
            
            -----
            prevList: 5 -> 4 -> 3 -> 2 -> 1 -> 
            CurrentList: No head or next.
        return prevList
        """

        while i_curr:
            # print(i_curr.val, end=' -> ')
            tempNext = i_curr.next
            i_curr.next = prev
            prev = i_curr
            i_curr = tempNext
            printList(prev, 'prevList:')
            printList(i_curr, 'CurrentList:')

        return prev

    def reverseList(self):
        # return self.reverseRecursive_()
        # return self.reverseRec(self.head)
        return self.reverseIterative()


sl = SinglyLinkedList()

sl.push(1)
sl.push(22)
sl.push(3)
sl.push(44)
sl.push(55)


def printList(li, *data):
    if data:
        print(*data, end=' ')

    if li and hasattr(li, 'head'):
        print(li.val, end=' -> ')
        li = li.head
    elif li and hasattr(li, 'next'):
        print(li.val, end=' -> ')
        li = li.next
    else:
        print("No head or next.")

    while li:
        print(li.val, end=' -> ')
        li = li.next
    print()
    return li


print(f"SinglyList.py::37 sl: ", sl)
print(f"SinglyList.py::37 sl reversed: ", sl.reverseList())
# printList(sl.reverseList())


"""
---- Internet solutions:

def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
    curr = head
    prev = None
    while curr:
        hold = curr.next # hold.val = 3  hold.next = rest of the node
        curr.next  = prev # curr.val = 1 curr.next = None
        prev = curr # prev.val = 1  prev.next = None
        curr = hold # curr.val = 2  curr.next = rest of the node
        
    return prev
    

def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
  prev,curr = None,head
  while curr:
      temp = curr.next
      curr.next = prev
      prev=curr
      curr = temp
  return prev
"""


""" Temp study 
0
next-> 1
       next-> 2
               next-> 3
                      null
                      current is None
                      
0 1 2 3 4         

l1 = 0 -> 1 -> 2 -> 3 -> 4
l2 = None
l2.add(4)

"""
