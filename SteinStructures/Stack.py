"""
Stack: een ADT waarbij gegevens 'gestapeld worden' en bij het opvragen het laatst toegevoegde item word terug gegeven FILA
De stack zal gemaakt worden bij het aanroepen van de classe
De stack bevat volgende bewerkingen:
1) __innit__: creëert een lege stack
2) isEmpty: Bepaald of de stack leeg is
3) push: Voegt een element aan de stack toe
4) pop: Verwijdert het laatst toegevoegde element uit de stack
5) getTop: Vraagt het laatst toegevoede element op uit de stack
"""
class Stack:
    """
    Creëert een lege stack
    Précondities: geen
    Postcondities: Maakt een niewe lege stack aan
    """
    def __init__(self, maxlengt):
        self.stack = []
        self.maxlen = maxlengt
        self.count = 0;
        pass

    """
    Controleerd of de stack leeg is
    Précondities: geen
    Postcondities: geeft True terug indien de stack leeg is,indien de stack niet leeg is False
    """
    def isEmpty(self):
        return len(self.stack) == 0


    """
    Voeg een element toe aan de stack
    Précondities: het item dat toevevoegd word moet hetzelfde datatype zijn als de al reeds toegevoegde items
    Postcondities: 
        success: geeft True terug indien het item in de stack is geplaatst, indien er iets fout is gegaan False
    """
    def push(self, item):
        self.count += 1
        if(self.maxlen > len(self.stack)):
            self.stack.append(item)
            return True
        else:
            return False

    """
    Verwijderd het laatst toegevoegde element van de stack
    Précondities: de stack is niet leeg
    Postcondities:
    Zal het laatst toegevoegde element verwijderen,
    zal een tuple terug geven met een 
        success: geeft True terug indien het item van de stack is verwijderd, indien er iets fout is gegaan False
        stackTop: de waarde van het laatst toegevoegde element
    """
    def pop(self):
        self.count -= 1
        if (len(self.stack) > 0):
            returnValue = self.stack[len(self.stack) - 1];
            self.stack.remove(self.stack[len(self.stack) - 1])
            return(returnValue, True)
        else:
            return (False, False)

    """
    Zal de waarde van het laatst toegevoegde item in de variable stackTop plaatsen 
    Précondities: de stack is niet leeg
    Postcondities:
    Zal het laatst toegevoegde element teruggeven,
    zal een tuple terug geven met een 
        success: geeft True terug indien het gelukt is, False indien niet
        stackTop: de waarde van het laatst toegevoegde element
    """
    def getTop(self):
        if(len(self.stack) > 0):
            return (self.stack[len(self.stack) - 1], True)
        else:
            return (False, False)

    def save(self):
        return self.stack

    def load(self, stack):
        self.stack = stack

    def getLength(self):
        return self.count