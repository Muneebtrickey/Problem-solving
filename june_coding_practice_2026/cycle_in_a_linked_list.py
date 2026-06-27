# find cycyle in the linked list
class Node:
    def __init__(self,val):
        self.val = val
        self.next = None


def find_cycle(head):
    # using slow and fast pointer
    slow = head
    fast = head 

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            return True
    

    return False  


head = Node(1)
node1 = Node(2)
node3 = Node(3)

head.next = node1
node1.next = node3
node3.next = head

print(find_cycle(head))


