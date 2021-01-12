class Node:
    def __init__(self,item):
        self.item = item
        self.next = None

class Stack:
    def __init__(self):
        """
        Creëert een lege stack
        """
        self.top = None
        self.size = 0
    def isEmpty(self):
        """
        Bepaalt of een stack leeg is
        :return: True als de stack leeg is en False als de stack niet leeg is
        :preconditie:
        None
        :postconditie:
        None
        """
        if self.top == None:
            return True
        return False
    def push(self,item):
        """
        Voegt het element 'k' toe op de top van een stack
        :param k: Het element dat je wilt toevoegen aan een stack
        :return: De stack met het element eraan toegevoegd
        :preconditie:
        Er bestaat een stack 'self.stack'
        :postconditie:
        Het element k is element van de stack 'self.stack'
        """
        new_node = Node(item)
        if self.top is None:
            self.top = new_node
            self.size = 1
            return True
        new_node.next = self.top
        self.top = new_node
        self.size += 1
        return True
    def pop(self):
        """
        Verwijdert de top van een stack en geeft een boolean die aangeeft of het is gelukt
        :return: False als de stack leeg is en (Topstack,True) als de top van de stack is verwijderd
        :preconditie:
        De stack is niet leeg
        :postconditie:
        De top van de stack is veranderd
        """
        if self.top is None:
            return (False,False)
        stackTop = self.top.item
        del self.top.item
        self.top = self.top.next
        self.size -= 1
        return (stackTop,True)
    def getTop(self):
        """
        Plaatst de top van een stack in ‘stackTop’ en laat de stack ongewijzigd.
        :return: False als de stack leeg is en (Topstack,True) als de stack niet leeg is
        :preconditie:
        De stack is niet leeg
        :postconditie:
        None
        """
        if self.top is None:
            return (False,False)
        Top = self.top.item
        return (Top,True)
    def save(self):
        L = []
        new_node=self.top.next
        L.append(self.top.item)
        i = 0
        while i < self.size -1:
            L.append(new_node.item)
            new_node = new_node.next
            i += 1
        L.reverse()
        return L
    def load(self,lijst):
        i = 0
        while i < self.size:
            self.pop()
            i += 1
        j = 0
        while j < len(lijst):
            self.push(lijst[j])
            j += 1
        self.size = len(lijst)

    def getLength(self):
        return self.size

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