"""
ADT voor reservatie
"""
#Implementeren: William
#Testen: Stein
class Reservatie:
    def __init__(self, gebruiker_id, vertoning_id, plaatsen_gereserveerd, timestamp, datum):
        """
        Maak een nieuwe reservatie aan met een gebruikersid, een vertoningsid, een timestamp en het aantal gereserveerde
        plaatsen
        Hiervoor gebruiken wij een id generator, die we er later gaan bijvoegen

        :param gebruiker_id: De id van de gebruiker, die een reservatie maakt (int)
        :param vertoning_id: De id van de vertoning (int)
        :param timestamp: Het tijdstip waarop de reservatie is gemaakt (int of string)
        :param plaatsen_gereserveerd: Het aantal gereserveerde plaatsen (int)

        precondities:
            gebruiker_id, vertoning_id, timestamp, plaatsen_gereserveerd > 0 en int

        postcondities:
            Object reservatie is aangemaakt
        """
        self.gebruiker_id = gebruiker_id
        self.vertoning_id = vertoning_id
        self.plaatsen_gereserveerd = plaatsen_gereserveerd
        self.timestamp = timestamp
        self.datum = datum

    def delete(self):
        """
        Verwijdert een reservatie

        :return: None

        precondities:
            reservatie bestaat in de database
        postcondities:
            Object reservatie is verwijderd
        """
        pass


