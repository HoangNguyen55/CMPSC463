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
        # race condition, return the other list if one of them is empty
        if not list1:
            return list2
        if not list2:
            return list1

        # variable to keep track of the starting point of the LinkList
        returnHead = ListNode()

        # temporary variable to keep track of the currentNode, NextNode of list 1, and NextNode of list 2.
        currentNode = returnHead
        nextNode1 = list1
        nextNode2 = list2

        while True:
            # check for the value of nextNode1 and nextNode2.
            if nextNode1.val <= nextNode2.val:
                # set the value of the currentNode to the value of the node that is smaller
                currentNode.val = nextNode1.val
                # move nextNode into the next item of the linklist
                nextNode1 = nextNode1.next
            else:
                currentNode.val = nextNode2.val
                nextNode2 = nextNode2.next

            # break out of the loop once one of the two LinkList hit the end
            if nextNode1 == None or nextNode2 == None:
                break

            # create an empty Node for the next node of the currentNode
            currentNode.next = ListNode()
            # move the currentNode into the newly created empty Node
            currentNode = currentNode.next


        # check to see what list hit the end.
        if nextNode1 == None:
            # then just add all the value of the other list into the currentNode
            while nextNode2 != None:
                currentNode.next = ListNode(nextNode2.val)
                nextNode2 = nextNode2.next
                currentNode = currentNode.next

        elif nextNode2 == None:
            while nextNode1 != None:
                currentNode.next = ListNode(nextNode1.val)
                nextNode1 = nextNode1.next
                currentNode = currentNode.next

        # return the starting point of the LinkList.
        return returnHead
