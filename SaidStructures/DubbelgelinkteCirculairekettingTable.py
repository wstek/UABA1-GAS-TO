from SaidStructures.DubbelgelinkteCirulaireKetting import *

class LinkedChainTable:
    def __init__(self):
        self.table = LinkedChain()

    def tableIsEmpty(self):  # {query}

        return self.table.isEmpty()

    def tableLength(self):  # {query}

        return self.table.getLength()

    def tableDelete(self, pos):

        return self.table.delete(pos)

    def tableRetrieve(self, pos):

        return self.table.retrieve(pos)

    def tableInsert(self, pos, item):

        return self.table.insert(pos, item)

    def save(self):

        return self.table.save()

    def load(self, lijst):

        return self.table.load(lijst)