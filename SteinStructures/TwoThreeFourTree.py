def createTreeItem(key,val):
    return TreeItem(key, val)

class TwoThreeFourTree:
    def __init__(self):
        xnode = node()
        xnode.root[0] = None
        self.root = xnode;

    def isEmpty(self):
        """
        functie die true zal geven als de boom leeg is
        :parameter
        :return succes(bool)
        """
        return self.root.root[0] == None

    def insertItem(self, value, xnode=None, parrant=None):
        """
        functie voor het toevoegen van een kind
        :parameter value: een value het die toegevoegd moet worden
        :return (bool):
            True: het kind is toegevoegd
            False: er is iets fout gegaan
        """
        if(xnode == None):
            xnode = self.root

        if xnode.root[2] != None and value.key > xnode.root[2].key and xnode.children[3] != None:
            self.insertItem(value, xnode.children[3], xnode)
            return
        elif xnode.children[2] != None and xnode.root[1] != None and ((xnode.root[2] == None and value.key > xnode.root[0].key) or (xnode.root[2] != None and (value.key > xnode.root[1].key and value.key < xnode.root[2].key))):
            self.insertItem(value, xnode.children[2], xnode)
            return
        elif xnode.children[1] != None and (xnode.root[0] != None) and ((xnode.root[1] == None and value.key > xnode.root[0].key) or (xnode.root[1] != None and (value.key > xnode.root[0].key and value.key < xnode.root[1].key))):
            self.insertItem(value, xnode.children[1], xnode)
            return
        elif xnode.root[0] != None and value.key < xnode.root[0].key and xnode.children[0] != None:
            self.insertItem(value, xnode.children[0], xnode)
            return

        if xnode.insert(value) != None:
            self.moveUpTo(xnode,value, parrant)

        return True

    def moveUpTo(self, xnode, value, parrant):
        if(parrant == None):
            nood1 = node()
            nood1.insert(xnode.root[0])
            nood1.children[0] = xnode.children[0]
            nood1.children[1] = xnode.children[1]
            xnode.children[0] = None
            xnode.children[1] = None
            xnode.children[0] = nood1
            nood1 = node()
            nood1.insert(xnode.root[2])
            nood1.children[0] = xnode.children[2]
            nood1.children[1] = xnode.children[3]
            xnode.children[2] = None
            xnode.children[3] = None
            xnode.children[1] = nood1
            xnode.root[0] = xnode.root[1]
            xnode.root[1] = None
            xnode.root[2] = None
            self.insertItem(value, xnode)
        elif(parrant.root.count(None) == 0):
            self.moveUpTo(parrant,xnode.root[1], None)
            self.insertItem(value)
        else:
            test1 = parrant.root[0].key
            test = xnode.root[1].key
            parrant.insert(xnode.root[1])
            xnode.insert(value)
            self.insertItem(value, xnode)
            parrant.children.remove(xnode)
            if test < test1:
                parrant.children = xnode.children + parrant.children
            else:
                parrant.children = parrant.children + xnode.children

            while(len(parrant.children) > 4):
                parrant.children.remove(None)

            print("normal move up")

    def print(self, action, xnode=None):
        list = {}
        if (xnode == None):
            xnode = self.root

        root = []
        for i in xnode.root:
            if (i != None):
                root.append(i.key)

        list["root"] = root

        children = []
        for i in xnode.children:
            if (i != None):
                children.append(self.print(action, i))

        if (len(children) != 0):
            list["children"] = children

        if(action == print):
            print(list)

        return list

    def retrieveItem(self, value,xnode = None, getNode=False):
        """
        functie voor de knoop te vinden van een bepaalde key waarde
        :parameter value(string)
        :return (list): geeft het knoop object met als value de meegegeven value
        """
        if (xnode == None):
            xnode = self.root

        for i in range(0,3):
            if(xnode.root[i] != None and xnode.root[i].key == value):
                if getNode:
                    return (xnode, i)
                return (xnode.root[i].val, True)

        if xnode.root[2] != None and value > xnode.root[2].key and xnode.children[3] != None:
            return self.retrieveItem(value, xnode.children[3], getNode)
        elif xnode.children[2] != None and xnode.root[1] != None and ((xnode.root[2] == None and value > xnode.root[0].key) or (xnode.root[2] != None and (value.key > xnode.root[1].key and value.key < xnode.root[2].key))):
            return self.retrieveItem(value, xnode.children[2], getNode)
        elif xnode.children[1] != None and (xnode.root[0] != None) and ((xnode.root[1] == None and value > xnode.root[0].key) or (xnode.root[1] != None and (value.key > xnode.root[0].key and value.key < xnode.root[1].key))):
            return self.retrieveItem(value, xnode.children[1], getNode)
        elif xnode.root[0] != None and value < xnode.root[0].key and xnode.children[0] != None:
            return self.retrieveItem(value, xnode.children[0], getNode)

        return (None, False)

    def inorderTraverse(self, action, xnode = None):
        """
       functie voor een inorder Traverse te krijgen
       :parameter value(string): de value van de knoop
       :return (int): de innorder successor
       """
        if xnode == None:
            xnode = self.root

        for i in xnode.root:
            if (i != None):
                if(xnode.children[0] != None):
                    self.inorderTraverse(print, xnode.children[0])
                print(i.val)
                if(xnode.children[1] != None):
                    self.inorderTraverse(print, xnode.children[1])

    def load(self, tree, xnode = None):
        """
       functie voor heet inladen van een dict in de 2-3-4 boom
       :parameter value(string): een dict
       :return: Geen
       """
        xnode = node()
        self.root = self.loadLoop(tree)

    def loadLoop(self, tree):
        teller = 0
        xnode = node()
        for i in tree["root"]:
            xnode.root[teller] = TreeItem(i,i)
            teller1 = 0
            if "children" in tree:
                for a in tree["children"]:
                    xnode.children[teller1] = self.loadLoop(a)
                    teller1 = teller1 + 1
            teller = teller + 1

        return xnode


    def save(self, xnode=None):
        """
        functie voor een dict overzicht van de boom te krijgen
        :parameter
        :return (list): een overzicht van de boom
        """
        return self.print(None)

    def deleteItem(self, value):
        """
        functie voor een node te verwijderen bij de value
        :parameter value(string)
        :return (bool): True als het gelukt is
        """
        xnode = self.retrieveItem(value, None, True)[0]
        if xnode == False:
            return False

        xnode.root[0] = xnode.children[1].root[0]
        xnode.children[1].root[0] = None
        return True

    def inorderSuccessor(self, value):
        xnode = self.retrieveItem(value, None, True)[0]
        rootindex = self.retrieveItem(value, None, True)[1]

        print(self.retrieveItem(value, None, True)[1])
        #2 knoop --> 3knoop
        if(xnode.root[1] == None):
            xnode.root[1] = xnode.root[0]
            xnode.root[0] = xnode.children[0].root[0]
            xnode.root[2] = xnode.children[1].root[0]




class node:
    """children [node, node, node, node]"""
    def __init__(self):
        #[node, node, node, node]
        self.children = [None, None, None, None]
        #[TreeItem,TreeItem,TreeItem]
        self.root = [None, None, None];

    def insert(self, value):
        if self.root[2] != None:
            return self.root[1]
        else:
            if(self.root[0] == None):
                self.root[0] = value
            elif value.key < self.root[0].key:
                self.root[2] = self.root[1]
                self.root[1] = self.root[0]
                self.root[0] = value
            elif self.root[1] == None:
                self.root[1] = value
            elif value.key > self.root[1].key:
                self.root[2] = value
            else:
                self.root[2] = self.root[1]
                self.root[1] = value
            return None;


class TreeItem:
    def __init__(self, key,val):
        self.key = key
        self.val = val

    def getKey(self):
        return self.key

    def getVal(self):
        return self.val