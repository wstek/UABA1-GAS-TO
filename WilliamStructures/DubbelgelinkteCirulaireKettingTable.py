"""
ADT contract voor tabel, ketting implementatie
"""

import LinkedChain

class LinkedChainTable():
    def __init__(self):
        """
        Creëer een lege tabel.
        """
        self.linked_chain = LinkedChain.LinkedChain()

    def load(self, LC_lijst):
        """
        Laadt de tabel (ketting implementatie) uit een lijst.
        :param LC_lijst: lijst met items
        :return: None
        """
        self.linked_chain.load(LC_lijst)

    def save(self):
        """
        Slaagt de tabel (ketting implementatie) op in een lijst.
        :return: lijst
        """
        return self.linked_chain.save()

    def tableIsEmpty(self):
        """
        Bepaalt of de tabel leeg is. (query)
        :return: boolean
        """
        return self.linked_chain.isEmpty()

    def tableLength(self):
        """
        Geeft de lengte van de tabel terug. (query)
        :return: lengte van de tabel
        """
        return self.linked_chain.getLength()

    def tableInsert(self, n, newItem):
        """
        Voegt newItem toe de tabel op positie n. Success geeft weer of het toevoegen gelukt is.
        :return: success (boolean)
        """
        return self.linked_chain.insert(n, newItem)

    def tableDelete(self, searchKey):
        """
        Verwijdert een entry in de tabel mbv een zoeksleutel. Success geeft weer of het toevoegen gelukt is.
        :param searchKey: zoeksleutel (KeyType)
        :return: success (boolean)
        """
        return self.linked_chain.delete(searchKey)

    def tableRetrieve(self, searchKey):
        """
        Geeft een waarde terug mbv de zoeksleutel.
        :param searchKey: zoeksleutel (KeyType)
        :return: tableItem (TableItemType), success (boolean)
        """
        return self.linked_chain.retrieve(searchKey)

if __name__ == "__main__":
    l = LinkedChainTable()
    print(l.tableIsEmpty())
    print(l.tableLength())
    print(l.tableRetrieve(4)[1])
    print(l.tableInsert(4,500))
    print(l.tableIsEmpty())
    print(l.tableInsert(1,500))
    print(l.tableRetrieve(1)[0])
    print(l.tableRetrieve(1)[1])
    print(l.save())
    print(l.tableInsert(1,600))
    print(l.save())
    l.load([10,-9,15])
    l.tableInsert(3,20)
    print(l.tableDelete(0))
    print(l.save())
    print(l.tableDelete(10))
    print(l.save())