"""
ADT voor reservatie
"""

class Reservatie:
    def __init__(self, gebruiker_id, vertoning_id, timestamp, plaatsen_gereserveerd):
        """
        Voegt een reservatie toe aan de database

        :param gebruiker_id:
        :param vertoning_id:
        :param timestamp:
        :param plaatsen_gereserveerd:

        precondities:
            gebruiker_id, vertoning_id, timestamp, plaatsen_gereserveerd > 0 en int

        postcondities:
            1 reservatie meer in de database
        """
        pass

    def verwijder(self):
        """
        Verwijdert een reservatie uit de database

        :return: None

        precondities:
            reservatie bestaat in de database
        postcondities:
            1 reservatie minder in de database
        """
        # del reservaties[self.id]
        pass


# Dit is een functie, aub geen method van maken
def aantal_reservaties(vertoning_id=None):
    """
    Geeft aantal reservaties (als vertoning_id gegeven, dan geeft die aantal reservaties voor die vertoning)

    :param vertoning_id: id van de vertoning (int)
    :return: aantal reservaties (int in tuple)

    precondities:
        vertoning_id > 0 en int
    """
    pass