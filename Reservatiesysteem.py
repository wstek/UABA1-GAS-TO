"""
ADT voor reservatiesysteem
"""
from Film import *
from Reservatie import *
from Gebruiker import *
from Zaal import *
from Vertoning import *
from BSTTable import *
from Queue_ import Queue
import shlex
import os

#Implementeren: Sam
#Testen: Said
class Reservatiesysteem:
    def __init__(self):
        self.log_count = 0
        self.zalen = BSTTable()
        self.filmen = BSTTable()
        self.vertoningen = BSTTable()
        self.gebruikers = BSTTable()
        self.reservaties = Queue()
        self.log = BSTTable() # key: datum, value: {zaal_id: [vstlg slot1, slot2, slot3, slot4]}

    def readScript(self, scriptname):
        """
        Leest een tekstbestand in en verwerkt de script.
        :param scriptname: naam van het bestand
        :return: None
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

            com_args = shlex.split(command)

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

                    logding = self.log.tableRetrieve(nieuwe_vertoning.datum_vertoning)[0]
                    if logding is None:
                        self.log.tableInsert(createTreeItem(
                            nieuwe_vertoning.datum_vertoning,
                            {nieuwe_vertoning.zaalnummer: [None, None, None, None]}
                        ))
                        self.log.tableRetrieve(nieuwe_vertoning.datum_vertoning)[0][nieuwe_vertoning.zaalnummer][nieuwe_vertoning.timeslot - 1] = nieuwe_vertoning
                    else:
                        logding[nieuwe_vertoning.zaalnummer][nieuwe_vertoning.timeslot - 1] = nieuwe_vertoning

                if com_args[0] == "gebruiker":
                    nieuwe_gebruiker = Gebruiker(com_args[2], com_args[3], com_args[4])
                    self.gebruikers.tableInsert(createTreeItem(int(com_args[1]), nieuwe_gebruiker))

            if is_start:
                # onionsoup
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

        # Sluit het bestand
        file.close()

    def updateReservaties(self):
        """
        Verwerkt elke reservatie in de queue
        :return: None
        """
        while not self.reservaties.isEmpty():
            reservatie = self.reservaties.dequeue()[0]

            # Als er plaats is
            if self.vertoningen.tableRetrieve(reservatie.vertoning_id)[0].aantal_vrije_plaatsen > reservatie.plaatsen_gereserveerd:
                print("Gereserveerd!")
                self.vertoningen.tableRetrieve(reservatie.vertoning_id)[0].aantal_vrije_plaatsen -= reservatie.plaatsen_gereserveerd

                for plaats in range(reservatie.plaatsen_gereserveerd):
                    self.vertoningen.tableRetrieve(reservatie.vertoning_id)[0].verwachte_personen.push("ticket")
            else:
                print("Geen plaats meer!")

    def updateAanwezigen(self, vertoning_id, aantal_aanwezigen):
        """
        Verwerkt de personen die aangekomen zijn om de film te bekijken
        :param vertoning_id: id van de vertoning
        :param aantal_aanwezigen: aantal personen die aankomen
        :return: None
        """
        vertoning = self.vertoningen.tableRetrieve(vertoning_id)[0]
        for aanwezige in range(aantal_aanwezigen):
            vertoning.verwachte_personen.pop()
            vertoning.aanwezig += 1

        if vertoning.verwachte_personen.isEmpty():
            vertoning.gestart = True
            print(f'Iedereen is aangekomen en de film "{self.filmen.tableRetrieve(vertoning.film_id)[0].titel}" begint!')

    def createLog(self, timestamp, datum):
        """
        Creëert een log in een htmlbestand
        :return:
        """
        # Voor elke film en datum een nieuwe rij in de tabel
        # Maak een folder logs aan als die nog niet bestaat
        if not os.path.exists('logs'):
            os.makedirs('logs')
        # Maak een nieuwe html bestand aan of overschrijf het
        log_file = open(f"logs/log{self.log_count}.html", "w")

        log_file.write("""
        <html><head><meta http-equiv="content-type" content="text/html; charset=windows-1252"><style>
		table {border-collapse: collapse;}
		table, td, th {border: 1px solid black;}
	    </style></head><body>
	    """)
        log_file.write(f"<h1>Log op {datum} {timestamp}</h1>")
        log_file.write("<table><thead><tr><td>Datum</td><td>Film</td><td>14:30</td><td>17:00</td><td>20:00</td><td>22:30</td></tr></thead>")

        for zaalnummer in self.log.tableRetrieve(datum)[0]:
            is_waiting = False
            film_id = self.log.tableRetrieve(datum)[0][zaalnummer][0].film_id
            log_file.write(f"<tbody><tr><td>{datum}</td><td>{self.filmen.tableRetrieve(film_id)[0].titel}")
            for vertoning in self.log.tableRetrieve(datum)[0][zaalnummer]:
                if vertoning is None:
                    log_file.write(f"<td></td>")
                elif vertoning.gestart:
                    log_file.write(f"<td>F:{vertoning.aanwezig}</td>")

                elif not vertoning.gestart and not is_waiting:
                    log_file.write(f"<td>W:{vertoning.verwachte_personen.getLength()}</td>")
                    is_waiting = True

                elif not vertoning.gestart:
                    log_file.write(f"<td>G:{vertoning.verwachte_personen.getLength()}</td>")


            log_file.write("</tr></tbody></table>")

        log_file.write("</body></html>")

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


if __name__ == "__main__":
    sys = Reservatiesysteem()
    sys.readScript("system(1).txt")
    print("Hello World!")
    # print(sys.gebruikers.tableRetrieve(2)[0].firstname)