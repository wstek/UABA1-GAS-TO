"""
ADT voor film
"""

class Film:
    def __init__(self, film_titel, film_rating=0):
        """
        Voegt een film toe aan de database

        :param film_titel: titel van de film (string)
        :param film_rating: rating van de film (float)

        precondities:
            film_titel is een string
            film_rating is een float

        postcondities:
            1 film meer in de database
        """
        pass

    def verwijder(self):
        """
        Verwijdert een film uit de database

        :param film_id: titel van de film (string)
        :return: None

        precondities:
            film_id > 0 en int

        postcondities:
            1 element minder in de dictionary
        """
        pass


def aantal_filmen():
    """
    Geeft het aantal filmen in de database

    :return: aantal filmen in de database (int in tuple)
    """
    pass