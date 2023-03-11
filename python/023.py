# You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.
# Merge all the linked-lists into one sorted linked-list and return it.
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

import heapq


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []
        new_head = ListNode()
        current_element = new_head
        pointers = {i: node for i, node in enumerate(lists) if node is not None}
        if pointers:
            for i, q in pointers.items():
                heap.append((q.val, i))
                pointers[i] = q.next
            heapq.heapify(heap)
            while heap:
                value, i = heapq.heappop(heap)
                current_element.next = ListNode(value)
                current_element = current_element.next
                if pointers[i]:
                    heapq.heappush(heap, (pointers[i].val, i))
                    pointers[i] = pointers[i].next
        return new_head.next
