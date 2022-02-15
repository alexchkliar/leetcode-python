# # A Binary tree node
# class Node:

#     # Constructor to create a new node
#     def __init__(self, data):
#         self.data = data
#         self.left = None
#         self.right = None

# # Function to get the count of leaf nodes in binary tree
# def getLeafCount(node):
#     if node is None:
#         return 0
#     if(node.left is None and node.right is None):
#         return 1
#     else:
#         return getLeafCount(node.left) + getLeafCount(node.right)


# # Driver program to test above function
# root = Node(1)
# root.left = Node(2)
# root.right = Node(3)
# root.left.left = Node(4)
# root.left.right = Node(5)

# print ("Leaf count of the tree is %d" %(getLeafCount(root)))


# A Binary tree node, lfet count

# class Node:

#     # Constructor to create a new node
#     def __init__(self, data):
#         self.data = data
#         self.left = None
#         self.right = None

# # Function to get the count of leaf nodes in binary tree
# def getLeftLeafCount(node, cumul):
#     if node is None:
#         return 0
#     if(node.left is None and node.right is None):
#         return cumul
#     if(node.left):
#         return getLeftLeafCount(node.left, cumul + 1) + getLeftLeafCount(node.right, 0)

# # Driver program to test above function
# root = Node(1)
# root.left = Node(2)
# root.right = Node(3)
# root.right.left = Node(4)
# root.right.right = Node(5)
# root.left.left = Node(6)
# root.left.right = Node(7)
# root.left.right.left = Node(8)

# print ("Leaf count of the tree is %d" %(getLeftLeafCount(root, 0)))

class Node:
    # A utility function to create a new node
    def __init__(self ,key):
        self.data = key
        self.left = None
        self.right = None

def getfullCount(root):
    # Base Case
    if root is None:
        return 0

    # Create an empty queue for level order traversal
    queue = []

    # Enqueue Root and initialize count
    queue.append(root)

    count = 0 #initialize count for full nodes
    while(len(queue) > 0):
        node = queue.pop(0)

        # if it is full node then increment count
        if node.left is not None and node.right is not None:
            count = count+1

        # Enqueue left child
        if node.left is not None:
            queue.append(node.left)

        # Enqueue right child
        if node.right is not None:
            queue.append(node.right)

    return count

# Driver Program to test above function
root = Node(2)
root.left = Node(7)
root.right = Node(5)
root.left.right = Node(6)
root.left.right.left = Node(1)
root.left.right.right = Node(11)
root.right.right = Node(9)
root.right.right.left = Node(4)
