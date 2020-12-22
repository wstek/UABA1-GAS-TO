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

    # def delete(self):
    #     """
    #     Verwijdert een gebruiker
    #
    #     :return: None
    #
    #     precondities:
    #         gebruiker bestaat in de database
    #
    #     postcondities:
    #         Object gebruiker is verwijderd
    #     """
    #     pass
    #
    # def change_password(self, new_password):
    #     """
    #     Verandert het password van de gebruiker
    #
    #     :param new_password: Nieuw password (string)
    #     :return: None
    #
    #     precondities:
    #         gebruiker bestaat in de database
    #         new_password != self.password
    #
    #     postcondities:
    #         password van de gebruiker wordt verandert door het nieuw gegeven password
    #     """
    #     pass


# # Dit is een functie, aub geen method van maken
# def gebruiker_id(email):
#     """
#     Geeft de gebruiker_id van de gebruiker
#
#     :param email: e-mailadres van de gebruiker (string)
#     :return: gebruiker_id: id van de gebruiker (int in tuple)
#
#     precondities:
#         email is een string
#         email bestaat in de dictionary
#     """
#     pass



