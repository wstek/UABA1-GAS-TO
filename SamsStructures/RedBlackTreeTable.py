from SamsStructures.RedBlackTree import *


class RedBlackTreeTable:
    def __init__(self):
        self.RBT = RedBlackTree()

    def tableIsEmpty(self):  # {query}
        """
        zet een tableIsEmpty om naar een binzoekboom isEmpty
        :return isEmpty():
        """
        return self.RBT.isEmpty()

    def tableDelete(self, item):
        """
        zet een tableDelete om in een deleteItem
        @param item: searchkey
        :return deleteItem:
        """
        return self.RBT.deleteItem(item)

    def tableRetrieve(self, item):
        """
        zet een tableRetrieve om in een retrieveItem
        @param item: searchkey
        :return retrieveItem:
        """
        return self.RBT.retrieveItem(item)

    def tableInsert(self, item):
        """
        zet een tableInsert om in een insertItem
        @param item: searchkey
        :return insertItem:
        """
        return self.RBT.insertItem(item)

    def traverseTable(self, functie=None):
        """
        zet een traverseTable om in een inorderTraverse
        :return inorderTraverse:
        """
        return self.RBT.inorderTraverse(functie)

    def save(self):
        """
        zet een table save om in een RBT save
        :return RBT.save():
        """
        return self.RBT.save()

    def load(self, lijst):
        """
        zet een table load om in een RBT load
        @param lijst: de in te laden lijst
        :return RBT.load(lijst):
        """
        return self.RBT.load(lijst)
