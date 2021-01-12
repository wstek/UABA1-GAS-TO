class ChainNode:
    def __init__(self, value, previous=None, next=None):
        """
        maakt een nieuwe knoop aan in de ketting
        :param previous: vorige object in de ketting
        :param value: de data van het huidige object
        :param next: volgende object in de chain
        """
        self.previous = previous
        self.value = value
        self.next = next


class LinkedChain:
    def __init__(self, Head=None):
        """
        maakt een nieuwe ketting aan
        :param Head: de Headpointer
        """
        self.Head = Head

    def insert(self, pos, node, currentPos=1, currentNode=None, Start=True):
        """
        insert een nieuwe node in de ketting
        :param node: de node (object met next en previous pointers)
        :param pos: de positie waarin de node moet geplaatst worden
        :param currentPos: huidige positie in de chain
        :param currentNode: huide node in de chain
        :param Start: houdt bij of het recursieniveau 0 is
        :return bool: het al dan niet slagen van de insert.
        :precondities: de ketting bestaat
        :postcondities: aantal elementen in de ketting += 1, pos van alle items met index >= pos += 1
        """
        #begin in de headnode en initialiseer de kettingNode
        if Start:
            node = ChainNode(node)
            currentNode = self.Head
        # als de positie groter of gelijk aan de lengte
        if pos > self.getLength() + 1:
            return False
        if currentPos == pos:
            if not self.Head:
                self.Head = node
                node.next = node
                node.previous = node
                return True
            else:
                #als het in de eerste positie moet, verander de headpointer
                if pos == 1:
                    self.Head = node
                #insert de node
                node.next = currentNode
                node.previous = currentNode.previous

                currentNode.previous.next = node
                currentNode.previous = node
                return True
        else:
            #anders, recursie met volgende positie en volgende node
            return self.insert(pos, node, currentPos + 1, currentNode.next, False)

    def destroy(self):
        """
        maakt de ketting leeg
        :precondities: de lijst bestaat
        :postcondities: self.getLength = 0
        """
        # python garbage collector
        self.Head = None

    def isEmpty(self):  # {query}
        """
        kijkt na of de ketting leeg is
        :return: boolean True on empty
        :precondities: de ketting bestaat
        """
        if not self.Head:
            return True
        else:
            return False

    def getLength(self):  # {query}
        """
        geeft de lenge van de lijst terug
        :return length: lengte van de lijst
        :precondities: 
        :postcondities: 
        """
        if not self.Head:
            return 0
        length = 1
        currentNode = self.Head.next
        while currentNode != self.Head:
            length += 1
            currentNode = currentNode.next
        return length

    def retrieve(self, pos):  # {query}
        """
        zoekt het object op positie pos en returnt deze
        :parameter pos: positie van het te retrieven item
        :return currentNode.value: object met positie pos
        :precondities: de ketting bestaat
        """
        # ketting mag niet leeg zijn en positie moet kleiner of gelijk zijn aan het aantal items
        if not self.isEmpty() and pos < self.getLength()+1:
            currentNode = self.Head
            currentPos = 1
            # blijf loopen tot de gevraagde pos gelijk is aan de huidige positie
            for i in range(self.getLength() + 1):
                if pos == currentPos:
                    return currentNode.value, True
                else:
                    currentNode = currentNode.next
        return None, False

    def traverse(self, functie=None):
        """
        loopt over alle items in de ketting en voert de meegegeven functie uit
        @param functie: de uit te voeren functie
        @precondition de ketting bestaat
        """
        if self.Head:
            currentNode = self.Head
            functie(currentNode.value)
            currentNode = currentNode.next
            while currentNode != self.Head:
                functie(currentNode.value)
                currentNode = currentNode.next

    def delete(self, pos):
        """
        deletes het item met positie pos
        :param pos: de positie van het item dat gedelete moet worden
        :return:
        :precondities: de ketting bestaat, de positie is kleiner of gelijk aan het aantal elementen
        :postcondities: self.getLength() -= 1 en voor alle elementen met positie > pos => positie -= 1
        """
        currentPos = 1
        currentNode = self.Head
        #loop over alle nodes
        for i in range(1, self.getLength() + 1):
            #als de positie de te deleten positie is
            if pos == currentPos:
                #haal de node er tussen uit
                currentNode.previous.next = currentNode.next
                currentNode.next.previous = currentNode.previous
                #als de positie 1 is, verander ook de headpointer
                if pos == 1:
                    self.Head = self.Head.next
                return True
            else:
                #anders, ga naar de volgende node
                currentPos += 1
                currentNode = currentNode.next
        return False

    def save(self, currentNode=None, list=[], Start=True):  # {query}
        """
        itereerd over de chain en slaagd de objecten op in een python lijst
        :param currentNode: de huidige node van de chain
        :param list: lijst die de objecten opslaagt
        :param Start: houdt bij of de recursiediepte 0 is
        :return list: de list die bestaat uit alle objecten
        """
        #bij de start is de lijst leeg
        if Start:
            list = []
            currentNode = self.Head
        list.append(currentNode.value)
        #als de volgende node terug de start is is de lijst compleet
        if currentNode.next == self.Head:
            return list
        else:
            currentNode = currentNode.next
            return self.save(currentNode, list, False)

    def load(self, lijst):
        """
        laad een lijst in in de ketting
        @param lijst: de in te laden lijst
        @return bool: True on success
        """
        #maak de lijstleeg
        self.destroy()
        #loop over de lijst en insert deze in hun juiste positie
        for i in lijst:
            self.insert(self.getLength() + 1, i)
        return True


