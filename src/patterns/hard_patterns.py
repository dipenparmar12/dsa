
def pattern1(n):
    """
        1
        0 1
        0 1 0
        1 0 1 0
        1 0 1 0 1
        0 1 0 1 0 1
        0 1 0 1 0 1 0
    """
    temp = 0
    for i in range(n):
        temp += 2
        print('', )
        for j in range(0, i + 1):
            print(f"{1 if temp % 2 == 0 else 0} ", end='')
            temp += 1
    print()

pattern1(5)
pattern1(6)
pattern1(7)


# def pattern2(n):
#     temp = 0
#     for i in range(n):
#         temp += 2
#         print(' ', )
#         for j in range(0, i + 1):
#             print(f"{1 if temp % 2 == 0 else 0} ", end='')
#             temp += 1
#     print()
#
# pattern2(5)
# pattern2(6)
# pattern2(7)
