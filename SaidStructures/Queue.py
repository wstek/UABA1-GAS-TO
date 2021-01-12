class Node:
    def __init__(self,item):
        self.item = item
        self.next = None

class Queue:
    def __init__(self):
        """
        Creëert een lege queue.
        """
        self.front = None
        self.back = None
        self.size = 0
    def isEmpty(self):
        """
        Bepaalt of een queue leeg is
        :return: True als de queue leeg is en False als de queue niet leeg is
        :preconditie:
        None
        :postconditie:
        None
        """
        if self.front is None:
            return True
        return False
    def enqueue(self,item):
        """
        Voegt het element ‘k’ toe aan het eind van de queue
        :param k: Het element dat je aan de queue toevoegd
        :return: De queue met het element k toegevoegd
        :preconditie:
        Er bestaat een queue
        :postconditie:
        Het element k is toegevoegd aan de queue
        """
        new_node = Node(item)
        if self.front is None:
            self.front = new_node
            self.back = new_node
            self.size = 1
            return True
        self.back.next = new_node
        self.back = self.back.next
        self.size += 1
        return  True
    def dequeue(self):
        """
        Plaatst de kop van een queue in ‘queueFront’ en verwijdert dan deze kop en duidt aan of het verwijderen gelukt is
        :return: False als de queue leeg is en (queueFront,True) als de top van de queue is verwijderd
        :preconditie:
        De queue is niet leeg
        :postconditie:
        De queueFront is veranderd
        """
        if self.front == None:
            return (False,False)
        Front = self.front.item
        self.front = self.front.next
        self.size -= 1
        return (Front,True)
    def getFront(self):
        """
        Plaatst de kop van een queue in ‘queueFront’ en laat de queue ongewijzigd
        :return: False als de queue leeg is en (queueFront,True) als de queue niet leeg is
        :preconditie:
        De queue is niet leeg
        :postconditie:
        None
        """
        if self.front == None:
            return (False,False)
        queueFront = self.front.item
        return (queueFront,True)

    def save(self):
        L = []
        new_node = self.front.next
        L.append(self.front.item)
        i = 0
        while i < self.size -1:
            L.append(new_node.item)
            new_node = new_node.next
            i += 1
        L.reverse()
        return L
    def load(self,lijst):
        lijst.reverse()
        j = 0
        while j < self.size:
            self.dequeue()
            j += 1
        self.front = None
        self.back = None
        i = 0
        while i < len(lijst):
            self.enqueue(lijst[i])
            i += 1
        self.size = len(lijst)


q = Queue()
print(q.isEmpty())
print(q.getFront()[1])
print(q.dequeue()[1])
print(q.enqueue(2))
print(q.enqueue(4))
print(q.isEmpty())
print(q.dequeue()[0])
q.enqueue(5)
print(q.save())

q.load(['a', 'b', 'c'])
print(q.save())
print(q.dequeue()[0])
print(q.save())
print(q.getFront()[0])
print(q.save())