"""
ADT contract voor stack
"""

class StackNode:
    def __init__(self, value=None):
        """
        Creëer een knoop voor een Stack.
        :param value: waarde
        """
        self.value = value
        self.next = None

class Stack:
    def __init__(self):
        """
        Creëert een lege stack.
        """
        self.top = None
        self.count = 0

    def load(self, StackLijst):
        """
        Laadt de stack uit een lijst.
        :param StackLijst:
        :return: None
        """
        # Als de stack leeg is
        if not StackLijst:
            return

        # Doorloop de elementen in de lijst en voeg die toe aan de stack
        prev_node = None
        for item in StackLijst:
            self.count += 1
            current_node = StackNode(item)
            current_node.next = prev_node
            prev_node = current_node

        # Maak de laatste node de top van de stack
        self.top = current_node

        return True

    def save(self):
        """
        Slaagt de stack op in een lijst.
        :return: lijst
        """
        # Als de stack leeg is
        if self.top is None:
            return []

        StackLijst = []
        # Maak huidige knoop de top
        current_node = self.top
        while True:
            if current_node is None:
                return StackLijst
            StackLijst.insert(0, current_node.value)
            current_node = current_node.next

    def print(self):
        """
        Print de stack op het scherm.
        :return: None
        """
        print(self.save())

    def isEmpty(self):
        """
        Kijkt of de stack leeg is.
        :return: True als leeg en False als niet leeg
        """
        if self.top is None:
            return True
        else:
            return False

    def push(self, newItem):
        """
        Voegt een element toe aan de stack.
        :param newItem: item die wordt toegevoegd
        :return: None

       postcondities:
            1 item meer in de stack
        """
        # Als de stack leeg is
        if self.top is None:
            self.top = StackNode(newItem)
        else:
            # Creëer een nieuwe node en laat die wijzen naar de oude top
            new_top = StackNode(newItem)
            new_top.next = self.top
            self.top = new_top
        self.count += 1
        return True

    def pop(self):
        """
        Verwijdert het laatst toegevoegde element uit de stack.
        :return: het laatst toegevoegde element

        postcondities:
            1 item minder in de stack
        """
        if self.top is not None:
            # Neem de waarde van de top node en return die op het einde
            value = self.top.value
        else:
            return None, False

        # Maak de volgende van de top de top
        self.top = self.top.next

        self.count -= 1
        return value, True

    def getTop(self):
        """
        Vraagt het laatst toegevoegde element uit de stack op.
        :return: het laatst toegevoegde element
        """
        if self.top is not None:
            return self.top.value, True
        return None, False

    def getLength(self):
        """
        Geeft het aantal items in de stack.
        :return: int
        """
        return self.count

if __name__ == "__main__":
    s = Stack()
    print(s.isEmpty())
    print(s.getTop()[1])
    print(s.pop()[1])
    print(s.push(2))
    print(s.push(4))
    print(s.isEmpty())
    print(s.pop()[0])
    s.push(5)
    print(s.save())

    s.load(['a','b','c'])
    print(s.save())
    print(s.pop()[0])
    print(s.save())
    print(s.getTop()[0])
    print(s.save())