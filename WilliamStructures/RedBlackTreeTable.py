"""
ADT contract voor tabel, rood-zwartboom implementatie
"""

import WilliamStructures.RedBlackTree as RedBlackTree

def createTreeItem(key,val=None):
    return key, val

class RedBlackTreeTable:
    def __init__(self):
        """
        Creëer een lege tabel.
        """
        self.RBT = RedBlackTree.RedBlackTree()

    def load(self, RBTDict):
        """
        Laadt de tabel (rood-zwartboom implementatie) uit een dictionary.
        :param RBTDict: dictionary
        :return: None
        """
        self.RBT.load(RBTDict)

    def save(self):
        """
        Slaagt de tabel (rood-zwartboom implementatie) op in een dictionary.
        :return: dictionary
        """
        return self.RBT.save()

    def tableIsEmpty(self):     #{query}
        """
        Bepaalt of de tabel leeg is.
        :return: boolean
        """
        return self.RBT.isEmpty()

    def tableLength(self):      #{query}
        """
        Geeft de lengte van de tabel terug.
        :return: lengte van de tabel
        """
        return self.RBT.getNumberOfNodes()

    def tableInsert(self, newItem):
        """
        Voegt newItem toe aan een table met items met verschillende search key warden,
        verschillend van de search key van newItem. Success geeft weer of het toevoegen gelukt is.
        :return: success (boolean)
        """
        return self.RBT.insertItem(newItem)

    def tableDelete(self, searchKey):
        """
        Verwijdert een entry in de tabel mbv een zoeksleutel.
        :param searchKey: zoeksleutel (KeyType)
        :return: success (boolean)
        """
        return self.RBT.deleteItem(searchKey)

    def tableRetrieve(self, searchKey):
        """
        Geeft een waarde terug mbv de zoeksleutel.
        :param searchKey: zoeksleutel (KeyType)
        :return: tableItem (TableItemType), success (boolean)
        """
        return self.RBT.retrieveItem(searchKey)

    def traverseTable(self, FunctionType):
        """
        Doorloopt alle items in de tabel.
        :param FunctionType: functie dat toegepast wordt op de items van de tabel
        :return: None
        """
        self.RBT.inorderTraverse(FunctionType)

if __name__ == "__main__":
    t = RedBlackTreeTable()
    print(t.tableIsEmpty())
    print(t.tableInsert(createTreeItem(8,8)))
    print(t.tableInsert(createTreeItem(5,5)))
    print(t.tableInsert(createTreeItem(10,10)))
    print(t.tableInsert(createTreeItem(15,15)))
    print(t.tableIsEmpty())
    print(t.tableRetrieve(5)[0])
    print(t.tableRetrieve(5)[1])
    t.traverseTable(print)
    print(t.save())
    t.load({'root': 8,'color': 'black','children':[{'root':5,'color': 'black'},{'root':10,'color': 'black'}]})
    t.tableInsert(createTreeItem(15,15))
    print(t.tableDelete(0))
    print(t.save())
    print(t.tableDelete(10))
    print(t.save())