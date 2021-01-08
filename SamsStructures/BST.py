def createTreeItem(key, val):
    return key, val


class BST:
    def __init__(self, TreeItem=None):
        """
        maakt een nieuwe binaire zoekboom aan
        :param TreeItem: het eventuele object dat in de root wordt gezet
        """
        # als er een item wordt meegegeven
        if TreeItem:
            self.key = TreeItem[0]
            self.value = TreeItem[1]
        # als er geen wordt meegegevem
        else:
            self.key = None
            self.value = None
        # linkerchild
        self.lc = None
        # rechterchild
        self.rc = None
        # aantal items in de boom
        self.items = 0

    def isEmpty(self):  # {query}
        """
        kijkt na of de bst leeeg is
        returns bool: True wanneer empty, anders False
        preconditie: de bst bestaat
        """
        if not self.key:
            return True
        else:
            return False

    def searchTreeInsert(self, TreeItem):
        """
        insert een item in de boom
        :param TreeItem: het toe te voegen object
        :return bool: True bij slagen van de functie
        :precondities: de boom bestaat, de key is uniek (TreeItem[0])
        :postcondities: self.items += 1
        """
        # lege boom
        if not self.key:
            self.key = TreeItem[0]
            self.value = TreeItem[1]
            self.items += 1
            return True
        # als de key van het toe te voegen item kleiner is dan de key van de huidige node
        elif TreeItem[0] < self.key:
            self.items += 1
            # als er nog geen linkerkind is, maak een nieuwe en initialiseer deze met de meegegeven data
            if not self.lc:
                lc = BST(TreeItem)
                self.lc = lc
                return True
            # anders recursief vanaf de linkerdeelboom
            else:
                return self.lc.searchTreeInsert(TreeItem)
        # als de key van het toe te voegen item groter is dan die van de huidige node
        elif TreeItem[0] > self.key:
            self.items += 1
            # als er geen rechterboom bestaat wordt dit een nieuwe boom met de data die meegegeven is
            if not self.rc:
                rc = BST(TreeItem)
                self.rc = rc
                return True
            # anders recursief vanaf de rechterdeelboom
            else:
                return self.rc.searchTreeInsert(TreeItem)

        else:
            return False

    def searchTreeRetrieve(self, key):  # {query}
        """
        vraagt een item met zoeksleutel key op uit de bst
        :param key: de zoeksleutel gekoppeld aan het object
        :return[0] self.value: de data die verbonden is met de key
        :return[1] bool: True bij success
        :precondities: de bst bestaat, de key is uniek
        """
        if self.key == key:
            # als de key gelijk is aan de key van de node, return de data
            return self.value, True
        elif self.lc and key < self.key:
            # kleiner -> ga naar linkerdeelboom (indien die bestaat)
            return self.lc.searchTreeRetrieve(key)
        elif self.rc and key > self.key:
            # groter -> ga naar rechterdeelboom
            return self.rc.searchTreeRetrieve(key)
        else:
            # return None wanneer je niet meer verder kan (geen bijhoordende deelboom waar de key mogelijk inzit)
            return None, False

    def inorderTraverse(self, functie=None):
        """
        gaat de bst af op een inorder manier en voert steeds de meegegeven functie hierop uit
        par functie: de uit te voeren functie
        returns: hangt af van de meegegeven functie
        preconditie: de bst bestaat
        """
        if self.lc:
            self.lc.inorderTraverse(functie)
        functie(self.data)
        if self.rc:
            self.rc.inorderTraverse(functie)

    def destroy(self):
        """
        maakt de boom leeg
        :return bool: het al dan niet slagen van de functie, True = success
        :precondities: de bst bestaat
        :postcondities: self.items = 0, de bst is leeg
        """
        # garbagecollecter doet het meeste werk
        self.key = None
        self.value = None
        self.lc = None
        self.rc = None
        self.items = 0

    def save(self):  # {query}
        """
        maakt van de binaire zoekboom een python dictionary die bestaat uit de root en mogelijks een lijst met children
        :return dict: de dictionary wanneer deze volledig is
        :preconditie: de boom bestaat
        """
        # dictionary is leeg
        dict = {}
        dict["root"] = self.key
        if not self.rc and not self.lc:
            # return dict indien je in een blad zit
            return dict
        else:
            # anders is er minstens een deelboon
            dict["children"] = []
            # als er een linkerdeelboom is, append de linkerdeelboom in de kinderenlijst van de huidige boom
            if self.lc:
                dict["children"].append(self.lc.save())
            # anders, append None in de kinderenlijst van de huidige boom
            else:
                dict["children"].append(None)
            # als er een rechterdeelboom is, append de linkerdeelboom in de kinderenlijst van de huidige boom
            if self.rc:
                dict["children"].append(self.rc.save())
            # anders, append None in de kinderenlijst van de huidige boom
            else:
                dict["children"].append(None)
            return dict

    def load(self, dict, Start=True):
        """
        laad een dictionary in de bst
        parameter dict: de in te laden dictionarry
        parameter Start: gebruikt om bij te houden of de recursiediepte 0 is
        preconditie: de dictionary is opgebebouwd in het juiste formaat 
        postconditie: de bst is gelijk aan de weergave dictionary-vorm
        """
        self.items = len(dict)
        # maak de bst leeg
        if Start:
            self.destroy()
        # rootelement wordt key
        self.key = dict['root']
        if 'children' in dict:
            if dict['children'][0]:
                # eerste element wordt linkerdeelboom
                self.lc = BST()
                self.lc.load(dict['children'][0], False)
            if dict['children'][1]:
                # tweede element wordt linkerdeelboom
                self.rc = BST()
                self.rc.load(dict['children'][1], False)

    def findInorderSuccessor(self, Start=True):  # {query}
        """
        zoekt de inorder successor van de bst
        parameter Start: gebruikt om bij te houden of het recursieniveau 0 is
        returns self: de inorder successor
        precondities: de bst bestaat
        """
        if Start and self.rc:
            # eerste doorloop eenmaal naar rechterdeelboom
            return self.rc.findInorderSuccessor(False)
        elif not Start and self.lc:
            # vanaf dan zo veel mogelijk naar linkerdeelboom
            return self.lc.findInorderSuccessor(False)
        else:
            return self

    def searchTreeDelete(self, key, inorderNode=None):
        """
        delete een item uit de tree
        parameter key: de key van het te deleten item
        parameter inorderNode: de inorder successor van het item dat gedelete moet worden
        returns bool: True bij success
        precondities: de bst bestaat, de key is een key in de bst
        postcondities: self.items -= 1 (een item minder in de bst)
        """
        # als er een inordernode is
        if inorderNode:
            # als de inordernode de linkerdeelboom is
            if self.lc and inorderNode == self.lc:
                self.lc = None
                return True
            # als de inordernode de rechterdeelboom is
            if self.rc and inorderNode == self.rc:
                self.rc = None
                return True

        if key > self.key:
            # key groter dan de key in de huidige node en er is een rechterdeelboom
            if self.rc:
                return self.rc.searchTreeDelete(key, inorderNode)
            # geen rechterdeelboom
            else:
                return False

        if key < self.key:
            # key kleiner dan de key in de huidige node en er is een linkerdeelboom
            if self.lc:
                return self.lc.searchTreeDelete(key, inorderNode)
            else:
                return False

        if self.key == key:
            # als dit de node is die gedelete moet worden
            if self.lc and not self.rc:
                # als er enkel een rechterdeelboom is kan de huidige node worden overgeslagen
                self.value = self.lc.value
                self.key = self.lc.key
                self.rc = self.lc.rc
                self.lc = self.lc.lc

            elif self.rc and not self.lc:
                # als er enkel een linkerdeelboom is kan de huidige node worden overgeslagen
                self.value = self.rc.value
                self.key = self.rc.key
                self.lc = self.rc.lc
                self.rc = self.rc.rc
            if not inorderNode:
                # als er nog geen inordersuccessor gegeven is
                inorderNode = self.findInorderSuccessor()
                # swap de inordernode en te deleten node
                self.value = inorderNode.value
                self.key = inorderNode.key
            if inorderNode == self:
                # als de inordersuccessor gelijk is aan de huidige node kunnen we deze leegmaken
                self.key = None
                self.value = None

            if self.rc and self.lc:
                # als er zowel een linker als rechterboom is
                # zoek terug welke node gedelete moet worden, deze zit nu in een blad
                self.rc.searchTreeDelete(self.key, inorderNode)

        # deelboom zonder key uit de boom verwijderen
        if self.rc and not self.rc.key:
            self.rc = None
            return True

        elif self.lc and not self.lc.key:
            self.lc = None
            return True

