class BST:
    def __init__(self):
        self.root = None

    def destroySearchTree(self):
        """
        functie die de boom zal verwijderen
        :parameter
        :return succes(bool)
        """
        self.root = None
        return True

    def isEmpty(self):
        """
        functie die true zal geven als de boom leeg is
        :parameter
        :return succes(bool)
        """
        if self.root == None:
            return True
        return self.root.leftchild == None and self.root.rightchild == None

    def searchTreeInsert(self, newItem, xnode=None):
        """
        functie voor het toevoegen van een kind
        :parameter value: een value het die toegevoegd moet worden
        :return (bool):
            True: het kind is toegevoegd
            False: er is iets fout gegaan
        """
        if xnode == None:
            if (self.root == None):
                self.root = node(newItem, None, None)
                return True
            xnode = self.root

        if xnode.value > newItem:
            if (xnode.leftchild == None):
                xnode.leftchild = node(newItem, None, None)
                return True
            else:
                return self.searchTreeInsert(newItem, xnode.leftchild)
        else:
            if (xnode.rightchild == None):
                xnode.rightchild = node(newItem, None, None)
                return True
            else:
                return self.searchTreeInsert(newItem, xnode.rightchild)

    def preorderTraverse(self, value, xnode):
        """
       functie voor een preorder traverse te krijgen
       :parameter value(string): de value van de knoop
       :return (int): de innorder successor
       """

    def inorderTraverse(self, value, xnode=None):
        """
       functie voor een inorder Traverse te krijgen
       :parameter value(string): de value van de knoop
       :return (int): de innorder successor
       """
        if(value == print):
            for knoop in self.get_list_as_iot():
                print(knoop)
            return
        if xnode == None:
            xnode = self.root

        if xnode.value == value:
            if xnode.rightchild == None:
                return xnode.leftchild
            else:
                innorderSuccesor = self.most_left_leave(xnode.rightchild)
                if innorderSuccesor != None:
                    return innorderSuccesor
        elif xnode.value < value:
            self.inorderTraverse(value,xnode.rightchild)
        elif xnode.value > value:
            self.inorderTraverse(value,xnode.leftchild)

    def postorderTraverse(self, value, xnode):
        """
       functie voor een postorder traverse te krijgen
       :parameter value(string): de value van de knoop
       :return (int): de innorder successor
       """
        if xnode.value == value:
            if xnode.rightchild == None:
                return xnode.leftchild
            else:
                innorderSuccesor = self.most_left_leave(xnode.rightchild)
                if innorderSuccesor != None:
                    return innorderSuccesor
        elif xnode.value < value:
            self.postorderTraverse(value,xnode.rightchild)
        elif xnode.value > value:
            self.postorderTraverse(value,xnode.leftchild)

    def save(self, xnode=None):
        """
        functie voor een dict overzicht van de boom te krijgen
        :parameter
        :return (list): een overzicht van de boom
        """
        list = []
        if xnode == None:
            xnode = self.root

        if xnode.leftchild != None and xnode.rightchild != None:
            return {"root":xnode.value,"children":[self.save(xnode.leftchild),self.save(xnode.rightchild)]}
        elif xnode.rightchild != None:
            return {"root":xnode.value,"children":[None,self.save(xnode.rightchild)]}
        elif xnode.leftchild != None:
            return {"root":xnode.value,"children":[self.save(xnode.leftchild),None]}
        else:
            return {"root":xnode.value}

    def searchTreeDelete(self, value):
        """
        functie voor een node te verwijderen bij de value
        :parameter value(string)
        :return (bool): True als het gelukt is
        """
        if value not in self.get_list_as_iot():
            return False
        node = self.searchTreeRetrieve(value, None, True)
        newNode = self.inorderTraverse(value,self.root)
        parrant = self.get_parrent(newNode.value)
        if parrant[0]:
            parrant[1].rightchild = None
        else:
            parrant[1].leftchild = None

        node.value = newNode.value

        return True

    def searchTreeRetrieve(self, value, xnode = None, asNode = False):
        """
        functie voor de knoop te vinden van een bepaalde knoop
        :parameter value(string)
        :return (list): geeft het knoop object met als value de meegegeven value
        """
        if xnode == None:
            xnode = self.root

        if xnode.value == value:
            if asNode:
                return xnode
            return (xnode.value, True)
        if xnode.value > value:
            if(xnode.leftchild != None):
                return self.searchTreeRetrieve(value, xnode.leftchild, asNode)
            else:
                return (False,False)
        else:
            if (xnode.rightchild != None):
                return self.searchTreeRetrieve(value, xnode.rightchild, asNode)
            else:
                return (False,False)


    def child_count(self, xnode=None):
        """
        functie voor het aantal knopen in een boom te achterhalen
        :parameter
        :return (int): het aantal knopen in de boom
        """
        count = 1
        if xnode == None:
            xnode = self.root

        if xnode.rightchild != None:
            count += self.child_count(xnode.rightchild)
        if xnode.leftchild != None:
            count += self.child_count(xnode.leftchild)

        return count

    def get_list_as_iot(self, xnode = None):
        """
        functie voor een lijst overzicht van de boom te krijgen
        :parameter
        :return (list): geeft de inorder traversal van de boom als lijst
        """
        if xnode == None:
            xnode = self.root

        if xnode.leftchild == None and xnode.rightchild == None:
            return [xnode.value]
        elif xnode.leftchild == None and xnode.rightchild != None:
             return [xnode.value] + self.get_list_as_iot(xnode.rightchild)
        elif xnode.leftchild != None and xnode.rightchild == None:
            return self.get_list_as_iot(xnode.leftchild) + [xnode.value]
        else:
            return self.get_list_as_iot(xnode.leftchild) + [xnode.value]+ self.get_list_as_iot(xnode.rightchild)

    def most_left_leave(self,xnode):
        """
       functie voor het meest linkse blad terug te krijgen van de boom of deelboom
       :parameter xnode de boom
       :return (node): meest linkse blad
       """
        if xnode == None:
            return None
        if xnode.leftchild == None:
            return xnode
        else:
            return self.most_left_leave(xnode.leftchild)

    def get_parrent(self, value, xnode = None):
        """
        functie voor de ouder van een boom te krijgen
        :parameter value(string)
        :return (node): geeft de ouder terug
        """
        if xnode == None:
            xnode = self.root

        if xnode.rightchild.value == value:
            return (True,xnode)
        elif xnode.leftchild.value == value:
            return (False, xnode)
        elif xnode.value < value:
            return self.get_parrent(value,xnode.rightchild)
        elif xnode.value > value:
            return self.get_parrent(value,xnode.leftchild)

    def load(self, dict, delete = False):
        if(delete == False):
            self.destroySearchTree();

        self.searchTreeInsert(dict['root'])
        if('children' in dict):
            if dict['children'][0] != None:
                self.load(dict['children'][0], True)
            if dict['children'][1] != None:
                self.load(dict['children'][1], True)

class node:
    def __init__(self, value, leftchild, rightchild):
        self.leftchild = leftchild
        self.rightchild = leftchild
        self.value = value

def createTreeItem(key,val):
    return key;