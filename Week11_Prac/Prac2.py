import bstree
# test the BSTree
elements = [23, 45, 78, 12, 22, 90, 5]
bstree = bstree.BSTree()
for item in elements:
    bstree.add(item)

print(bstree)
print('The height of the tree is: ', bstree.height())
print('The smallest element is: ', bstree.getMin())
