from SteinStructures.BST import *

class BSTTable:
    def __init__(self):
        self.bst = BST()
        pass

    def destroyTable(self):
        return self.bst.destroySearchTree()

    def tableIsEmpty(self):
        return self.bst.isEmpty()

    def tableLength(self):
        return self.bst.child_count()

    def tableInsert(self, item):
        return self.bst.searchTreeInsert(item)

    def tableDelete(self, item):
        return self.bst.searchTreeDelete(item)

    def tableRetrieve(self, value):
        return self.bst.searchTreeRetrieve()