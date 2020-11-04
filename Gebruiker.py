"""
ADT voor gebruiker
"""

class Gebruiker:
    def __init__(self, voornaam, achternaam, email, wachtwoord):
        """
        Voegt een gebruiker toe aan de database

        :param voornaam: voornaam van de gebruiker (string)
        :param achternaam: achternaam van de gebruiker (string)
        :param email: e-mailadres van de gebruiker (string)
        :param wachtwoord: wachtwoord van de gebruiker (string)

        precondities:
            voornaam, achternaam, string, wachtwoord zijn strings
        postcondities:
            1 gebruiker meer in de database
        """
        pass

    def verwijder(self):
        """
        Verwijdert de gebruiker uit de database

        :return: None

        precondities:
            gebruiker bestaat in de database

        postcondities:
            1 gebruiker minder in de database
        """
        pass

    def verander_wachtwoord(self, nieuw_wachtwoord):
        """
        Verandert het wachtwoord van de gebruiker

        :param nieuw_wachtwoord: Nieuw wachtwoord (string)
        :return: None

        precondities:
            gebruiker bestaat in de database
            nieuw_wachtwoord is een string
            nieuw_wacthwoord != self.wachtwoord

        postcondities:
            wachtwoord van de gebruiker wordt verandert door het nieuw gegeven wachtwoord
        """
        pass


def gebruiker_id(email):
    """
    Geeft de gebruiker_id van de gebruiker

    :param email: e-mailadres van de gebruiker (string)
    :return: gebruiker_id: id van de gebruiker (int in tuple)

    precondities:
        email is een string
        email bestaat in de dictionary
    """
    pass


def aantal_gebruikers():
    """
    Geeft het aantal gebruikers in de database

    :return: aantal gebruikers (int in tuple)
    """
    pass
