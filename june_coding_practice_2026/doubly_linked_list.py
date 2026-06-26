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
    


root = Node(5)
node1 = Node(10)
node2 = Node(20)
node3 = Node(8)

root.next = node1
node1.pre = root
node1.next = node2
node2.pre = node1
node2.next = node3
node3.pre = node2

node_to_add = Node(8)



add_node(node1,node_to_add)

print(root.val)
print(root.next.val)
print(root.next.next.val)

