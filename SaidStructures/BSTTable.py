from SaidStructures.BST import *


class BSTTable:
    def __init__(self):
        self.tabel = BST()

    def tableIsEmpty(self):
        return self.tabel.isEmpty()

    def tableInsert(self, item):
        return self.tabel.searchTreeInsert(item)

    def tableDelete(self, key):
        return self.tabel.searchTreeDelete(key)

    def tableRetrieve(self, searchkey):
        return self.tabel.searchTreeRetrieve(searchkey)

    def traverseTable(self, FunctieType):
        return self.tabel.inorderTraverse(FunctieType)

    def save(self):
        return self.tabel.save()

    def load(self, map):
        return self.tabel.load(map)

"""
t = BSTTable()
print(t.tableIsEmpty())
print(t.tableInsert(createTreeItem(8, 8)))
print(t.tableInsert(createTreeItem(5, 5)))
print(t.tableIsEmpty())
print(t.tableRetrieve(5)[0])
print(t.tableRetrieve(5)[1])
t.traverseTable(print)
print(t.save())
t.load({'root': 10, 'children': [{'root': 5}, None]})
t.tableInsert(createTreeItem(15, 15))
print(t.tableDelete(0))
print(t.save())
print(t.tableDelete(10))
print(t.save())
"""