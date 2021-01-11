from SteinStructures.LinkedChain import *

class LinkedChainTable:
    def __init__(self):
        self.ketting = LinkedChain()
        pass

    def destroyTable(self):
        return self.ketting.destroySearchTree()

    def tableIsEmpty(self):
        return self.ketting.isEmpty()

    def tableLength(self):
        return self.ketting.getLength()

    def tableInsert(self, item):
        return self.ketting.insert(item)

    def tableDelete(self, item):
        return self.ketting.delete(item)

    def tableRetrieve(self, value):
        return self.ketting.retrieve()

    def save(self):
        return self.ketting.save()

    def load(self, dict):
        return self.ketting.load(dict)