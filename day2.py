#1.判断两个不同链表是否有相交点
#定义两个不同的指针，其中一个指着链表A的头，另外一个指着链表B的头，pointA和pointB往后移动，pointA遍历完A又回到B的头遍历到C1，走的总步数为a+(b-c)，pointB遍历完B又回到A的头遍历到C1，走的总步数为b+(a-c)，当两个指针相遇时，就是相交点C1
#若俩指针都走完了链表A和B还没有相遇，则说明两个链表不相交，即此时c=0；c!=0时，两个指针必然会在相交点相遇，此时我们找到c1
from pyparsing import Optional


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        # 边界判断
        if not headA or not headB:
            return None
        #也可以用下面的直白方式判断头节点是否为None
        # if (headA == None or headB == None):
        #     return None
        pointA = headA
        pointB = headB
        while pointA != pointB:
            pointA = pointA.next if pointA else headB
            pointB = pointB.next if pointB else headA
        return pointA
#时间复杂度O(m+n)，空间复杂度O(1)

#2.Leetcode 19.删除链表的倒数第N个节点
# 定义一个虚拟节点dummy,指向该位置，然后定义一个快指针fast，通过for循环在距离n的位置处，再定义一个慢指针slow，指向head处
# 然后让快指针和慢指针同时往后移动，直到快指针到达链表null，此时慢指针所处节点就是要删除的节点
# 将dummy的next更新为slow的next即可实现删除倒数第N个节点的功能
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(-1)
        dummy.next = head
        former = head
        cur = head
        latter = dummy
        for _ in range(n):
            former = former.next
        while former:
            former = former.next
            latter = cur
            cur = cur.next
        latter.next = cur.next
        return dummy.next

#该方法是往前了一个  
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        left = right = dummy = ListNode(next=head)
        for _ in range(n):
            right = right.next
        while right:
            right = right.next
            left = left.next
        left.next = left.next.next
        return dummy.next

#时间复杂度O(L)，空间复杂度O(1)

#3.leetcode 203.移除链表元素
#定义一个虚拟节点dummy，指向-1，next为head，然后定义一个指针cur，指向dummy
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        dummy = ListNode(next=head)
        pre = dummy
        cur = head
        if head == None:
            return head
        while cur:
            if cur.val == val:
                pre.next = cur.next
            else:
                pre = cur
            cur = cur.next
        return dummy.next
#时间复杂度O(n)，空间复杂度O(1)   

#4.leetcode 24.两两交换链表中的节点
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #边界情况单拎出来
        if head == None or head.next == None:
            return head
        subHead = swapPairs(head.next.next)
        newHead = head.next
        head.next = subHead
        newHead.next = head
        return newHead
#时间复杂度O(n)，空间复杂度O(n)递归栈空间