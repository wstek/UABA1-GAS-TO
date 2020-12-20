"""
ADT contract voor binaire zoekboom
"""

from graphviz import Graph

def createTreeItem(key,val=None):
    return key, val

class BSTNode:
    def __init__(self, key=None, value=None):
        """
        Creëer een knoop voor een binaire zoekboom.
        :param key: searchkey
        :param value: waarde
        """
        self.key = key
        self.value = value
        self.left = None
        self.right = None


class BST:
    def __init__(self, root=None, count=0):
        """
        Creëert een lege binaire zoekboom.
        """
        self.root = root
        self.count = count

    def load(self, BSTDict, node=None, start=True):
        """
        Laadt de binaire zoekboom uit een dictionary.
        :param BSTDict: dictionary
        :return: None
        """
        if start:
            # Als de dictionary leeg is
            if BSTDict is None or BSTDict == {}:
                return None
            self.clear()

            # Creëer een knoop voor de wortel
            self.root = BSTNode()
            node = self.root

        # Wijs de waarden aan de knoop toe
        if 'root' in BSTDict:
            node.key = BSTDict.get('root')
        if 'value' in BSTDict:
            node.value = BSTDict.get('value')

        # Voeg 1 toe aan het totaal aantal knopen
        self.count += 1

        # Kijk of de knoop kinderen heeft
        if 'children' in BSTDict:
            if BSTDict['children'][0] is not None:
                node.left = BSTNode()
                self.load(BSTDict['children'][0], node.left, False)

            if BSTDict['children'][1] is not None:
                node.right = BSTNode()
                self.load(BSTDict['children'][1], node.right, False)

    def save(self, addvalues=False, node=None, start=True):
        """
        Slaagt de binaire zoekboom op in een dictionary.
        :param addvalues: boolean die bepaalt of dat the waarden ook opgeslagen moeten worden
        :return: dictionary
        """
        if start:
            # Als de binaire zoekboom leeg is
            if self.root is None:
                return {}
            node = self.root
            self.save(addvalues, node, False)

        BSTDict = {}

        # Voeg de waarden van de knoop toe aan de dictionary
        if node.key is not None:
            BSTDict['root'] = node.key
        else:
            return
        if node.value is not None and addvalues:
            BSTDict['value'] = node.value


        # Als de knoop kinderen heeft
        if not (node.left is None and node.right is None):
            BSTDict['children'] = []
            for child in [node.left, node.right]:
                if child is not None:
                    BSTDict['children'].append(self.save(addvalues, child, False))
                else:
                    BSTDict['children'].append(None)

        return BSTDict

    def print(self, depth=0, node=None, start=True):
        """
        Print de binaire zoekboom op het scherm.
        :return: None
        """
        if start:
            if self.root is None:
                print(None)
                return
            node = self.root

        # Print de huidige knoop
        print('%s' % ((depth * '\t') + str(node.key) + ": " + str(node.value)))

        # Als de knoop geen kinderen heeft
        if node.left is None and node.right is None:
            return

        # Print het linkerkind
        if node.left is not None:
            self.print(depth + 1, node.left, False)
        else:
            print('%s' % (((depth + 1) * '\t') + "None"))

        # Print het rechterkind
        if node.right is not None:
            self.print(depth + 1, node.right, False)
        else:
            print('%s' % (((depth + 1) * '\t') + "None"))

    def isEmpty(self):
        """
        Bepaalt of de binaire zoekboom leeg is.
        :return: boolean
        """
        if self.root is None:
            return True
        else:
            return False

    def getHeight(self, current_node=None, start=True):
        """
        Geeft de hoogte van de binaire zoekboom.
        :return: integer
        """
        # Zet in het begin current_node gelijk aan die van de wortel
        if start:
            if self.root is None:
                return 0
            current_node = self.root

        # Geef 1 terug als de knoop geen kinderen heeft
        if current_node.left is None and current_node.right is None:
            return 1

        # Zoek de grootste hoogte bij de kinderen
        else:
            max_height = 0
            if current_node.left is not None:
                temp = self.getHeight(current_node.left, False)
                if temp > max_height:
                    max_height = temp

            if current_node.right is not None:
                temp = self.getHeight(current_node.right, False)
                if temp > max_height:
                    max_height = temp

            # Geef 1 + de hoogte van langste pad vanaf een kind van de huidige knoop
            return 1 + max_height

    def getNumberOfNodes(self):
        """
        Geeft het aantal knopen in de binaire zoekboom.
        :return: integer
        """
        return self.count

    def getRootData(self):
        """
        Geeft de waarde dat in de wortel van de binaire zoekboom zit.
        :return: waarde
        """
        return self.root.value

    def searchTreeInsert(self, t, key=None, newEntry=None, current_node=None, start=True):
        """
        Voegt een nieuwe item toe aan de binaire zoekboom.
        :param key: search key (int of string)
        :param newEntry: waarde
        :return: None
        """
        # Zet in het begin de current_node gelijk aan die van de root
        if start:
            key, newEntry = t[0], t[1]
            # Als de binaire boom leeg is add the item in de root
            if self.root is None:
                self.root = BSTNode(key, newEntry)
                return True
            else:
                self.searchTreeInsert(t, key, newEntry, self.root, False)
                return True
        else:
            # Linker kind
            if key < current_node.key:
                # Als de node zijn linker kind leeg is, wordt er een nieuwe node gemaakt
                if current_node.left is None:
                    current_node.left = BSTNode(key, newEntry)

                # Anders voeg toe bij dat kind
                else:
                    self.searchTreeInsert(t, key, newEntry, current_node.left, False)
            # Rechter kind
            else:
                # Als de node zijn rechter kind leeg is, wordt er een nieuwe node gemaakt
                if current_node.right is None:
                    current_node.right = BSTNode(key, newEntry)

                # Anders voeg toe bij dat kind
                else:
                    self.searchTreeInsert(t, key, newEntry, current_node.right, False)

            # Voeg 1 toe aan het totaal aantal knopen in de binaire zoekboom
            self.count += 1
            return True

    def inorderSuccessor(self, huidige_node, left=False):
        """
        Geeft de inorder successor van een node.
        :param huidige_node: huidige knoop
        :return: inorder successor van de node

        precondities:
            De node moet twee kinderen hebben
        """
        # Ga eerst 1 keer naar rechts
        if not left:
            if huidige_node.right is not None:
                return self.inorderSuccessor(huidige_node.right, True)
            else:
                return huidige_node
        # Blijf links gaan tot een blad
        else:
            if huidige_node.left is not None:
                return self.inorderSuccessor(huidige_node.left, True)
            else:
                return huidige_node

    def findParent(self, node, current_node=None, start=True):
        """
        Zoekt de ouder van een gegeven node
        :param node: node
        :return: ouder van node
        """
        # Zet in het begin de current_node gelijk aan die van de root
        if start:
            if self.root is None or node == self.root or node is None:
                return
            current_node = self.root

        # Als node een kind is van current_node
        if current_node.left == node or current_node.right == node:
            return current_node

        # Anders zoek bij de kinderen
        if current_node.left is not None:
            temp = self.findParent(node, current_node.left, False)
            if temp is not None:
                return temp
        if current_node.right is not None:
            temp = self.findParent(node, current_node.right, False)
            if temp is not None:
                return temp

    def replaceWithChild(self, node, child):
        """
        Vervangt een node met een kind. Het kind van de node wordt het kind van de ouder van de node.
        Deze functie wordt gebruikt bij searchTreeDelete.
        :param node: knoop
        :param child: kind van de knoop
        :return: None
        """
        parent = self.findParent(node)
        if parent.left == node:
            parent.left = child
        else:
            parent.right = child

    def searchTreeDelete(self, key, current_node=None, start=True, no_count=False):
        """
        Verwijdert het item met een gegeven zoeksleutel uit de binaire zoekboom.
        :param key: search key (int of string)
        :return: None
        """
        if start:
            if self.root is None:
                return False
            current_node = self.getNode(key)
            if current_node is None:
                return False

        # Als de knoop geen kinderen heeft
        if current_node.left is None and current_node.right is None:
            # Vervang de node met None
            self.replaceWithChild(current_node, None)

            # Neem 1 af van het totaal aantal knopen in de binaire zoekboom
            if not no_count:
                self.count -= 1
                return True

        # Als de knoop 1 kind heeft
        elif current_node.left is None or current_node.right is None:
            # Vervang de node met zijn kind
            if current_node.left is None:
                self.replaceWithChild(current_node, current_node.right)

                # Neem 1 af van het totaal aantal knopen in de binaire zoekboom
                if not no_count:
                    self.count -= 1
                    return True
            else:
                self.replaceWithChild(current_node, current_node.left)

                # Neem 1 af van het totaal aantal knopen in de binaire zoekboom
                if not no_count:
                    self.count -= 1
                    return True

        # Als de knoop 2 kinderen heeft
        else:
            # zoek de inorder successor van de te verwijderen knoop
            insu = self.inorderSuccessor(current_node)
            # Vervang de waarden van de knoop met die van de inorder successor
            current_node.key, current_node.value = insu.key, insu.value
            # Verwijder de inorder successor
            self.searchTreeDelete(insu.key, insu, False, True)

            # Neem 1 af van het totaal aantal knopen in de binaire zoekboom
            if not no_count:
                self.count -= 1
                return True

    def getNode(self, key, current_node=None, start=True):
        """
        Geeft de node terug die de search key bevat.
        :param key: search key (int of string)
        :return: waarde
        """
        # Zet in het begin current_node gelijk aan die van de root
        if start:
            if self.root is None:
                return
            current_node = self.root

        if current_node.key == key:
            return current_node

        # Zoek bij de kinderen
        else:
            # Als de key kleiner is dan de key van de huidige knoop
            if key < current_node.key and current_node.left is not None:
                temp = self.getNode(key, current_node.left, False)
                if temp is not None:
                    return temp

            # Als de key groter is dan de key van de huidige knoop
            if key > current_node.key and current_node.right is not None:
                temp = self.getNode(key, current_node.right, False)
                if temp is not None:
                    return temp

    def searchTreeRetrieve(self, key):
        """
        Geeft een specifieke waarde terug uit de binaire zoekboom mbv de zoeksleutel.
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
            if node.left is not None:
                temp = self.contains(data, node.left, False)
                if temp is not None:
                    return temp
            if node.right is not None:
                temp = self.contains(data, node.right, False)
                if temp is not None:
                    return temp

        # Als het niet gevonden is en we zitten in de eerste stap van recursie
        if start:
            return False

    def clear(self):
        """
        Wist de binaire zoekboom.
        :return: None
        """
        self.root = None

    def preorderTraverse(self, current_node=None, start=True):
        """
        Doorloopt de knopen in de binaire zoekboom in preorder volgorde.
        :return: None
        """
        # Zet in het begin current_node gelijk aan die van de wortel
        if start:
            if self.root is None:
                print(None)
                return
            current_node = self.root

        # Print de searchkey van de huidige knoop
        print(current_node.key)

        # Doorloop de linkerdeelboom van de knoop
        if current_node.left is not None:
            self.preorderTraverse(current_node.left, False)

        # Doorloop de rechterdeelboom van de knoop
        if current_node.right is not None:
            self.preorderTraverse(current_node.right, False)

    def inorderTraverse(self, current_node=None, start=True):
        """
        Doorloopt de knopen in de binaire zoekboom in inorder volgorde.
        :return: None
        """
        # Zet in het begin current_node gelijk aan die van de wortel
        if start:
            if self.root is None:
                print(None)
                return
            current_node = self.root

        # Doorloop de linkerdeelboom van de knoop
        if current_node.left is not None:
            self.inorderTraverse(current_node.left, False)

        # Print de searchkey van de huidige knoop
        print(current_node.key)

        # Doorloop de rechterdeelboom van de knoop
        if current_node.right is not None:
            self.inorderTraverse(current_node.right, False)

    def postorderTraverse(self, current_node=None, start=True):
        """
        Doorloopt de knopen in de binaire zoekboom in postorder volgorde.
        :return: None
        """
        # Zet in het begin current_node gelijk aan die van de wortel
        if start:
            if self.root is None:
                print(None)
                return
            current_node = self.root

        # Doorloop de linkerdeelboom van de knoop
        if current_node.left is not None:
            self.postorderTraverse(current_node.left, False)

        # Doorloop de rechterdeelboom van de knoop
        if current_node.right is not None:
            self.postorderTraverse(current_node.right, False)

        # Print de searchkey van de huidige knoop
        print(current_node.key)

    def traverse(self, current_node=None, start=True):
        """
        Doorloopt de knopen in de binaire zoekboom en geeft een lijst terug.
        :return:
        """
        # Zet in het begin de current_node gelijk aan die van de wortel
        if start:
            if self.root is None:
                return []
            current_node = self.root
        l = []

        # Doorloop de linkerdeelboom van de knoop
        if current_node.left is not None:
            l += self.traverse(current_node.left, False)

        # Print de searchkey van de huidige knoop
        l.append(current_node.key)

        # Doorloop de rechterdeelboom van de knoop
        if current_node.right is not None:
            l += self.traverse(current_node.right, False)

        return l

    def toDot(self, print_value=False, current_node=None, dot=None, start=True):
        """
        Maakt een afbeelding van de binaire boom
        :param print_value: True: print de waarden van de knopen False: print geen waarden
        :return: None
        """
        # Zet in het begin de current_node gelijk aan die van de root
        if start:
            if self.root is None:
                print("Dot: lege BST!")
                return
            current_node = self.root

            # Maak een dot object
            name = f"tree" # f"tree{self.id}"
            print(name)
            dot = Graph(comment=name, format='png', graph_attr={"splines": "false"})

        if not print_value:
            dot.node(str(current_node.key), str(current_node.key))
        else:
            dot.node(str(current_node.key), str(current_node.key) + "\n" + str(current_node.value))

        # Doorloop de linkerdeelboom van de node
        if current_node.left is not None:
            self.toDot(print_value, current_node.left, dot, False)
            dot.edge(str(current_node.key)+":sw", str(current_node.left.key))

        # Doorloop de rechterdeelboom van de node
        if current_node.right is not None:
            self.toDot(print_value, current_node.right, dot, False)
            dot.edge(str(current_node.key)+":se", str(current_node.right.key))

        if start:
            # Geef de binaire zoekboom weer
            dot.render(f'test-output/{name}.gv', view=True)


# Testing
if __name__ == "__main__":
    d = {'root': 14, 'value': "test", 'children': [
            {'root': 7, 'children': [
                {'root': 5},
                {'root': 9, 'value': "test2"}
            ]},
            {'root': 21, 'children': [
                {'root': 16, 'children': [
                    None,
                    {'root': 17}
                ]},
                {'root': 23}]}
        ]}

    boom = BST()
    boom.load(d)
    print(boom.traverse())

    # for i in range(25, 31):
    #     boom.searchTreeInsert(createTreeItem(i, "new"))

    boom.searchTreeDelete(27)
    boom.searchTreeInsert(createTreeItem(27))

    boom.clear()
    boom.toDot()

# # Inginious testing
# if __name__ == "__main__":
#     t = BST()
#     print(t.isEmpty())
#     print(t.searchTreeInsert(createTreeItem(8,8)))
#     print(t.searchTreeInsert(createTreeItem(5,5)))
#     print(t.isEmpty())
#     print(t.searchTreeRetrieve(5)[0])
#     print(t.searchTreeRetrieve(5)[1])
#     t.inorderTraverse(print)
#     print(t.save())
#     t.load({'root': 10,'children':[{'root':5},None]})
#     t.searchTreeInsert(createTreeItem(15,15))
#     print(t.searchTreeDelete(0))
#     print(t.save())
#     print(t.searchTreeDelete(10))
#     print(t.save())