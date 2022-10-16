"""
@title: 121. Best Time to Buy and Sell Stock
@src: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
@Difficulty: EASY

You are given an array prices where prices[i] is the price of a given stock on the ith day.
You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

Example 1:
Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.
Example 2:
Input: prices = [7,6,4,3,1]
Output: 0
Explanation: In this case, no transactions are done and the max profit = 0.


@Score:
Runtime: 1097 ms, faster than 92.64% of Python3 online submissions for Best Time to Buy and Sell Stock.
Memory Usage: 25 MB, less than 85.23% of Python3 online submissions for Best Time to Buy and Sell Stock.

Attempt-1: 3 Hours
Attempt-2: 3 Hours
Total: 6 Hours, using  Hint 


"""
import unittest


class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        profit = 0
        i = 0
        j = 1
        while i < len(prices) and j < len(prices):
            # print(i, j, prices[j], prices[i], prices, )
            diff = prices[j] - prices[i]
            if diff > profit:
                profit = diff

            if prices[j] > prices[i]:
                j += 1
            elif prices[j] < prices[i]:
                i += 1
            elif prices[j] == prices[i]:
                j += 1
        # print(f"main.py::87 i,j,profit,prices", i, j, profit, prices)
        return profit

    def maxProfitBruteForce(self, prices: list[int]) -> int:
        if len(prices) <= 1:
            return 0
        # print(len(prices))
        # prices = list(set(prices))
        maxProfit = 0
        for i in range(len(prices)):
            today = int(prices[i])
            for j in range(i + 1, len(prices)):
                nextDay = int(prices[j])
                if maxProfit < nextDay - today:
                    maxProfit = nextDay - today

        return maxProfit

    # def maxProfit1(self, prices: list[int]) -> int:
    #     if len(prices) <= 1:
    #         return 0

    #     mxIdx = len(prices) - 1
    #     mxVal = 0

    #     for i in range(0, len(prices)):
    #         if prices[i] > prices[mxIdx]:
    #             if i != 0:
    #                 mxIdx = i

    #     mxVal = prices[mxIdx]
    #     minVal = mxVal

    #     for num in prices[:mxIdx]:
    #         if num < minVal:
    #             minVal = num

    #     print(f"minVal:{minVal}, mxVal:{mxVal}, {prices}")
    #     profit = mxVal - minVal
    #     print("profit:", profit)

    #     return profit if profit > 0 else 0
    #     # [3, 3, 5, 0, 0, 3, 1, 4]


que = Solution()


# # Driver Code
# print(list(reversed(createList(-1, 1000))))

class TestMaxProfit(unittest.TestCase):
    def testCase0(self):
        userInput = [2, 4, 1]
        expected = 2
        msg = f"Should be {expected} Got: {que.maxProfit(userInput)}"
        self.assertEqual(que.maxProfit(userInput), expected, msg)

    def testCase1(self):
        userInput = [2, 1, 2, 1, 0, 1, 2]
        expected = 2
        msg = f"Should be {expected} Got: {que.maxProfit(userInput)}"
        self.assertEqual(que.maxProfit(userInput), expected, msg)

    def testCase11(self):
        userInput = [3, 3, 5, 0, 0, 3, 1, 4]
        expected = 4
        msg = f"Should be {expected} Got: {que.maxProfit(userInput)}"
        self.assertEqual(que.maxProfit(userInput), expected, msg)

    def testCase2(self):
        self.assertEqual(que.maxProfit([7, 1, 5, 3, 6, 4]), 5, "Should be 5")
        self.assertEqual(que.maxProfit([7, 6, 4, 3, 1]), 0, "Should be 0")
        self.assertEqual(que.maxProfit([1]), 0, "Should be 0")
        self.assertEqual(que.maxProfit([1, 2]), 1, "Should be 1")
        self.assertEqual(que.maxProfit([6, 14, 10]), 8, "Should be 8")
        self.assertEqual(que.maxProfit([3, 2, 6, 5, 0, 3]), 4, "Should be 4")

    # def createList(self, r1, r2):
    #     if (r1 == r2):
    #         return r1
    #     else:
    #         res = []
    #         while (r1 < r2 + 1):
    #             res.append(r1)
    #             r1 += 1
    #         return res

    # def testCasesLarge(self):
    #     userInput = list(reversed(self.createList(-1, 1000))) + [0,0,0,0,0]
    #     expected = 3
    #     msg = f"Should be {expected} Got: {que.maxProfit(userInput)}"
    #     self.assertEqual(que.maxProfit(userInput), expected, msg)
    #
    # def testCaseFile(self):
    #     file = open("testCases.txt", "r")
    #     file.seek(0)
    #     userInput = list(file.readline().strip().split(','))
    #     # print(userInput)
    #     file.close()
    #     expected = 10000
    #     msg = f"Should be {expected} Got: {que.maxProfit(userInput)}"
    #     self.assertEqual(que.maxProfit(userInput), expected, msg)


unittest.main()

# que.maxProfit([2, 3, 4, 5, 6, 3, 1])
# que.maxProfit([3, 2, 6, 5, 0, 3])
# que.maxProfit([7, 1, 5, 3, 6, 4])
