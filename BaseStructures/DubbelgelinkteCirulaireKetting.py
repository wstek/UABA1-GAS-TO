import copy

class DubbelgelinkteCirulaireKetting:
    def __init__(self):
        self.N = 0
        self.firstNode = node(None,None,None)

    def isEmpty(self):
        return self.firstNode.value == None and self.firstNode.nextPointer == None

    def getLength(self):
        return self.N

    def add(self, value, xnode=None):
        """
        functie voor het toevoegen van een item achteraan in de ketting
        :parameter value
        :return boolian True=toevoegen is gelukt, False=er is iets fout gegaan
        """
        if self.exist(value):
            return False

        if xnode == None:
            xnode = self.firstNode

        if xnode.nextPointer == None:
            newNode = node(xnode, None, value)
            xnode.nextPointer = newNode
            self.firstNode.previousPointer = newNode
            return True
        else:
            return self.add(value, xnode.nextPointer)

    def delete(self, value, xnode = None):
        """
        functie voor het verwijderen van een item met een bepaalde value
        :parameter value
        :return boolian True=verwijderen is gelukt, False=er is iets fout gegaan
        """
        if not self.exist(value):
            return False

        if xnode == None:
            xnode = self.firstNode

        if xnode.value == value:
            xnode.previousPointer.nextPointer = xnode.nextPointer
            xnode.nextPointer.previousPointer = xnode.previousPointer
            del xnode
            return True
        else:
            return self.delete(value, xnode.nextPointer)

    def insert(self, value, valueBefore = None, xnode = None):
        """
        functie voor het inserten van een item echter een ander item
        :parameter value (de waarde die moet worden geinserd, valueBefore get item waar het achter moet geplaatst worden
        :return boolian True=insert is gelukt, False=er is iets fout gegaan
        """
        if self.exist(value) or (not self.exist(valueBefore) and valueBefore != None):
            return False

        if xnode == None:
            xnode = self.firstNode

        if xnode.value == valueBefore:
            if xnode.nextPointer == self.firstNode:
                next = None
            else:
                next = xnode.nextPointer
            newNode = node(xnode, next, value)
            xnode.nextPointer = newNode
            xnode.nextPointer.previousPointer = newNode
            return True
        else:
            return self.insert(value,valueBefore, xnode.nextPointer)

    def update(self, newvalue, oldValue = None, xnode = None):
        """
        functie voor de waarde te update van een item
        :parameter newvalue= de waarde dat het moet worden,  oldValue= de waarde die het momenteel heeft
        :return boolian True=update is gelukt, False=er is iets fout gegaan
        """
        if not self.exist(oldValue) or self.exist(newvalue):
            return False

        if xnode == None:
            xnode = self.firstNode

        if xnode.value == oldValue:
            xnode.value = newvalue
            return True
        else:
            return self.update(newvalue,oldValue, xnode.nextPointer)

    def print(self, node = None):
        """
        functie die de ketting in volgorde uitprint
        :parameter GEEN
        :return GEEN
        """
        if node == None:
            node = self.firstNode

        print(node.value)
        if node.nextPointer != None:
            self.print(node.nextPointer)

    def save(self, asNode=False, count=None, node=None, list=None):
        """
        functie die een lijst van de ketting terug geeft
        :parameter
            asNode (bool):
                False (lijst met values van knopen)
                True (lijst met knopen)
            count (int): aantal items
            node (node): start knoop
        :return lijst
        """
        if list == None:
            list = []

        if node == None:
            node = self.firstNode

        if node.nextPointer != None and count == None:
            if asNode:
                list.append(node)
            elif node.value != None:
                list.append(node.value)
            return self.save(asNode, count, node.nextPointer, list)
        elif count != None:
            if count > 1:
                if asNode:
                    list.append(node)
                else:
                    list.append(node.value)
                count -= 1
                return self.save(asNode, count, node.nextPointer, list)

        if asNode:
            node.nextPointer = self.firstNode
            list.append(copy.copy(node))
            node.nextPointer = None
        else:
            list.append(node.value)
        return list

    def get_previous_note(self, value, xnode = None):
        """
        functie voor de vorige node te krijgen
        :parameter value: een value van een bestaande note
        :return de note die voor de value van de gegeven note zit
        """
        if xnode == None:
            xnode = self.firstNode

        if xnode.value == value:
            return xnode.previousPointer
        else:
            return self.get_previous_note(value, xnode.previousPointer)

    def get_next_note(self, value, xnode = None):
        """
        functie voor de volgende node te krijgen
        :parameter value: een value van een bestaande note
        :return de note die na de value van de gegeven note zit
        """
        if xnode == None:
            xnode = self.firstNode

        if xnode.value == value:
            if xnode.nextPointer == None:
                return self.firstNode
            return xnode.nextPointer
        else:
            return self.get_next_note(value, xnode.nextPointer)

    def retrieve(self, value, xnode=None):
        """
        functie voor de node met een value te krijgen
        :parameter value: een value van een bestaande note
        :return de not van die value
        """
        if xnode == None:
            xnode = self.firstNode

        if xnode.value == value:
            return xnode
        else:
            if(xnode.nextPointer == None):
                return (False, False)
            return self.retrieve(value, xnode.nextPointer)

    def exist(self, value, xnode = None):
        """
        functie voor het bestaan van een waarde te controleren
        :parameter value: een waarde
        :return (bool):
            True: de waarde zit in de ketting
            False: De waarde zit niet in de ketting
        """
        if xnode == None:
            xnode = self.firstNode.nextPointer

        if xnode == None:
            return False
        elif xnode.value == value:
            return True
        elif xnode.nextPointer == None:
            return False
        else:
            return self.exist(value, xnode.nextPointer)

    def load(self, list):
        for item in list:
            self.insert(item)

class node:
    def __init__(self, previousPointer, nextPointer, value):
        self.previousPointer = previousPointer
        self.nextPointer = nextPointer
        self.value = value





















