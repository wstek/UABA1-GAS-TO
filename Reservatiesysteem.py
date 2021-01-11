"""
Made By: William, Said, Stein, Sam
Date: 14/01/2020
ADT voor reservatiesysteem

Mogelijke Structuren:
-   DubbelgelinkteCirulaireKettingTable     - alle 4
-   BSTTable                                - alle 4
-   RedBlackTreeTable                       - Sam & William
-   ######################################################################234 van said
-   ######################################################################stein

Specifieke structuren:
-   Stack (voor tickets in vertoning)       - alle 4
-   Queue (reservaties)                     - alle 4
"""

# add (name+s)Structures. om een andere structuur te gebruiken example: "from SamsStructures.BSTTable import *"
from Film import *
from Reservatie import *
from Gebruiker import *
from Zaal import *
from Vertoning import *
from BSTTable import *
from Queue import Queue
import shlex
import os


class Reservatiesysteem:
    def __init__(self):
        """
        initialiseerd het reservatiesysteem
        """
        self.log_count = 0  # ID van de logfile, zodat die steeds uniek is en er meerdere kunnen gemaakt worden in 1 run
        self.zalen = BSTTable()
        self.filmen = BSTTable()
        self.vertoningen = BSTTable()
        self.gebruikers = BSTTable()
        self.reservaties = Queue()
        self.log = BSTTable()  # key: datum, value: {zaal_id: [vertoningen op pos slot]}

    def readScript(self, scriptname):
        """
        Leest en verwerkt het scriptbestand.
        :param scriptname: relatief pad/naam van het bestand
        :return: None
        precondition: script met scriptname bestaat
        """
        file = open(scriptname, "r")
        commands = file.read().split("\n")

        is_init = False
        is_start = False

        for command in commands:
            if command == "" or command[0] == "#":
                continue

            if command == "init":
                is_init = True
                is_start = False
                continue

            if command == "start":
                is_start = True
                is_init = False
                continue

            # shlex splits de string op spaties, bijhalve bij aanhalingstekens
            # dit zorgt ervoor dat de naam van een film niet wordt gesplitst
            com_args = shlex.split(command)

            # Initialisatie van de verschillende objecten
            if is_init:
                if com_args[0] == "zaal":
                    nieuwe_zaal = Zaal(int(com_args[1]), int(com_args[2]))
                    self.zalen.tableInsert(createTreeItem(int(com_args[1]), nieuwe_zaal))

                if com_args[0] == "film":
                    nieuwe_film = Film(com_args[2], com_args[3])
                    self.filmen.tableInsert(createTreeItem(int(com_args[1]), nieuwe_film))

                if com_args[0] == "vertoning":
                    nieuwe_vertoning = Vertoning(int(com_args[2]), int(com_args[5]), int(com_args[3]),
                                                 com_args[4], int(com_args[6]))
                    self.vertoningen.tableInsert(createTreeItem(int(com_args[1]), nieuwe_vertoning))

                    # Vertoningen worden in self.log gestoken om dat later makkelijker in een tabel te zetten
                    # Maar ik weet niet of dat dit goed is
                    log = self.log.tableRetrieve(nieuwe_vertoning.datum_vertoning)[0]
                    if log is None:
                        temp_list = []
                        for slot in Vertoning.sloten:
                            temp_list.append(None)

                        self.log.tableInsert(createTreeItem(
                            nieuwe_vertoning.datum_vertoning,
                            {nieuwe_vertoning.zaalnummer: temp_list}
                        ))

                        self.log.tableRetrieve(nieuwe_vertoning.datum_vertoning)[0][nieuwe_vertoning.zaalnummer][
                            nieuwe_vertoning.timeslot - 1] = nieuwe_vertoning
                    else:
                        log[nieuwe_vertoning.zaalnummer][nieuwe_vertoning.timeslot - 1] = nieuwe_vertoning

                if com_args[0] == "gebruiker":
                    nieuwe_gebruiker = Gebruiker(com_args[2], com_args[3], com_args[4])
                    self.gebruikers.tableInsert(createTreeItem(int(com_args[1]), nieuwe_gebruiker))

            # Dit is voor reservaties en zo
            if is_start:
                datum = com_args[0]
                timestamp = com_args[1]

                if com_args[2] == "reserveer":
                    nieuwe_reservatie = Reservatie(int(com_args[3]), int(com_args[4]), int(com_args[5]),
                                                   timestamp, datum)
                    self.reservaties.enqueue(nieuwe_reservatie)

                if com_args[2] == "ticket":
                    self.updateAanwezigen(int(com_args[3]), int(com_args[4]))

                if com_args[2] == "log":
                    self.createLog(timestamp, datum)

                if not self.reservaties.isEmpty():
                    self.updateReservaties()

        file.close()

    def updateReservaties(self):
        """
        Verwerkt elke reservatie in de queue
        :return: None
        """
        while not self.reservaties.isEmpty():
            reservatie = self.reservaties.dequeue()[0]
            vertoning = self.vertoningen.tableRetrieve(reservatie.vertoning_id)[0]

            # Als er plaats is
            # Verminder de aantal vrije plaatsen
            # Voeg tickets toe aan de verwachte_personen stack (van het vertoningobject)
            if vertoning.aantal_vrije_plaatsen > reservatie.plaatsen_gereserveerd:
                print("Gereserveerd!")
                vertoning.aantal_vrije_plaatsen -= reservatie.plaatsen_gereserveerd

                for plaats in range(reservatie.plaatsen_gereserveerd):
                    vertoning.verwachte_personen.push("ticket")
            else:
                print("Onvolgoende Vrije Plaatsen!")

    def updateAanwezigen(self, vertoning_id, aantal_aanwezigen):
        """
        Verwerkt de personen die aangekomen zijn om de film te bekijken
        :param vertoning_id: id van de vertoning
        :param aantal_aanwezigen: aantal personen die aankomen
        :return: None
        """
        vertoning = self.vertoningen.tableRetrieve(vertoning_id)[0]

        # Pop de tickets van de stack en incrementeer vertoning.aanwezig
        for aanwezige in range(aantal_aanwezigen):
            vertoning.verwachte_personen.pop()
            vertoning.aanwezig += 1

        # Als iedereen aanwezig is dan start de film
        if vertoning.verwachte_personen.isEmpty():
            vertoning.gestart = True
            print(
                f'Iedereen is aangekomen en de film "{self.filmen.tableRetrieve(vertoning.film_id)[0].titel}" begint!')

    def createLog(self, timestamp, datum):
        """
        Creëert een log in een htmlbestand
        :return: None
        :postcondition: er is een html bestaand aangemaakt met de log
        """
        # Voor elke zaal een nieuwe rij in de tabel met de film en de vertoningen op die dag
        # Ik neem aan dat de log enkel voor 1 datum is

        # Maak een folder logs aan als die nog niet bestaat
        if not os.path.exists('logs'):
            os.makedirs('logs')
        # Maak een nieuwe html bestand aan of overschrijf het
        log_file = open(f"logs/log{self.log_count}.html", "w")
        self.log_count += 1  # log_count is voor als we meerdere logbestanden willen maken in 1 run

        # html stuff
        log_file.write("""
        <html><head><meta http-equiv="content-type" content="text/html; charset=windows-1252"><style>
        table {border-collapse: collapse;}
        table, td, th {border: 1px solid black;}
        </style></head><body>
        """)
        log_file.write(f"<h1>Log op {datum} {timestamp}</h1>")
        log_file.write(f"""
        <table><thead><tr>
        <td>Datum</td>
        <td>Film</td>""")
        for i in Vertoning.sloten:
            log_file.write(f"""<td>{i}</td>""")
        log_file.write(f"""</tr></thead>""")

        # Als er geen vertoningen zijn voor die datum
        if self.log.tableRetrieve(datum)[0] is None:
            print("Geen vertoningen voor die datum!")
            return

        for zaalnummer in self.log.tableRetrieve(datum)[0]:
            is_waiting = False
            film_id = self.log.tableRetrieve(datum)[0][zaalnummer][0].film_id

            # Titel
            log_file.write(f"<tbody><tr><td>{datum}</td><td>{self.filmen.tableRetrieve(film_id)[0].titel}")

            # Rijen in de tabel
            for vertoning in self.log.tableRetrieve(datum)[0][zaalnummer]:
                if vertoning is None:
                    log_file.write(f"<td></td>")

                # F betekent dat de film gestart is gevolgd door het aantal mensen in de zaal
                elif vertoning.gestart:
                    log_file.write(f"<td>F:{vertoning.aanwezig}</td>")

                # W betekent dat de film wacht om gestart te worden gevolgd
                # door het aantal mensen waarop nog gewacht wordt
                elif vertoning.isOverTime(timestamp):
                    log_file.write(f"<td>W:{vertoning.verwachte_personen.getLength()}</td>")

                # G betekent gepland, gevolgd door het aantal verkochte ticketten
                else:
                    log_file.write(f"<td>G:{vertoning.verwachte_personen.getLength()}</td>")

            log_file.write("</tr></tbody>")

        log_file.write("</table></body></html>")

        log_file.close()

    # def log_in(self, gebruiker_id, password):
    #     """
    #     Meldt een gebruiker aan
    #
    #     :param gebruiker_id: id van de gebruiker (int)
    #     :param password: password van de gebruiker (string)
    #     :return success: True bij success, False bij failure (bool)
    #     precondities: De gebruiker bestaat
    #     """
    #
    # def log_out(self, gebruiker_id):
    #     """
    #     Meldt een gebruiker af
    #
    #     :param gebruiker_id: id van de gebruiker (int)
    #     :return: None
    #
    #     precondities:
    #         De gebruiker is aangemeld
    #     """
    #     pass
    #
    # def forgot_password(self, email):
    #     """
    #     Stuurt de gebruiker een email om zijn passworde te veranderen
    #
    #     :param email: email van de gebruiker (string)
    #     :return: None
    #
    #     precondities:
    #         er is een gebruiker met een email waarmee het gegeven email overeenkomt
    #
    #     postcondities:
    #         gebruiker kan zijn password veranderen
    #     """
    #     pass

    # def maak_reservatie(self, gebruiker_id, vertoning_id, timestamp, plaatsen_gereserveerd):
    #     """
    #     Maakt een reservatie voor de gebruiker
    #
    #     :param gebruiker_id: id van de gebruiker (int)
    #     :param vertoning_id: id van de vertoning (int)
    #     :param timestamp:
    #     :param plaatsen_gereserveerd: aantal plaatsen gereserveerd (int)
    #     :return: reservatie_id (int in tuple)
    #
    #     precondities:
    #         gebruiker is aangemeld
    #         vertoning_id bestaat
    #         gebruiker_id en vertoning_id > 0 en int
    #
    #     postcondities:
    #         1 reservatie meer in de database
    #     """
    #     pass

    # def free_Places(self,vertoningid):
    #     """
    #     Bepaalt het aantal vrije plaatsen voor een vertoning
    #     :param vertoningid: De vertonings id
    #
    #     :return: Aantal vrije plaatsen voor een vertoning
    #
    #     :preconditie:
    #         De vertoning bestaat
    #     """
    #
    # def cancel(self, gebruiker_id, reservatie_id):
    #     """
    #     Annuleert een reservatie van de gebruiker
    #
    #     Deze functie gebruikt de "gebruikers" dictionary van Gebruiker.py
    #     Deze functie gebruikt de "reservaties" dictionary van Reservatie.py
    #     :param gebruiker_id: id van de gebruiker (int)
    #     :param reservatie_id: id van de reservatie (int)
    #     :return: None
    #
    #     precondities:
    #         gebruiker is aangemeld
    #         reservatie_id bestaat
    #         gebruiker_id en reservatie_id > 0 en int
    #
    #     postcondities:
    #         De reservatie is geannuleerd
    #     """
    #     pass


# Dit is een functie, aub geen method van maken
# def verzoek_reservaties(self, gebruiker_id):
#     """
#     Geeft een tuple met alle reservaties van de gebruiker
#
#     :param gebruiker_id: id van de gebruiker (int)
#     :return: tuple met alle reservatie_id's van de gebruiker (int in tuple)
#
#     precondities:
#         gebruiker is aangemeld
#         gebruiker_id > 0 en int
#     """
#     pass
#     onion soup

if __name__ == "__main__":
    sys = Reservatiesysteem()
    sys.readScript("system(1).txt")
    # print("Hello World!")
    # print(sys.gebruikers.tableRetrieve(2)[0].firstname)
