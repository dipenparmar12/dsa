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

Attempt-1: 3 Hours
"""
import unittest


class Solution:
    def maxProfit1(self, prices: list[int]) -> int:
        if len(prices) <= 1:
            return 0
        buy = prices[0]
        profit = 0
        day = 0

        for i in range(0, len(prices) - 1):
            today = prices[i]
            if buy > today:
                buy = today
                day = i

        print(f"LOG1: ", buy, profit, day, prices)

        for i in range(day, len(prices)):
            salePriceToday = prices[i]
            profitToday = salePriceToday - buy
            if profit < profitToday:
                profit = profitToday

        # print(f"LOG2: ", buy, profit, day, prices)

        return profit

    def maxProfit2(self, prices: list[int]) -> int:
        print(f"main.py::50 prices", prices)
        if len(prices) <= 1:
            return 0
        buy = prices[0]
        sale = 0
        profit = 0
        day = 0

        for i in range(0, len(prices) - 1):
            today = prices[i]
            if buy > today:
                buy = today
                day = i

        for j in range(day + 1, len(prices)):
            futurePrice = prices[j]
            if profit < futurePrice - buy:
                profit = futurePrice - buy

        print(day, buy, sale, profit, prices)
        return profit if profit > 0 else 0

    def maxProfit(self, prices: list[int]) -> int:
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


que = Solution()


class TestMaxProfit(unittest.TestCase):
    def testCase(self):
        userInput = [2, 4, 1]
        output = 2
        msg = f"Should be {output} Got: {que.maxProfit(userInput)}"
        self.assertEqual(que.maxProfit(userInput), output, msg)

    def testCase1(self):
        userInput = [2, 1, 2, 1, 0, 1, 2]
        output = 2
        msg = f"Should be {output} Got: {que.maxProfit(userInput)}"
        self.assertEqual(que.maxProfit(userInput), output, msg)

    def testCases(self):
        self.assertEqual(que.maxProfit([7, 1, 5, 3, 6, 4]), 5, "Should be 5")
        self.assertEqual(que.maxProfit([7, 6, 4, 3, 1]), 0, "Should be 0")
        self.assertEqual(que.maxProfit([1]), 0, "Should be 0")
        self.assertEqual(que.maxProfit([1, 2]), 1, "Should be 1")
        self.assertEqual(que.maxProfit([6, 14, 10]), 8, "Should be 8")
        self.assertEqual(que.maxProfit([3, 2, 6, 5, 0, 3]), 4, "Should be 4")

    def testCaseLarge(self):
        file = open("testCases.txt", "r")
        file.seek(0)
        userInput = list(file.readline().strip().split(','))
        # print(userInput)
        file.close()
        output = 10000
        msg = f"Should be {output} Got: {que.maxProfit(userInput)}"
        self.assertEqual(que.maxProfit(userInput), output, msg)
        print("DONE ")


unittest.main()
