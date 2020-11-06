"""
ADT voor vertoning
"""
#Implementeren: Stein
#Testen: Sam
class Vertoning:
    def __init__(self, zaalnummer, film_id, slot, datum_vertoning):
        """
        Maakt een nieuwe vertoning aan
        Hiervoor gebruiken wij een id generator, die we er later gaan bijvoegen

        :param zaalnummer: zaalnummer (int)
        :param film_id: id van de film (int)
        :param slot: tijdsslot (string)
        :param datum_vertoning: datum van de vertoning (int)

        precondities
            zaalnummer, film_id, datum_vertoning > 0 en int
            slot is een string
        postcondities:
            Object vertoning is aangemaakt
        """
        pass

    def verwijder(self):
        """
        Verwijdert een vertoning

        :return: None

        precondities:
            vertoning bestaat in de database
        postcondities:
            1 vertoning minder in de database
        """
        pass

    def plaatsen_gereserveerd(self,aantal_gereserveerde_plaatsen):
        """
        Het aantal plaatsen dat gereserveerd wordt, wordt afgetrokken van het aantal vrije plaatsen
        :param aantal_gereserveerde_plaatsen: Het aantal plaatsen dat gereserveerd wordt (int)

        :return: Bool(True als plaatsen beschikbaar, anders False)

        :preconditie:
            De vertoning bestaat

        :postconditie:
            Aantal vrije plaatsen -= aantal gereserveerde plaatsen
        """



# # Dit is een functie, aub geen method van maken
# def aantal_vertoningen():
#     """
#     Geeft het aantal vertoningen in de database
#
#     :return: aantal vertoningen (int in tuple)
#     """
#     pass