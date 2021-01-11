"""
ADT voor zaal
"""


class Zaal:

    def __init__(self, nummer, seats):
        """
        Maakt een nieuwe zaal aan

        :param nummer: zaalnummer (int)
        :param seats: aantal places in de zaal (int)

        precondities:
            nummer en places > 0 en int
        postcondities:
            Object zaal is aangemaakt
        """
        self.nummer = nummer
        self.seats = seats
