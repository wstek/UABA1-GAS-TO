import copy


def createTreeItem(key, val):
    return Node(val, key)


class Node:
    def __init__(self, value, key):
        self.value = value
        self.key = key


class TwoThreeFourTree:
    def __init__(self):
        self.items = []
        self.leftsubtree = None
        self.rightsubtree = None
        self.middlesubtree = None
        self.rmiddlesubtree = None
        self.lmiddlesubtree = None
        self.parent = None

    def retrieveItem(self, key):
        "Deze methode retrieved een value van de node met de keywaarde key"
        if self.isEmpty():  # We kijken eerst of de tree leeg is, als dit het geval is returnen we false
            return (None, False)
        # We checken dan steeds de lengte van de huidige node
        if len(self.items) == 3:  # We kijken hier naar het geval van wanneer de lengte van de node 3 is
            # Als een van onze keywaardes van de node gelijk is aan de key, returnen we de value hiervan
            if key == self.items[0].key:
                return (self.items[0].value, True)
            elif key == self.items[1].key:
                return (self.items[1].value, True)
            elif key == self.items[2].key:
                return (self.items[2].value, True)
            # Als dit echter niet het geval zoeken we verder in de subtrees
            else:
                if self.leftsubtree:
                    if key < self.items[0].key:
                        return self.leftsubtree.retrieveItem(key)
                    if self.items[0].key < key < self.items[1].key:
                        return self.lmiddlesubtree.retrieveItem(key)
                    if self.items[1].key < key < self.items[2].key:
                        return self.rmiddlesubtree.retrieveItem(key)
                    else:
                        return self.rightsubtree.retrieveItem(key)
                else:
                    return (None, False)
        elif len(self.items) == 2:  # We kijken hier naar het geval van wanneer de lengte van de node 2 is
            # Als een van onze keywaardes van de node gelijk is aan de key, returnen we de value hiervan
            if key == self.items[0].key:
                return (self.items[0].value, True)
            elif key == self.items[1].key:
                return (self.items[1].value, True)
            # Als dit echter niet het geval zoeken we verder in de subtrees
            else:
                if self.leftsubtree:
                    if key < self.items[0].key:
                        return self.leftsubtree.retrieveItem(key)
                    if self.items[0].key < key < self.items[1].key:
                        return self.middlesubtree.retrieveItem(key)
                    else:
                        return self.rightsubtree.retrieveItem(key)
                else:
                    return (None, False)
        # We kijken hier naar het geval van wanneer de lengte van de node 2 is
        else:
            # Als onze keywaarde van de node gelijk is aan de key, returnen we de value hiervan
            if key == self.items[0].key:
                return (self.items[0].value, True)
            else:
                if self.leftsubtree:
                    if key < self.items[0].key:
                        return self.leftsubtree.retrieveItem(key)
                    else:
                        return self.rightsubtree.retrieveItem(key)
                else:
                    return (None, False)

    def split(self):
        "Deze functie split een overvolle knoop op"
        # We kijken eerst of de ouder van de node bestaat
        if self.parent:  # Dit is het geval voor wanneer de ouder van de node bestaat
            # We kijken naar de verschillende lengtes die de parent node kan hebben
            if len(self.parent.items) == 1:
                if self.parent.items[0].key < self.items[
                    1].key:  # We kijken hier naar het geval waar de huidige node de rightsubtree is van zijn parent
                    self.parent.items.append(
                        self.items[1])  # We voegen de 2de item van de huidige node toe aan de oudernode
                    self.parent.middlesubtree = TwoThreeFourTree()
                    self.parent.middlesubtree.items.append(self.items[
                                                               0])  # We maken hier een nieuwe subtree aan voor de parent en voegen daar de eerste item van de huidige node aan toe
                    self.items.pop(0)  # We verwijderen hier de eerste en 2de waarde uit de huidige node
                    self.items.pop(0)
                    # Hieronder voegen we nog wat waardes toe aan de middlesubtree van de parent
                    self.parent.middlesubtree.parent = self.parent
                    self.parent.middlesubtree.leftsubtree = self.leftsubtree
                    self.parent.middlesubtree.rightsubtree = self.lmiddlesubtree  # We stellen de leftsubtree van de middlesubtree van de parent gelijk aan de lmiddlesubtree van de huidige node
                    # Hieronder kijken we of de right en leftsubtree van onze middlesubtree van de parent bestaan en stellen de parents van beide gelijk aan de middlesubtree
                    if self.parent.middlesubtree.leftsubtree:
                        self.parent.middlesubtree.leftsubtree.parent = self.parent.middlesubtree
                    if self.parent.middlesubtree.rightsubtree:
                        self.parent.middlesubtree.rightsubtree.parent = self.parent.middlesubtree
                    # Omdat we onze huidige node omzetten naar een 2 knoop stellen we de leftsubtree gelijk aan de rmiddlesubtree en stellen de lm/rmiddlesubtree gelijk aan None
                    self.leftsubtree = self.rmiddlesubtree
                    self.rmiddlesubtree = None
                    self.lmiddlesubtree = None
                else:  # Dit is het geval voor het geval onze huidige node de leftsubtree is van de parent
                    self.parent.items.insert(0, self.items[
                        1])  # We voegen het 2de item van de huidige node toe aan het begin van de parent node
                    # We maken hier weer een middlesubtree aan in de parent en voegenh aan de middlesubtree het laatste element van de huidige node toe
                    self.parent.middlesubtree = TwoThreeFourTree()
                    self.parent.middlesubtree.items.append(self.items[2])
                    self.items.pop()
                    self.items.pop()
                    # Hieronder voegen we nog wat waardes toe aan de middlesubtree van de parent
                    self.parent.middlesubtree.parent = self.parent
                    self.parent.middlesubtree.rightsubtree = self.rightsubtree
                    self.parent.middlesubtree.leftsubtree = self.rmiddlesubtree  # We stellen de leftsubtree van de middlesubtree van de parent gelijk aan de rmiddlesubtree van de huidige node
                    if self.parent.middlesubtree.leftsubtree:
                        self.parent.middlesubtree.leftsubtree.parent = self.parent.middlesubtree
                    if self.parent.middlesubtree.rightsubtree:
                        self.parent.middlesubtree.rightsubtree.parent = self.parent.middlesubtree
                    self.rightsubtree = self.lmiddlesubtree
                    self.rmiddlesubtree = None
                    self.lmiddlesubtree = None
            elif len(self.parent.items) == 2:
                if self.parent.items[1].key < self.items[
                    1].key:  # We kijken hier naar het geval waar de huidige node de rightsubtree is van zijn parent
                    self.parent.items.append(
                        self.items[1])  # We voegen hier het 2de item van de huidige node toe aan de node van de parent
                    # Hier maken we een niewe rmiddlesubtree aan voor de parent en stellen de lmiddlesubtree van de parent gelijk aan zijn middlesubtree
                    self.parent.rmiddlesubtree = TwoThreeFourTree()
                    self.parent.rmiddlesubtree.parent = self.parent
                    self.parent.lmiddlesubtree = self.parent.middlesubtree
                    # Aan de rmiddlesubtree voegen we het eerste item van de huidige node toe
                    self.parent.rmiddlesubtree.items.append(self.items[0])
                    self.parent.middlesubtree = None
                    self.items.pop(0)
                    self.items.pop(0)
                    # De subtrees van de rmiddlesubtree van de parent zijn gelijk aan de leftsubtree en de lmiddlesubtree van de huidige node
                    self.parent.rmiddlesubtree.leftsubtree = self.leftsubtree
                    self.parent.rmiddlesubtree.rightsubtree = self.lmiddlesubtree
                    # Als de subtrees van de rmiddlesubtree niet None zijn, stellen wij hun parents gelijk aan de rmiddlesubtree
                    if self.parent.rmiddlesubtree.leftsubtree:
                        self.parent.rmiddlesubtree.leftsubtree.parent = self.parent.rmiddlesubtree
                    if self.parent.rmiddlesubtree.rightsubtree:
                        self.parent.rmiddlesubtree.rightsubtree.parent = self.parent.rmiddlesubtree
                    # We stellen de leftsubtree van de huidige node gelijk aan de rmiddlesubtree van de huidige node en stellen de 2 middelste subtrees gelijk aan None
                    self.leftsubtree = self.rmiddlesubtree
                    self.rmiddlesubtree = None
                    self.lmiddlesubtree = None
                elif self.parent.items[0].key < self.items[1].key < self.parent.items[
                    1].key:  # We kijken hier naar het geval waar de huidige node de middlesubtree is van zijn parent
                    self.parent.items.insert(1, self.items[
                        1])  # We voegen in onze parent de 2de item van de huidige node toe
                    # We maken hier een nieuwe rmiddlesubtree aan voor de parent en stellen zijn lmiddlesubtree gelijk aan de huidige node
                    self.parent.rmiddlesubtree = TwoThreeFourTree()
                    self.parent.rmiddlesubtree.parent = self.parent
                    self.parent.lmiddlesubtree = self
                    # Aan de rmiddlesubtree voegen we het laatste item van de huidige node aan toe
                    self.parent.rmiddlesubtree.items.append(self.items[2])
                    self.items.pop()
                    self.items.pop()
                    # We stellen de subtrees van de lm iddlesubtree en rmiddlesubtree gelijk aan die van de huidige node
                    self.parent.lmiddlesubtree.leftsubtree = self.leftsubtree
                    self.parent.lmiddlesubtree.rightsubtree = self.lmiddlesubtree
                    self.parent.rmiddlesubtree.leftsubtree = self.rmiddlesubtree
                    self.parent.rmiddlesubtree.rightsubtree = self.rightsubtree
                    # Vervolgens kijken we of deze subtrees niet None zijn, als dit het geval is stellen we hun parents gelijk aan of de lmiddlesubtree of de rmiddlesubtree
                    if self.parent.lmiddlesubtree.leftsubtree:
                        self.parent.lmiddlesubtree.leftsubtree.parent = self.parent.lmiddlesubtree
                    if self.parent.lmiddlesubtree.rightsubtree:
                        self.parent.lmiddlesubtree.rightsubtree.parent = self.parent.lmiddlesubtree
                    if self.parent.rmiddlesubtree.leftsubtree:
                        self.parent.rmiddlesubtree.leftsubtree.parent = self.parent.rmiddlesubtree
                    if self.parent.rmiddlesubtree.rightsubtree:
                        self.parent.rmiddlesubtree.rightsubtree.parent = self.parent.rmiddlesubtree
                    # Hier stellen we de middlesubtree van de parent gelijk aan None
                    self.parent.middlesubtree = None
                elif self.parent.items[0].key > self.items[
                    1].key:  # We kijken hier naar het geval waar de huidige node de leftsubtree is van zijn parent
                    # Hier gaan we op dezelfde manier te werk als bij de eerste if statement, alleen veranderen we onze rmiddlesubtree in een lmiddlesubtree
                    self.parent.items.insert(0, self.items[
                        1])  # We voegen aan de parent het middelste item van de huidige node aan toe
                    # Hier maken we voor de parent een nieuwe lmiddlesubtree aan en stellen zijn rmiddlesubtree gelijk aan de middlesubtree van de parent
                    self.parent.lmiddlesubtree = TwoThreeFourTree()
                    self.parent.lmiddlesubtree.parent = self.parent
                    self.parent.rmiddlesubtree = self.parent.middlesubtree
                    # Aan de lmiddlesubtree voegen we het laatste item van de huidige node toe
                    self.parent.lmiddlesubtree.items.append(self.items[2])
                    self.parent.middlesubtree = None
                    self.items.pop()
                    self.items.pop()
                    # We stellen de leftsubtree van de lmiddlesubtree gelijk aan de rmiddlesubtree van de huidige node en de rightsubtree gelijk aan de rightsubtree van de huidige node
                    self.parent.lmiddlesubtree.leftsubtree = self.rmiddlesubtree
                    self.parent.lmiddlesubtree.rightsubtree = self.rightsubtree
                    # We kijken hier of de subtrees van de lmiddlesubtree gelijk is aan None en zo niet stellen wij hun parent gelijk aan de lmiddlesubtree
                    if self.parent.lmiddlesubtree.leftsubtree:
                        self.parent.lmiddlesubtree.leftsubtree.parent = self.parent.lmiddlesubtree
                    if self.parent.lmiddlesubtree.rightsubtree:
                        self.parent.lmiddlesubtree.rightsubtree.parent = self.parent.lmiddlesubtree
                    # We stellen de rightsubtree van de huidige node gelijk aan de lmiddlesubtree van de huidige node en stellen de l/rmiddlesubtree van de huidige node gelijk aan None
                    self.rightsubtree = self.lmiddlesubtree
                    self.rmiddlesubtree = None
                    self.lmiddlesubtree = None
        # We kijken hier naar het geval dat de parent van de huidige node None is, dus bij de root van de 234 boom
        else:
            # We maken hier variables aan om de huidige subtrees op te slaan
            a = self.leftsubtree
            b = self.rightsubtree
            c = self.lmiddlesubtree
            d = self.rmiddlesubtree
            # We maken nieuwe subtrees aan voor de huidige node, om makkelijker te kunnen splitsen
            # We verwijderen de eerste en laatste item uit de huidige node en voegen deze toe aan de subtrees
            self.leftsubtree = TwoThreeFourTree()
            self.rightsubtree = TwoThreeFourTree()
            self.leftsubtree.items.append(self.items[0])
            self.rightsubtree.items.append(self.items[2])
            # We stellen de parent van de subtrees gelijk aan de huidige node
            self.leftsubtree.parent = self
            self.rightsubtree.parent = self
            self.items.pop()
            self.items.pop(0)
            # We gebruiken nu de variablen om de subtrees hun subtrees te geven
            self.leftsubtree.leftsubtree = a
            self.leftsubtree.rightsubtree = c
            self.rightsubtree.leftsubtree = d
            self.rightsubtree.rightsubtree = b
            # Als de subtrees van de subtrees van de huidige node niet None zijn, stellen wij hun parent gelijk aan een van de subtrees van de huidige node
            if self.leftsubtree.leftsubtree:
                self.leftsubtree.leftsubtree.parent = self.leftsubtree
            if self.leftsubtree.rightsubtree:
                self.leftsubtree.rightsubtree.parent = self.leftsubtree
            if self.rightsubtree.leftsubtree:
                self.rightsubtree.leftsubtree.parent = self.rightsubtree
            if self.rightsubtree.rightsubtree:
                self.rightsubtree.rightsubtree.parent = self.rightsubtree
            # Omdat onze huidige node een 2 knoop is, stellen we onze r/lmiddlesubtree gelijk aan None
            self.rmiddlesubtree = None
            self.lmiddlesubtree = None

    def isEmpty(self):
        "Dit is een methode dat kijkt of een gegeven 234 boom leeg is"
        # Als de 234 boom leeg is returned deze functie True, anders False
        if not self.items:
            return True
        return False

    def redistribute(self):
        "Dit is een functie dat 2 knopen omzet naar 3 of 4 knopen"
        # We kijken hier naar de verschillende lengtes die de parent kan hebben
        if len(self.parent.items) == 1:  # Dit is het geval voor als de lengte van onze parent gelijk is aan 1
            if self.parent.leftsubtree == self:  # We kijken hier naar het geval van als onze huidige node glijk is aan de leftsubtree van de parent
                # We kijken hier naar de verschillende lengtes die de rightsubtree kan hebben
                if len(self.parent.rightsubtree.items) == 2:
                    # Hier voegen we het eerste item van de parent toe aan de huidige knoop en voegen we ook het eerste item van de rightsubtree toe aan de parent
                    self.items.append(self.parent.items[0])
                    self.parent.items.pop(0)
                    self.parent.items.append(self.parent.rightsubtree.items[0])
                    self.parent.rightsubtree.items.pop(0)
                    # De middlesubtree van de huidige knoop stellen we gelijk aan de rightsubtree en de rightsubtree stellen we gelijk aan de leftsubtree van de rightsubtree van de parent
                    self.middlesubtree = self.rightsubtree
                    self.rightsubtree = self.parent.rightsubtree.leftsubtree
                    if self.rightsubtree:
                        self.rightsubtree.parent = self
                    # We stellen de leftsubtree van de rightsubtree van de parent gelijk aan zijn middlesubtree en de middlesubtree van de rightsubtree van de parent stellen we gelijk aan None
                    self.parent.rightsubtree.leftsubtree = self.parent.rightsubtree.middlesubtree
                    self.parent.rightsubtree.middlesubtree = None
                elif len(self.parent.rightsubtree.items) == 3:
                    # Hier voegen we het eerste item van de parent toe aan de huidige knoop en voegen we ook het eerste item van de rightsubtree toe aan de parent
                    self.items.append(self.parent.items[0])
                    self.parent.items.pop(0)
                    self.parent.items.append(self.parent.rightsubtree.items[0])
                    self.parent.rightsubtree.items.pop(0)
                    # De middlesubtree van de huidige knoop stellen we gelijk aan de rightsubtree en de rightsubtree stellen we gelijk aan de leftsubtree van de rightsubtree van de parent
                    self.middlesubtree = self.rightsubtree
                    self.rightsubtree = self.parent.rightsubtree.leftsubtree
                    if self.rightsubtree:
                        self.rightsubtree.parent = self
                    # We stellen de leftsubtree van de rightsubtree van de parent gelijk aan zijn lmiddlesubtree en de middlesubtree gelijk aan zijn rmiddlesubtree
                    self.parent.rightsubtree.leftsubtree = self.parent.rightsubtree.lmiddlesubtree
                    self.parent.rightsubtree.middlesubtree = self.parent.rightsubtree.rmiddlesubtree
                    # Vervolgens stellen ve de l/rmiddlesubtree van de rightsubtree van de paren gelijk aan None
                    self.parent.rightsubtree.lmiddlesubtree = None
                    self.parent.rightsubtree.rmiddlesubtree = None
                elif len(self.parent.rightsubtree.items) == 1:
                    self.items.append(self.parent.items[0])
                    self.items.append(self.parent.rightsubtree.items[0])
                    self.lmiddlesubtree = self.rightsubtree
                    self.rightsubtree = self.parent.rightsubtree.rightsubtree
                    self.rmiddlesubtree = self.parent.rightsubtree.leftsubtree
                    if self.rightsubtree:
                        self.rightsubtree.parent = self
                    if self.rmiddlesubtree:
                        self.rmiddlesubtree.parent = self
                    if self.rightsubtree:
                        self.rightsubtree.parent = self
                    if self.rmiddlesubtree:
                        self.rmiddlesubtree.parent = self
                    self.parent.rightsubtree = None
                    if self.parent.parent:
                        a = self.parent.parent
                        if self.parent.parent.leftsubtree == self.parent:
                            self.parent = a
                            self.parent.leftsubtree = self
                        elif self.parent.parent.lmiddlesubtree == self.parent:
                            self.parent = a
                            self.parent.lmiddlesubtree = self
                        elif self.parent.parent.rmiddlesubtree == self.parent:
                            self.parent = a
                            self.parent.middlesubtree = self
                        elif self.parent.parent.rmiddlesubtree == self.parent:
                            self.parent = a
                            self.parent.rmiddlesubtree = self
                        elif self.parent.parent.rightsubtree == self.parent:
                            self.parent = a
                            self.parent.rightsubtree = self
                    else:
                        self.parent = None
            elif self.parent.rightsubtree == self:  # We kijken hier naar het geval van als onze huidige node glijk is aan de rightsubtree van de parent
                # We kijken hier naar de verschillende lengtes die de sibling van de huidige node kan hebben
                if len(self.parent.leftsubtree.items) == 2:
                    # Hier voegen we het eerste item van de parent toe aan de huidige knoop en voegen we ook het eerste item van de leftsubtree toe aan de parent
                    self.items.insert(0, self.parent.items[0])
                    self.parent.items.pop(0)
                    self.parent.items.append(self.parent.leftsubtree.items[-1])
                    self.parent.leftsubtree.items.pop()
                    # De middlesubtree van de huidige node is gelijk aan zijn leftsubtree en zijn leftsubtree is gelijk aan de rightsubtree van zijn sibling
                    self.middlesubtree = self.leftsubtree
                    self.leftsubtree = self.parent.leftsubtree.rightsubtree
                    # Als de leftsubtree van de huidige node niet None is stellen we zijn parent gelijk aan de huidige node
                    if self.leftsubtree:
                        self.leftsubtree.parent = self
                    # De rightsubtree van de sibling wordt gelijk gesteld aan zijn middlesubtree en zijn middlesubtree wordt gelijkgesteld aan None
                    self.parent.leftsubtree.rightsubtree = self.parent.leftsubtree.middlesubtree
                    self.parent.leftsubtree.middlesubtree = None
                elif len(self.parent.leftsubtree.items) == 3:
                    # Hier voegen we het eerste item van de parent toe aan de huidige knoop en voegen we ook het eerste item van de leftsubtree toe aan de parent
                    self.items.insert(0, self.parent.items[0])
                    self.parent.items.pop(0)
                    self.parent.items.append(self.parent.leftsubtree.items[-1])
                    self.parent.leftsubtree.items.pop()
                    # De middlesubtree van de huidige node is gelijk aan zijn leftsubtree en zijn leftsubtree is gelijk aan de rightsubtree van zijn sibling
                    self.middlesubtree = self.leftsubtree
                    self.leftsubtree = self.parent.leftsubtree.rightsubtree
                    # Als de leftsubtree van de huidige node niet None is stellen we zijn parent gelijk aan de huidige node
                    if self.leftsubtree:
                        self.leftsubtree.parent = self
                    # De rightsubtree van de sibling is gelijk aan zijn rmiddlesubtree en de leftsubtree van de sibling is gelijk aan zijn lmiddlesubtree
                    # De l/rmiddlesubtree van de sibling worden gelijkgesteld aan None
                    self.parent.leftsubtree.rightsubtree = self.parent.leftsubtree.rmiddlesubtree
                    self.parent.leftsubtree.middlesubtree = self.parent.leftsubtree.lmiddlesubtree
                    self.parent.leftsubtree.rmiddlesubtree = None
                    self.parent.leftsubtree.lmiddlesubtree = None
                elif len(self.parent.leftsubtree.items) == 1:
                    self.items.insert(0, self.parent.items[-1])
                    self.items.insert(0, self.parent.leftsubtree.items[-1])
                    self.rmiddlesubtree = self.leftsubtree
                    self.lmiddlesubtree = self.parent.leftsubtree.rightsubtree
                    self.leftsubtree = self.parent.leftsubtree.leftsubtree
                    if self.lmiddlesubtree:
                        self.lmiddlesubtree.parent = self
                    if self.leftsubtree:
                        self.leftsubtree.parent = self
                    self.parent.leftsubtree = None
                    if self.parent.parent:
                        a = self.parent.parent
                        if self.parent.parent.leftsubtree == self.parent:
                            self.parent = a
                            self.parent.leftsubtree = self
                        elif self.parent.parent.lmiddlesubtree == self.parent:
                            self.parent = a
                            self.parent.lmiddlesubtree = self
                        elif self.parent.parent.rmiddlesubtree == self.parent:
                            self.parent = a
                            self.parent.middlesubtree = self
                        elif self.parent.parent.rmiddlesubtree == self.parent:
                            self.parent = a
                            self.parent.rmiddlesubtree = self
                        elif self.parent.parent.rightsubtree == self.parent:
                            self.parent = a
                            self.parent.rightsubtree = self
                    else:
                        self.parent = None
        elif len(self.parent.items) == 2:  # Bij dit geval is de lengte van de parent gelijk aan 2
            if self.parent.leftsubtree == self:  # We kijken hier naar het geval van als onze huidige node glijk is aan de leftsubtree van de parent
                # We kijken hier naar de verschillende lengtes die de sibling van de huidige node kan hebben
                if len(self.parent.middlesubtree.items) == 1:
                    # We voegen aan de huidige node de eerste waarde van de parent en de 1ste waarde van de sibling toe
                    self.items.append(self.parent.items[0])
                    self.items.append(self.parent.middlesubtree.items[0])
                    # We stellen de lmiddlesubtree van de huidige node gelijk aan zijn rightsubtree, zijn rmiddlesubtree aan de leftsubtree van zijn sibling en zijn rightsubtree aan de rightsubtree van zijn sibling
                    self.lmiddlesubtree = self.rightsubtree
                    self.rmiddlesubtree = self.parent.middlesubtree.leftsubtree
                    self.rightsubtree = self.parent.middlesubtree.rightsubtree
                    # We kijken of de subtrees None zijn of niet en op basis daarvan stellen we hun parent gelijk aan de huidige node
                    if self.rmiddlesubtree:
                        self.rmiddlesubtree.parent = self
                    if self.rightsubtree:
                        self.rightsubtree.parent = self
                    # We stellen de middlesubtree van de parent gelijk aan None en verwijderen het eerste item uit de parent
                    self.parent.middlesubtree = None
                    self.parent.items.pop(0)
                elif len(self.parent.middlesubtree.items) == 2:
                    # We voegen hier de eerste item van de parent toe aan de huidige node en voegen ook de eerste item van de sibling toe aan de parent
                    self.items.append(self.parent.items[0])
                    self.parent.items.pop(0)
                    self.parent.items.insert(0, self.parent.middlesubtree.items[0])
                    self.parent.middlesubtree.items.pop(0)
                    # We stellen de middlesubtree van de huidige node gelijk aan zijn rightsubtree en zijn rightsubtree gelijk aan de leftsubtree van zijn sibling
                    self.middlesubtree = self.rightsubtree
                    self.rightsubtree = self.parent.middlesubtree.leftsubtree
                    if self.rightsubtree:
                        self.rightsubtree.parent = self
                    # We stellen de leftsubtree van de sibling gelijk aan zijn middlesubtree en stellen zijn middlesubtree gelijk aan None
                    self.parent.middlesubtree.leftsubtree = self.parent.middlesubtree.middlesubtree
                    self.parent.middlesubtree.middlesubtree = None
                elif len(self.parent.middlesubtree.items) == 3:
                    # We voegen hier de eerste item van de parent toe aan de huidige node en voegen ook de eerste item van de sibling toe aan de parent
                    self.items.append(self.parent.items[0])
                    self.parent.items.pop(0)
                    self.parent.items.insert(0, self.parent.middlesubtree.items[0])
                    self.parent.middlesubtree.items.pop(0)
                    # We stellen de middlesubtree van de huidige node gelijk aan zijn rightsubtree en zijn rightsubtree gelijk aan de leftsubtree van zijn sibling
                    self.middlesubtree = self.rightsubtree
                    self.rightsubtree = self.parent.middlesubtree.leftsubtree
                    if self.rightsubtree:
                        self.rightsubtree.parent = self
                    # We stellen de leftsubtree van de sibling gelijk aan zijn lmiddlesubtree en zijn middlesubtree gelijk aan zijn rmiddlesubtree
                    # We stellen de l/rmiddlesubtree van de sibling gelijk aan None
                    self.parent.middlesubtree.leftsubtree = self.parent.middlesubtree.lmiddlesubtree
                    self.parent.middlesubtree.middlesubtree = self.parent.middlesubtree.rmiddlesubtree
                    self.parent.middlesubtree.rmiddlesubtree = None
                    self.parent.middlesubtree.lmiddlesubtree = None
            elif self.parent.middlesubtree == self:  # We kijken hier naar het geval van als onze huidige node gelijk is aan de middlesubtree van de parent
                # We kijken hier naar de verschillende lengtes die de sibling van de huidige node kan hebben
                if len(self.parent.rightsubtree.items) == 1:
                    # We voegen het 2de item van de parent en het eerste item van de sibling toe aan de huidige node
                    self.items.append(self.parent.items[1])
                    self.items.append(self.parent.rightsubtree.items[0])
                    # We stellen de lmiddlesubtree van de huidige node gelijk aan zijn rightsubtree, zijn rmiddlesubtree gelijk aan de leftsubtree van zijn sibling en zijn rightsubtree gelijk aan de sibling zijn rightsubtree
                    self.lmiddlesubtree = self.rightsubtree
                    self.rmiddlesubtree = self.parent.rightsubtree.leftsubtree
                    self.rightsubtree = self.parent.rightsubtree.rightsubtree
                    if self.rmiddlesubtree:
                        self.rmiddlesubtree.parent = self
                    if self.rightsubtree:
                        self.rightsubtree.parent = self
                    # De rightsubtree van de parent stellen we gelijk aan de huidige node en zijn middlesubtree stellen we gelijk aan None
                    self.parent.rightsubtree = self
                    self.parent.items.pop()
                    self.parent.middlesubtree = None
                elif len(self.parent.rightsubtree.items) == 2:
                    # We voegen de laatste item van de parent toe aan de huidige node en voegen het eerste item van de sibling toe aan de parent
                    self.items.append(self.parent.items[-1])
                    self.parent.items.pop()
                    self.parent.items.append(self.parent.rightsubtree.items[0])
                    self.parent.rightsubtree.items.pop(0)
                    # We stellen de middlesubtree van de huidige node gelijk aan zijn rightsubtree en zijn rightsubtree gelijk aan de leftsubtree van zijn sibling
                    self.middlesubtree = self.rightsubtree
                    self.rightsubtree = self.parent.rightsubtree.leftsubtree
                    if self.rightsubtree:
                        self.rightsubtree.parent = self
                    # We stellen de leftsubtree van de sibling gelijk aan zijn middlesubtree en zijn middlesubtree stellen we gelijk aan None
                    self.parent.rightsubtree.leftsubtree = self.parent.rightsubtree.middlesubtree
                    self.parent.rightsubtree.middlesubtree = None
                elif len(self.parent.rightsubtree.items) == 3:
                    # We voegen de laatste item van de parent toe aan de huidige node en voegen het eerste item van de sibling toe aan de parent
                    self.items.append(self.parent.items[-1])
                    self.parent.items.pop()
                    self.parent.items.append(self.parent.rightsubtree.items[0])
                    self.parent.rightsubtree.items.pop(0)
                    # We stellen de middlesubtree van de huidige node gelijk aan zijn rightsubtree en zijn rightsubtree gelijk aan de leftsubtree van zijn sibling
                    self.middlesubtree = self.rightsubtree
                    self.rightsubtree = self.parent.rightsubtree.leftsubtree
                    if self.rightsubtree:
                        self.rightsubtree.parent = self
                    # We stellen de leftsubtree van de sibling gelijk aan zijn lmiddlesubtree en zijn middlesubtree stellen we gelijk aan zijn rmiddlesubtree
                    # We stellen de r/lmiddlesubtree van de sibling gelijk aan None
                    self.parent.rightsubtree.leftsubtree = self.parent.rightsubtree.lmiddlesubtree
                    self.parent.rightsubtree.middlesubtree = self.parent.rightsubtree.rmiddlesubtree
                    self.parent.rightsubtree.lmiddlesubtree = None
                    self.parent.rightsubtree.rmiddlesubtree = None
            elif self.parent.rightsubtree == self:  # We kijken hier naar het geval van als onze huidige node glijk is aan de rightsubtree van de parent
                # We kijken hier naar de verschillende lengtes die de sibling van de huidige node kan hebben
                if len(self.parent.middlesubtree.items) == 1:
                    # We voegen het laatste item van de parent en het eerste item van de sibling toe aan de huidige node
                    self.items.insert(0, self.parent.items[-1])
                    self.items.insert(0, self.parent.middlesubtree.items[0])
                    # We stellen de rmiddlesubtree van de huidige node gelijk aan zijn leftsubtree, zijn lmiddlesubtree aan de rightsubtree van de sibling en zijn leftsubtree aan de leftsubtree van de sibling
                    self.rmiddlesubtree = self.leftsubtree
                    self.lmiddlesubtree = self.parent.middlesubtree.rightsubtree
                    self.leftsubtree = self.parent.middlesubtree.leftsubtree
                    if self.lmiddlesubtree:
                        self.lmiddlesubtree.parent = self
                    if self.leftsubtree:
                        self.leftsubtree.parent = self
                    # De middlesubtree van de parent stellen we gelijk aan None
                    self.parent.middlesubtree = None
                    self.parent.items.pop()
                elif len(self.parent.middlesubtree.items) == 2:
                    # We voegen aan de huidige node het laatste item van de parent toe en voegen aan de parent het laatste item van de sibling toe
                    self.items.insert(0, self.parent.items[-1])
                    self.parent.items.pop()
                    self.parent.items.append(self.parent.middlesubtree.items[-1])
                    self.parent.middlesubtree.items.pop()
                    # We stellen de middlesubtree van de huidige node gelijk aan zijn leftsubtree en stellen zijn  leftsubtree gelijk aan de rightsubtree van de sibling
                    self.middlesubtree = self.leftsubtree
                    self.leftsubtree = self.parent.middlesubtree.rightsubtree
                    if self.leftsubtree:
                        self.leftsubtree.parent = self
                    # We stellen de rightsubtree van de parent gelijk aan zijn middlesubtree en stellen zijn middlesubtree gelijk aan None
                    self.parent.middlesubtree.rightsubtree = self.parent.middlesubtree.middlesubtree
                    self.parent.middlesubtree.middlesubtree = None
                elif len(self.parent.middlesubtree.items) == 3:
                    # We voegen aan de huidige node het laatste item van de parent toe en voegen aan de parent het laatste item van de sibling toe
                    self.items.insert(0, self.parent.items[-1])
                    self.parent.items.pop()
                    self.parent.items.append(self.parent.middlesubtree.items[-1])
                    self.parent.middlesubtree.items.pop()
                    # We stellen de middlesubtree van de huidige node gelijk aan zijn leftsubtree en stellen zijn  leftsubtree gelijk aan de rightsubtree van de sibling
                    self.middlesubtree = self.leftsubtree
                    self.leftsubtree = self.parent.middlesubtree.rightsubtree
                    if self.leftsubtree:
                        self.leftsubtree.parent = self
                    # We stellen de rightsubtree van de sibling gelijk aan zijn rmiddlesubtree en zijn middlesubtree stellen we gelijk aan zijn lmiddlesubtree
                    # Zijn r/lmiddlesubtree stellen we gelijk aan None
                    self.parent.middlesubtree.rightsubtree = self.parent.middlesubtree.rmiddlesubtree
                    self.parent.middlesubtree.middlesubtree = self.parent.middlesubtree.lmiddlesubtree
                    self.parent.middlesubtree.rmiddlesubtree = None
                    self.parent.middlesubtree.lmiddlesubtree = None
        elif len(self.parent.items) == 3:
            if self.parent.leftsubtree == self:  # We kijken hier naar het geval van als onze huidige node glijk is aan de leftsubtree van de parent
                # We kijken hier naar de verschillende lengtes die de sibling van de huidige node kan hebben
                if len(self.parent.lmiddlesubtree.items) == 1:
                    # We voegen het eerste item van de parent en van de sibling toe aan de huidige node
                    self.items.append(self.parent.items[0])
                    self.items.append(self.parent.lmiddlesubtree.items[0])
                    self.parent.items.pop(0)
                    self.parent.lmiddlesubtree.items.pop(0)
                    # We stellen de lmiddlesubtree van de huidige node gelijk aan zijn rightsubtree, zijn rmiddlesubtree gelijk aan de leftsubtree van zijn sibling en zijn rightsubtree gelijk aan de rightsubtree van zijn sibling
                    self.lmiddlesubtree = self.rightsubtree
                    self.rmiddlesubtree = self.parent.lmiddlesubtree.leftsubtree
                    self.rightsubtree = self.parent.lmiddlesubtree.rightsubtree
                    if self.rmiddlesubtree:
                        self.rmiddlesubtree.parent = self
                    if self.rightsubtree:
                        self.rightsubtree.parent = self
                    # De lmiddlesubtree van de parent stellen we gelijk aan None
                    self.parent.lmiddlesubtree = None
                    # We stellen de middlesubtree van de parent gelijk aan de rmiddlesubtree en stellen de rmiddlesubtree gelijk aan None
                    self.parent.middlesubtree = self.parent.rmiddlesubtree
                    self.parent.rmiddlesubtree = None
                elif len(self.parent.lmiddlesubtree.items) == 2:
                    # We voegen het eerste item van de parent toe aan de huidige node en voegen het eerste item van de sibling toe aan de parent
                    self.items.append(self.parent.items[0])
                    self.parent.items.pop(0)
                    self.parent.items.insert(0, self.parent.lmiddlesubtree.items[0])
                    self.parent.lmiddlesubtree.items.pop(0)
                    # De middlesubtree van de huidige node stellen we gelijk aan zijn rightsubtree en zijn rightsubtree stellen we gelijk aan de leftsubtree van zijn sibling
                    self.middlesubtree = self.rightsubtree
                    self.rightsubtree = self.parent.lmiddlesubtree.leftsubtree
                    if self.rightsubtree:
                        self.rightsubtree.parent = self
                    # We stellen de leftsubtree van de sibling gelijk aan zijn middlesubtree en stellen zijn middlesubtree gelijk aan None
                    self.parent.lmiddlesubtree.leftsubtree = self.parent.lmiddlesubtree.middlesubtree
                    self.parent.lmiddlesubtree.middlesubtree = None
                elif len(self.parent.lmiddlesubtree.items) == 3:
                    # We voegen het eerste item van de parent toe aan de huidige node en voegen het eerste item van de sibling toe aan de parent
                    self.items.append(self.parent.items[0])
                    self.parent.items.pop(0)
                    self.parent.items.insert(0, self.parent.lmiddlesubtree.items[0])
                    self.parent.lmiddlesubtree.items.pop(0)
                    # De middlesubtree van de huidige node stellen we gelijk aan zijn rightsubtree en zijn rightsubtree stellen we gelijk aan de leftsubtree van zijn sibling
                    self.middlesubtree = self.rightsubtree
                    self.rightsubtree = self.parent.lmiddlesubtree.leftsubtree
                    if self.rightsubtree:
                        self.rightsubtree.parent = self
                    # We stellen de leftsubtree van de sibling gelijk aan zijn lmiddlesubtree en zijn middlesubtree gelijk aan zijn rmiddlesubtree
                    # We stellen zijn r/lmiddlesubtree gelijk aan None
                    self.parent.lmiddlesubtree.leftsubtree = self.parent.lmiddlesubtree.lmiddlesubtree
                    self.parent.lmiddlesubtree.middlesubtree = self.parent.lmiddlesubtree.rmiddlesubtree
                    self.parent.lmiddlesubtree.rmiddlesubtree = None
                    self.parent.lmiddlesubtree.lmiddlesubtree = None
            elif self.parent.lmiddlesubtree == self:  # We kijken hier naar het geval van als onze huidige node glijk is aan de lmiddlesubtree van de parent
                # We kijken hier naar de verschillende lengtes die de sibling van de huidige node kan hebben
                if len(self.parent.rmiddlesubtree.items) == 1:
                    # We voegen het 2de item van de parent en het eerste item van de sibling toe aan de huidige node
                    self.items.append(self.parent.items[1])
                    self.items.append(self.parent.rmiddlesubtree.items[0])
                    self.parent.items.pop(1)
                    self.parent.rmiddlesubtree.items.pop(0)
                    # De lmiddlesubtree van de huidige node stellen we gelijk aan zijn rightsubtree, zijn rmiddlesubtree aan de leftsubtree van de sibling en zijn rightsubtree aan de rightsubtree van de sibling
                    self.lmiddlesubtree = self.rightsubtree
                    self.rmiddlesubtree = self.parent.rmiddlesubtree.leftsubtree
                    self.rightsubtree = self.parent.rmiddlesubtree.rightsubtree
                    if self.rmiddlesubtree:
                        self.rmiddlesubtree.parent = self
                    if self.rightsubtree:
                        self.rightsubtree.parent = self
                    # We stellen de rmiddlesubtree van de parent gelijk aan None
                    self.parent.rmiddlesubtree = None
                    # We stellen de middlesubtree gelijk aan de huidige node en stellen de lmiddlesubtree van de parent gelijk aan None
                    self.parent.middlesubtree = self
                    self.parent.lmiddlesubtree = None
                elif len(self.parent.rmiddlesubtree.items) == 2:
                    # We voegen het 2de item van de parent aan de huidige node toe en voegen het eerste item van de sibling aan de parent toe
                    self.items.append(self.parent.items[1])
                    self.parent.items.pop(1)
                    self.parent.items.insert(1, self.parent.rmiddlesubtree.items[0])
                    self.parent.rmiddlesubtree.items.pop(0)
                    # We stellen de middlesubtree van de huidige node gelijk aan zijn rightsubtree en zijn rightsubtree gelijk aan de leftsubtree van de sibling
                    self.middlesubtree = self.rightsubtree
                    self.rightsubtree = self.parent.rmiddlesubtree.leftsubtree
                    if self.rightsubtree:
                        self.rightsubtree.parent = self
                    # We stellen de leftsubtree van de sibling gelijk aan zijn middlesubtree en stellen zijn middlesubtree gelijk aan None
                    self.parent.rmiddlesubtree.leftsubtree = self.parent.rmiddlesubtree.middlesubtree
                    self.parent.rmiddlesubtree.middlesubtree = None
                elif len(self.parent.rmiddlesubtree.items) == 3:
                    # We voegen het 2de item van de parent aan de huidige node toe en voegen het eerste item van de sibling aan de parent toe
                    self.items.append(self.parent.items[1])
                    self.parent.items.pop(1)
                    self.parent.items.insert(1, self.parent.rmiddlesubtree.items[0])
                    self.parent.rmiddlesubtree.items.pop(0)
                    # We stellen de middlesubtree van de huidige node gelijk aan zijn rightsubtree en zijn rightsubtree gelijk aan de leftsubtree van de sibling
                    self.middlesubtree = self.rightsubtree
                    self.rightsubtree = self.parent.rmiddlesubtree.leftsubtree
                    if self.rightsubtree:
                        self.rightsubtree.parent = self
                    # We stellen de leftsubtree van de sibling gelijk aan zijn lmiddlesubtree en zijn middlesubtree gelijk aan zijn rmiddlesubtree
                    # We stellen zijn r/lmiddlesubtree gelijk aan None
                    self.parent.rmiddlesubtree.leftsubtree = self.parent.rmiddlesubtree.lmiddlesubtree
                    self.parent.rmiddlesubtree.middlesubtree = self.parent.rmiddlesubtree.rmiddlesubtree
                    self.parent.rmiddlesubtree.lmiddlesubtree = None
                    self.parent.rmiddlesubtree.rmiddlesubtree = None
            elif self.parent.rmiddlesubtree == self:  # We kijken hier naar het geval van als onze huidige node glijk is aan de rmiddlesubtree van de parent
                # We kijken hier naar de verschillende lengtes die de sibling van de huidige node kan hebben
                if len(self.parent.rightsubtree.items) == 1:
                    # We voegen aan de huidige node het laatste item van de parent en het eerste item van de sibling toe
                    self.items.append(self.parent.items[-1])
                    self.items.append(self.parent.rightsubtree.items[0])
                    self.parent.items.pop()
                    self.parent.rightsubtree.items.pop(0)
                    # We stellen de lmiddlesubtree van de huidige node gelijk aan zijn rightsubtree, zijn rmiddlesubtree gelijk aan de leftsubtree van zijn sibling en zijn rightsubtree gelijk aan de rightsubtree van de sibling
                    self.lmiddlesubtree = self.rightsubtree
                    self.rmiddlesubtree = self.parent.rightsubtree.leftsubtree
                    self.rightsubtree = self.parent.rightsubtree.rightsubtree
                    if self.rmiddlesubtree:
                        self.rmiddlesubtree.parent = self
                    if self.rightsubtree:
                        self.rightsubtree.parent = self
                    # We stellen de rightsubtree van de parent gelijk aan de huidige node en stellen zijn middlesubtree gelijk aan zijn lmiddlesubtree
                    # We stellen zijn l/rmiddlesubtree gelijk aan None
                    self.parent.rightsubtree = self
                    self.parent.middlesubtree = self.parent.lmiddlesubtree
                    self.parent.lmiddlesubtree = None
                    self.parent.rmiddlesubtree = None
                elif len(self.parent.rightsubtree.items) == 2:
                    # We voegen aan de huidige node het laatste item van de parent toe en voegen aan de parent het eerste item van de sibling toe
                    self.items.append(self.parent.items[-1])
                    self.parent.items.pop()
                    self.parent.items.append(self.parent.rightsubtree.items[0])
                    self.parent.rightsubtree.items.pop(0)
                    # We stellen de middlesubtree van de huidige node gelijk aan zijn rightsubtree en zijn rightsubtree gelijk aan de leftsubtree van de sibling
                    self.middlesubtree = self.rightsubtree
                    self.rightsubtree = self.parent.rightsubtree.leftsubtree
                    if self.rightsubtree:
                        self.rightsubtree.parent = self
                    # We stellen de leftsubtree van de sibling gelijk aan zijn middlesubtree en zijn middlesubtree gelijk aan None
                    self.parent.rightsubtree.leftsubtree = self.parent.rightsubtree.middlesubtree
                    self.parent.rightsubtree.middlesubtree = None
                elif len(self.parent.rightsubtree.items) == 3:
                    # We voegen aan de huidige node het laatste item van de parent toe en voegen aan de parent het eerste item van de sibling toe
                    self.items.append(self.parent.items[-1])
                    self.parent.items.pop()
                    self.parent.items.append(self.parent.rightsubtree.items[0])
                    self.parent.rightsubtree.items.pop(0)
                    # We stellen de middlesubtree van de huidige node gelijk aan zijn rightsubtree en zijn rightsubtree gelijk aan de leftsubtree van de sibling
                    self.middlesubtree = self.rightsubtree
                    self.rightsubtree = self.parent.rightsubtree.leftsubtree
                    if self.rightsubtree:
                        self.rightsubtree.parent = self
                    # We stellen de leftsubtree van de sibling gelijk aan zijn lmiddlesubtree en zijn middlesubtree gelijk aan zijn rmiddlesubtree
                    # We stellen zijn r/lmiddlesubtree gelijk aan None
                    self.parent.rightsubtree.leftsubtree = self.parent.rightsubtree.lmiddlesubtree
                    self.parent.rightsubtree.middlesubtree = self.parent.rightsubtree.rmiddlesubtree
                    self.parent.rightsubtree.rmiddlesubtree = None
                    self.parent.rightsubtree.lmiddlesubtree = None
            elif self.parent.rightsubtree == self:  # We kijken hier naar het geval van als onze huidige node glijk is aan de rightsubtree van de parent
                # We kijken hier naar de verschillende lengtes die de sibling van de huidige node kan hebben
                if len(self.parent.rmiddlesubtree.items) == 1:
                    # We voegen het laatste item van de parent en het eerste item van de sibling toe aan de huidige node
                    self.items.insert(0, self.parent.items[-1])
                    self.items.insert(0, self.parent.rmiddlesubtree.items[0])
                    self.parent.items.pop()
                    # We stellen de rmiddlesubtree van de huidige node gelijk aan zijn leftsubtree, zijn lmiddlesubtree gelijk aan de rightsubtree van de sibling en zijn leftsubtree gelijk aan de leftsubtree van de sibling
                    self.rmiddlesubtree = self.leftsubtree
                    self.lmiddlesubtree = self.parent.rmiddlesubtree.rightsubtree
                    self.leftsubtree = self.parent.rmiddlesubtree.leftsubtree
                    if self.lmiddlesubtree:
                        self.lmiddlesubtree.parent = self
                    if self.leftsubtree:
                        self.leftsubtree.parent = self
                    # We stellen de rmiddlesubtree van de parent gelijk aan None
                    self.parent.rmiddlesubtree = None
                    # We stellen de middlesubtree van de parent gelijk aan zijn lmiddlesubtree en stellen zijn lmiddlesubtree gelijk aan None
                    self.parent.middlesubtree = self.parent.lmiddlesubtree
                    self.parent.lmiddlesubtree = None
                elif len(self.parent.rmiddlesubtree.items) == 2:
                    # We voegen aan de huidige node het laatste item van de parent toe en voegen aan de parent het laatste item van de sibling toe
                    self.items.insert(0, self.parent.items[-1])
                    self.parent.items.pop()
                    self.parent.items.append(self.parent.rmiddlesubtree.items[-1])
                    self.parent.rmiddlesubtree.items.pop()
                    # De middlesubtree van de huidige node stellen we gelijk aan zijn leftsubtree en zijn leftsubtree stellen we gelijk aan de rightsubtree van de sibling
                    self.middlesubtree = self.leftsubtree
                    self.leftsubtree = self.parent.rmiddlesubtree.rightsubtree
                    if self.leftsubtree:
                        self.leftsubtree.parent = self
                    # De rightsubtree van de sibling stellen we gelijk aan zijn middlesubtree en zijn middlesubtree aan None
                    self.parent.rmiddlesubtree.rightsubtree = self.parent.rmiddlesubtree.middlesubtree
                    self.parent.rmiddlesubtree.middlesubtree = None
                elif len(self.parent.rmiddlesubtree.items) == 3:
                    # We voegen aan de huidige node het laatste item van de parent toe en voegen aan de parent het laatste item van de sibling toe
                    self.items.insert(0, self.parent.items[-1])
                    self.parent.items.pop()
                    self.parent.items.append(self.parent.rmiddlesubtree.items[-1])
                    self.parent.rmiddlesubtree.items.pop()
                    # De middlesubtree van de huidige node stellen we gelijk aan zijn leftsubtree en zijn leftsubtree stellen we gelijk aan de rightsubtree van de sibling
                    self.middlesubtree = self.leftsubtree
                    self.leftsubtree = self.parent.rmiddlesubtree.rightsubtree
                    if self.leftsubtree:
                        self.leftsubtree.parent = self
                    # De rightsubtree van de sibling stellen we gelijk aan zijn rmiddlesubtree en zijn middlesubtree stellen we gelijk aan zijn lmiddlesubtree
                    # We stellen zijn l/rmiddlesubtree gelijk aan None
                    self.parent.rmiddlesubtree.rightsubtree = self.parent.rmiddlesubtree.rmiddlesubtree
                    self.parent.rmiddlesubtree.middlesubtree = self.parent.rmiddlesubtree.lmiddlesubtree
                    self.parent.rmiddlesubtree.rmiddlesubtree = None
                    self.parent.rmiddlesubtree.lmiddlesubtree = None

    def inordersuccesor(self, item):
        "Deze functie zoekt de inorder succesor van de node met het gegeven item"
        # Hier kijken we naar de verschillende lengtes die de huidige node kan hebben
        if len(self.items) == 3:
            if self.items[
                0].key == item:  # Als het 1ste key van de huidige node gelijk is aan item kijken we verder in de lmiddlesubtree
                if self.leftsubtree:
                    return self.lmiddlesubtree.inordersuccesor(item)
                else:  # Als dit echter een blad is returnen we het item met de key waaraan onze item gelijk is
                    return self.items[0]
            if self.items[
                1].key == item:  # Als het 2de key van de huidige node gelijk is aan item kijken we verder in de rmiddlesubtree
                if self.leftsubtree:
                    return self.rmiddlesubtree.inordersuccesor(item)
                else:  # Als dit echter een blad is returnen we het item met de key waaraan onze item gelijk is
                    return self.items[1]
            if self.items[
                2].key == item:  # Als het 3de key van de huidige node gelijk is aan item kijken we verder in de rightsubtree
                if self.leftsubtree:
                    return self.rightsubtree.inordersuccesor(item)
                else:  # Als dit echter een blad is returnen we het item met de key waaraan onze item gelijk is
                    return self.items[2]
            else:  # We kijken hier naar het geval dat onze item niet in onze huidige node zit
                # Als onze subtrees bestaan kijken we verder in onze leftsubtree, zo niet dan returnen we het eerste item van de huidige node
                if self.rightsubtree and self.leftsubtree and self.lmiddlesubtree and self.rmiddlesubtree:
                    return self.leftsubtree.inordersuccesor(item)
                else:
                    return self.items[0]
        elif len(self.items) == 2:
            if self.items[0].key == item:
                if self.leftsubtree:
                    return self.middlesubtree.inordersuccesor(item)
                else:  # Als dit echter een blad is returnen we het item met de key waaraan onze item gelijk is
                    return self.items[0]
            if self.items[1].key == item:
                if self.leftsubtree:
                    return self.rightsubtree.inordersuccesor(item)
                else:  # Als dit echter een blad is returnen we het item met de key waaraan onze item gelijk is
                    return self.items[1]
            else:  # We kijken hier naar het geval dat onze item niet in onze huidige node zit
                # Als onze subtrees bestaan kijken we verder in onze leftsubtree, zo niet dan returnen we het eerste item van de huidige node
                if self.rightsubtree and self.leftsubtree and self.middlesubtree:
                    return self.leftsubtree.inordersuccesor(item)
                else:
                    return self.items[0]
        elif len(self.items) == 1:
            # Als de lengte van de huidige node gelijk is aan 1 moeten we eerst checken of het een parent heeft of niet
            if self.parent:  # Als deze een parent heeft moeten we eerst gaan redistributen en dan roepen we de inordersuccesor weer terug
                self.redistribute()
                return self.inordersuccesor(item)
            else:  # Als dit niet het geval is zoeken we verder in de rightsubtree
                return self.rightsubtree.inordersuccesor(item)

    def insertItem(self, item):
        "Dit is de methode waarmee je waardes in de 234 boom kan zetten"
        if not self.items:  # We kijken hier eerst of onze tree leeg is of niet
            self.items.append(item)
            return True
        else:
            # We gaan hier alle verschillende lengtes af dat onze huidige node kan hebben
            if len(self.items) == 3:
                self.split()  # Als de lengte van onze node gelijk is aan 3 moeten we eerst splitsen voor we kunnen doorgaan
                # Als onze parent bestaat kijken we naar de verschillende lengtes die de parent kan zijn
                if self.parent:
                    # Afhankelijk van onze insertkeywaarde kijken we steeds verder in een andere subtree
                    if len(self.parent.items) == 2:
                        if self.parent.items[0].key > item.key:
                            return self.parent.leftsubtree.insertItem(item)
                        if self.parent.items[0].key < item.key < self.parent.items[1].key:
                            return self.parent.middlesubtree.insertItem(item)
                        if self.parent.items[1].key < item.key:
                            return self.parent.rightsubtree.insertItem(item)
                    if len(self.parent.items) == 3:
                        if self.parent.items[0].key > item.key:
                            return self.parent.leftsubtree.insertItem(item)
                        if self.parent.items[0].key < item.key < self.parent.items[1].key:
                            return self.parent.lmiddlesubtree.insertItem(item)
                        if self.parent.items[1].key < item.key < self.parent.items[2].key:
                            return self.parent.rmiddlesubtree.insertItem(item)
                        if self.parent.items[2].key < item.key:
                            return self.parent.rightsubtree.insertItem(item)
                # Dit is het geval waarbij we geen parent hebben, dus wanneer we in de root zitten
                else:
                    # We hebben hier heel zeker een 2 knoop dus we moeten afhankelijk van de keywaarde van het ingegeven element in een van de subtrees kijken
                    if self.items[0].key < item.key:
                        return self.rightsubtree.insertItem(item)
                    if self.items[0].key > item.key:
                        return self.leftsubtree.insertItem(item)
            if len(self.items) == 2:
                # Als onze subtrees bestaan moeten we verder kijken afhankelijk van de key waarde van de ingegeven item
                if self.leftsubtree and self.rightsubtree and self.middlesubtree:
                    if self.items[0].key > item.key:
                        return self.leftsubtree.insertItem(item)
                    if self.items[0].key < item.key < self.items[1].key:
                        return self.middlesubtree.insertItem(item)
                    if self.items[1].key < item.key:
                        return self.rightsubtree.insertItem(item)
                # Als we geen subtrees hebben zitten we in een blad dus we kijken eerst of er al een item inzit met dezelfde key waarde
                # Zo ja return False, zo nee insert de item op de juiste positie
                else:
                    if self.items[0].key == item.key:
                        return False
                    if self.items[1].key == item.key:
                        return False
                    if self.items[0].key > item.key:
                        self.items.insert(0, item)
                        return True
                    if self.items[0].key < item.key < self.items[1].key:
                        self.items.insert(1, item)
                        return True
                    if self.items[1].key < item.key:
                        self.items.append(item)
                        return True
            if len(self.items) == 1:
                # Als onze subtrees bestaan gaan we verderkijken in een van de subtrees
                if self.leftsubtree and self.rightsubtree:
                    if self.items[0].key > item.key:
                        return self.leftsubtree.insertItem(item)
                    if self.items[0].key < item.key:
                        return self.rightsubtree.insertItem(item)
                # Zo niet kijken we of de item al in de boom zit
                # Zo ja returnen we False, zo nee returnen we True
                else:
                    if self.items[0].key < item.key:
                        self.items.append(item)
                        return True
                    if self.items[0].key == item.key:
                        return False
                    else:
                        self.items.insert(0, item)
                        return True

    def deleteItem(self, key):
        "Dit is een methode waarmee we het element verwijderen met het gegeven keywaarde"
        if not self.items:  # We kijken eerst of de huidige node leeg is , zo ja return False
            return False
        if len(
                self.items) == 1 and self.parent != None:  # Dit is het geval voor als we een 2 knoop hebben dat niet de root is
            if self.leftsubtree or self.items[0].key == key:
                self.redistribute()
                return self.deleteItem(key)
            else:
                return False
        # Hieronder is het geval voor als we een 2 knoop hebben waar de key niet inzit of het geval voor als we een 2 knoop hebben waar de key wel inzit en waar de huidige node de root is van de boom
        if len(self.items) == 1 and self.items[0].key != key and len(self.leftsubtree.items) == 1 and len(
                self.rightsubtree.items) == 1 or len(self.items) == 1 and self.items[0].key == key and len(
                self.leftsubtree.items) == 1 and len(self.rightsubtree.items) == 1 and self.parent == None:
            self.lmiddlesubtree = self.leftsubtree.rightsubtree
            self.rmiddlesubtree = self.rightsubtree.leftsubtree
            self.items.insert(0, self.leftsubtree.items[0])
            self.items.append(self.rightsubtree.items[0])
            self.leftsubtree = self.leftsubtree.leftsubtree
            self.rightsubtree = self.rightsubtree.rightsubtree
            if self.leftsubtree:
                self.leftsubtree.parent = self
            if self.rightsubtree:
                self.rightsubtree.parent = self
            if self.lmiddlesubtree:
                self.lmiddlesubtree.parent = self
            if self.rmiddlesubtree:
                self.rmiddlesubtree.parent = self
            return self.deleteItem(key)
        else:
            # We kijken hier naar de verschillende lengtes die de huidige node kan hebben
            if len(self.items) == 2:
                # We kijken hier of de key in de huidige node zit
                if self.items[0].key == key or self.items[1].key == key:
                    # We kijken hier of de huidige node subtrees bevat
                    if self.leftsubtree:
                        # We kijken hier of de subtrees subtrees bevatten
                        if self.rightsubtree.leftsubtree:
                            a = self.inordersuccesor(key)
                            if self.items[0].key == key:
                                self.items.pop(0)
                                self.items.insert(0, a)
                                return self.middlesubtree.deleteItem(a.key)
                            if self.items[1].key == key:
                                self.items.pop(1)
                                self.items.insert(1, a)
                                return self.rightsubtree.deleteItem(a.key)
                        # Dit is het geval waarbij de subtrees geen subtrees hebben
                        else:
                            a = self.inordersuccesor(key)
                            if len(self.items) == 1:
                                if a.key < self.items[0].key:
                                    return self.leftsubtree.deleteItem(a.key)
                                else:
                                    if self.items[0].key == key:
                                        self.items.pop()
                                        self.items.append(a)
                                    return self.rightsubtree.deleteItem(a.key)
                            if len(self.items) == 2:
                                if a.key < self.items[0].key:
                                    return self.leftsubtree.deleteItem(a.key)
                                if self.items[0].key < a.key < self.items[1].key:
                                    if self.items[0].key == key:
                                        self.items.pop(0)
                                        self.items.insert(0, a)
                                    return self.middlesubtree.deleteItem(key)
                                else:
                                    if self.items[1].key == key:
                                        self.items.pop()
                                        self.items.append(a)
                                    return self.rightsubtree.deleteItem(a.key)
                            if len(self.items) == 3:
                                if a.key < self.items[0].key:
                                    return self.leftsubtree.deleteItem(a.key)
                                if self.items[0].key < a.key < self.items[1].key:
                                    if self.items[0].key == key:
                                        self.items.pop(0)
                                        self.items.insert(0, a)
                                    return self.lmiddlesubtree.deleteItem(key)
                                if self.items[1].key < a.key < self.items[2].key:
                                    if self.items[1].key == key:
                                        self.items.pop(1)
                                        self.items.insert(1, a)
                                    return self.rmiddlesubtree.deleteItem(key)
                                else:
                                    if self.items[2].key == key:
                                        self.items.pop()
                                        self.items.append(a)
                                    return self.rightsubtree.deleteItem(a.key)
                    # Dit is het geval waarbij de huidige node geen subtrees heeft
                    else:
                        if self.items[0].key == key:
                            self.items.pop(0)
                            return True
                        elif self.items[1].key == key:
                            self.items.pop()
                            return True
                        else:
                            return False
                # Dit is het geval waarbij het item met het gegeven keywaarde niet in de huidige node zit
                else:
                    if self.leftsubtree:
                        if self.items[0].key > key:
                            return self.leftsubtree.deleteItem(key)
                        elif self.items[0].key < key < self.items[1].key:
                            return self.middlesubtree.deleteItem(key)
                        else:
                            return self.rightsubtree.deleteItem(key)

            if len(self.items) == 3:
                if self.items[0].key == key or self.items[1].key == key or self.items[2].key == key:
                    if self.leftsubtree:
                        if self.rightsubtree.leftsubtree:
                            a = self.inordersuccesor(key)
                            if self.items[0].key == key:
                                self.items.pop(0)
                                self.items.insert(0, a)
                                return self.lmiddlesubtree.deleteItem(a.key)
                            if self.items[1].key == key:
                                self.items.pop(1)
                                self.items.insert(1, a)
                                return self.rmiddlesubtree.deleteItem(a.key)
                            if self.items[2].key == key:
                                self.items.pop()
                                self.items.append(a)
                                return self.rightsubtree.deleteItem(a.key)
                        else:
                            a = self.inordersuccesor(key)
                            if len(self.items) == 1:
                                if a.key < self.items[0].key:
                                    return self.leftsubtree.deleteItem(a.key)
                                else:
                                    if self.items[0].key == key:
                                        self.items.pop()
                                        self.items.append(a)
                                    return self.rightsubtree.deleteItem(a.key)
                            if len(self.items) == 2:
                                if a.key < self.items[0].key:
                                    return self.leftsubtree.deleteItem(a.key)
                                if self.items[0].key < a.key < self.items[1].key:
                                    if self.items[0].key == key:
                                        self.items.pop(0)
                                        self.items.insert(0, a)
                                    return self.middlesubtree.deleteItem(key)
                                else:
                                    if self.items[1].key == key:
                                        self.items.pop()
                                        self.items.append(a)
                                    return self.rightsubtree.deleteItem(a.key)
                            if len(self.items) == 3:
                                if a.key < self.items[0].key:
                                    return self.leftsubtree.deleteItem(a.key)
                                if self.items[0].key < a.key < self.items[1].key:
                                    if self.items[0].key == key:
                                        self.items.pop(0)
                                        self.items.insert(0, a)
                                    return self.lmiddlesubtree.deleteItem(key)
                                if self.items[1].key < a.key < self.items[2].key:
                                    if self.items[1].key == key:
                                        self.items.pop(1)
                                        self.items.insert(1, a)
                                    return self.rmiddlesubtree.deleteItem(key)
                                else:
                                    if self.items[2].key == key:
                                        self.items.pop()
                                        self.items.append(a)
                                    return self.rightsubtree.deleteItem(a.key)
                    else:
                        if self.items[0].key == key:
                            self.items.pop(0)
                            return True
                        elif self.items[1].key == key:
                            self.items.pop(1)
                        elif self.items[2].key == key:
                            self.items.pop()
                            return True
                        else:
                            return False
                else:
                    if self.items[0].key == key:
                        self.items.pop(0)
                        return True
                    if self.items[1].key == key:
                        self.items.pop(1)
                        return True
                    if self.items[2].key == key:
                        self.items.pop(2)
                        return True
            else:
                if len(self.items) == 1:
                    if key < self.items[0].key:
                        if self.leftsubtree:
                            return self.leftsubtree.deleteItem(key)
                        else:
                            return False
                    if key > self.items[0].key:
                        if self.rightsubtree:
                            return self.rightsubtree.deleteItem(key)
                        else:
                            return False
                if len(self.items) == 2:
                    if key < self.items[0].key:
                        if self.leftsubtree:
                            return self.leftsubtree.deleteItem(key)
                        else:
                            return False
                    if self.items[0].key < key < self.items[1].key:
                        if self.middlesubtree:
                            return self.middlesubtree.deleteItem(key)
                        else:
                            return False
                    if key > self.items[1].key:
                        if self.rightsubtree:
                            return self.rightsubtree.deleteItem(key)
                        else:
                            return False
                elif len(self.items) == 3:
                    if key < self.items[0].key:
                        if self.leftsubtree:
                            return self.leftsubtree.deleteItem(key)
                        else:
                            return False
                    if self.items[0].key < key < self.items[1].key:
                        if self.lmiddlesubtree:
                            return self.lmiddlesubtree.deleteItem(key)
                        else:
                            return False
                    if self.items[1].key < key < self.items[2].key:
                        if self.rmiddlesubtree:
                            return self.rmiddlesubtree.deleteItem(key)
                        else:
                            return False
                    if self.items[2].key < key:
                        if self.rightsubtree:
                            return self.rightsubtree.deleteItem(key)
                        else:
                            return False

    def inorderTraverse(self, FunctieType):
        if len(self.items) == 3:
            if self.leftsubtree:
                self.leftsubtree.inorderTraverse(FunctieType)
            FunctieType(self.items[0].key)
            if self.lmiddlesubtree:
                self.lmiddlesubtree.inorderTraverse(FunctieType)
            FunctieType(self.items[1].key)
            if self.rmiddlesubtree:
                self.rmiddlesubtree.inorderTraverse(FunctieType)
            FunctieType(self.items[2].key)
            if self.rightsubtree:
                self.rightsubtree.inorderTraverse(FunctieType)
        if len(self.items) == 2:
            if self.leftsubtree:
                self.leftsubtree.inorderTraverse(FunctieType)
            FunctieType(self.items[0].key)
            if self.middlesubtree:
                self.middlesubtree.inorderTraverse(FunctieType)
            FunctieType(self.items[1].key)
            if self.rightsubtree:
                self.rightsubtree.inorderTraverse(FunctieType)
        if len(self.items) == 1:
            if self.leftsubtree:
                self.leftsubtree.inorderTraverse(FunctieType)
            FunctieType(self.items[0].key)
            if self.rightsubtree:
                self.rightsubtree.inorderTraverse(FunctieType)

    def save(self):
        a = {}
        b = []
        for i in range(len(self.items)):
            b.append(self.items[i].key)
        a['root'] = b
        if self.leftsubtree is None:
            return {'root': b}
        else:
            a['children'] = []
            if len(self.items) == 3:
                a['children'].append(self.leftsubtree.save())
                a['children'].append(self.lmiddlesubtree.save())
                a['children'].append(self.rmiddlesubtree.save())
                a['children'].append(self.rightsubtree.save())
            if len(self.items) == 2:
                a['children'].append(self.leftsubtree.save())
                a['children'].append(self.middlesubtree.save())
                a['children'].append(self.rightsubtree.save())
            if len(self.items) == 1:
                a['children'].append(self.leftsubtree.save())
                a['children'].append(self.rightsubtree.save())
        return a

    def load(self, dict, Start=True):
        if Start == True:
            self.clear()
        if 'root' in dict:
            for i in range(len(dict['root'])):
                if isinstance(dict['root'][i], tuple):
                    b = Node(dict['root'][i][0], dict['root'][i][1])
                    self.items.append(b)
                    Start = False
                else:
                    b = Node(dict['root'][i], dict['root'][i])
                    self.items.append(b)
                    Start = False
        if 'children' in dict:
            if len(self.items) == 3:
                for j in dict['children']:
                    if j is None:
                        continue
                    else:
                        if j['root'][0] < self.items[0].key:
                            self.leftsubtree = TwoThreeFourTree()
                            self.leftsubtree.parent = self
                            self.leftsubtree.load(j, Start)
                        elif self.items[0].key < j['root'][0] < self.items[1].key:
                            self.lmiddlesubtree = TwoThreeFourTree()
                            self.lmiddlesubtree.parent = self
                            self.lmiddlesubtree.load(j, Start)
                        elif self.items[1].key < j['root'][0] < self.items[2].key:
                            self.rmiddlesubtree = TwoThreeFourTree()
                            self.rmiddlesubtree.parent = self
                            self.rmiddlesubtree.load(j, Start)
                        else:
                            self.rightsubtree = TwoThreeFourTree()
                            self.rightsubtree.parent = self
                            self.rightsubtree.load(j, Start)
            elif len(self.items) == 2:
                for j in dict['children']:
                    if j is None:
                        continue
                    else:
                        if j['root'][0] < self.items[0].key:
                            self.leftsubtree = TwoThreeFourTree()
                            self.leftsubtree.parent = self
                            self.leftsubtree.load(j, Start)
                        elif self.items[0].key < j['root'][0] < self.items[1].key:
                            self.middlesubtree = TwoThreeFourTree()
                            self.middlesubtree.parent = self
                            self.middlesubtree.load(j, Start)
                        else:
                            self.rightsubtree = TwoThreeFourTree()
                            self.rightsubtree.parent = self
                            self.rightsubtree.load(j, Start)
            elif len(self.items) == 1:
                for j in dict['children']:
                    if j is None:
                        continue
                    else:
                        if j['root'][0] < self.items[0].key:
                            self.leftsubtree = TwoThreeFourTree()
                            self.leftsubtree.parent = self
                            self.leftsubtree.load(j, Start)
                        else:
                            self.rightsubtree = TwoThreeFourTree()
                            self.rightsubtree.parent = self
                            self.rightsubtree.load(j, Start)

    def clear(self):
        self.items = []
        self.rightsubtree = None
        self.rmiddlesubtree = None
        self.middlesubtree = None
        self.lmiddlesubtree = None
        self.leftsubtree = None