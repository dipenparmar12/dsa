"""
@title: 338. Counting Bits
@src: https://leetcode.com/problems/counting-bits/
@Difficulty: EASY

@Definition:
Given an integer n, return an array ans of length n + 1 such that for each i (0 <= i <= n), ans[i] is the number of 1's in the binary representation of i.


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


Follow up:
It is very easy to come up with a solution with a runtime of O(n log n). Can you do it in linear time O(n) and possibly in a single pass?
Can you do it without using any built-in function (i.e., like __builtin_popcount in C++)?


@Score:
Runtime: 842 ms, faster than 5.01% of Python3 online submissions for Counting Bits.
Memory Usage: 20.8 MB, less than 30.12% of Python3 online submissions for Counting Bits.

"""

import unittest


class Solution:
    def countOfOneInBinary(self, n):
        if n < 0:
            return 0
        if n == 2 or n == 1:
            return 1
        if n == 0:
            return 0

        rest = self.countOfOneInBinary(n // 2)
        count = 0 if n % 2 == 0 else 1
        count += rest
        return count

    def countBits(self, n):
        result = []
        for i in range(0, n + 1):
            result.append(self.countOfOneInBinary(i))
        return result

    def countBits_Internet(self, n: int) -> list[int]:
        res = [0] * (n + 1)
        bias = 1
        for i in range(1, n + 1):
            # print(i, end='')
            if (bias * 2 == i):
                bias = i
            res[i] = 1 + res[i - bias]

        return res

    def countBits_Internet1(self, n: int) -> list[int]:
        dp = [0]*(n+1)
        for i in range(1, n+1):
            dp[i] = dp[i & (i-1)]+1

        return dp

    def countBits_Internet2(self, n: int) -> list[int]:
        ans = [0] * (n + 1)
        for x in range(1, n + 1):
            # x // 2 is x >> 1 and x % 2 is x & 1
            ans[x] = ans[x >> 1] + (x & 1)
        return ans

    def countBits_Internet3(self, n: int) -> list[int]:
        dp = [0] * (n + 1)
        # initialize dynamic programming return as array with 0 for length of n + 1
        offset = 1  # start offset at 1

        for i in range(1, n + 1):
            # starting at 1 since 0 will always be 0 since we go to n + 1
            if offset * 2 == i:  # then we reach a significant new value
                offset = i  # set the offset to i
            dp[i] = 1 + dp[i - offset]
            # set the array value to 1 new 1 + the previous significant offset number of 1's
        return dp
        # O(n)


que = Solution()

# print(que.countBits(2))
# print(que.countBits(5))
# print(que.countBits(11))
# print(que.countBits(20))
# print(que.countBits(257))
# print(que.countBits(511))
# print(que.countBits(10**5))

# que.countOfOneInBinary(2)    # [0, 1, 0]
# que.countOfOneInBinary(5)    # [0, 1, 0, 1]
# que.countOfOneInBinary(11)   # [0, 1, 0, 1, 1]
# que.countOfOneInBinary(20)   # [0, 1, 0, 1, 0, 0]
# que.countOfOneInBinary(257)  # [0, 1, 0, 0, 0, 0, 0, 0, 0, 1]
# que.countOfOneInBinary(511)  # [0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1]


class TestProgram(unittest.TestCase):
    def testCase0(self):
        userInput = 5
        expected = [0, 1, 1, 2, 1, 2]
        msg = f"Should be {expected} Got: {que.countBits(userInput)}"
        self.assertEqual(que.countBits(userInput), expected, msg)

    def testCase1(self):
        userInput = 2
        expected = [0, 1, 1]
        msg = f"Should be {expected} Got: {que.countBits(userInput)}"
        self.assertEqual(que.countBits(userInput), expected, msg)

    def testCase2(self):
        userInput = 1
        expected = [0, 1, 1, 2, 1, 2, 2, 3, 1, 2, 2, 3]
        msg = f"Should be {expected} Got: {que.countBits(userInput)}"
        self.assertEqual(que.countBits(userInput), expected, msg)

    def testCase3(self):
        userInput = 20
        expected = [0, 1, 1, 2, 1, 2, 2, 3, 1,
                    2, 2, 3, 2, 3, 3, 4, 1, 2, 2, 3, 2]
        msg = f"Should be {expected} Got: {que.countBits(userInput)}"
        self.assertEqual(que.countBits(userInput), expected, msg)

    def testCase4(self):
        self.assertEqual(que.countBits(1), [0, 1], "Should be [0, 1]")


# unittest.main()
