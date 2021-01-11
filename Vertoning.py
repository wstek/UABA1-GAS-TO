"""
ADT voor vertoning
"""

from BaseStructures.Stack import Stack


#Implementeren: Stein
#Testen: Sam
class Vertoning:

    sloten = ["14:30", "17:00", "20:00", "22:30"]

    def __init__(self, zaalnummer, film_id, timeslot, datum_vertoning, aantal_vrije_plaatsen):
        """
        Maakt een nieuwe vertoning aan

        :param zaalnummer: zaalnummer (int)
        :param film_id: id van de film (int)
        :param timeslot: timeslot (int)
        :param datum_vertoning: datum van de vertoning (int)
        :param aantal_vrije_plaatsen: aantal vrije plaatsen van een vertoning (int)

        precondities
            zaalnummer, film_id, datum_vertoning, aantal_vrije_plaatsen  > 0 en int
            timeslot < sloten.lenght
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

    def isOverTime(self, timestamp):
        """
        :param timestamp: huidig tijdstip (string)
        :return true indien de huidige tijd groter is als de voorstellingstijd
        precondities
            timestamp string van formaar 00:00
        postconditie
            boolian die weergeeft of de voorstelling overtijd is

        """
        hourH = timestamp.split(':')[0]         #huidige uur
        minutesH = timestamp.split(':')[1]       #huidige minuten

        hourV = Vertoning.sloten[self.timeslot - 1].split(':')[0]     #vertoning uur
        minutesV = Vertoning.sloten[self.timeslot - 1].split(':')[1]  #vertoning minuten
        return hourH > hourV or (minutesH > minutesV and hourH >= hourV)    #indien het huidig uur groter is of het huidig aantal minuten en het uur is gelijk aan of groter dan de vertoning




    # def delete(self):
    #     """
    #     Verwijdert een vertoning
    #
    #     :return: None
    #
    #     precondities:
    #         vertoning bestaat
    #     postcondities:
    #         vertoning is verwijderd
    #     """
    #     pass
    #
    # def reserve_places(self, reserved_places):
    #     """
    #     Het aantal plaatsen dat gereserveerd wordt, wordt afgetrokken van het aantal vrije plaatsen
    #     :param aantal_gereserveerde_plaatsen: Het aantal plaatsen dat gereserveerd wordt (int)
    #
    #     :return: Bool(True als plaatsen beschikbaar, anders False)
    #
    #     :preconditie:
    #         De vertoning bestaat
    #
    #     :postconditie:
    #         empty_places -= reserved_places
    #     """



# # Dit is een functie, aub geen method van maken
# def aantal_vertoningen():
#     """
#     Geeft het aantal vertoningen in de database
#
#     :return: aantal vertoningen (int in tuple)
#     """
#     pass