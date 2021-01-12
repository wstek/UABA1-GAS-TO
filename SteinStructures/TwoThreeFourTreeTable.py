from SteinStructures.TwoThreeFourTree import *


class TwoThreeFourTreeTable:
    def __init__(self):
        self.tabel = TwoThreeFourTree()

    def tableIsEmpty(self):
        """
        Is de TwoThreeFourTree leeg
        :param geen
        :return isEmpty (bool)
        """
        return self.tabel.isEmpty()

    def tableInsert(self, item):
        """
        insert een node op een bepaalde positie
        :param pos: possitie (int), item: waarde van de node
        :return insert gelukt (bool)
        """
        return self.tabel.insertItem(item)

    def tableRetrieve(self, key):
        return self.tabel.retrieveItem(key)

    def traverseTable(self, Functie):
        return self.tabel.inorderTraverse(self, Functie)

    def save(self):
        return self.tabel.save()

    def tableDelete(self, key):
        return self.tabel.deleteItem(key)

    def load(self, dict):
        return self.tabel.load(dict)
