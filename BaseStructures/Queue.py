"""
ADT contract voor queue
"""

class QueueNode:
    def __init__(self, value=None):
        """
        Creëer een knoop voor een Stack.
        :param value: waarde
        """
        self.value = value
        self.next = None

class Queue:
    def __init__(self):
        """
        Creëert een lege queue.
        """
        self.front = None
        self.back = None

    def load(self, QueueLijst):
        """
        Laadt de queue uit een lijst.
        :param QueueLijst: lijst
        :return: None
        """
        # Als de Queue leeg is
        if not QueueLijst:
            return
        self.front = QueueNode(QueueLijst.pop(-1))
        # Als de lijst 1 element heeft
        if not QueueLijst:
            self.back = self.front
            return

        # Doorloop de elementen van de lijst en voeg die toe aan de queue
        prev_node = self.front
        for item in QueueLijst[::-1]:
            current_node = QueueNode(item)
            prev_node.next = current_node
            prev_node = current_node

        # Maak de laatste knoop de back
        self.back = current_node

        return True

    def save(self):
        """
        Slaagt de queue op in een lijst.
        :return: lijst
        """
        # Als de queue leeg is
        if self.back is None:
            return []

        l = []
        # Maak de front de huidige node
        current_node = self.front
        while True:
            if current_node is None:
                return l
            l.insert(0, current_node.value)
            current_node = current_node.next

    def print(self):
        """
        Print de queue op het scherm.
        :return: None
        """
        print(self.save())

    def isEmpty(self):
        """
        Kijkt of de queue leeg is.
        :return: True als leeg en False als niet leeg
        """
        if self.front is None:
            return True
        return False

    def enqueue(self, newItem):
        """
        Voegt een element toe aan de queue.
        :param newItem: item die wordt toegevoegd
        :return: None

       postcondities:
            1 item meer in de queue
        """
        # Maak een nieuwe new_node met newItem als value
        new_node = QueueNode(newItem)

        # Als de queue leeg is, wijzen front and back naar de nieuwe new_node
        if self.isEmpty():
            self.front, self.back = new_node, new_node
        else:
            # Voeg achteraan toe
            self.back.next = new_node
            self.back = new_node

        return True

    def dequeue(self):
        """
        Verwijdert het eerst toegevoegde element uit de queue.
        :return: het eerst toegevoegde element

        postcondities:
            1 item minder in de queue
        """
        if self.front is not None:
            # Neem de waarde van de front knoop en return die op het einde
            value = self.front.value
        else:
            return None, False

        # Als er 1 item in de queue zit
        if self.getLength() == 1:
            self.front = None
            self.back = None
        else:
            # Maak de volgende van de front de front
            self.front = self.front.next

        return value, True

    def getFront(self):
        """
        Vraagt het eerst toegevoegde element uit de queue op.
        :return: het eerst toegevoegde element
        """
        if self.front is not None:
            return self.front.value, True
        else:
            return None, False

    def getLength(self):
        """
        Geeft de lengte van de queue terug
        :return: lengte van de queue (int)
        """
        count = 1
        current_node = self.front
        while current_node != self.back:
            count += 1
            current_node = current_node.next

        return count
