from SamStructures.DubbelgelinkteCirulaireKetting import *


class DubbelgelinkteCirulaireKettingTable():
    def __init__(self):
        self.theChain = LinkedChain()

    def tableIsEmpty(self):  # {query}
        """
        zet een tableIsEmpty om in een LinkedChain isEmpty
        :return isEmpty():
        """
        return self.theChain.isEmpty()

    def tableLength(self):  # {query}
        """
        zet een tableLength om in een LinkedChain getLength
        :return getLength():
        """
        return self.theChain.getLength()

    def tableDelete(self, pos):
        """
        zet een tableDelete om in een LinkedChain delete
        :param pos: position of the item to delete
        :return delete(pos):
        """
        return self.theChain.delete(pos)

    def tableRetrieve(self, pos):
        """
        zet een tableRetrieve om in een LinkedChain retrieve
        :param pos: position of the item to delete
        :return retrieve(pos):
        """
        return self.theChain.retrieve(pos)

    def tableInsert(self, pos, item):
        """
        zet een tableInsert om in een LinkedChain insert
        :param pos: position of the item to insert
        :param item: the item to insert
        :return insert(pos, item):
        """
        return self.theChain.insert(pos, item)

    def traverseTable(self, functie=None):
        """
        zet een traverseTable om in een LinkedChain traverse
        :return traverse():
        """
        return self.theChain.traverse(functie)

    def save(self):
        """
        zet een table save om in een LinkedChain save
        :return save():
        """
        return self.theChain.save()

    def load(self, lijst):
        """
        zet een table load om in een LinkedChain load
        :return load():
        """
        return self.theChain.load(lijst)

