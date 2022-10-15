"""
@title: [TITLE]
@src: [URL]
@Difficulty: EASY/MEDIUM/HARD
 

[String]

--- Example 1:

--- Example 2:

--- Example 3:

@Score: 

"""

import unittest


def testMethod(input):
    return input


class TestCase(unittest.TestCase):
    def testCase0(self):
        userInput = [2, 1, 2, 1, 0, 1, 2]
        output = 2
        res = testMethod(userInput)
        msg = f"Should be {output} Got: {res}"
        self.assertEqual(res, output, msg)

    def testCase1(self):
        self.assertEqual(testMethod(5), 5, "Should be 5")
        self.assertEqual(testMethod(10), 100, "Should be 10")

    def testCase2(self):
        assert self.assertEqual(testMethod(
            [2, 4]) == 2, True, "Should be True")


unittest.main()

# Method                        Equivalent to
# .assertEqual(a, b)	          a == b
# .assertTrue(x)	              bool(x) is True
# .assertFalse(x)	              bool(x) is False
# .assertIs(a, b)	              a is b
# .assertIsNone(x)	            x is None
# .assertIn(a, b)	              a in b
# .assertIsInstance(a, b)	      isinstance(a, b)
