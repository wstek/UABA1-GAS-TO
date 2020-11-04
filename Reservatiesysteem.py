"""
ADT voor reservatiesysteem
"""

class Reservatiesysteem:
    def __int__(self):
        pass

    def maak_account(self, voornaam, achternaam, email, wachtwoord):
        """
        Maakt een account in de database aan voor de gebruiker
        """
        pass

    def verwijder_account(self, gebruiker_id):
        """
        Verwijdert een account uit de database

        :param gebruiker_id: id van de gebruiker (int)
        :return: None

        precondities:
            gebruiker is aangemeld
            gebruiker bestaat in de database
        postcondities:
            1 gebruiker minder in de database
        """
        pass

    def meld_aan(self, gebruiker_id, wachtwoord):
        """
        Meldt de gebruiker aan

        Deze functie gebruikt de "gebruikers" dictionary van Gebruiker.py
        :param gebruiker_id: id van de gebruiker (int)
        :param wachtwoord: wachtwoord van de gebruiker (string)
        :return: None

        precondities:
            gebruiker bestaat in de database
        """
        pass

    def meld_af(self, gebruiker_id):
        """
        Meldt de gebruiker af

        Deze functie gebruikt de "gebruikers" dictionary van Gebruiker.py
        :param gebruiker_id: id van de gebruiker (int)
        :return: None

        precondities:
            gebruiker is aangemeld
        """
        pass

    def wachtwoord_vergeten(self, email):
        """
        Stuurt de gebruiker een email om zijn wachtwoorde te veranderen

        Deze functie gebruikt de "gebruikers" dictionary van Gebruiker.py
        :param email: email van de gebruiker (string)
        :return: None

        precondities:
            er is een gebruiker met een email waarmee de gegeven email overeenkomt

        postcondities:
            gebruiker kan zijn wachtwoord veranderen
        """
        pass


    def maak_reservatie(self, gebruiker_id, vertoning_id, timestamp, plaatsen_gereserveerd):
        """
        Maakt een reservatie voor de gebruiker

        :param gebruiker_id: id van de gebruiker (int)
        :param vertoning_id: id van de vertoning (int)
        :param timestamp:
        :param plaatsen_gereserveerd: aantal plaatsen gereserveerd (int)
        :return: reservatie_id (int in tuple)

        precondities:
            gebruiker is aangemeld
            vertoning_id bestaat
            gebruiker_id en vertoning_id > 0 en int

        postcondities:
            1 reservatie meer in de database
        """
        pass

    def annuleer_reservatie(self, gebruiker_id, reservatie_id):
        """
        Annuleert een reservatie voor de gebruiker

        Deze functie gebruikt de "gebruikers" dictionary van Gebruiker.py
        Deze functie gebruikt de "reservaties" dictionary van Reservatie.py
        :param gebruiker_id: id van de gebruiker (int)
        :param reservatie_id: id van de reservatie (int)
        :return: None

        precondities:
            gebruiker is aangemeld
            reservatie_id bestaat
            gebruiker_id en reservatie_id > 0 en int

        postcondities:
            1 reservatie minder in de database
        """
        pass

    def verzoek_reservaties(self, gebruiker_id):
        """
        Geeft een tuple met alle reservaties van de gebruiker

        :param gebruiker_id: id van de gebruiker (int)
        :return: tuple met alle reservatie_id's van de gebruiker (int in tuple)

        precondities:
            gebruiker is aangemeld
            gebruiker_id > 0 en int
        """
        pass