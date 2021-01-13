from SaidStructures.TwoThreeFourTree import *


class TwoThreeFourTreeTable:
    def __init__(self):
        self.tabel = TwoThreeFourTree()

    def tableIsEmpty(self):
        return self.tabel.isEmpty()

    def tableInsert(self, item):
        return self.tabel.insertItem(item)

    def tableRetrieve(self, key):
        return self.tabel.retrieveItem(key)

    def traverseTable(self, Functie):
        return self.tabel.inorderTraverse(Functie)

    def save(self):
        return self.tabel.save()

    def tableDelete(self, key):
        return self.tabel.deleteItem(key)

    def load(self, dict):
        return self.tabel.load(dict)

    def tableLength(self):      #{query}
        return self.tabel.getLength()