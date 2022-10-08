def closestNum(nums: list[int], target: int) -> int:
    # return  min(myList, key=lambda num:abs(num-target))  # sorter version
    absolute_difference_function = lambda nums: abs(nums - target)
    closest_value = min(nums, key=absolute_difference_function)
    return closest_value


print(closestNum([3, 5, 6, 12, 4, 7, 9, 10, 16], 12))
print(closestNum([3, 5, 6, 12, 4, 7, 9, 10, 16], 8))


"""
T = 12
L = [3, 5, 6,12,4,7,9,10,16,-10]
        i
res = L[0] = (3)

12-3=9
12-5=7 (res)
12-6=6
12-12=0
12-4=8
12-7=5
12-9=3
12-10=2
12-16=4
12-(-10)=22

IF res and res > current:
    res = current
"""


# def closestNum(nums: list[int], target: int) -> int:
#     result = None
#     diff = None
#     for num in nums:
#         cur_diff = target - num
#         if diff and (0 < cur_diff < diff): # and (cur_diff != 0):
#             diff = cur_diff
#             result = num
#
#         if result is None:
#             result = num
#             diff = target - num
#
#     return result
