"""
ADT contract voor rood-zwartboom
"""

def createTreeItem(key,val=None):
    """
    De items worden in een tuple gestoken en die worden in de insertmethode van de rood-zwartboom terug uitgepakt.
    (Ik had bij het maken van de roodzwartboom bij de insertmethode key en value als parameters gebruikt en
    geen rood-zwartknoop.)

    :param key: searchkey
    :param val: waarde
    :return: tuple
    """
    return key, val

class RBTNode:
    def __init__(self, key=None, value=None, color=None, left=None, right=None, parent=None):
        """
        Creëert een knoop voor een rood zwart boom.
        """
        self.key = key
        self.value = value
        self.color = color
        self.left = left
        self.right = right
        self.parent = parent

    def is2node(self):
        """
        Kijkt na of dat de knoop een 2-knoop is. (kan alleen bij zwarte knopen gebruikt worden)
        :return: boolean
        """
        # Een knoop is een 2-knoop als beide kinderen zwart zijn
        for child in [self.left, self.right]:
            if child is None:
                return False
            if child.color == "red":
                return False
        return True

    def is3node(self):
        """
        Kijkt na of dat de knoop een 3-knoop is. (kan alleen bij zwarte knopen gebruikt worden)
        :return: boolean
        """
        # Een knoop is een 3-knoop als 1 kind zwart is en de andere rood
        if self.left is not None and self.right is not None:
            if self.left.color == "red":
                if self.right.color == "black":
                    return True
            else:
                if self.right.color == "red":
                    return True
        return False

    def is4node(self):
        """
        Kijkt na of dat de knoop een 4-knoop is (kan alleen bij zwarte knopen gebruikt worden)
        :return: boolean
        """
        # Een knoop is een 4-knoop als beide kinderen rood zijn
        for child in [self.left, self.right]:
            if child is None:
                return False
            if child.color == "black":
                return False
        return True

    def isLeftChild(self):
        """
        Kijkt na of dat de knoop een linkerkind is
        :return: boolean
        """
        return self == self.parent.left

    def isRightChild(self):
        """
        Kijkt na of dat de knoop een rechterkind is.
        :return: boolean
        """
        return self == self.parent.right

    def switchColor(self):
        """
        Wisselt de kleur van de knoop
        :return: None
        """
        if self.color == "red":
            self.color = "black"
        else:
            self.color = "red"

    def colorChanges(self):
        """
        Wisselt de kleur van de knoop en zijn kinderen
        :return: None
        """
        self.left.switchColor()
        self.right.switchColor()
        self.switchColor()

    def getTwoThreeFourParent(self):
        """
        Geeft de ouder van de rood-zwartknoop volgens de 2-3-4boom.
        :return: RBTNode object
        """
        if self.parent.color == "black":
            return self.parent
        else:
            return self.parent.parent

    def getLeftSibling(self):
        """
        Geeft de linker sibling van de huidige rood-zwartknoop volgens de 2-3-4boom.
        Als er geen linker sibling is dan wordt None terug gegeven.
        :return: RBTNode object
        """
        twothreefour_parent = self.getTwoThreeFourParent()

        if twothreefour_parent.is2node() and self.isRightChild():
            return self.parent.left

        elif twothreefour_parent.is3node():
            if self.parent.color == "red" and self.isRightChild():
                return self.parent.left
            elif self.parent.color == "red" and self.isLeftChild() and self.parent.isRightChild():
                return self.parent.parent.left
            elif self.parent.color == "black" and self.isRightChild():
                return self.parent.left.right

        elif twothreefour_parent.is4node():
            if self.isRightChild():
                return self.parent.left
            elif self.isLeftChild() and self.parent.isRightChild():
                return self.parent.parent.left.right

    def getRightSibling(self):
        """
        Geeft de rechter sibling van de huidige rood-zwartknoop volgens de 2-3-4boom.
        Als er geen rechter sibling is dan wordt None terug gegeven.
        :return: RBTNode object
        """
        twothreefour_parent = self.getTwoThreeFourParent()

        if twothreefour_parent.is2node() and self.isLeftChild():
            return self.parent.right

        elif twothreefour_parent.is3node():
            if self.parent.color == "red" and self.isLeftChild():
                return self.parent.right
            elif self.parent.color == "red" and self.isRightChild() and self.parent.isLeftChild():
                return self.parent.parent.right
            elif self.parent.color == "black" and self.isLeftChild():
                return self.parent.right.left

        elif twothreefour_parent.is4node():
            if self.isLeftChild():
                return self.parent.right
            elif self.isRightChild() and self.parent.isLeftChild():
                return self.parent.parent.right.left


