"""
ADT voor gebruiker
"""

class Gebruiker:
    def __init__(self, firstname, lastname, email, password):
        """
        Maak een nieuwe gebruiker aan met een voornaam, een achternaam, een email en een wachtwoord
        Hiervoor gebruiken wij een id generator, die we er later gaan bijvoegen

        :param firstname: voornaam van de gebruiker (string)
        :param lastname: achternaam van de gebruiker (string)
        :param email: e-mailadres van de gebruiker (string)
        :param password: wachtwoord van de gebruiker (string)

        precondities:
            Email is bestaat en is niet in gebruik
        postcondities:
            Object Gebruiker is aangemaakt
        """
        pass

    def delete(self):
        """
        Verwijdert de gebruiker uit de database

        :return: None

        precondities:
            gebruiker bestaat in de database

        postcondities:
            Object gebruiker is verwijderd
        """
        pass

    def change_password(self, new_password):
        """
        Verandert het wachtwoord van de gebruiker

        :param new_password: Nieuw wachtwoord (string)
        :return: None

        precondities:
            gebruiker bestaat in de database
            new_password != self.password

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
#Hallo