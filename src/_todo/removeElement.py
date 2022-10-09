# @see: https://leetcode.com/problems/3sum-closest/

def removeElement(nums, val) -> int:
    for i in range(0, len(nums)):
        # print(i)
        if nums[i] == val:
            nums[i] = '_'

    print(nums)

    for i in range(0, len(nums) - 1):
        pass

    print(nums)
    return len(nums)


removeElement([3, 2, 2, 3], 3)

# from dsa.getCombinations import getCombinationsRec
#
# """
# [1 2 3]
# Res -> (2^n ->  2^3  ->   8)
#
# [1 2 3 4]
# Res -> (2^n ->  2^4   ->   16)
#
# """
#
#
# def comb(li, arr=False):
#     pass
#     res = [[]]
#
#     # Array combinations
#     if arr:
#         for item in li:
#             copy = [*res]
#             for prefix in copy:
#                 res.append([*prefix, *item])
#         return res
#
#     # String combinations
#     for item in li:
#         copy = [*res]
#         for prefix in copy:
#             print(f"index.py::19 item {[*prefix, *item]} {[*item]}")
#             res.append([''.join(map(str, [*prefix, item]))])
#
#     print(len(res))
#     return res
#
#
# print(f"index.py::16 ->", comb(list("123")))
# # print(f"index.py::16 ->", comb(list("1234")))
#
# # res = getCombinationsRec([1, 2, 3])
# # print(f"index.py::10 len(res), res", len(res), res)
#
# # res = getCombinationsRec([1, 2, 3, 4])
# # print(f"index.py::10 len(res), res", len(res), res)
# # # 16 -> [[], [4], [3], [4, 3], [2], [4, 2], [3, 2], [4, 3, 2], [1], [4, 1], [3, 1], [4, 3, 1], [2, 1], [4, 2, 1], [3, 2, 1], [4, 3, 2, 1]]
# #
# # res = getCombinationsRec(list("ABC"))
# # # 8 ->  [[], ['C'], ['B'], ['C', 'B'], ['A'], ['C', 'A'], ['B', 'A'], ['C', 'B', 'A']]
# # print(f"index.py::10 len(res), res", len(res), res)
# #
# # """
# # [1 2 3 4, 5] => 32
# #  ->  2^5  ->   16
# # """
# # print(f"index.py::19 ", 2 * 2 * 2 * 2 * 2)
#
#
# """js
#
# const powerset = (array) => { // O(2^n)
# 	const results = [[]];
# 	for (const value of array) {
# 		const copy = [...results]; // See note below.
# 		for (const prefix of copy) {
# 			results.push(prefix.concat(value));
# 		}
# 	}
# 	return results;
# };
#
# console.log(
# 	powerset(['A', 'B', 'C'])
# );
#
# function combinations(str) {
#     var fn = function(active, rest, a) {
#         if (!active && !rest)
#             return;
#         if (!rest) {
#             a.push(active);
#         } else {
#             fn(active + rest[0], rest.slice(1), a);
#             fn(active, rest.slice(1), a);
#         }
#         return a;
#     }
#     return fn("", str, []);
# }
#
# function getCombinations(chars) {
#   var result = [];
#   var f = function(prefix, chars) {
#     for (var i = 0; i < chars.length; i++) {
#       result.push(prefix + chars[i]);
#       f(prefix + chars[i], chars.slice(i + 1));
#     }
#   }
#   f('', chars);
#   return result;
# }
#
#
# function string_recurse(active, rest) {
#     if (rest.length == 0) {
#         console.log(active);
#     } else {
#         string_recurse(active + rest.charAt(0), rest.substring(1, rest.length));
#         string_recurse(active, rest.substring(1, rest.length));
#     }
# }
# string_recurse("", "abc");
#
#
# """
