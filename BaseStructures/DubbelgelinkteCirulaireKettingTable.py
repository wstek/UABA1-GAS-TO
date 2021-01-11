from BaseStructures.DubbelgelinkteCirulaireKetting import *

class DubbelgelinkteCirulaireKettingTable():
    def __init__(self):
        self.ketting = DubbelgelinkteCirulaireKetting()

    def tableIsEmpty(self):  # {query}
        """
        Is de ketting leeg
        :param geen
        :return isEmpty (bool)
        """
        return self.ketting.isEmpty()

    def tableLength(self):  # {query}
        """
        lengte van de ketting
        :param geen
        :return lenght (int)
        """
        return self.ketting.getLength()

    def tableDelete(self, value):
        """
        delete node van ketting
        :param de value van de ketting die verwijderd moet worden
        :return correct verwijderd (bool)
        """
        return self.ketting.delete(value)

    def tableRetrieve(self, value):
        """
        retrieve node van ketting
        :param valie (int)
        :return de opgevraagde node
        """
        return self.ketting.retrieve(value)

    def tableInsert(self, value):
        """
        insert een node op een bepaalde positie
        :param pos: possitie (int), item: waarde van de node
        :return insert gelukt (bool)
        """
        return self.ketting.insert(value)

    def save(self):
        """
        geeft de gelinkte ketting als list
        :return de gelikte ketting als list
        """
        return self.ketting.save()

    def load(self, lijst):
        """
        laad ene lijst in de gelinkte ketting
        :return indien het innladen gelukt is (bool)
        """
        return self.ketting.load(lijst)
