"""
@title: 136. Single Number
@src: https://leetcode.com/problems/single-number/
@Difficulty: EASY

Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.
You must implement a solution with a linear runtime complexity and use only constant extra space.

Example 1:
Input: nums = [2,2,1]
Output: 1
Example 2:
Input: nums = [4,1,2,1,2]
Output: 4
Example 3:
Input: nums = [1]
Output: 1

@Score: 
Runtime: 223 ms, faster than 67.41% of Python3 online submissions for Single Number.
Memory Usage: 16.7 MB, less than 83.57% of Python3 online submissions for Single Number.


"""

import os
os.system('clear')


def singleNumber(nums):
    temp = {}
    for num in nums:
        if num in temp:
            temp.pop(num)
        else:
            temp[num] = True

    res = list(temp.keys())[0]
    return res


# def singleNumber(nums):
#     temp = {}
#     for num in nums:
#         if num in temp:
#             temp.pop(num)
#         else:
#             temp[num] = True

#     res = list(temp.keys())[0]
#     return res


singleNumber([2, 2, 1])  # 1
singleNumber([4, 1, 2, 1, 2])  # 4
