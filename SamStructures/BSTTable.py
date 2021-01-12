from SamStructures.BST import *


class BSTTable:
    def __init__(self):
        """
        zet een bst initializer om naar een bst initializer
        """
        self.searchTree = BST()

    def tableIsEmpty(self):  # {query}
        """
        zet een tableIsEmpty om naar een binzoekboom isEmpty
        :return isEmpty():
        """
        return self.searchTree.isEmpty()

    def tableDelete(self, item):
        """
        zet een tableDelete om in een searchTreeDelete
        :param item: searchkey
        :return searchTreeDelete:
        """
        return self.searchTree.searchTreeDelete(item)

    def tableRetrieve(self, item):
        """
        zet een tableRetrieve om in een searchTreeRetrieve
        :param item: searchkey
        :return searchTreeRetrieve:
        """
        return self.searchTree.searchTreeRetrieve(item)

    def tableInsert(self, item):
        """
        zet een tableInsert om in een searchTreeInsert
        :param item: searchkey
        :return searchTreeInsert:
        """
        return self.searchTree.searchTreeInsert(item)

    def traverseTable(self, functie=None):
        """
        zet een traverseTable om in een inorderTraverse
        :return inorderTraverse:
        """
        return self.searchTree.inorderTraverse(functie)

    def save(self):
        """
        zet een table save om in een searchTree save
        :return searchTree.save():
        """
        return self.searchTree.save()

    def load(self, lijst):
        """
        zet een table load om in een searchTree load
        :param lijst: de in te laden lijst
        :return searchTree.load(lijst):
        """
        return self.searchTree.load(lijst)
