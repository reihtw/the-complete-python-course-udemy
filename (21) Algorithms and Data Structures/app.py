from node import Node
from binary_tree import BinaryTree

tree = BinaryTree(Node(9))
tree.add(Node(5))
tree.add(Node(11))

tree.inorder()
tree.pre_order()
print(tree.find(11))
# print(tree.find(200)) -> LookUpError: A node with value 200 was not found.

print('--------')

tree = BinaryTree(Node(6))

nodes = [5, 3, 9, 7, 8, 7.5, 12, 11]

for n in nodes:
    tree.add(Node(n))

tree.delete(9)
tree.inorder()
tree.pre_order()