class QueueNode:
    def __init__(self, item):
        """
        initialiseerd een Node met object(item)
        :param item(object): het item dat in de node komt
        """
        self.item = item
        self.next = None


class Queue:
    def __init__(self):
        """
        maakt een queue aan
        """
        self.items = []
        self.queueFront = None
        self.queueBack = None

    def isEmpty(self):  # {query}
        """
        kijkt na of een queue leeg is
        :return: boolean {query}: True/False
        :precondities: queue bestaat
        :postcondities: geen
        """
        if not self.queueFront:
            return True
        else:
            return False

    def enqueue(self, newItem):
        """
        voegt een item toe in de queue
        :param newItem: toe te voegen item
        :return: boolean True = success/False = mislukt
        :precondities: de queue bestaat
        :postcondities: len(self.items) += 1
        """
        newPtr = QueueNode(newItem)
        if self.isEmpty():
            self.queueFront = newPtr
            self.queueBack = newPtr
        else:
            self.queueBack.next = newPtr
            self.queueBack = newPtr
        return True

    def dequeue(self):
        """
        verwijdert het eerst toegevoegde item
        :return: boolean True = success/False = mislukt
        :precondities: de queue bestaat
        :postcondities: len(self.items) -= 1 en queueFront = volgende item
        """
        if self.isEmpty():
            return None, False
        else:
            toRemove = self.queueFront
            self.queueFront = self.queueFront.next
            toRemove.next = None
            return toRemove.item, True

    def getFront(self):
        """
        returnt het eerst toegevoegde item
        :return: eerste item, boolean {query}: True = success/False = mislukt
        :precondities: de stack bestaat
        """
        if self.isEmpty():
            return None, False
        else:
            return self.queueFront.item, True

    def save(self, currentNode=None, queuelist=[], Flag=True):  # {query}
        """
        zet de queue om in een python lijst en geeft deze terug
        :param currentNode: de huidige node
        :param queuelist: de lijst met de toegevoegde objecten
        :param Flag: houdt bij of er nog geen recursie heeft plaatsgevonden
        :return queuelist: de lijst van alle objecten
        """
        # recursiediepte 0, lijst is leeg
        if Flag:
            currentNode = self.queueFront
            queuelist = []
        # eerste element in de lijst is laatste in de queue
        queuelist.insert(0, currentNode.item)
        #als er geen volgende is
        if not currentNode.next:
            return queuelist
        else:
            currentNode = currentNode.next
            return self.save(currentNode, queuelist, False)

    def load(self, qlist):
        #zolang de queue niet leeg is, dequeue
        while not self.isEmpty():
            self.dequeue()
        # loop over alle elementen in de lijst, begin bij het laatste element en loop tot het eerste element
        for i in range(len(qlist) - 1, -1, -1):
            self.enqueue(qlist[i])

