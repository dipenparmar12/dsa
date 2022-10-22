
import unittest


def findSecondLargestNum(nums):
    if len(nums) == 0:
        return None

    # print("=" * 50)
    f = nums[0]
    s = nums[0]

    for n in nums:
        if f < n:
            f = n
        elif s < n:
            s = n
    # print("-" * 50)

    return s


class TestProgram(unittest.TestCase):
    def testCase0(self):
        userInput = [1, 2, 5, 6, 10, 7, 8, 9, 3, 4]
        expected = 9
        res = findSecondLargestNum(userInput)
        msg = f"Should be {expected} Got: {res}"
        self.assertEqual(res, expected, msg)

    def testCase1(self):
        userInput = [5, 4, 3, 6]
        expected = 5
        res = findSecondLargestNum(userInput)
        msg = f"Should be {expected} Got: {res}"
        self.assertEqual(res, expected, msg)

    def testCase2(self):
        userInput = [1]
        expected = 1
        res = findSecondLargestNum(userInput)
        msg = f"Should be {expected} Got: {res}"
        self.assertEqual(res, expected, msg)

    def testCase3(self):
        userInput = [9, 8, 1, 2, 3, 4, 5, 6, 7]
        expected = 8
        res = findSecondLargestNum(userInput)
        msg = f"Should be {expected} Got: {res}"
        self.assertEqual(res, expected, msg)

    def testCase3(self):
        userInput = []
        expected = None
        res = findSecondLargestNum(userInput)
        msg = f"Should be {expected} Got: {res}"
        self.assertEqual(res, expected, msg)


unittest.main()
