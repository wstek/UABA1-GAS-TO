class Node:
    def __init__(self, item):
        """
        Een nieuwe node met een item wordt gemaakt
        :param item: Een item die je in een node wilt zetten

        :return: Een lege node

        :preconditie:
        None

        :postconditie:
        None
        """
        self.item = item
        self.next = None
        self.previous = None

class LinkedChain:

    def __init__(self):
        """
        Een nieuwe dubbelgelinkte ketting wordt gemaakt

        :preconditie:
        None

        :postconditie:
        None
        """
        self.head = None
        self.size = 1

    def isEmpty(self):
        if self.head is None:
            return True
        return False
    def getLength(self):
        return self.size - 1

    def insert(self,n,item):
        """
        Een item wordt in de ketting toegevoegd
        :param item: De item die je in de ketting voegd
        :param n: De index van waar je de item wilt toevoegen

        :return: De ketting met het toegevoegde item erin

        :preconditie:
        None

        :postconditie:
        None
        """
        a = Node(item)
        node = self.head
        if n > self.size:
            return (False)
        if self.head is None:
            self.head = a
            a.next = a
            a.previous = a
            return True
        elif n == 1:
            a.previous = self.head.previous
            a.next = self.head
            self.head.previous.next = a
            self.head.previous = a
            if self.size == 1:
                self.head.next = a
            self.head = a
            self.size += 1
            return True
        else:
            current_node = self.head
            for i in range(n-1):
                current_node = current_node.next
                if current_node == self.head:
                    return False
            a.previous = current_node.previous
            a.next = current_node
            current_node.previous.next = a
            current_node.previous = a

            self.size += 1
            return True
    def retrieve(self,k):
        if self.head == None:
            return (False,False)
        if k > self.size:
            return (False,False)
        current_node = self.head
        for i in range(k-1):
            if current_node.next == self.head:
                return (False,False)
            current_node = current_node.next
        return (current_node.item,True)

    def print(self):
        """
        Dit print de ketting uit

        :preconditie:
        None

        :postconditie:
        None
        """
        node = self.head
        while True:
            node.item.print()
            node = node.next
            if node == self.head:
                break

    def delete(self,index):
        """
        Hierbij delete je een item met een bepaalde id
        :param item: De item die je wilt verwijderen
        :param id: De id van de item die je wilt verwijderen

        :return: De ketting zonder de item

        :preconditie:
        None

        :postconditie:
        None
        """
        if self.head is None:
            return False
        current_node = self.head
        if index <= 0:
            return False

        if index == 1:
            self.head = self.head.next
            current_node.next.previous = current_node.previous
            current_node.previous.next = current_node.next
            self.size -= 1
            return True
        else:
            for i in range(index-1):
                current_node = current_node.next
                if current_node.next == self.head:
                    return False
            current_node.next.previous = current_node.previous
            current_node.previous.next = current_node.next
            self.size -= 1
            return True

    def save(self):
        L = []
        L.append(self.head.item)
        current_Node = self.head.next
        for i in range(self.size - 1):
            L.append(current_Node.item)
            current_Node = current_Node.next
            if current_Node== self.head:
                break
        return L

    def load(self,lijst):
        self.head = None
        lijst.reverse()
        for j in range(len(lijst)):
            self.insert(1,lijst[j])

l = LinkedChain()
print(l.isEmpty())
print(l.getLength())
print(l.retrieve(4)[1])
print(l.insert(4,500))
print(l.isEmpty())
print(l.insert(1,500))
print(l.retrieve(1)[0])
print(l.retrieve(1)[1])
print(l.save())
print(l.insert(1,600))
print(l.save())
l.load([10,-9,15])
l.insert(3,20)
print(l.delete(0))
print(l.save())
print(l.delete(1))
print(l.save())






