class StackNode:
    def __init__(self, item):
        """
        initialiseert een node met een object
        :param item: het object dat in de node komt
        """
        self.item = item
        self.next = None


class Stack:
    def __init__(self):
        """
        maakt een stack aan
        """
        self.top = None
        self.length = 0

    def isEmpty(self):  # {query}
        """
        kijkt na of de stack leeg is
        :return: boolean True/False
        :precondities: stack bestaat
        :postcondities: geen
        """
        if not self.top:
            return True
        else:
            return False

    def push(self, newItem):
        """
        voegt een item toe op de stack
        :param newItem: toe te voegen item
        :return: boolean True = success/False = mislukt
        :precondities: de queue bestaat
        :postcondities: items in de stack += 1
        """
        if self.isEmpty():
            newNode = StackNode(newItem)
            newNode.next = None
            self.top = newNode
            if self.top == newNode and not self.top.next:
                self.length += 1
                return True
            else:
                return False
        else:
            oldTop = self.top
            newNode = StackNode(newItem)
            newNode.next = self.top
            self.top = newNode
            if self.top == newNode and self.top.next == oldTop:
                self.length += 1
                return True
            else:
                return False

    def pop(self):
        """
        verwijdert het laatst toegevoegde item, returnt dit
        :return: item, boolean {query}: True = success/False = mislukt
        :precondities: de queue bestaat
        :postcondities: len(self.items) -= 1
        """
        if self.isEmpty():
            return None, False
        else:
            toDelete = self.top
            self.top = toDelete.next
            if self.top != toDelete:
                return toDelete.item, True
                self.length -= 1
            else:
                return None, False

    def getTop(self):  # {query}
        """
        geef het laatst toegevoegde item terug
        :return: laatst toegevoegde item, boolean: True = success/False = mislukt
        :precondities: stack bestaat
        :postcondities: geen
        """
        if self.isEmpty():
            return None, False
        else:
            return self.top.item, True

    def save(self, currentNode=None, stacklist=[], Flag=True):
        """
        itereerd over de stack en slaagt de objecten op in een python lijst
        :param currentNode: de huidige node van de chain
        :param stacklist: lijst die de objecten opslaagt
        :param Flag: houdt bij of recursie al heeft plaatsgevonden
        :return stacklist: de list die bestaat uit alle objecten
        """
        # eerste keer, nieuwe lijst
        if Flag:
            currentNode = self.top
            stacklist = []
        # insert item als eerste element (links in lijst = vanonder in stack)
        stacklist.insert(0, currentNode.item)
        if not currentNode.next:
            return stacklist
        else:
            currentNode = currentNode.next
            return self.save(currentNode, stacklist, False)

    def load(self, stacklist):
        """
        laad een lijst in in een stack
        parameter stacklist: de python lijst die moet ingeladen worden in de stack
        postconditie: len(stacklist) == items in de stack
        """
        # maak stack leeg
        while not self.isEmpty():
            self.pop()
        # push de elementen in de queue
        for i in range(0, len(stacklist)):
            self.push(stacklist[i])

    def getLength(self):
        """
        geeft de lengte van de stack terug
        :return: lengte van de stack (int)
        """
        return self.length
