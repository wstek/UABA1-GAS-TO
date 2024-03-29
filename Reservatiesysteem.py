"""
Made By: William, Said, Stein, Sam
Date: 14/01/2020
ADT voor reservatiesysteem

Logbestanden worden in /logs genereerd.

Mogelijke Structuren:
-   BSTTable                                - alle 4
-   RedBlackTreeTable                       - Sam & William
-   BSTTableTable                   - Said & Stein

Specifieke structuren:
-   DubbelgelinkteCirulaireKettingTable     - alle 4
-   Stack (voor tickets in vertoning)       - alle 4
-   Queue (reservaties)                     - alle 4
TijdSloten:
-   Kunnen worden aangepast in vertoning
"""

# add (name+s)Structures. om een andere structuur te gebruiken example: "from SamStructures.BSTTable import *"
from Film import *
from Reservatie import *
from Gebruiker import *
from Zaal import *
from Vertoning import *
from BaseStructures.BSTTable import *
from BaseStructures.Queue import Queue
import shlex
import os
from copy import deepcopy


class Reservatiesysteem:
    def __init__(self):
        """
        initialiseerd het reservatiesysteem
        """
        self.zalen = BSTTable()
        self.films = BSTTable()
        self.vertoningen = BSTTable()
        self.gebruikers = BSTTable()
        self.reservaties = Queue()

        self.log = BSTTable()  # key: datum, value: {zaal_id: [vertoningen op pos slot]}
        self.log_count = 0  # ID van de logfile, zodat die steeds uniek is en er meerdere kunnen gemaakt worden in 1 run
        self.logs_folder = "logs"  # Naam van de folder die de logbestanden bevat
        self.clearLogFiles()

    def readScript(self, scriptname):
        """
        Leest en verwerkt het scriptbestand.
        :param scriptname: relatief pad/naam van het bestand
        :return: succes
        precondition: script met scriptname bestaat
        """
        file = open(scriptname, "r")
        commands = file.read().split("\n")

        is_init = False
        is_start = False
        logs = []

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

            # shlex splits de string op spaties, behalve bij aanhalingstekens
            # dit zorgt ervoor dat de naam van een film niet wordt gesplitst
            com_args = shlex.split(command)

            # Initialisatie van de verschillende objecten
            if is_init:
                if com_args[0] == "zaal":
                    self.addZaal(int(com_args[1]), int(com_args[2]))

                if com_args[0] == "film":
                    self.addFilm(int(com_args[1]), com_args[2], com_args[3])

                if com_args[0] == "vertoning":
                    self.addVertoning(int(com_args[1]), int(com_args[2]), int(com_args[5]), int(com_args[3]),
                                      com_args[4], int(com_args[6]))

                if com_args[0] == "gebruiker":
                    self.addGebruiker(int(com_args[1]), com_args[2], com_args[3], com_args[4])

            # reservaties, tickets, log
            if is_start:
                datum = com_args[0]
                timestamp = com_args[1]

                if com_args[2] == "reserveer":
                    self.addReservatie(int(com_args[3]), int(com_args[4]), int(com_args[5]), timestamp, datum)

                if com_args[2] == "ticket":
                    self.updateAanwezigen(int(com_args[3]), int(com_args[4]))

                if com_args[2] == "log":
                    filepath = self.createLog(timestamp, datum)
                    if filepath:
                        logs.append(filepath[0])

                if not self.reservaties.isEmpty():
                    self.updateReservaties()

        file.close()
        return logs, True

    def addZaal(self, nummer, seats):
        """
        Voegt een zaal toe aan het systeem.
        :return: None
        """
        nieuwe_zaal = Zaal(nummer, seats)
        self.zalen.tableInsert(createTreeItem(nummer, nieuwe_zaal))

    def addFilm(self, film_id, film_titel, film_rating):
        """
        Voegt een film toe aan het systeem.
        :return: None
        """
        nieuwe_film = Film(film_titel, film_rating)
        self.films.tableInsert(createTreeItem(film_id, nieuwe_film))

    def addVertoning(self, vertoning_id, zaalnummer, film_id, timeslot, datum_vertoning, aantal_vrije_plaatsen):
        """
        Voegt een vertoning toe aan het systeem.
        :return: None
        """
        nieuwe_vertoning = Vertoning(zaalnummer, film_id, timeslot, datum_vertoning, aantal_vrije_plaatsen)
        self.vertoningen.tableInsert(createTreeItem(vertoning_id, nieuwe_vertoning))

        # Vertoningen worden in self.log gestoken om dat later makkelijker in een tabel te zetten
        log_datum = self.log.tableRetrieve(nieuwe_vertoning.datum)[0]

        # als de log op die datum leeg is
        # voeg dan een dictionary met zaal_id en een lijst met None #sloten keer
        if log_datum is None:
            temp_list = []
            for slot in Vertoning.sloten:
                temp_list.append(None)

            self.log.tableInsert(createTreeItem(
                nieuwe_vertoning.datum,
                {nieuwe_vertoning.zaalnummer: temp_list}
            ))

            # insert de vertoning in de lijst
            self.log.tableRetrieve(nieuwe_vertoning.datum)[0][nieuwe_vertoning.zaalnummer][
                nieuwe_vertoning.timeslot - 1] = nieuwe_vertoning

        # als er een log is op die datum maar de zaalnummer is niet in de dictionary
        elif nieuwe_vertoning.zaalnummer not in log_datum:
            temp_list = []
            for slot in Vertoning.sloten:
                temp_list.append(None)

            # insert de vertoning in de lijst
            log_datum[nieuwe_vertoning.zaalnummer] = temp_list

            # insert de vertoning in de lijst
            log_datum[nieuwe_vertoning.zaalnummer][nieuwe_vertoning.timeslot - 1] = nieuwe_vertoning
        else:
            # insert de vertoning in de lijst
            log_datum[nieuwe_vertoning.zaalnummer][nieuwe_vertoning.timeslot - 1] = nieuwe_vertoning

        # Voeg de vertoning toe aan het film object
        self.films.tableRetrieve(film_id)[0].vertoningen.append(vertoning_id)

    def addGebruiker(self, gebruiker_id, firstname, surname, email):
        """
        Voegt een gebruiker toe aan het systeem.
        :return: None
        """
        nieuwe_gebruiker = Gebruiker(firstname, surname, email)
        self.gebruikers.tableInsert(createTreeItem(gebruiker_id, nieuwe_gebruiker))

    def addReservatie(self, gebruiker_id, vertoning_id, plaatsen_gereserveerd, timestamp, datum):
        """
        Voegt een reservatie toe aan het systeem.
        :return: None
        """
        nieuwe_reservatie = Reservatie(gebruiker_id, vertoning_id, plaatsen_gereserveerd, timestamp, datum)
        self.reservaties.enqueue(nieuwe_reservatie)

    def updateReservaties(self):
        """
        Verwerkt elke reservatie in de queue.
        :return: None
        """
        while not self.reservaties.isEmpty():
            reservatie = self.reservaties.dequeue()[0]
            vertoning = self.vertoningen.tableRetrieve(reservatie.vertoning_id)[0]

            # Als er plaats is
            # Verminder het aantal vrije plaatsen
            # Voeg tickets toe aan de verwachte_personen stack (van het vertoningobject)
            if vertoning.aantal_vrije_plaatsen > reservatie.plaatsen_gereserveerd:
                print("gereserveerd")
                vertoning.aantal_vrije_plaatsen -= reservatie.plaatsen_gereserveerd

                for plaats in range(reservatie.plaatsen_gereserveerd):
                    vertoning.verwachte_personen.push("ticket")
            else:
                print("geen vrije plaatsen meer")

    def updateAanwezigen(self, vertoning_id, aantal_aanwezigen):
        """
        Verwerkt de personen die aangekomen zijn om de film te bekijken.
        :param vertoning_id: id van de vertoning
        :param aantal_aanwezigen: aantal personen die aankomen
        :return: None
        """
        vertoning = self.vertoningen.tableRetrieve(vertoning_id)[0]

        # Pop de tickets van de stack en incrementeer vertoning.aanwezig
        for aanwezige in range(aantal_aanwezigen):
            succes = vertoning.verwachte_personen.pop()[1]
            if succes:
                vertoning.aanwezig += 1
            else:
                return

        # Als iedereen aanwezig is dan start de film
        if vertoning.verwachte_personen.isEmpty():
            vertoning.gestart = True
            print(f'film "{self.films.tableRetrieve(vertoning.film_id)[0].titel}" begint')

    def createLog(self, timestamp, datum):
        """
        Creëert een log in een htmlbestand.
        Een tabel met voor elke zaal een nieuwe rij met de film en de vertoningen op die dag.
        :return: filename, Succes
        :postcondition: er is een html bestaand aangemaakt met de log
        """
        # Maak een folder logs aan als die nog niet bestaat
        if not os.path.exists('logs'):
            os.makedirs('logs')

        # Maak een nieuwe html bestand aan of overschrijf het
        log_file = open(f"logs/log{self.log_count}.html", "w")
        file_path = f"logs/log{self.log_count}.html"
        self.log_count += 1  # log_count is voor als we meerdere logbestanden willen maken in 1 run

        # html basis
        log_file.write("""
        <html><head><meta http-equiv="content-type" content="text/html; charset=windows-1252"><style>
        table {border-collapse: collapse;}
        table, td, th {border: 1px solid black;}
        </style></head><body>
        """)

        # titel
        log_file.write(f"<h1>Log op {datum} {timestamp}</h1>")

        # head van de tabel
        # de eerste twee kolommen: datum en film
        log_file.write(f"""
        <table><thead><tr>
        <td>Datum</td>
        <td>Film</td>
        """)

        # de andere kolommen
        # hangt af van het aantal sloten in Vertoning.py
        for slot in Vertoning.sloten:
            log_file.write(f"<td>{slot}</td>")
        log_file.write(f"</tr></thead>")

        zaal_dict = self.log.tableRetrieve(datum)[0]

        # Als er geen vertoningen zijn op die datum
        if zaal_dict is None:
            print(f"geen vertoningen op {datum}")
            return None, False

        # voor elke zaal een nieuwe rij
        for zaalnummer in zaal_dict:
            zaal_verts = zaal_dict[zaalnummer]
            curr_film_id = None
            vak_items = []

            # kolommen in de tabel
            for vertoning in zaal_verts:
                # Als er geen vertoningen zijn op die datum
                if vertoning is None:
                    vak_items.append(None)
                    continue

                if curr_film_id is None:
                    curr_film_id = vertoning.film_id

                # Als er een vertoning in dezelfde zaal is met een andere film
                # dan een nieuwe rij maken met de andere film
                elif curr_film_id != vertoning.film_id:
                    temp_list = deepcopy(vak_items)
                    while len(temp_list) < len(Vertoning.sloten):
                        temp_list.append(None)

                    self.addRow(log_file, datum, timestamp, self.films.tableRetrieve(curr_film_id)[0].titel, temp_list)
                    temp_list2 = []
                    for item in vak_items:
                        temp_list2.append(None)
                    vak_items = temp_list2
                    curr_film_id = vertoning.film_id

                # F betekent dat de film gestart is gevolgd door het aantal mensen in de zaal
                if vertoning.gestart:
                    vak_items.append(f"F:{vertoning.aanwezig}")

                # W betekent dat de film wacht om gestart te worden gevolgd
                elif vertoning.isOverTime(timestamp):
                    vak_items.append(f"W:{vertoning.verwachte_personen.getLength()}")

                # G betekent gepland, gevolgd door het aantal verkochte ticketten
                else:
                    vak_items.append(f"G:{vertoning.verwachte_personen.getLength()}")

            self.addRow(log_file, datum, timestamp, self.films.tableRetrieve(curr_film_id)[0].titel, vak_items)

        log_file.write("</table></body></html>")

        log_file.close()
        return file_path, True

    def addRow(self, log_file, datum, timestamp, filmtitel, vak_items):
        log_file.write(f"<tbody><tr><td>{datum}</td><td>{filmtitel}</td>")

        for item in vak_items:
            if item is None:
                log_file.write("<td></td>")
            else:
                log_file.write(f"<td>{item}</td>")

        log_file.write("</tr></tbody>")

    def clearLogFiles(self):
        """
        Verwijder alle logs
        :return: None
        """
        # zet log_count terug op nul
        self.log_count = 0

        try:
            files = os.listdir(self.logs_folder)
            succes = True
        except:
            succes = False

        if succes:
            for filename in os.listdir(self.logs_folder):
                file_path = os.path.join(self.logs_folder, filename)
                try:
                    if os.path.isfile(file_path) or os.path.islink(file_path):
                        os.unlink(file_path)
                except Exception as e:
                    print('Kon het bestand %s niet verwijderen. Reden: %s' % (file_path, e))

    def reset(self):
        """
        Reset het reservatiesysteem.
        :return: None
        """
        # verwijder logbestanden
        self.clearLogFiles()

        # clear alle datastructuren
        self.zalen = BSTTable()
        self.films = BSTTable()
        self.vertoningen = BSTTable()
        self.gebruikers = BSTTable()
        self.reservaties = Queue()
        self.log = BSTTable()


if __name__ == "__main__":
    sys = Reservatiesysteem()
    sys.readScript("test_script.txt")
