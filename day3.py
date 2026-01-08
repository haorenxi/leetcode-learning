## 1.leetcode21.合并两个有序链表
# 定义一个虚拟节点，指向-1，
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:

        dummy = ListNode(-1)
        cur = dummy
        while l1 and l2:
            if l1.val >= l2.val:
                cur.next = l1
                l1=l1.next
            else:
                cur.next = l2
                l2=l2.next
            cur = cur.next
        if l1:
            cur.next = l1
        if l2:
            cur.next = l2
        return dummy.next
#时间复杂度O(m+n)，空间复杂度O(1)

#2.leetcode 237.删除链表中的节点
class Solution:
    def deleteNode(self, node: ListNode) -> None:
        node.val = node.next.val
        node.next = node.next.next
#时间复杂度O(1)，空间复杂度O(1)

## 2.leetcode 328.奇偶链表
class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if head == None or head.next == None:
            return head
        odd = head
        even = head.next
        evenhead = even
        while even != None and even.next !=None:
            odd.next = even.next
            odd = odd.next
            even.next = odd.next
            even = even.next
            odd.next = evenhead
        return head
    
#时间复杂度O(n)，空间复杂度O(1)


