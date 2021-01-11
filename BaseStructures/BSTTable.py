"""
ADT contract voor tabel, binaire zoekboom implementatie
"""

from BaseStructures import BST


def createTreeItem(key,val=None):
    return key, val

class BSTTable:
    def __init__(self):
        """
        Creëer een lege tabel.
        """
        self.BST = BST.BST()

    def load(self, BSTDict):
        """
        Laadt de tabel (binaire zoekboom implementatie) uit een dictionary.
        :param BSTDict: dictionary
        :return: None
        """
        self.BST.load(BSTDict)

    def save(self):
        """
        Slaagt de tabel (binaire zoekboom implementatie) op in een dictionary.
        :return: dictionary
        """
        return self.BST.save()

    def tableIsEmpty(self):     #{query}
        """
        Bepaalt of de tabel leeg is.
        :return: boolean
        """
        return self.BST.isEmpty()

    def tableLength(self):      #{query}
        """
        Geeft de lengte van de tabel terug.
        :return: lengte van de tabel
        """
        return self.BST.getNumberOfNodes()

    def tableInsert(self, newItem):
        """
        Voegt newItem toe aan een table met items met verschillende search key warden,
        verschillend van de search key van newItem. Success geeft weer of het toevoegen gelukt is.
        :return: success (boolean)
        """
        return self.BST.searchTreeInsert(newItem)

    def tableDelete(self, searchKey):
        """
        Verwijdert een entry in de tabel mbv een zoeksleutel.
        :param searchKey: zoeksleutel (KeyType)
        :return: success (boolean)
        """
        return self.BST.searchTreeDelete(searchKey)

    def tableRetrieve(self, searchKey):
        """
        Geeft een waarde terug mbv de zoeksleutel.
        :param searchKey: zoeksleutel (KeyType)
        :return: tableItem (TableItemType), success (boolean)
        """
        return self.BST.searchTreeRetrieve(searchKey)

    def traverseTable(self, FunctionType):
        """
        Doorloopt alle items in de tabel.
        :param FunctionType: functie dat toegepast wordt op de items van de tabel
        :return: None
        """
        l = self.BST.traverse()
        for i in l:
            FunctionType(i)

if __name__ == "__main__":
    t = BSTTable()
    print(t.tableIsEmpty())
    print(t.tableInsert(createTreeItem(8,8)))
    print(t.tableInsert(createTreeItem(5,5)))
    print(t.tableIsEmpty())
    print(t.tableRetrieve(5)[0])
    print(t.tableRetrieve(5)[1])
    t.traverseTable(print)
    print(t.save())
    t.load({'root': 10,'children':[{'root':5},None]})
    t.tableInsert(createTreeItem(15,15))
    print(t.tableDelete(0))
    print(t.save())
    print(t.tableDelete(10))
    print(t.save())

