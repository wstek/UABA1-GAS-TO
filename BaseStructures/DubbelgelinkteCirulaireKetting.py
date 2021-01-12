"""
ADT contract voor circulaire dubbelgelinkte ketting
"""

class LCNode:
    def __init__(self, item=None, next_node=None, prev_node=None):
        """
        Creëer een knoop voor een circulaire dubbelgelinkte ketting.
        :param item: waarde
        :param next_node: volgende knoop
        :param prev_node: vorige knoop
        """
        self.item = item
        self.next = next_node
        self.prev = prev_node


class LinkedChain:
    def __init__(self):
        """
        Creëert een lege circulaire dubbelgelinkte ketting.
        """
        self.head = None
        self.count = 0

    def load(self, LC_lijst):
        """
        Laadt de circulaire dubbelgelinkte ketting uit een lijst.
        :param LC_lijst: lijst met items
        :return: None
        """
        # Creëer de head
        self.head = LCNode(LC_lijst[0])
        prev_node = self.head

        # Doorloop alle items in de lijst, maak daar knopen van en laat hun wijzen naar voor en achter
        for i in LC_lijst[1:]:
            n = LCNode(i)
            prev_node.next = n
            n.prev = prev_node
            prev_node = n

        # Laat de laatste knoop wijzen naar de head
        prev_node.next = self.head
        self.head.prev = prev_node

    def save(self):
        """
        Slaagt de circulaire dubbelgelinkte ketting op in een lijst.
        :return: lijst
        """
        # Return een lege lijst als de ketting leeg is
        if self.head is None:
            return []

        # Creëer een lege lijst en zet de eerste knoop gelijk aan current_node
        LC_lijst = []
        current_node = self.head

        # Doorloop alle knopen en voeg die toe aan de LC_lijst
        while True:
            LC_lijst.append(current_node.item)
            current_node = current_node.next
            if current_node == self.head:
                return LC_lijst

    def print(self):
        """
        Print de circulaire dubbelgelinkte ketting op het scherm.
        :return: None
        """
        print(self.save())

    def isEmpty(self):
        """
        Kijkt of de circulaire dubbelgelinkte ketting leeg is.
        :return: boolean
        """
        if self.head is None:
            return True
        return False

    def getLength(self):
        """
        Geeft de lengte van de circulaire dubbelgelinkte ketting terug.
        :return: int
        """
        return self.count

    def insert(self, n, newItem):
        """
        Voegt het element 'newItem' toe op positie n in de circulaire dubbelgelinkte ketting.
        :param newItem: waarde
        :param n: positie
        :return: None
        """
        # Ongeldige positie
        if n > self.getLength() + 1 or n <= 0:
            return False

        # Lege ketting
        if self.head is None:
                new_node = LCNode(newItem)
                new_node.next = new_node
                new_node.prev = new_node
                self.head = new_node

                # Verhoog de count met 1
                self.count += 1

                # succes
                return True

        # n = 1
        elif n == 1:
            # Zet current_node gelijk aan de laatste knoop van de ketting
            current_node = self.head.prev
        elif n > 1:
            # Zet current_node gelijk aan de knoop op pos n - 1
            current_node = self.head
            for i in range(n - 2):
                current_node = current_node.next

        # Creëer een nieuwe knoop
        new_node = LCNode(newItem)
        # Laat de next pointer naar het eerstvolgende element wijzen
        new_node.next = current_node.next
        # en de prev pionter naar het vorige element wijzen
        new_node.prev = current_node

        # Laat de next pointer van het laatste element wijzen naar de nieuwe knoop
        current_node.next = new_node
        # Laat de prev pointer van de knoop voor de nieuwe knoop naar de nieuwe knoop wijzen
        new_node.next.prev = new_node

        # Laat de headpointer naar de nieuwe knoop wijzen als de gegeven positie 1 is
        if n == 1:
            self.head = new_node

        # Verhoog de count met 1
        self.count += 1

        # succes
        return True

    def delete(self, n):
        """
        Verwijdert het element op positie n uit de circulaire dubbelgelinkte ketting.
        :param n: positie van het element
        :return: boolean
        """
        # Ongeldige positie
        if n <= 0:
            return False

        # Zoek de te verwijderen knoop
        current_node = self.retrieveNode(n)
        if current_node is None:
            return False

        # Als de te verwijderen node de eerste in de ketting is
        if current_node == self.head:
            self.head = current_node.next

        # Laat de pointer van de vorige en de volgende knoop niet meer naar current_node wijzen,
        # maar naar de volgende/vorige in de ketting
        current_node.prev.next = current_node.next
        current_node.next.prev = current_node.prev

        self.count -= 1

        return True

    def retrieveNode(self, n):
        """
        Geeft de knoop die op positie n staat in de circulaire dubbelgelinkte ketting terug.
        :param n: positie van de node
        :return: LCNode
        """
        if self.head is None:
            return None

        # Doorloop de knopen tot aan de gegeven positie
        current_node = self.head
        for i in range(n - 1):
            current_node = current_node.next

        return current_node

    def retrieve(self, n):
        """
        Geeft het element op positie n terug in de circulaire dubbelgelinkte ketting.
        :param n: positie van de item
        :return: value
        """
        node = self.retrieveNode(n)
        if node is not None:
            return node.item, True
        else:
            return None, False

    def clear(self):
        """
        Wist de circulaire dubbelgelinkte ketting.
        :return: success (boolean)
        """
        # Laat de headpointer wijzen naar None en zet de counter terug op 0
        self.head = None
        self.count = 0

        # succes
        return True