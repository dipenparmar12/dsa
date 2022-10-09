

def inPlaceReverse(li):
    i = 0
    while i < len(li) // 2:
        print(li)
        t = li[i]
        li[i] = li[-(i + 1)]
        li[-(i + 1)] = t
        i += 1
    return li

# [1, 2, 3, 4] -> swap    i-0 <-> (last - 0)
# [4, 2, 3, 1] -> swap    i-1 <-> (last - 1)
# [1, 2, 3, 4] -> swap    i-2 <-> (last - 2)


print("[1, 2, 3, 4] -> ", inPlaceReverse([1, 2, 3, 4]))
print("[1, 2, 3, 4, 5] -> ", inPlaceReverse([1, 2, 3, 4, 5]))
print("[1, 2, 3, 4, 5, 6, 7, 8] -> ", inPlaceReverse([1, 2, 3, 4, 5, 6, 7, 8]))


"""

"""
