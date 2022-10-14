"""
@title: 70. Climbing Stairs
@src: https://leetcode.com/problems/climbing-stairs
@Difficulty: EASY
 
You are climbing a staircase. It takes n steps to reach the top.
Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?


Example 1:
Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps
Example 2:
Input: n = 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step

@Score: 
Runtime: 28 ms, faster than 97.03% of Python3 online submissions for Climbing Stairs.
Memory Usage: 13.8 MB, less than 56.98% of Python3 online submissions for Climbing Stairs.

"""

import os
os.system('clear')


"""


"""


class Solution:
    def climbStairsRes(self, n: int, DP={}) -> int:
        if n == 1:
            return 1
        if n == 2:
            return 2
        if n in DP:
            return DP[n]

        stepOne = self.climbStairsRes(n - 1, DP)
        stepTwo = self.climbStairsRes(n - 2, DP)
        DP[n] = stepOne + stepTwo

        return stepOne + stepTwo

    def climbStairs(self, n: int) -> int:
        return self.climbStairsRes(n)

    def climbStairs_internet(self, n: int) -> int:
        if n == 1:
            return 1
        one = 1
        two = 1
        total = 0
        for i in range(0, n-1):
            total = one + two
            two = one
            one = total
        return total

    def climbStairs_internet_(self, n: int) -> int:
        dp = [-1]*46

        if n < 3:
            return n

        for i in range(3):
            dp[i] = i

        for i in range(3, n+1):
            dp[i] = dp[i-1] + dp[i-2]
        return dp[n]

    def climbStairs_internet__(self, n: int) -> int:
        memo = [0] * (n+1)
        memo[0] = 1
        memo[1] = 1
        for i in range(2, n+1):
            memo[i] = memo[i-1] + memo[i-2]
        return memo[n]


sol = Solution()

print(sol.climbStairs(2))  # 2
print(sol.climbStairs(3))  # 2
print(sol.climbStairs(4))  # 5
print(sol.climbStairs(5))  # 8
print(sol.climbStairs(6))  # 13
print(sol.climbStairs(7))  # 21
print(sol.climbStairs(8))  # 34
print(sol.climbStairs(34))  # 34

# def climbStairs(n: int, position=0) -> int:
#     if position > n:
#         return 0
#     if position == n:
#         return 1
#
#     stepOne = climbStairs(n - 1, position)
#     stepTwo = climbStairs(n - 2, position)
#     return stepOne + stepTwo
