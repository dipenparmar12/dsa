
"""
@title: 141. Linked List Cycle
@src: https://leetcode.com/problems/linked-list-cycle/
@Difficulty: EASY

@Definition:
Given head, the head of a linked list, determine if the linked list has a cycle in it.
There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to. Note that pos is not passed as a parameter.
Return true if there is a cycle in the linked list. Otherwise, return false.

 

Example 1:
3 -> 2 -> 0 -> -4  -> (2  -> 0 -> -4) -> (2  -> 0 -> -4)...
Input: head = [3,2,0,-4], pos = 1
Output: true
Explanation: There is a cycle in the linked list, where the tail connects to the 1st node (0-indexed).

Example 2:
1 -> 2  -> (1 -> 2) -> (1 -> 2) ...
Input: head = [1,2], pos = 0
Output: true
Explanation: There is a cycle in the linked list, where the tail connects to the 0th node.
Example 3:
1 -> 
Input: head = [1], pos = -1
Output: false
Explanation: There is no cycle in the linked list.
 

Constraints:
The number of the nodes in the list is in the range [0, 104].
-105 <= Node.val <= 105
pos is -1 or a valid index in the linked-list.
 

Follow up: Can you solve it using O(1) (i.e. constant) memory?

@Score:



@attempt
  - 3 Hours
"""

import unittest


class ListNode:
    def __init__(self, x):
        self.data = x
        self.next = None
        self.maxNext = 1000

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


class Solution:
    def funName(self, n):
        pass


que = Solution()


class TestProgram(unittest.TestCase):

    def testCase5(self):
        expected = False
        node1 = CreateToSinglyList([-21, 10, 5])
        msg = f"Should be {expected} Got: {que.hasCycle(node1)}"
        self.assertEqual(que.hasCycle(node1), expected, msg)

    def testCase6(self):
        expected = False
        node1 = CreateToSinglyList(
            [-21, 10, 17, 8, 4, 26, 5, 35, 33, -7, -16, 27, -12, 6, 29, -12, 5, 9, 20, 14, 14,
             2, 13, -24, 21, 23, -21, 5])

        msg = f"Should be {expected} Got: {que.hasCycle(node1)}"
        self.assertEqual(que.hasCycle(node1), expected, msg)

    def testCase0(self):
        expected = True
        node1 = ListNode(3)
        node2 = ListNode(2)
        node3 = ListNode(0)
        node4 = ListNode(-4)

        node1.next = node2
        node2.next = node3
        node3.next = node4
        node4.next = node2

        msg = f"Should be {expected} Got: {que.hasCycle(node1)}"
        self.assertEqual(que.hasCycle(node1), expected, msg)

    def testCase1(self):
        expected = False
        node1 = ListNode(1)
        node1.next = ListNode(2)
        msg = f"Should be {expected} Got: {que.hasCycle(node1)}"
        self.assertEqual(que.hasCycle(node1), expected, msg)

    def testCase2(self):
        expected = False
        node1 = ListNode(10)
        msg = f"Should be {expected} Got: {que.hasCycle(node1)}"
        self.assertEqual(que.hasCycle(node1), expected, msg)

    def testCase3(self):
        expected = False
        node1 = ListNode(11)
        node1.next = ListNode(22)
        msg = f"Should be {expected} Got: {que.hasCycle(node1)}"
        self.assertEqual(que.hasCycle(node1), expected, msg)


unittest.main()


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
