def createTreeItem(key, val):
    return (key, val)


class Node:
    def __init__(self, item=(None, None)):
        self.key = item[0]
        self.value = item[1]


class BST:
    def __init__(self, item=None):
        """
        Een nieuwe lege BST wordt aangemaakt

        :return: Een lege BST

        :preconditie:
        None

        :postconditie:
        None
        """
        self.root = item
        self.leftsubtree = None
        self.rightsubtree = None

    def searchTreeInsert(self, item):
        """
        Een item wordt in de BST gevoegd
        :param item: De item die aan de BST wordt toegevoegd

        :return: De BST met het toegevoegde item

        :preconditie:
        None

        :postconditie:
        None
        """
        a = Node(item)
        if self.root is None:
            self.root = a
            return True
        elif self.root.key < a.key:
            if self.rightsubtree is None:
                self.rightsubtree = BST()
                self.rightsubtree.root = a
                return True
            elif self.rightsubtree.root is None:
                self.rightsubtree.root = a
            else:
                self.rightsubtree.searchTreeInsert(item)
        elif self.root.key > a.key:
            if self.leftsubtree is None:
                self.leftsubtree = BST()
                self.leftsubtree.root = a
                return True
            elif self.leftsubtree.root is None:
                self.leftsubtree.root = a
            else:
                self.leftsubtree.searchTreeInsert(item)

    def isEmpty(self):
        """
        Hier wordt gekeken of een BST leeg is
        :return: True als de boom leeg is en False als deze niet leeg is

        :preconditie:
        None

        :postconditie:
        None
        """
        if self.root is None:
            return True
        return False

    def inorderTraverse(self, FunctieType):
        """
        Een BST wordt inorder doorlopen
        :param L: Een lijst die als volgorde de inorder van de boom heeft
        :return: De inorder van de boom

        :preconditie:
        None

        :postconditie:
        None
        """
        if self.leftsubtree:
            self.leftsubtree.inorderTraverse(FunctieType)
        FunctieType(self.root.key)
        if self.rightsubtree:
            self.rightsubtree.inorderTraverse(FunctieType)

    def InorderSuccessor(self):
        if self.leftsubtree:
            self.leftsubtree.inorderTraverse()
        else:
            return self.root

    def searchTreeDelete(self, key):
        if key == self.root.key:
            if self.rightsubtree is None and self.leftsubtree is None:
                self.root = None
                return True
            elif self.rightsubtree is None and self.leftsubtree:
                self.root = self.leftsubtree.root
                self.root.key = self.leftsubtree.root.key
                return self.leftsubtree.searchTreeDelete()
            elif self.rightsubtree and self.leftsubtree is None:
                self.root = self.rightsubtree.root
                self.root.key = self.rightsubtree.root.key
                return self.rightsubtree.searchTreeDelete()
            elif self.leftsubtree and self.rightsubtree:
                a = self.rightsubtree.InorderSuccessor()
                self.root.key = a.key
                self.root.value = a.value
                a.key = key
                return self.rightsubtree.searchTreeDelete(key)
            else:
                return False
        else:
            if key > self.root.key:
                if self.rightsubtree:
                    return self.rightsubtree.searchTreeDelete(key)
                else:
                    return False
            elif key < self.root.key:
                if self.leftsubtree:
                    return self.leftsubtree.searchTreeDelete(key)
                else:
                    return False

    def preorderTraverse(self, FunctieType):
        FunctieType(self.root.key)
        if self.leftsubtree:
            self.leftsubtree.preorderTraverse(FunctieType)
        if self.rightsubtree:
            self.rightsubtree.preorderTraverse(FunctieType)

    def searchTreeRetrieve(self, key):
        if self.isEmpty is True:
            return (False)
        elif key == self.root.key:
            return (self.root.value, True)
        elif key < self.root.key:
            return self.leftsubtree.searchTreeRetrieve(key)

        else:
            return self.rightsubtree.searchTreeRetrieve(key)

    def save(self):
        a = {}
        a['root'] = self.root.key
        if self.leftsubtree is None and self.rightsubtree is None:
            return {"root": self.root.key}
        if self.leftsubtree is not None:
            if self.leftsubtree.root is not None:
                a['children'] = []
                a['children'].append(self.leftsubtree.save())
            else:
                a["children"].append(None)
        else:
            a["children"].append(None)
        if self.rightsubtree is not None:
            if self.rightsubtree.root is not None:
                if "children" in a:
                    a['children'].append(self.rightsubtree.save())
                else:
                    a['children'] = []
                    a['children'].append(self.rightsubtree.save())
            else:
                a["children"].append(None)
        else:
            a["children"].append(None)
        return a

    def clear(self):
        self.root = None
        self.leftsubtree = None
        self.rightsubtree = None

    def load(self, dict, Start=True):
        if Start == True:
            self.clear()
        if "root" in dict:
            self.root = Node()
            self.root.key = dict["root"]
            self.root.value = dict["root"]
            Start = False
        if "children" in dict:
            for i in dict["children"]:
                if i is None:
                    continue
                else:
                    if i["root"] < self.root.key:
                        if self.leftsubtree is None:
                            self.leftsubtree = BST()
                            self.leftsubtree.root = Node()
                        self.leftsubtree.load(i)
                    else:
                        if self.rightsubtree is None:
                            self.rightsubtree = BST()
                            self.rightsubtree.root = Node()
                        self.rightsubtree.load(i)


t = BST()
print(t.isEmpty())
print(t.searchTreeInsert(createTreeItem(8, 8)))
print(t.searchTreeInsert(createTreeItem(5, 5)))
print(t.isEmpty())
print(t.searchTreeRetrieve(5)[0])
print(t.searchTreeRetrieve(5)[1])
t.inorderTraverse(print)
print(t.save())
t.load({'root': 10, 'children': [{'root': 5}, None]})
t.searchTreeInsert(createTreeItem(15, 15))
print(t.searchTreeDelete(0))
print(t.save())
print(t.searchTreeDelete(10))
print(t.save())
