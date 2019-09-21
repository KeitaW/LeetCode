from typing import List
# Definition for a binary tree node.


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        pass


def print_binary_tree(root):
    node = root
    current = [node]
    while current:
        next_level = []
        for node in current:
            print(node.val, end=" ")
            if node.left:
                next_level.append(node.left)
            if node.right:
                next_level.append(node.right)
        print()
        current = next_level
