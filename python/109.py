# Given the head of a singly linked list where elements are sorted in ascending order,
# convert it to a  height-balanced binary search tree.
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        sorted_array = []
        while head:
            sorted_array.append(head.val)
            head = head.next
        
        def buildBST(l, r):
            if l > r:
                return None
            mid = (l + r) // 2
            node = TreeNode(sorted_array[mid])
            if l == r:
                return node
            node.left = buildBST(l, mid - 1)
            node.right = buildBST(mid + 1, r)
            return node
        
        return buildBST(0, len(sorted_array) - 1)
