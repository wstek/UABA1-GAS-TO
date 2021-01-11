"""
Stack: een ADT waarbij gegevens in een 'wachtrij' worden geplaatst en bij het opvragen het eerst toegevoegde item word terug gegeven FIFO
De Queue zal gemaakt worden bij het aanroepen van de classe
Alle items is de Queue zijn van hetzelfde datatype!
De Queue bevat volgende bewerkingen:
1) __innit__: creëert een lege Queue
2) isEmpty: Bepaald of de Queue leeg is
3) enqueue: Voegt een element aan de queue
4) dequeue: Verwijdert het eerst toegevoegde element uit de queue
5) getFront: Vraagt het eerst toegevoede element op uit de queue
"""
class Queue:
    """
    Creëert een lege queue
    Précondities: geen
    Postcondities: Maakt een niewe queue aan
    """
    def __init__(self):
        self.queue = []


    """
    Controleerd of de queue is
    Précondities: geen
    Postcondities: geeft True terug indien de queue leeg is,indien de queue niet leeg is False
    """
    def isEmpty(self):
        return len(self.queue) == 0


    """
    Voeg een element toe aan de queue
    Précondities: het item dat toevevoegd word moet hetzelfde datatype zijn als de al reeds toegevoegde items
    Postcondities: 
        success: geeft True terug indien het item in de queue is geplaatst, indien er iets fout is gegaan False
        """
    def enqueue(self, item):
        self.queue.insert(0,item)
        pass

    """
    Verwijderd het eerst toegevoegde element van de queue
    Précondities: de queue is niet leeg
    Postcondities:
    Zal het eerst toegevoegde element verwijderen,
    zal een tuple terug geven met een 
        success: geeft True terug indien het item van de queue is verwijderd, indien er iets fout is gegaan False
        stackTop: de waarde van het eerst toegevoegde element
    """
    def dequeue(self):
        waarde = self.queue[len(self.queue) - 1]
        self.queue.remove(waarde)
        return (True, waarde)

    """
    Zal de waarde van het eerst toegevoegde item in de variable stackTop plaatsen 
    Précondities: de stack is niet leeg
    Postcondities:
    Zal het eerst toegevoegde element teruggeven,
    zal een tuple terug geven met een 
        success: geeft True terug indien het gelukt is, False indien niet
        stackTop: de waarde van het eerst toegevoegde element
    """
    def getFront(self):
        if len(self.queue) > 0:
            return (True,self.queue[len(self.queue - 1)])
        return (False,"")

    def safe(self):
        return self.queue