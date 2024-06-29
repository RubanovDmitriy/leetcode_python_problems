from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def inorder_traversal(root: Optional[TreeNode]) -> list[int]:
    res = []

    def inorder(root):
        if not root:
            return
        inorder_traversal(root.left)
        res.append(root.val)
        inorder_traversal(root.right)

    inorder(root)
    return res





