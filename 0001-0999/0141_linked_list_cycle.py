class ListNode:
    def __init__(self, value):
        self.value = value
        self.next = None


def hasCycle(head: ListNode) -> bool:
    slow_pointer = fast_pointer = head
    while fast_pointer and fast_pointer.next:
        slow_pointer = slow_pointer.next
        fast_pointer = fast_pointer.next.next
        if slow_pointer == fast_pointer:
            return True
    return False



# Create the linked list
head = ListNode(3)
node2 = ListNode(2)
node3 = ListNode(0)
node4 = ListNode(-4)

head.next = node2
node2.next = node3
node3.next = node4

# Create the cycle: node4 points back to node2 (position 1)
node4.next = node2

# Check if the list has a cycle
print(hasCycle(head))