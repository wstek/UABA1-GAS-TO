"""
ADT voor vertoning
"""

class Vertoning:
    def __init__(self, zaalnummer, film_id, slot, datum_vertoning):
        """
        Voegt een vertoning toe aan de database
        :param zaalnummer: zaalnummer (int)
        :param film_id: id van de film (int)
        :param slot: tijdsslot (string)
        :param datum_vertoning: datum van de vertoning (int)

        precondities
            zaalnummer, film_id, datum_vertoning > 0 en int
            slot is een string
        postcondities:
            1 Vertoning meer in de database
        """
        pass

    def verwijder(self):
        """
        Verwijdert een vertoning uit de database

        :return: None

        precondities:
            vertoning bestaat in de database
        postcondities:
            1 vertoning minder in de database
        """
        pass


    def reset_plaatsen(self):
        pass


def aantal_vertoningen(self):
    """
    Geeft het aantal vertoningen in de database

    :return: aantal vertoningen (int in tuple)
    """
    pass