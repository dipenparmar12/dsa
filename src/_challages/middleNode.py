"""
@title: 876. Middle of the Linked List
@src: https://leetcode.com/problems/middle-of-the-linked-list
@Difficulty: EASY

@Definition:
Given the head of a singly linked list, return the middle node of the linked list.
If there are two middle nodes, return the second middle node.

 
Example 1:
Input: head = [1,2,3,4,5]
Output: [3,4,5]
Explanation: The middle node of the list is node 3.
Example 2:
Input: head = [1,2,3,4,5,6]
Output: [4,5,6]
Explanation: Since the list has two middle nodes with values 3 and 4, we return the second one.
 

Constraints:
The number of nodes in the list is in the range [1, 100].
1 <= Node.val <= 100

--- Example 1:
--- Example 2:
--- Example 3:

@Score:
Runtime: 55 ms, faster than 49.74% of Python3 online submissions for Middle of the Linked List.
Memory Usage: 13.8 MB, less than 55.04% of Python3 online submissions for Middle of the Linked List.

"""

import unittest


class Solution:
    def middleNode(self, head):
        i = 0
        cur = head
        while cur:
            i += 1
            cur = cur.next

        res = head
        for j in range(i // 2):
            res = res.next

        return res


que = Solution()


class ListNode:
    def __init__(self, x):
        self.data = x
        self.next = None


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


def singlyListToArr(head):
    if head is None:
        return None
    current = head
    items = []
    while current:
        items.append(current.data)
        current = current.next

    return items


class TestProgram(unittest.TestCase):
    def testCase0(self):
        node1 = CreateToSinglyList([1, 2, 3, 4, 5])
        expected = [3, 4, 5]
        result = singlyListToArr(que.middleNode(node1))

        msg = f"Should be {expected} Got: {result}"
        self.assertEqual(result, expected, msg)

    def testCase1(self):
        node1 = CreateToSinglyList([1, 2, 3, 4, 5, 6])
        expected = [4, 5, 6]
        result = singlyListToArr(que.middleNode(node1))

        msg = f"Should be {expected} Got: {result}"
        self.assertEqual(result, expected, msg)

    def testCase2(self):
        node1 = CreateToSinglyList([1])
        expected = [1]
        result = singlyListToArr(que.middleNode(node1))

        msg = f"Should be {expected} Got: {result}"
        self.assertEqual(result, expected, msg)

    def testCase_2(self):
        node1 = CreateToSinglyList(list("1") * 100)
        expected = list("1") * 50
        result = singlyListToArr(que.middleNode(node1))

        msg = f"Should be {expected} Got: {result}"
        self.assertEqual(result, expected, msg)


unittest.main()
