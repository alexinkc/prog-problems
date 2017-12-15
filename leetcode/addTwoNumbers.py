class ListNode(object):
    """
    Node for a linked list
    """

    def __init__(self, val):
        self.val = val
        self.next = None


class Solution(object):
    """
    Solution for the leetcode problem https://leetcode.com/problems/add-two-numbers/description/
    """

    def __init__(self):
        self.nothing = None

    @classmethod
    def add_two_numbers(cls, list_1, list_2):
        """
        :type list_1: ListNode
        :type list_2: ListNode
        :rtype: ListNode
        """
        suml = ListNode(0)
        point = suml
        carry = 0
        sum_val = 0
        while list_1 != None or list_2 != None:
            sum_val = carry
            if list_1 != None:
                sum_val += list_1.val
                list_1 = list_1.next
            if list_2 != None:
                sum_val += list_2.val
                list_2 = list_2.next
            carry = int(sum_val/ 10)
            point.next = ListNode(int(sum_val% 10))
            point = point.next
        if carry == 1:
            point.next = ListNode(1)
        return suml.next


if __name__ == '__main__':
    A = ListNode(2)
    A.next = ListNode(4)
    A.next.next = ListNode(3)
    B = ListNode(5)
    B.next = ListNode(6)
    B.next.next = ListNode(4)
    RESULT = Solution().add_two_numbers(A, B)
    print("{0} -> {1} -> {2}".format(RESULT.val, RESULT.next.val, RESULT.next.next.val))
