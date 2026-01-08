public class ReverJava{
    public static class Node{
        public int val;
        public ListNode next;
        public ListNode(int val,ListNode next){
            this.val = val;
            this.next = next;
        }
    }
    // 单链表反转
    public static ReverseList(ListNode head){
        ListNode pre = null;
        ListNode next = null; 
        while(head != null){
            next = head.next;
            head.next = pre;
            pre = head;
            head = next;
        }
        return pre;
    }

    // 双链表反转
    //// 定义双链表结构
    public static class DouleListNode{
        public int val;
        public doubleListNode next;
        public doubleListNode last; 
        public static ReverseDoubleNode(ListNode head){
            DoubleListNode pre = null;
            DoubleListNode next = null;
            while(head != null){
                next = head.next;
                head.next = pre;
                head.last = next;
                pre = head;
                head = next; 
            }
            return pre;
        }
    }

    // 合并俩有序链表

}

public class MergeTwoLists{
    // 定义俩链表
    public static ListNode {
        public int val;
        public ListNode next;

        public ListNode(int val){
            this.val = val;
            this.next = next;
        }

        public ListNode(int val){
            this.val = val;
        }
    }
// 思路就是定义俩游针，游针a指向俩链表中head最小的数据；游针b指向俩链表中head较大的数据
// 当cur1和cur2非空时，循环遍历数据大小，比较cur1和cur2大小，将较小的节点接到合并链表的尾部，然后将对应的游针后移一位
// 当cur1或者cur2为空时，就摘出来非空链表合并到尾部
// 用 pre 来穿数据，head一直指向头保持不变
    class Solution {
        public static ListNode(ListNode head1,ListNode head2){
            if (head1 == null || head2 == null){
                return head1 == null ? head2 :head1;
            }
            ListNode head = head1 <= head2 ? head1 : head2;
            LisrNode cur1 = head.next;
            ListNode cur2 = head1 <= head2 ? head2 : head1;  
            ListNode pre = head;
            while(head1 != null && head2 != null){
                if(cur1.val <= cur2.val){
                    pre.next = cur1;
                    cur1 = cur1.next;
                }else{
                    pre.next = cur2;
                    cur2 = cur2.next;
                }
                pre = pre.next;
            }
            pre.next = cur1 != null ? cur1 :cur2;
            return head;
        }
    }
}