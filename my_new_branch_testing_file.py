class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def find_min_in_tree(root):
    if root is None:
        return None
    current = root
    while current.left:
        current = current.left
    return current.val

# Example usage:
# Constructing a simple BST
#       5
#      / \
#     3   7
#    /
#   2
root = TreeNode(5)
root.left = TreeNode(3)
root.right = TreeNode(7)
root.left.left = TreeNode(2)

print("Smallest element in the tree:", find_min_in_tree(root))