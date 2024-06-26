# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        list3 = []
        for i in range(len(list1)):
            if list1[i] > list2[i]:
                list2[i].next(list1[i])
                list3.append(list2[i])
            else:
                list1[i].next(list2[i])
                list3.append(list1[i])
        return list3
solution = Solution()
list1 = list([1,2,4])
list2 = list([1, 3, 4])
print(list1)
print(solution.mergeTwoLists(list1, list2))
# print(solution.mergeTwoLists([1,2,4], []))