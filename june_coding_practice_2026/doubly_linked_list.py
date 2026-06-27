class Node:
    def __init__(self,val):
        self.val = val
        self.next = None
        self.pre = None


def add_node(node, node_to_add):
    pre_node = node.pre
    node_to_add.next = node
    node_to_add.pre = pre_node
    pre_node.next = node_to_add
    node.pre = node_to_add


def delete_node(node):
    pre_node = node.pre
    next_node = node.next
    pre_node.next = next_node
    next_node.pre = pre_node







# root = Node(5)
# node1 = Node(10)
# node2 = Node(20)
# node3 = Node(8)

# root.next = node1
# node1.pre = root
# node1.next = node2
# node2.pre = node1
# node2.next = node3
# node3.pre = node2

# node_to_add = Node(8)



# add_node(node1,node_to_add)

# print(root.val)
# print(root.next.val)
# print(root.next.next.val)






# adding sential nodes which is head and tail to avoid errors when node is not present

def add_at_end(node_to_add):
    node_to_add.next = tail
    node_to_add.pre = tail.pre
    tail.pre.next = node_to_add
    tail.pre = node_to_add


def remove_from_end():
    if head.next == tail:
        return 
    
    node_to_remove = tail.pre
    node_to_remove.pre.next = tail
    tail.pre = node_to_remove.pre


def add_to_start(node_to_add):
    node_to_add.pre = head
    node_to_add.next = head.next
    head.next.pre = node_to_add
    head.next = node_to_add


def remove_from_start():
    if head.next == tail:
        return 
    
    node_to_remove = head.next
    node_to_remove.next.pre = head
    head.next = node_to_remove.next
    








head = Node(None)
tail = Node(None)

head.next = tail
tail.pre = head

add_at_end(Node(5))
add_at_end(Node(10))
add_at_end(Node(15))
add_at_end(Node(20))

print(head.next.val)
print(tail.pre.val)

# after deleting last element 
remove_from_end()

print(tail.pre.val)
