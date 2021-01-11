"""
ADT voor film
Dit is een test
"""


# Implementeren: Stein
# Testen: Sam
class Film:
    def __init__(self, film_titel, film_rating=0):
        """
        Maakt een nieuwe film aan met een id, een titel en een rating

        :param film_titel: titel van de film (string)
        :param film_rating: rating van de film (float)

        precondities:
            film_titel is een string
            film_rating is een float
        postcondities:
            Object Film is aangemaakt
        """
        self.titel = film_titel
        self.rating = film_rating
        self.vertoningen = {}
