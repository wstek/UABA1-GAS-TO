"""
ADT voor gebruiker
"""
#Implementeren:Said
#Testen:William
class Gebruiker:
    def __init__(self, firstname, surname, email):
        """
        Maak een nieuwe gebruiker aan met een firstname, een surname en een email

        :param firstname: firstname van de gebruiker (string)
        :param surname: surname van de gebruiker (string)
        :param email: e-mailadres van de gebruiker (string)

        precondities:
            Email is bestaat en is niet in gebruik
        postcondities:
            Object Gebruiker is aangemaakt
        """
        self.firstname = firstname
        self.surname = surname
        self.email = email
