"""
ADT contract voor tabel, rood-zwartboom implementatie
"""

import BaseStructures.RedBlackTree as RedBlackTree

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