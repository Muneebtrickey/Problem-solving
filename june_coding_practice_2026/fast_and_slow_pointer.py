class Node:
    def __init__(self,val):
        self.val = val
        self.next = None


root = Node(1)
node1 = Node(2)
node2 = Node(3)
node3 = Node(4)
node4 = Node(5)

root.next = node1
node1.next = node2
node2.next = node3
node3.next = node4


def find_middle_element(head):
    slow = head 
    fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    
    return slow.val


print(find_middle_element(root))