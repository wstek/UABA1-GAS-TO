Red = 2
Black = 1


class RBTNode:
    def __init__(self, key, data=None):
        """
        initialiseerd een node voor in de RedBlackTree
        @param data: het data die in de node zit
        
        """
        self.key = key
        self.data = data


def createTreeItem(key, data):
    return RBTNode(key, data)


class RedBlackTree:
    def __init__(self, node=None):
        """
        initialiseerd een red black tree
        @param node: het eerste object dat eventueel in de root wordt gezet
        """
        self.key = None
        self.node = None
        self.RChild = None
        self.LChild = None
        self.parent = None
        self.root = None
        self.color = Red
        if node:
            self.key = node.key
            self.node = node
            self.root = node

    def findRoot(self):
        """
        zoekt de root van de tree
        @return: de root tree van de rbt
        """
        if self.parent:
            return self.parent.findRoot()
        else:
            return self

    def isEmpty(self):
        """
        kijkt na of de functie leeg is
        @return: True voor empty
        """
        if not self.findRoot().key:
            return True
        else:
            return False

    def colorswap(self):
        """
        splits een equivalente 234 node in rbt vorm 
        @return: niets
        """
        self.color = Red
        self.LChild.color = Black
        self.RChild.color = Black

    def rotate(self):
        """
        rotate de tree wamnneer deze twee rode nodes onder elkaar heeft, zoekt zelf welke rotation nodig is
        @return: niets
        """
        if self.LChild and self.LChild.color == Red:
            if self.parent and self.parent.LChild == self:
                newRChild = self.parent
                temp = self.RChild
                self.RChild = newRChild

                if self.parent.parent:
                    grandparent = self.parent.parent
                    if self.parent == grandparent.LChild:
                        grandparent.LChild = self
                    if self.parent == grandparent.RChild:
                        grandparent.RChild = self
                self.parent = self.parent.parent

                newRChild.LChild = temp
                if newRChild.LChild:
                    newRChild.LChild.parent = newRChild

                newRChild.parent = self
                newRChild.color = Red
                self.color = Black

            elif self.parent and self.parent.RChild == self:
                newParent = self.LChild
                newSibling = self.parent
                if self.parent.parent:
                    grandparent = self.parent.parent
                    if self.parent == grandparent.LChild:
                        grandparent.LChild = newParent
                    if self.parent == grandparent.RChild:
                        grandparent.RChild = newParent
                newParent.parent = self.parent.parent
                temp = newParent.RChild
                temp2 = newParent.LChild

                newParent.LChild = newSibling
                newParent.RChild = self

                newSibling.RChild = temp2
                if newSibling.RChild:
                    newSibling.RChild.parent = newSibling

                newSibling.parent = newParent

                self.LChild = temp
                if self.LChild:
                    self.LChild.parent = self

                self.parent = newParent

                newSibling.color = Red
                newParent.color = Black

        elif self.RChild and self.RChild.color == Red:
            if self.parent and self.parent.LChild == self:
                newParent = self.RChild
                newSibling = self.parent
                if self.parent.parent:
                    grandparent = self.parent.parent
                    if self.parent == grandparent.LChild:
                        grandparent.LChild = newParent
                    if self.parent == grandparent.RChild:
                        grandparent.RChild = newParent
                temp = newParent.LChild
                temp2 = newParent.RChild
                newParent.parent = self.parent.parent
                newParent.RChild = newSibling
                newParent.LChild = self

                newSibling.LChild = temp2
                if newSibling.LChild:
                    newSibling.LChild.parent = newSibling

                newSibling.parent = newParent

                self.RChild = temp
                if self.RChild:
                    self.RChild.parent = self

                self.parent = newParent

                newSibling.color = Red
                newParent.color = Black
            elif self.parent and self.parent.RChild == self:
                newLChild = self.parent

                temp = self.LChild
                self.LChild = newLChild

                if self.parent.parent:
                    grandparent = self.parent.parent
                    if self.parent == grandparent.LChild:
                        grandparent.LChild = self
                    if self.parent == grandparent.RChild:
                        grandparent.RChild = self
                self.parent = self.parent.parent

                newLChild.RChild = temp
                if newLChild.RChild:
                    newLChild.RChild.parent = newLChild

                newLChild.parent = self
                newLChild.color = Red
                self.color = Black

    def insertItem(self, node, Flag=True):
        """
        insert een node in de boom
        @param node: het toe te voegen object
        @param Flag: houdt bij of de functie voor de eerste keer overlopen wordt, zodat het vanaf de root kan beginnen
        :return: print het slagen van de functie af op het scherm
        :precondities:
        :postcondities: 1 item meer in de tree
        """
        out = False
        if Flag:
            self.root = self.findRoot()
            out = self.root.insertItem(node, False)
            self.findRoot().color = Black
            return out
        if self.RChild:
            RChildKleur = self.RChild.color
        else:
            RChildKleur = Black
        if self.LChild:
            LChildKleur = self.LChild.color
        else:
            LChildKleur = Black
        if LChildKleur == Red and RChildKleur == Red:
            self.colorswap()
            RChildKleur = Black
            LChildKleur = Black
            if self.parent:
                return self.parent.insertItem(node, False)
            else:
                self.color = Black
        if LChildKleur == Red and self.color == Red or RChildKleur == Red and self.color == Red:
            self.rotate()
            if self.parent:
                return self.parent.insertItem(node, False)
        if not self.node:
            self.node = node
            self.key = node.key
            self.color = Black
            return True
        elif node.key < self.node.key:
            if self.LChild:
                return self.LChild.insertItem(node, False)
            else:
                self.LChild = RedBlackTree()
                self.LChild.key = node.key
                self.LChild.parent = self
                self.LChild.node = node
                out = True
                if self.parent and self.parent.RChild and self.parent.RChild.color == Red and self.parent.LChild and \
                        self.parent.LChild.color == Red:
                    self.parent.colorswap()
                if self.color == Red:
                    self.rotate()
                return out

        elif node.key > self.node.key:
            if self.RChild:
                return self.RChild.insertItem(node, False)
            else:
                self.RChild = RedBlackTree()
                self.RChild.key = node.key
                self.RChild.parent = self
                self.RChild.node = node
                out = True
                if self.parent and self.parent.RChild and self.parent.RChild.color == Red and self.parent.LChild and \
                        self.parent.LChild.color == Red:
                    self.parent.colorswap()
                if self.color == Red:
                    self.rotate()
                return out

    def leftRedistribute(self, leftSibling):
        """
        gaat van de linkersibling een item lenen om knopen te vullen op weg naar het blad
        @param leftSibling: een node uit de 234 equivalente node 
        @return: niets
        @precondition de 234 equivalente sibling heeft meer dan een item, self (234 equiv) is een 2node
        @postcondition self (234 equivalent) is een drienode
        """
        
        newParent = leftSibling.rightItemOfNode()
        if self.key > self.parent.key > leftSibling.key:
            oldParent = self.parent
        elif self.key > leftSibling.parent.key > leftSibling.key:
            oldParent = leftSibling.parent
        else:
            oldParent = self.parent.parent
        if newParent.color == Red:
            newParent.parent.RChild = newParent.LChild
            # if newParent.LChild:
            #     newParent.LChild.parent = newParent.parent

            newParent.LChild = oldParent.LChild
            if newParent.LChild:
                newParent.LChild.parent = newParent

            oldParent.LChild = newParent.RChild
            if oldParent.LChild:
                oldParent.LChild.parent = oldParent

            newParent.RChild = oldParent.RChild
            if newParent.RChild:
                newParent.RChild.parent = newParent

            if oldParent.parent:
                if oldParent.parent.RChild == oldParent:
                    oldParent.parent.RChild = newParent
                elif oldParent.parent.LChild == oldParent:
                    oldParent.parent.LChild = newParent
            newParent.parent = oldParent.parent

            oldParent.RChild = self.LChild
            if oldParent.RChild:
                oldParent.RChild.parent = oldParent

            self.LChild = oldParent
            if self.LChild:
                self.LChild.parent = self

            newParent.color = oldParent.color
            oldParent.color = Red

        else:
            if newParent.parent == Red:
                newParent.parent.RChild = newParent.LChild
                newParent.parent.RChild.parent = newParent.parent

            if oldParent.parent:
                if oldParent.parent.RChild == oldParent:
                    oldParent.parent.RChild = newParent
                elif oldParent.parent.LChild == oldParent:
                    oldParent.parent.LChild = newParent
            newParent.parent = oldParent.parent

            oldParent.LChild = newParent.RChild
            if oldParent.LChild:
                oldParent.LChild.parent = oldParent

            newParent.RChild = oldParent.RChild
            if newParent.RChild:
                newParent.RChild.parent = newParent

            oldParent.RChild = self.LChild
            if oldParent.RChild:
                oldParent.RChild.parent = oldParent

            # self.parent = newParent
            # newParent.LChild = self

            self.LChild = oldParent
            if self.LChild:
                self.LChild.parent = self

            newParent.color = oldParent.color
            oldParent.color = Red

    def rightRedistribute(self, rightSibling):
        """
        gaat van de rechtersibling een item lenen om knopen te vullen op weg naar het blad
        @param rightSibling: een node uit de 234 equivalente node 
        @return: niets
        @precondition de 234 equivalente sibling heeft meer dan een item, self (234 equiv) is een 2node
        @postcondition self (234 equivalent) is een drienode
        """
        newParent = rightSibling.leftItemOfNode()
        if self.key < self.parent.key < rightSibling.key:
            oldParent = self.parent
        elif self.key < rightSibling.parent.key < rightSibling.key:
            oldParent = rightSibling.parent
        else:
            oldParent = self.parent.parent

        if newParent.color == Red:

            newParent.parent.LChild = newParent.RChild
            if newParent.RChild:
                newParent.RChild.parent = newParent.parent

            newParent.RChild = oldParent.RChild
            if newParent.RChild:
                newParent.RChild.parent = newParent

            oldParent.RChild = newParent.LChild
            if oldParent.RChild:
                oldParent.RChild.parent = oldParent

            newParent.LChild = oldParent.LChild
            if newParent.LChild:
                newParent.LChild.parent = newParent

            if oldParent.parent:
                if oldParent.parent.LChild == oldParent:
                    oldParent.parent.LChild = newParent
                elif oldParent.parent.RChild == oldParent:
                    oldParent.parent.RChild = newParent
            newParent.parent = oldParent.parent

            oldParent.LChild = self.RChild
            if oldParent.RChild:
                oldParent.LChild.parent = oldParent

            self.RChild = oldParent
            if self.RChild:
                self.RChild.parent = self

            newParent.color = oldParent.color
            oldParent.color = Red
        else:
            if newParent.parent == Red:
                newParent.parent.LChild = newParent.RChild
                newParent.parent.LChild.parent = newParent.parent

            if oldParent.parent:
                if oldParent.parent.LChild == oldParent:
                    oldParent.parent.LChild = newParent
                elif oldParent.parent.RChild == oldParent:
                    oldParent.parent.RChild = newParent
            newParent.parent = oldParent.parent

            oldParent.RChild = newParent.LChild
            if oldParent.RChild:
                oldParent.RChild.parent = oldParent

            newParent.LChild = oldParent.LChild
            if newParent.LChild:
                newParent.LChild.parent = newParent

            oldParent.LChild = self.RChild
            if oldParent.LChild:
                oldParent.LChild.parent = oldParent

            # self.parent = newParent
            # newParent.LChild = self

            self.RChild = oldParent
            if self.RChild:
                self.RChild.parent = self

            newParent.RChild.color = Black
            newParent.color = oldParent.color
            oldParent.color = Red

    def deleteItem(self, key, Flag=True, nodeToDelete=None):
        """
        delete een item(object) met Id key uit de boom
        @param key: het Id van het te verwijderen object
        @param Flag: houdt bij of de functie voor de eerste keer overlopen wordt, zodat het vanaf de root kan beginnen
        @param nodeToDelete: de te verwijderen node indien deze al gevonden is
        @return: het slagen van de functie
        @precondition de boom bestaat
        @postcondition 1 item minder in de tree
        """
        root = False
        if Flag:
            if not self.retrieveItem(key)[1]:
                return False
            return self.findRoot().deleteItem(key, False)
        if self.findRoot() == self:
            root = True
        # check if self is een 2 knoop
        if self.isTwoNode() and not root:
            if self.findRSibling() and not self.findRSibling().isTwoNode():
                sibling = self.findRSibling()
                self.rightRedistribute(sibling)
            elif self.findLSibling() and not self.findLSibling().isTwoNode():
                sibling = self.findLSibling()
                self.leftRedistribute(sibling)

            else:
                self.merge()

        if nodeToDelete:
            if self.LChild:
                return self.LChild.deleteItem(key, False, nodeToDelete)
            else:
                self.swapNodes(nodeToDelete)
                if self.RChild:
                    self.swapNodes(self.RChild)
                    # self.RChild.parent = None
                    # anders zal bij het verwijderen van het eerst toegevoegde item de rbt onbereikbaar worden
                    self.RChild = None
                    return True
                else:
                    if self.parent.RChild == self:
                        self.parent.RChild = None
                    elif self.parent.LChild == self:
                        self.parent.LChild = None
                    # self.parent = None
                    return True
        elif key < self.key and self.LChild:
            return self.LChild.deleteItem(key, False)

        elif key > self.key and self.RChild:
            return self.RChild.deleteItem(key, False)

        elif key == self.key:
            if self.RChild:
                return self.RChild.deleteItem(key, False, self)
            else:
                if self.LChild:
                    self.swapNodes(self.LChild)
                    self.LChild.parent = None
                    self.LChild = None
                    return True
                else:
                    if self.parent.RChild == self:
                        self.parent.RChild = None
                    elif self.parent.LChild == self:
                        self.parent.LChild = None
                    self.parent = None
                    return True
        else:
            return False

    def swapNodes(self, node2):
        tempNode = self.node
        tempKey = self.key

        self.node = node2.node
        self.key = node2.key

        node2.node = tempNode
        node2.key = tempKey

    def retrieveItem(self, key, Flag=True):  # {query}
        """
        vraagt een item met zoeksleutel key op uit de boom
        @param key: de zoeksleutel gekoppeld aan het object
        :return self.item: het gezochte object
        :precondities:
        :postcondities:
        """
        if Flag:
            return self.findRoot().retrieveItem(key, False)
        if self.key == key:
            return self.node.data, True
        elif self.LChild and key < self.key:
            return self.LChild.retrieveItem(key, False)
        elif self.RChild and key > self.key:
            return self.RChild.retrieveItem(key, False)
        else:
            return None, False

    def inorderTraverse(self, functie, Flag=True):
        """
        overloopt de rbt en voort de functie uit op de data in een inorder manier
        @param functie: de uit te voeren functie
        @param Flag: houdt bij of de functie voor de eerste keer overlopen wordt, zodat het vanaf de root kan beginnen
        @return: hangt af van de meegegeven functie
        """
        if Flag:
            self.findRoot().inorderTraverse(functie, False)
            return
        if self.LChild:
            self.LChild.inorderTraverse(functie, False)
        functie(self.node.data)
        if self.RChild:
            self.RChild.inorderTraverse(functie, False)

    def getLength(self, count, Flag=True):
        """
        overloopt de rbt en voort de functie uit op de data in een inorder manier
        @param Flag: houdt bij of de functie voor de eerste keer overlopen wordt, zodat het vanaf de root kan beginnen
        @return: hangt af van de meegegeven functie
        """
        count += 1
        if Flag:
            count = 0
            self.findRoot().inorderTraverse(count, False)

        if self.LChild:
            self.LChild.inorderTraverse(count, False)

        if self.RChild:
            self.RChild.inorderTraverse(count, False)
        return count

    def isTwoNode(self):
        """
        kijkt na of de huidige node een 234 equivalente 2 node is
        @return: True als twonode
        """
        if self.color == Black:
            if self.LChild and self.LChild.color == Red:
                return False
            elif self.RChild and self.RChild.color == Red:
                return False
            else:
                return True
        else:
            return False

    def isThreeNode(self):
        """
        kijkt na of de huidige node een 234 equivalente 3 node is
        @return: True als threeNode
        """
        if self.color == Black:
            if self.RChild and self.RChild.color == Red and not self.LChild and not self.LChild.color == Red:
                return True
            elif self.LChild and self.LChild.color == Red and not self.RChild and not self.RChild.color == Red:
                return True
            else:
                return False
        else:
            return self.parent.isThreeNode()

    def isFourNode(self):
        """
        kijkt na of de huidige node een 234 equivalente 4 node is
        @return: True als foutNode
        """
        if self.color == Black:
            if self.RChild and self.RChild.color == Red and self.LChild and self.LChild.color:
                return True
            else:
                return False
        else:
            return self.parent.isFourNode()

    def findRSibling(self):
        """
        zoekt de 234 equivalente rechtersibling als deze bestaat
        @return: een node van de rechtersibling in rbt vorm, none als er geen is
        """
        if self.parent.RChild == self:
            if self.parent.rightItemOfNode() == self.parent:
                return None
            if self.parent.parent and self.parent.rightItemOfNode() == self.parent.parent:
                if self.parent.parent.RChild:
                    return self.parent.parent.RChild
            if self.parent.parent.RChild and self.parent.parent.RChild == self.parent.rightItemOfNode():
                if self.parent.parent.RChild.LChild:
                    return self.parent.parent.RChild.LChild
        elif self.parent.RChild:
            if self.parent.RChild.color == Black:
                return self.parent.RChild
            else:
                return self.parent.RChild.LChild
        return None

    def findLSibling(self):
        """
        zoekt de 234 equivalente linkersibling als deze bestaat
        @return: een node van de linkersibling in rbt vorm, none als er geen is
        """
        if self.parent.LChild == self:
            if self.parent == self.parent.leftItemOfNode():
                return None
            if self.parent.parent and self.parent.leftItemOfNode() == self.parent.parent:
                if self.parent.parent.LChild:
                    return self.parent.parent.LChild
            if self.parent.parent.LChild and self.parent.parent.LChild == self.parent.leftItemOfNode():
                if self.parent.parent.LChild.RChild:
                    return self.parent.parent.LChild.RChild
        elif self.parent.LChild:
            if self.parent.LChild.color == Black:
                return self.parent.LChild
            else:
                return self.parent.LChild.RChild
        return None

    def leftItemOfNode(self):
        """
        zoekt de meest linkse noode van de equivalente 234 node
        @return: de linkernode van de node in 234 vorm
        """
        if self.color == Red:
            return self.parent.leftItemOfNode()
        if self.LChild and self.LChild.color == Red:
            return self.LChild
        else:
            return self

    def rightItemOfNode(self):
        """
        zoekt de meest rechtse noode van de equivalente 234 node
        @return: de rechternode van de node in 234 vorm
        """
        if self.color == Red:
            return self.parent.rightItemOfNode()
        if self.RChild and self.RChild.color == Red:
            return self.RChild
        else:
            return self

    def merge(self):
        """
        merged de huidige node, gepaste parent en gepaste sibling
        @return: None
        @precondition None
        @postcondition de 234 equivalent van de node is een 3 of 4 node
        """
        sibling = None
        if self.parent.isTwoNode() and self.isTwoNode():
            if self.parent.LChild == self and self.parent.RChild:
                sibling = self.parent.RChild
            elif self.parent.RChild == self and self.parent.LChild:
                sibling = self.parent.LChild
            self.color = Red
            sibling.color = Red
            return
        if self.parent.color == Red:
            if self.parent.RChild == self:
                sibling = self.parent.LChild
            elif self.parent.LChild == self:
                sibling = self.parent.RChild
        else:
            if self.parent.RChild == self:
                sibling = self.parent.LChild.RChild
            elif self.parent.LChild == self:
                sibling = self.parent.RChild.LChild

        if (self.parent.isThreeNode() or self.parent.isFourNode()) and sibling.isTwoNode() and self.isTwoNode():
            parent = self.parent
            if self.parent.color == Red:
                parent.color = Black
                sibling.color = Red
                self.color = Red
            else:
                if self.parent.RChild == self:
                    if parent.parent:
                        if parent.parent.LChild == parent:
                            parent.parent.LChild = sibling.parent
                        elif parent.parent.RChild == parent:
                            parent.parent.RChild = sibling.parent

                    sibling.parent.RChild = parent
                    parent.parent = sibling.parent

                    sibling.parent = parent
                    parent.LChild = sibling
                elif self.parent.LChild == self:
                    sibling.parent.parent = parent.parent
                    if parent.parent:
                        if parent.parent.LChild == parent:
                            parent.parent.LChild = sibling.parent
                        elif parent.parent.RChild == parent:
                            parent.parent.RChild = sibling.parent

                    sibling.parent.LChild = parent
                    parent.parent = sibling.parent

                    sibling.parent = parent
                    parent.RChild = sibling

                self.parent.parent.color = Black
                sibling.color = Red
                self.color = Red

    def save(self, Start=True):  # {query}
        """
        maakt van de RBT een python dictionary die bestaat uit de root, kleur en mogelijks een lijst met children
        :return dict: de dictionary wanneer deze volledig is
        :preconditie: de boom bestaat
        """
        dict = {}
        if Start:
            return self.findRoot().save(False)
        # dictionary is leeg

        dict["root"] = self.key
        if self.color == Red:
            dict["color"] = "red"
        else:
            dict["color"] = "black"
        if not self.RChild and not self.LChild:
            # return dict indien je in een blad zit
            return dict
        else:
            # anders is er minstens een deelboon
            dict["children"] = []
            # als er een linkerdeelboom is, append de linkerdeelboom in de kinderenlijst van de huidige boom
            if self.LChild:
                dict["children"].append(self.LChild.save(False))
            # anders, append None in de kinderenlijst van de huidige boom
            else:
                dict["children"].append(None)
            # als er een rechterdeelboom is, append de linkerdeelboom in de kinderenlijst van de huidige boom
            if self.RChild:
                dict["children"].append(self.RChild.save(False))
            # anders, append None in de kinderenlijst van de huidige boom
            else:
                dict["children"].append(None)
            return dict

    def load(self, dict, Start=True):
        """
        laad een dictionary in de rbt
        parameter dict: de in te laden dictionarry
        parameter Start: gebruikt om bij te houden of de recursiediepte 0 is
        preconditie: de dictionary is opgebebouwd in het juiste formaat 
        postconditie: de bst is gelijk aan de weergave dictionary-vorm
        """
        # maak de bst leeg
        if Start:
            self.destroy()
        # rootelement wordt key
        self.key = dict['root']
        if dict['color'] == "red":
            self.color = Red
        else:
            self.color = Black
        self.node = createTreeItem(self.key, None)
        if 'children' in dict:
            if dict['children'][0]:
                # eerste element wordt linkerdeelboom
                self.LChild = RedBlackTree()
                self.LChild.parent = self
                self.LChild.load(dict['children'][0], False)
            if dict['children'][1]:
                # tweede element wordt linkerdeelboom
                self.RChild = RedBlackTree()
                self.RChild.parent = self
                self.RChild.load(dict['children'][1], False)

    def destroy(self):
        """
        maakt de boom leeg
        @return: True als het geleegd is
        """
        self.parent = None
        self.root = None
        self.LChild = None
        self.RChild = None
        self.node = None
        self.key = None
        return True



