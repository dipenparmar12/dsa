"""
@title: [TITLE]
@src: [URL]
@Difficulty: EASY/MEDIUM/HARD

@Definition:


--- Example 1:
--- Example 2:
--- Example 3:

@Score:

"""

import unittest


class Solution:
    def funName(self, n):
        pass


solution = Solution()

class TestProgram(unittest.TestCase):
    def testCase0(self):
        userInput = [2, 4, 1]
        expected = 2
        msg = f"Should be {expected} Got: {solution.funName(userInput)}"
        self.assertEqual(solution.funName(userInput), expected, msg)

    def testCase2(self):
        self.assertEqual(solution.funName(5), 5, "Should be 5")


unittest.main()

# """
# Method                        Equivalent to
# .assertEqual(a, b)	          a == b
# .assertTrue(x)	              bool(x) is True
# .assertFalse(x)	              bool(x) is False
# .assertIs(a, b)	              a is b
# .assertIsNone(x)	            x is None
# .assertIn(a, b)	              a in b
# .assertIsInstance(a, b)	      isinstance(a, b)
# """
