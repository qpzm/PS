class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def middleNode(head):
    middle = head
    while(head.next):
        middle = middle.next
        if head.next.next:
            head = head.next.next
        else:
            break
    return middle

# middle이 바뀌는 지점까지 갈 수 있는지만 확인하면 됨을 이용
def middleNode(head):
    fast = slow = head
    while fast and fast.next:
        fast, slow = fast.next.next, slow.next
    return slow
