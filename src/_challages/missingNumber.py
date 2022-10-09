"""
@src: https://leetcode.com/problems/missing-number
@Difficulty: EASY

268. Missing Number
Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array.
Example 1:

Input: nums = [3,0,1]
Output: 2
Explanation: n = 3 since there are 3 numbers, so all numbers are in the range [0,3]. 2 is the missing number in the range since it does not appear in nums.
Example 2:

Input: nums = [0,1]
Output: 2
Explanation: n = 2 since there are 2 numbers, so all numbers are in the range [0,2]. 2 is the missing number in the range since it does not appear in nums.
Example 3:

Input: nums = [9,6,4,2,3,5,7,0,1]
Output: 8
Explanation: n = 9 since there are 9 numbers, so all numbers are in the range [0,9]. 8 is the missing number in the range since it does not appear in nums.

1st
Runtime: 304 ms, faster than 39.79% of Python3 online submissions for Missing Number.
Memory Usage: 15.3 MB, less than 41.89% of Python3 online submissions for Missing Number.
-
2nd
Runtime: 208 ms, faster than 71.13% of Python3 online submissions for Missing Number.
Memory Usage: 15.3 MB, less than 41.89% of Python3 online submissions for Missing Number.
-
3rd 
Runtime: 132 ms, faster than 98.32% of Python3 online submissions for Missing Number.
Memory Usage: 15.4 MB, less than 20.77% of Python3 online submissions for Missing Number.

6   1 2 3
10   1 2 3 4
15   1 2 3 4 5

Sn = n(n+1)/2
"""


def sumOf(n):
    # return n(n+1)/2
    return (n * (n + 1)) / 2


def missingNumber(nums):
    expected_sum = len(nums)*(len(nums)+1)//2
    actual_sum = sum(nums)
    return expected_sum - actual_sum

# def missingNumber(nums):
#     return ((len(nums) * (len(nums) + 1)) // 2) - sum(nums)
#     _sum = 0
#     for num in nums:
#         _sum += num
#     return int(sumOf(len(nums)) - _sum)
#     # return int(((len(nums) * (len(nums) + 1)) / 2) - _sum)


print(missingNumber([9, 6, 4, 2, 3, 5, 7, 0, 1]))
print(missingNumber([3, 0, 1]))

# Input: nums = [3,0,1]
# Output: 2
# Input: nums = [9,6,4,2,3,5,7,0,1]
# Output: 8

print(f"index.py::20 sumOf(1,3)", sumOf(3))
print(f"index.py::20 sumOf(1,5)", sumOf(5))
print(f"index.py::20 sumOf(1,100)", sumOf(10))

"""
1  2    3    4
n, n+1, n+2, n+3

a     = 1
diff    = 1
n       = 10

n/2 * (2a - (n-1) * d)
"""
# def sumOf(a, n, diff=1):
#     return (n / 2) * ((2 * a) + ((n - 1) * diff))
#
# print(f"index.py::20 sumOf(1,3)", sumOf(1, 3))
# print(f"index.py::20 sumOf(1,5)", sumOf(1, 5))
# print(f"index.py::20 sumOf(1,100)", sumOf(1, 10))
