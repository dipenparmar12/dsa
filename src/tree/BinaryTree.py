class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self) -> str:
        return str(self.val)


def binaryTreeFromArr(items):
    """
    Create BT from list of values.
    :param items:
    :return: TreeNode
    newTree = binaryTreeFromArr([5, 4, 8, 11, None, 13, 4, 7, 2, None, None, None, 1])
             5
            / \
           /   \
          4     8
         /     / \
        11    13  4
       / \         \
      7   2         1
    """
    length = len(items)
    root = TreeNode(items[0])
    queue = [root]
    i = 1

    while i < length:
        curr = queue.pop(0)
        # print(f"main.py::16 cur.val", curr.val, i)

        if i < length and items[i] is not None:
            leftNode = TreeNode(items[i])
            curr.left = leftNode
            queue.append(leftNode)
        i += 1

        if i < length and items[i] is not None:
            rightNode = TreeNode(items[i])
            curr.right = rightNode
            queue.append(rightNode)
        i += 1

    return root


# t0 = binaryTreeFromArr([1, 2, 3, 4, 5, 6])
"""
        01
     /     \      
    02       03   
  /   \     /   \ 
 04   05   06    
"""


# t1 = binaryTreeFromArr([1, 2, None, 4, 5, 6])
# print("1", t1.val)
# print("2", t1.left.val)
# print("None", t1.right)
#
# print("4", t1.left.left.val)
# print("5", t1.left.left.left.val)
# print("5", t1.left.right.val)
"""
        1
     /     \      
    2       
   / \      
  4   5
 /   
6    
"""

# t2 = binaryTreeFromArr([5, 4, 8, 11, None, 13, 4, 7, 2, None, None, None, 1])
# print(f"main.py::45 t2", t2)

"""
       5
      / \
     /   \
    4     8
   /     / \
  11    13  4
 / \         \
7   2         1
"""