class RedBlackTree:
    counter = 0

    def __init__(self):
        """
        Creëert een lege rood-zwartboom.
        """
        self.root = None
        self.count = 0
        self.NULLNode = RBTNode()

    def load(self, RBTDict, node=None, start=True):
        """
        Laadt de rood-zwartboom uit een dictionary.
        :param RBTDict: dictionary
        :return: RedBlackTree object
        """
        if start:
            # Als de dictionary leeg is
            if RBTDict is None or RBTDict == {}:
                return None

            # Creëer een knoop voor de wortel
            self.root = RBTNode()
            node = self.root

        # Wijs de waarden aan de knoop toe
        if 'root' in RBTDict:
            node.key = RBTDict.get('root')
        if 'value' in RBTDict:
            node.value = RBTDict.get('value')
        if 'color' in RBTDict:
            node.color = RBTDict.get('color')

        # Voeg 1 toe aan het totaal aantal knopen
        self.count += 1

        # Kijk of de knoop kinderen heeft
        if 'children' in RBTDict:
            if RBTDict['children'][0] is not None:
                node.left = RBTNode()
                node.left.parent = node
                self.load(RBTDict['children'][0], node.left, False)
            else:
                node.left = self.NULLNode

            if RBTDict['children'][1] is not None:
                node.right = RBTNode()
                node.right.parent = node
                self.load(RBTDict['children'][1], node.right, False)
            else:
                node.right = self.NULLNode
        else:
            node.left = self.NULLNode
            node.right = self.NULLNode

    def save(self, addvalues=False, node=None, start=True):
        """
        Slaagt de rood-zwartboom op in een dictionary.
        :param addvalues: boolean die bepaalt of dat the waarden ook opgeslagen moeten worden
        :return: dictionary
        """
        RBTDict = {}

        if start:
            # Als de rood-zwartboom leeg is
            if self.root is None:
                return RBTDict

            node = self.root
            self.save(addvalues, node, False)

        # Voeg de waarden van de knoop toe aan de dictionary
        if node.key is not None:
            RBTDict['root'] = node.key
        else:
            return
        if node.value is not None and addvalues:
            RBTDict['value'] = node.value
        if node.color is not None:
            RBTDict['color'] = node.color

        # Als de knoop kinderen heeft
        if not (node.left == self.NULLNode and node.right == self.NULLNode):
            RBTDict['children'] = []
            for child in [node.left, node.right]:
                if child != self.NULLNode:
                    RBTDict['children'].append(self.save(addvalues, child, False))
                else:
                    RBTDict['children'].append(None)

        return RBTDict

    def print(self, depth=0, node=None, start=True):
        """
        Print de rood-zwartboom in de console.
        :return: None
        """
        if start:
            # Als de rood-zwartboom leeg is
            if self.root is None:
                print(None)
                return
            node = self.root

        # Print de huidige knoop
        if node.color == "black":
            print('%s' % ((depth * '\t') + "|B| " + str(node.key) + ": " + str(node.value)))
        else:
            print('%s' % ((depth * '\t') + "|R| " + str(node.key) + ": " + str(node.value)))

        # Als de knoop geen kinderen heeft
        if node.left == self.NULLNode and node.right == self.NULLNode:
            return

        # Print het linkerkind
        if node.left != self.NULLNode:
            self.print(depth + 1, node.left, False)
        else:
            print('%s' % (((depth + 1) * '\t') + "None"))

        # Print het rechterkind
        if node.right != self.NULLNode:
            self.print(depth + 1, node.right, False)
        else:
            print('%s' % (((depth + 1) * '\t') + "None"))

    def isEmpty(self):
        """
        Kijkt of de rood-zwartboom leeg is.
        :return: boolean
        """
        if self.root is None:
            return True
        else:
            return False

    def getHeight(self, current_node=None, start=True):
        """
        Geeft de hoogte van de rood-zwartboom.
        :return: integer, boolean
        """
        # Zet in het begin current_node gelijk aan die van de wortel
        if start:
            if self.root is None:
                return 0
            current_node = self.root

        # Geef 1 terug als de knoop geen kinderen heeft
        if current_node.left == self.NULLNode and current_node.right == self.NULLNode:
            return 1

        # Zoek de grootste hoogte bij de kinderen
        else:
            max_height = 0
            if current_node.left != self.NULLNode:
                temp = self.getHeight(current_node.left, False)
                if temp > max_height:
                    max_height = temp

            if current_node.right != self.NULLNode:
                temp = self.getHeight(current_node.right, False)
                if temp > max_height:
                    max_height = temp

            # Geef 1 + de hoogte van langste pad vanaf een kind van de huidige knoop
            return 1 + max_height

    def getNumberOfNodes(self):
        """
        Geeft het aantal knopen in de rood-zwartboom.
        :return: integer, boolean
        """
        return self.count

    def getRootData(self):
        """
        Geeft de waarde dat in de wortel van de rood-zwartboom zit.
        :return: value, boolean
        """
        return self.root.value

    def leftRotate(self, current_node):
        """
        Voert een leftrotate uit op een rood-zwartknoop.
        :param current_node: knoop die wordt geroteerd
        :return: None
        """
        if current_node.parent is None:
            self.root = current_node.right

        if current_node.parent is not None:
            if current_node.isLeftChild():
                current_node.parent.left = current_node.right
            else:
                current_node.parent.right = current_node.right

        current_node.right.parent = current_node.parent
        current_node.parent = current_node.right

        temp = current_node.right.left
        current_node.right.left = current_node
        current_node.right = temp
        if temp is not None:
            current_node.right.parent = current_node

    def rightRotate(self, current_node):
        """
        Voert een rightrotate uit op een rood-zwartknoop.
        :param current_node: knoop die wordt geroteerd
        :return: None
        """
        if current_node.parent is None:
            self.root = current_node.left

        if current_node.parent is not None:
            if current_node.isLeftChild():
                current_node.parent.left = current_node.left
            else:
                current_node.parent.right = current_node.left

        current_node.left.parent = current_node.parent
        current_node.parent = current_node.left

        temp = current_node.left.right
        current_node.left.right = current_node
        current_node.left = temp
        if temp is not None:
            current_node.left.parent = current_node

    def insertItem(self, TreeItem, key=None, value=None, current_node=None, start=True):
        """
        Voegt een nieuwe item toe aan de rood-zwartboom.
        :param key: search key (int of string)
        :param value: waarde
        :return: boolean
        """
        # Zet in het begin de current_node gelijk aan die van de wortel
        if start:
            # Pak TreeItem uit
            key, value = TreeItem[0], TreeItem[1]

            # Als de boom leeg is
            if self.root is None:
                self.root = RBTNode(key, value, "black")
                self.root.left = self.NULLNode
                self.root.right = self.NULLNode

                self.count += 1
                return True

            self.insertItem(None, key, value, self.root, False)
            return True

        # Splits de huidige knoop als die een 4-knoop is
        if current_node.color == "black" and current_node.is4node():
            self.split4Node(current_node)

        # Als de te inserten key kleiner is dan de key van de huidige knoop en de huidige knoop is een blad
        if key < current_node.key and current_node.left == self.NULLNode:
            current_node.left = RBTNode(key, value, "red", parent=current_node)
            current_node.left.left = self.NULLNode
            current_node.left.right = self.NULLNode
            new_node = current_node.left
            self.count += 1

            if current_node.color == "red" and new_node.color == "red":
                if current_node.isLeftChild():
                    self.rightRotate(current_node.parent)

                    current_node.switchColor()
                    current_node.right.switchColor()

                else:
                    self.rightRotate(current_node)
                    current_node = current_node.parent
                    self.leftRotate(current_node.parent)

                    current_node.switchColor()
                    current_node.left.switchColor()

            return True

        # Als de te inserten key kleiner is dan de key van de huidige knoop en de huidige knoop is geen blad
        elif key < current_node.key and current_node.left != self.NULLNode:
            self.insertItem(None, key, value, current_node.left, False)

        # Als de te inserten key groter is dan de key van de huidige knoop en de huidige knoop is een blad
        elif key > current_node.key and current_node.right == self.NULLNode:
            current_node.right = RBTNode(key, value, "red", parent=current_node)
            current_node.right.left = self.NULLNode
            current_node.right.right = self.NULLNode
            new_node = current_node.right
            self.count += 1

            if current_node.color == "red" and new_node.color == "red":
                if current_node.isRightChild():
                    self.leftRotate(current_node.parent)

                    current_node.switchColor()
                    current_node.left.switchColor()
                else:
                    self.leftRotate(current_node)
                    current_node = current_node.parent
                    self.rightRotate(current_node.parent)

                    current_node.switchColor()
                    current_node.right.switchColor()

            return True

        # Als de te inserten key groter is dan de key van de huidige knoop en de huidige knoop is geen blad
        elif key > current_node.key and current_node.right != self.NULLNode:
            self.insertItem(None, key, value, current_node.right, False)

    def split4Node(self, current_node):
        """
        Hulpfunctue van insertItem. Splitst een 4-knoop op.
        :param current_node: huidige knoop
        :return: None
        """
        if current_node == self.root:
            current_node.left.switchColor()
            current_node.right.switchColor()
            return

        twothreefour_parent = current_node.getTwoThreeFourParent()

        if twothreefour_parent.is2node():
            current_node.colorChanges()

        # Als de ouder rood is moet die rotaties doen
        elif twothreefour_parent.is3node() and current_node.parent.color == "red":
            # Als current_node en ouder linkerkinderen zijn
            if current_node.isLeftChild() and current_node.parent.isLeftChild():
                self.rightRotate(current_node.parent.parent)
                current_node.parent.switchColor()
                current_node.parent.right.switchColor()
                current_node.colorChanges()

            # Als current_node en ouder rechterkinderen zijn
            elif current_node.isRightChild() and current_node.parent.isRightChild():
                self.leftRotate(current_node.parent.parant)
                current_node.parent.switchColor()
                current_node.parent.left.switchColor()
                current_node.colorChanges()

            # Als current_node linkerkind is en ouder rechterkind
            elif current_node.isLeftChild() and current_node.parent.isRightChild():
                current_node.left.switchColor()
                current_node.right.switchColor()
                self.rightRotate(current_node.parent)
                self.leftRotate(current_node.parent)
                current_node.left.switchColor()

            # Als current_node rechterkind is en ouder linkerkind
            elif current_node.isRightChild() and current_node.parent.isLeftChild():
                current_node.left.switchColor()
                current_node.right.switchColor()
                self.leftRotate(current_node.parent)
                self.rightRotate(current_node.parent)
                current_node.right.switchColor()

        # Als de ouder niet rood is moed die color changes doen
        elif twothreefour_parent.is3node() and current_node.parent.color == "black":
            current_node.colorChanges()

    def deleteItem(self, key):
        """
        Verwijdert de knoop dat het gegeven zoeksleutel bevat.
        :param key: zoeksleutel
        :return: boolean
        """
        # Kijk of dat de knoop bestaat in de boom
        if not self.retrieveItem(key)[1]:
            return False

        # Zoek de knoop die het te verwijderen item bevat en
        # vorm elke 2-knoop (behalve de wortel) op dit pad om tot een 3-knoop of een 4-knoop
        if self.root.key == key:
            if self.root.left == self.NULLNode and self.root.right == self.NULLNode:
                self.root = None

        node_to_delete = self.deleteSearchNode(key)
        if node_to_delete is None:
            return False

        # Zoek de inorder successor van de knoop
        inosuc = self.deleteSearchInorderSuccessor(node_to_delete)

        # Verwissel de items van de knopen
        node_to_delete.key = inosuc.key
        node_to_delete.value = inosuc.value

        # Verwijder de inorder successor
        if inosuc.color == "red":
            if inosuc.isLeftChild():
                inosuc.parent.left = self.NULLNode
            else:
                inosuc.parent.right = self.NULLNode
        else:
            if inosuc.is3node():
                if inosuc.left.color == "red":
                    self.rightRotate(inosuc)
                    inosuc.parent.switchColor()
                    inosuc.parent.right = self.NULLNode
                else:
                    self.leftRotate(inosuc)
                    inosuc.parent.switchColor()
                    inosuc.parent.left = self.NULLNode
            elif inosuc.is4node():
                self.leftRotate(inosuc)
                inosuc.parent.parent.switchColor()
                inosuc.parent.left = self.NULLNode

        self.count -= 1
        return True

    def deleteSearchNode(self, key, current_node=None, start=True):
        """
        Hulpfunctie van deleteItem. Zoekt de te verwijderen knoop en vormt elke 2-knoop (behalve de wortel) op
        dit pad om tot een 3-knoop of een 4-knoop.
        :return: RBTNode object
        """
        # Zet in het begin current_node gelijk aan die van de wortel
        if start:
            # Als de boom leeg is
            if self.root is None:
                return None
            return self.deleteSearchNode(key, self.root, False)

        # Herverdeel of merge als het een 2-knoop is
        self.mergeOrRedistribute(current_node)

        if key == current_node.key:
            return current_node
        elif key < current_node.key and current_node.left is not None:
            if current_node.left == self.NULLNode:
                return None
            return self.deleteSearchNode(key, current_node.left, False)
        elif key > current_node.key and current_node.right is not None:
            if current_node.right == self.NULLNode:
                return None
            return self.deleteSearchNode(key, current_node.right, False)

    def deleteSearchInorderSuccessor(self, current_node, left=False):
        """
        Hulpfunctie van deleteItem. Zoekt de inorder successor van de te verwijderen knoop en vormt elke
        2-knoop (behalve de wortel) op dit pad om tot een 3-knoop of een 4-knoop.
        :return: RBTNode object
        """
        # Herverdeel of merge als het een 2-knoop is
        self.mergeOrRedistribute(current_node)

        # Ga eerst 1 keer naar rechts
        if not left:
            if current_node.right != self.NULLNode:
                return self.deleteSearchInorderSuccessor(current_node.right, True)
            else:
                return current_node
        # Blijf links gaan tot een blad
        else:
            if current_node.left != self.NULLNode:
                return self.deleteSearchInorderSuccessor(current_node.left, True)
            else:
                return current_node

    def mergeOrRedistribute(self, current_node):
        """
        Hulpfunctie van deleteSearchNode en deleteSearchInorderSuccessor. Kijkt of dat de gegeven knoop een
        2-knoop is en bepaald of dat er gemerged of gedeeld moet worden.
        :return: None
        """
        # Als de node een 2node is en die is geen root
        if current_node != self.root and current_node.color == "black" and current_node.is2node():
            # Kijk of dat de linkersibling iets kan uitlenen en redistribute
            left_sibling = current_node.getLeftSibling()
            right_sibling = current_node.getRightSibling()
            if left_sibling is not None and (left_sibling.is3node() or left_sibling.is4node()):
                self.leftredistribute(current_node)

            # Kijk of dat de rechtersibling iets kan uitlenen en redistribute
            elif right_sibling is not None and (right_sibling.is3node() or right_sibling.is4node()):
                self.rightredistribute(current_node)

            # Anders merge met linkersibling (of rechtersibling als waarde meest rechtse is volgens 234boom)
            else:
                self.merge2node(current_node)

    def leftredistribute(self, current_node):
        """
        Hulpfunctie van mergeOrRedistribute. Herverdeelt en zorgt ervoor dat de huidige knoop geen 2-knoop meer is.
        :return: None
        """
        twothreefour_parent = current_node.getTwoThreeFourParent()
        left_sibling = current_node.getLeftSibling()

        if left_sibling.is3node():
            if left_sibling.right is not None and left_sibling.right.color == "red":
                self.leftRotate(left_sibling)
                left_sibling.switchColor()
                left_sibling.parent.switchColor()
                left_sibling = left_sibling.parent
        else:
            self.leftRotate(left_sibling)
            left_sibling.switchColor()
            left_sibling.parent.switchColor()
            left_sibling = left_sibling.parent

        if twothreefour_parent.is2node():
            self.rightRotate(current_node.parent)
            current_node.switchColor()
            current_node.parent.parent.left.switchColor()

        elif twothreefour_parent.is3node():
            if current_node == twothreefour_parent.right.right:
                self.rightRotate(current_node.parent)
                current_node.parent.parent.colorChanges()
                current_node.switchColor()

            elif current_node == twothreefour_parent.right:
                self.leftRotate(current_node.parent.left)
                self.rightRotate(current_node.parent)
                current_node.switchColor()
                current_node.parent.parent.left.right.switchColor()

            elif current_node == twothreefour_parent.right.left:
                current_node.parent.switchColor()
                self.leftRotate(current_node.parent.parent)
                current_node.parent.left.switchColor()
                current_node.parent.left.left.switchColor()
                self.rightRotate(current_node.parent)
                current_node.switchColor()

            elif current_node == twothreefour_parent.left.right:
                current_node.parent.switchColor()
                current_node.parent.left.switchColor()
                current_node.parent.left.left.switchColor()
                self.rightRotate(current_node.parent)
                current_node.switchColor()

        elif twothreefour_parent.is4node():
            if current_node.isRightChild():
                self.rightRotate(current_node.parent)
                current_node.switchColor()
                current_node.parent.switchColor()
                current_node.parent.parent.switchColor()
                current_node.parent.parent.left.switchColor()
            else:
                self.leftRotate(left_sibling.parent)
                self.rightRotate(current_node.parent.parent)
                self.leftRotate(current_node.parent.parent)
                current_node.switchColor()
                current_node.parent.parent.parent.left.right.switchColor()

    def rightredistribute(self, current_node):
        """
        Hulpfunctie van mergeOrRedistribute. Herverdeelt en zorgt ervoor dat de huidige knoop geen 2-knoop meer is.
        :return: None
        """
        twothreefour_parent = current_node.getTwoThreeFourParent()
        right_sibling = current_node.getRightSibling()

        if right_sibling.is3node():
            if right_sibling.left is not None and right_sibling.left.color == "red":
                self.rightRotate(right_sibling)
                right_sibling.switchColor()
                right_sibling.parent.switchColor()
                right_sibling = right_sibling.parent
        else:
            self.rightRotate(right_sibling)
            right_sibling.switchColor()
            right_sibling.parent.switchColor()
            right_sibling = right_sibling.parent

        if twothreefour_parent.is2node():
            self.leftRotate(current_node.parent)
            current_node.switchColor()
            current_node.parent.parent.right.switchColor()

        elif twothreefour_parent.is3node():
            if current_node == twothreefour_parent.left.left:
                self.leftRotate(current_node.parent)
                current_node.parent.parent.colorChanges()
                current_node.switchColor()

            elif current_node == twothreefour_parent.left:
                self.rightRotate(current_node.parent.right)
                self.leftRotate(current_node.parent)
                current_node.switchColor()
                current_node.parent.parent.right.left.switchColor()

            elif current_node == twothreefour_parent.left.right:
                current_node.parent.switchColor()
                self.rightRotate(current_node.parent.parent)
                current_node.parent.right.switchColor()
                current_node.parent.right.right.switchColor()
                self.leftRotate(current_node.parent)
                current_node.switchColor()

            elif current_node == twothreefour_parent.right.left:
                current_node.parent.switchColor()
                current_node.parent.right.switchColor()
                current_node.parent.right.right.switchColor()
                self.leftRotate(current_node.parent)
                current_node.switchColor()

        elif twothreefour_parent.is4node():
            if current_node.isLeftChild():
                self.leftRotate(current_node.parent)
                current_node.switchColor()
                current_node.parent.switchColor()
                current_node.parent.parent.switchColor()
                current_node.parent.parent.right.switchColor()
            else:
                self.rightRotate(right_sibling.parent)
                self.leftRotate(current_node.parent.parent)
                self.rightRotate(current_node.parent.parent)
                current_node.switchColor()
                current_node.parent.parent.parent.right.left.switchColor()

    def merge2node(self, current_node):
        """
        Hulpfunctie van mergeOrRedistribute. Merged de 2-knoop met zijn sibling en een item van de ouder (volgens
        de 234boom).
        :return: None
        """
        twothreefour_parent = current_node.getTwoThreeFourParent()

        if twothreefour_parent.is2node():
            # Doe een colorswitch
            current_node.switchColor()
            if current_node.isLeftChild():
                current_node.parent.right.switchColor()
            else:
                current_node.parent.left.switchColor()

        elif twothreefour_parent.is3node():
            left_sibling = current_node.getLeftSibling()
            if left_sibling is not None:
                if current_node.isRightChild() and left_sibling.isLeftChild():
                    current_node.parent.colorChanges()
                elif current_node.isLeftChild() and left_sibling.isLeftChild():
                    self.leftRotate(current_node.parent.parent)

                    current_node.switchColor()
                    current_node.parent.left.switchColor()
                    current_node.parent.parent.switchColor()
                elif current_node.isRightChild() and left_sibling.isRightChild():
                    self.rightRotate(current_node.parent)

                    current_node.switchColor()
                    current_node.parent.left.switchColor()
                    current_node.parent.parent.switchColor()
            else:
                right_sibling = current_node.getRightSibling()
                if right_sibling.isRightChild():
                    current_node.parent.colorChanges()
                else:
                    self.leftRotate(current_node.parent)

                    current_node.switchColor()
                    current_node.parent.right.switchColor()
                    current_node.parent.parent.switchColor()

        elif twothreefour_parent.is4node():
            left_sibling = current_node.getLeftSibling()
            if left_sibling is not None:
                if current_node.isRightChild():
                    current_node.parent.colorChanges()
                else:
                    self.rightRotate(current_node.parent.parent)
                    self.leftRotate(current_node.parent.parent)

                    current_node.switchColor()
                    current_node.parent.left.switchColor()
                    current_node.parent.parent.parent.switchColor()
            else:
                current_node.parent.colorChanges()

    def clear(self):
        """
        Wist de rood-zwartboom.
        :return: boolean
        """
        self.root = None

    def getNode(self, key, current_node=None, start=True):
        """
        Geeft de knoop terug die de zoeksleutel bevat.
        :param key: search key (int of string)
        :return: waarde
        """
        # Zet in het begin current_node gelijk aan die van de wortel
        if start:
            if self.root is None:
                return
            current_node = self.root

        if current_node.key == key:
            return current_node

        # Zoek bij de kinderen
        else:
            # Als de key kleiner is dan de key van de huidige node
            if key < current_node.key and current_node.left != self.NULLNode:
                temp = self.getNode(key, current_node.left, False)
                if temp is not None:
                    return temp

            # Als de key groter is dan de key van de huidige node
            if key > current_node.key and current_node.right != self.NULLNode:
                temp = self.getNode(key, current_node.right, False)
                if temp is not None:
                    return temp

    def retrieveItem(self, key):
        """
        Geeft een waarde terug uit de rood-zwartboom mbv de searchkey.
        :param key: search key (int of string)
        :return: waarde
        """
        node = self.getNode(key)
        if node is not None:
            return node.value, True
        else:
            return None, False

    def contains(self, data, node=None, start=True):
        """
        Kijkt of dat de gegeven waarde in de boom zit.
        :param data: waarde
        :return: boolean
        """
        if start:
            if self.root is None:
                return
            node = self.root

        if node.value == data:
            return True

        # Zoek bij de kinderen
        else:
            if node.left != self.NULLNode:
                temp = self.contains(data, node.left, False)
                if temp is not None:
                    return temp
            if node.right != self.NULLNode:
                temp = self.contains(data, node.right, False)
                if temp is not None:
                    return temp

        # Als het niet gevonden is en we zitten in de eerste stap van recursie
        if start:
            return False

    def preorderTraverse(self, FunctionType, current_node=None, start=True):
        """
        Doorloopt de knopen in de rood-zwartboom in preorder volgorde.
        :return: None
        """
        # Zet in het begin current_node gelijk aan die van de wortel
        if start:
            if self.root is None:
                print(None)
                return
            current_node = self.root

        # Print de searchkey van de huidige knoop
        FunctionType(current_node.key)

        # Doorloop de linkerdeelboom van de knoop
        if current_node.left != self.NULLNode:
            self.preorderTraverse(FunctionType, current_node.left, False)

        # Doorloop de rechterdeelboom van de knoop
        if current_node.right != self.NULLNode:
            self.preorderTraverse(FunctionType, current_node.right, False)

    def inorderTraverse(self, FunctionType, current_node=None, start=True):
        """
        Doorloopt de knopen in de rood-zwartboom in inorder volgorde.
        :return: None
        """
        # Zet in het begin current_node gelijk aan die van de wortel
        if start:
            if self.root is None:
                print(None)
                return
            current_node = self.root

        # Doorloop de linkerdeelboom van de knoop
        if current_node.left != self.NULLNode:
            self.inorderTraverse(FunctionType, current_node.left, False)

        # Print de searchkey van de huidige knoop
        FunctionType(current_node.key)

        # Doorloop de rechterdeelboom van de knoop
        if current_node.right != self.NULLNode:
            self.inorderTraverse(FunctionType, current_node.right, False)

    def postorderTraverse(self, FunctionType, current_node=None, start=True):
        """
        Doorloopt de knopen in de rood-zwartboom in postorder volgorde.
        :return: None
        """
        # Zet in het begin current_node gelijk aan die van de wortel
        if start:
            if self.root is None:
                print(None)
                return
            current_node = self.root

        # Doorloop de linkerdeelboom van de knoop
        if current_node.left != self.NULLNode:
            self.postorderTraverse(FunctionType, current_node.left, False)

        # Doorloop de rechterdeelboom van de knoop
        if current_node.right != self.NULLNode:
            self.postorderTraverse(FunctionType, current_node.right, False)

        # Print de searchkey van de huidige knoop
        FunctionType(current_node.key)

    def check(self, current_node=None, start=True):
        """
        Controleert of dat de rood-zwartboom correct is.
        :return: Aantal zwarte knopen op 1 pad
        """
        # Zet in het begin de current_node gelijk aan die van de wortel
        if start:
            if self.root is None:
                print("---De boom is leeg---")
                return
            current_node = self.root
            # Kijk of dat de kleur van de root zwart is
            if current_node.color != "black":
                print("---Root is rood!---")

            # Kijk of dat de wortel geen ouder heeft
            if current_node.parent is not None:
                print("---Root heeft een ouder!---")

        else:
            # Kijk na of dat current_node een ouder heeft
            if current_node.parent is None or current_node.parent == self.NULLNode:
                print(f"---{current_node.key} heeft geen ouder!---")
            else:
                if current_node.isLeftChild():
                    if current_node.parent.left != current_node:
                        print(f"---Ouder van {current_node.key} is niet juist of ouder zijn kind is niet juist!---")
                else:
                    if current_node.parent.right != current_node:
                        print(f"---Ouder van {current_node.key} is niet juist of ouder zijn kind is niet juist!---")

        blackcountl = 0
        blackcountr = 0

        # Doorloop de linkerdeelboom van de node
        if current_node.left != self.NULLNode:
            blackcountl = self.check(current_node.left, False)

        # Doorloop de rechterdeelboom van de node
        if current_node.right != self.NULLNode:
            blackcountr = self.check(current_node.right, False)

        if blackcountl != blackcountr:
            print(f"---Aantal zwarte nodes kloppen niet bij {current_node.key}---")

        if not start:
            if current_node.color == "black":
                return 1 + blackcountl
            else:
                return blackcountl