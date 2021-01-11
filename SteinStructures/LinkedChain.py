class LinkedChain:
    def __init__(self):
        self.chain = []

    def isEmpty(self):
        return len(self.chain) == 0

    def getLength(self):
        return len(self.chain)

    def delete(self, location):
        """
        functie voor het verwijderen van een item met een bepaalde value
        :parameter value
        :return boolian True=verwijderen is gelukt, False=er is iets fout gegaan
        """
        locatie = location - 1
        if locatie < len(self.chain) and locatie >= 0:
            self.chain.remove(self.chain[locatie])
            return True
        return False

    def insert(self, locatie, value):
        """
        functie voor het inserten van een item echter een ander item
        :parameter value (de waarde die moet worden geinserd, valueBefore get item waar het achter moet geplaatst worden
        :return boolian True=insert is gelukt, False=er is iets fout gegaan
        """
        locatie = locatie - 1
        if locatie <= len(self.chain):
            self.chain.insert(locatie,value)
            return True
        return False

    def save(self):
        return self.chain

    def retrieve(self, locatie):
        """
        functie voor de node met een value te krijgen
        :parameter value: een value van een bestaande note
        :return de not van die value
        """
        locatie = locatie - 1
        if locatie < len(self.chain):
            return (self.chain[locatie], True)
        return (False, False)

    def load(self, list):
        self.chain = list