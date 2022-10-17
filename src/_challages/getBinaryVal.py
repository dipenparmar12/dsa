"""
@title: [TITLE]
@src: [URL]
@Difficulty: EASY/MEDIUM/HARD

@Definition:
Given an integer n, return an array ans of length n + 1 such that for each i (0 <= i <= n), ans[i]
is the number of 1's in the binary representation of i.


Example 1:
Input: n = 2
Output: [0,1,1]
Explanation:
0 --> 0
1 --> 1
2 --> 10
Example 2:
Input: n = 5
Output: [0,1,1,2,1,2]
Explanation:
0 --> 0
1 --> 1
2 --> 10
3 --> 11
4 --> 100
5 --> 101


Constraints:
0 <= n <= 105


--- Example 1:
--- Example 2:
--- Example 3:

@Score:

"""

import unittest


class Solution:

    def getBinaryRecursive(self, n):
        if n < 0:
            return []
        if n == 1:
            return [1]

        return [*self.getBinaryRecursive(n // 2), n % 2]

        # rest = self.countBits(n // 2)
        # return [*rest, n % 2]

        # res = [n % 2]
        # rest = self.countBits(n // 2)
        # res = [*rest, *res]
        # return res

    def getBinary(self, n):
        res = []
        while 0 < n:
            remainder = n % 2
            n = n // 2
            res.append(remainder)
        print(res)
        return res

    def getBinaryMySolution(self, n):
        pass
        bTable = [1]
        temp = 1
        while temp <= n:
            bTable.append(bTable[-1] * 2)
            temp += bTable[-1]
        # print(bTable)

        res = [0]
        for i in range(len(bTable) - 1, -1, -1):
            el = bTable[i]

            if el <= n:
                n -= el
                res.append(1)
            else:
                res.append(0)

        print(res)

        # for num in bTable[-1::-1]:
        #     print(num)

        return res


que = Solution()

# que.getBinary(2)    # [0, 1, 0]
# que.getBinary(5)    # [0, 1, 0, 1]
# que.getBinary(11)   # [0, 1, 0, 1, 1]
# que.getBinary(20)   # [0, 1, 0, 1, 0, 0]
# que.getBinary(257)  # [0, 1, 0, 0, 0, 0, 0, 0, 0, 1]
# que.getBinary(511)  # [0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1]


class TestProgram(unittest.TestCase):
    def testCase0(self):
        userInput = 2
        expected = [0, 1, 0]
        msg = f"Should be {expected} Got: {que.getBinary(userInput)}"
        self.assertEqual(que.getBinary(userInput), expected, msg)

    def testCase1(self):
        userInput = 5
        expected = [0, 1, 0, 1]
        msg = f"Should be {expected} Got: {que.getBinary(userInput)}"
        self.assertEqual(que.getBinary(userInput), expected, msg)

    def testCase11(self):
        userInput = 257
        expected = [0, 1, 0, 0, 0, 0, 0, 0, 0, 1]
        msg = f"Should be {expected} Got: {que.getBinary(userInput)}"
        self.assertEqual(que.getBinary(userInput), expected, msg)

    def testCase2(self):
        self.assertEqual(que.getBinary(511), [
                         0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1], "Should be [0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1]")


unittest.main()
