"""
@title: 448. Find All Numbers Disappeared in an Array
@src: https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/
@Difficulty: EASY

Given an array nums of n integers where nums[i] is in the range [1, n], return an array of all the integers in the range [1, n] that do not appear in nums.

Example 1:
Input: nums = [4,3,2,7,8,2,3,1]
Output: [5,6]
Example 2:
Input: nums = [1,1]
Output: [2]

Constraints:
n == nums.length
1 <= n <= 105
1 <= nums[i] <= n
 

@Score: 
"""


def findDisappearedNumbers(nums: list[int]):
    # Created expected array from 1 to length of array
    expectedArray = list(range(1, len(nums)+1))
    # Subtract the expected array from given array
    result = list(set(expectedArray) - set(nums))

    return result


findDisappearedNumbers([4, 3, 2, 7, 8, 2, 3, 1])  # [5,6]
findDisappearedNumbers([1, 1])  # [2]


# Approach-2
# def findDisappearedNumbers(nums: list[int]):
#     arr = set(nums)
#     res = []
#     for i in range(1, len(nums) + 1):
#         if i not in arr:
#             res.append(i)

#     print(res)
#     return res


# Time Limit Exceeded
# Approach-1
# def findDisappearedNumbers(nums: list[int]):
#     res = []
#     for i in range(1, len(nums) + 1):
#         pass
#         if i not in nums:
#             res.append(i)
#
#     print(list(res))
#     return list(res)
#
