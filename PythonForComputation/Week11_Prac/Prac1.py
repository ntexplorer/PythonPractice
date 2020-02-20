import bstree

elements = [23, 45, 78, 12, 22, 90, 5]
bstree = bstree.BSTree()
for item in elements:
    bstree.add(item)

print(bstree)

unknown = bstree.unknown()
print(unknown)
