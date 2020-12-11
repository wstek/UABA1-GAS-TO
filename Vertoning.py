"""
ADT voor vertoning
"""

from Stack import Stack

#Implementeren: Stein
#Testen: Sam
class Vertoning:
    def __init__(self, zaalnummer, film_id, timeslot, datum_vertoning, aantal_vrije_plaatsen):
        """
        Maakt een nieuwe vertoning aan
        Hiervoor gebruiken wij een id generator, die we er later gaan bijvoegen

        :param zaalnummer: zaalnummer (int)
        :param film_id: id van de film (int)
        :param timeslot: timeslot (string)
        :param datum_vertoning: datum van de vertoning (int)

        precondities
            zaalnummer, film_id, datum_vertoning > 0 en int
            timeslot is een string
        postcondities:
            Object vertoning is aangemaakt
        """
        self.zaalnummer = zaalnummer
        self.film_id = film_id
        self.timeslot = timeslot
        self.datum_vertoning = datum_vertoning
        self.aantal_vrije_plaatsen = aantal_vrije_plaatsen
        self.verwachte_personen = Stack()
        self.aanwezig = 0
        self.gestart = False

    def delete(self):
        """
        Verwijdert een vertoning

        :return: None

        precondities:
            vertoning bestaat
        postcondities:
            vertoning is verwijderd
        """
        pass

    def reserve_places(self, reserved_places):
        """
        Het aantal plaatsen dat gereserveerd wordt, wordt afgetrokken van het aantal vrije plaatsen
        :param aantal_gereserveerde_plaatsen: Het aantal plaatsen dat gereserveerd wordt (int)

        :return: Bool(True als plaatsen beschikbaar, anders False)

        :preconditie:
            De vertoning bestaat

        :postconditie:
            empty_places -= reserved_places
        """



# # Dit is een functie, aub geen method van maken
# def aantal_vertoningen():
#     """
#     Geeft het aantal vertoningen in de database
#
#     :return: aantal vertoningen (int in tuple)
#     """
#     pass