"""
ADT voor film
Dit is een test
"""
#Implementeren: Stein
#Testen: Sam
class Film:
    def __init__(self, film_titel, film_rating=0):
        """
        Maakt een nieuwe film aan met een id, een titel en een rating
        Hiervoor gebruiken wij een id generator, die we er later gaan bijvoegen

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

    # def delete(self):
    #     """
    #     Verwijdert het object
    #
    #     :param film_id: titel van de film (string)
    #     :return: None
    #
    #     precondities:
    #         film_id > 0 en int
    #
    #     postcondities:
    #         Object Film is verwijderd
    #     """
    #     pass


# # Dit is een functie, aub geen method van maken
# def aantal_filmen():
#     """
#     Geeft het aantal filmen in de database
#
#     :return: aantal filmen in de database (int in tuple)
#     """
#     pass