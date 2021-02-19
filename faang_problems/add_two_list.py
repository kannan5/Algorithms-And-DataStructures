class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        curr, run, carry = 0, True, 0
        res = None
        while run:
            if l1 is None and l2 is None:
                run = False
                if carry is 0:
                    curr = None

            if l1 is not None:
                curr += l1.val
                l1 = l1.next

            if l2 is not None:
                curr += l2.val
                l2 = l2.next

            curr += carry
            if curr < 10:
                carry = 0
            else:
                if curr == 10:
                    carry = 1
                else:
                    carry = curr // 10
                curr = curr % 10

            if curr is not None:
                if res is None:
                    res = ListNode(curr)
                    cur_node = res
                else:
                    cur_node.next = ListNode(curr)
                    cur_node = cur_node.next
                curr = 0

        return res


if __name__ == '__main__':
    L1 = ListNode(2)
    L1.next = ListNode(4)
    L1.next.next = ListNode(3)
    L2 = ListNode(5)
    L2.next = ListNode(6)
    L2.next.next = ListNode(4)
    a = Solution()
    b3 = a.addTwoNumbers(L1, L2)
