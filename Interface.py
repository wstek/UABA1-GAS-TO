"""
GUI voor Reservatiesysteem.py

Bevat alle functionaliteit van reservatiesysteem.
Er is niet zo veel aandacht besteed aan ongeldige gebruikersinvoer, error handling en de lay-out van het programma.
Logbestanden worden in /logs genereerd.

gebruikte bronnen:
https://likegeeks.com/python-gui-examples-tkinter-tutorial/
https://stackoverflow.com/questions/7546050/switch-between-two-frames-in-tkinter
https://riptutorial.com/tkinter/example/29713/grid--
"""
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
from tkinter import scrolledtext
from tkinter.ttk import Combobox
from Reservatiesysteem import Reservatiesysteem
from Vertoning import Vertoning
from copy import deepcopy
import webbrowser
import os

# INSTELLINGEN
WIDTH = 800
HEIGHT = 500
auto_open_log = True


class ReservatiesysteemInterface(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)

        # huidige frame
        self._frame = None

        # reservatiesysteem
        self.sys = Reservatiesysteem()
        self.time = [18, 0]
        self.date = [1, 1, 2021]

        # zet de windowsize en titel
        self.geometry(f"{WIDTH}x{HEIGHT}")
        self.title("Reservatiesysteem Sandbox")

        # Maak de window niet resizable
        self.resizable(False, False)

        # menubar
        self.menu = tk.Menu(self)
        self.menu.add_command(label="Lees script", command=lambda: self.readScript())
        self.menu.add_command(label="Reset", command=lambda: self.reset())
        self.config(menu=self.menu)

        # ga naar de startpagina
        self.switchFrame(StartFrame)

        self.protocol("WM_DELETE_WINDOW", self.closeWindow)
        self.mainloop()

    def switchFrame(self, frame_class):
        """
        Vernietigt de huidige frame en vervangt het met een andere.
        """
        if self._frame is not None:
            self.sys = self._frame.sys
            self.time = self._frame.time
            self.date = self._frame.date
            self._frame.destroy()

        new_frame = frame_class(self, self.sys, self.time, self.date)
        self._frame = new_frame
        self._frame.pack()

    def readScript(self):
        """
        Vraagt de gebruiker om een txt bestand dat het script bevat te selecteren. Het huidige reservatiesysteem
        wordt gereset en het script wordt verwerkt.
        """
        # vraag voor het bestand
        file_path = filedialog.askopenfilename(filetypes=(("Text files", "*.txt"), ("all files", "*.*")))

        # als er geen bestand werd geselecteerd
        if not file_path:
            return

        # slaag het huidige reservatiesysteem tijdelijk op
        temp_sys = deepcopy(self.sys)

        # reset het huidige reservatiesysteem
        self.sys.reset()

        # lees de script
        logs_succes = self.sys.readScript(file_path)

        # Popups
        if logs_succes[1]:
            # open elke log die gemaakt werd tijdens het lezen van de script
            if auto_open_log:
                for log in logs_succes[0]:
                    filename = os.path.abspath(log)
                    print(filename)
                    webbrowser.open_new_tab(filename)

            # ga Terug naar de startpagina
            self.switchFrame(StartFrame)

            messagebox.showinfo("Info", "Script succesvol verwerkt!")
        else:
            messagebox.showinfo("Error", "Script kon niet verwerkt worden", icon='warning')
            # Zet het oude reservatiesysteem Terug
            self.sys = temp_sys

    def reset(self):
        """
        Vraagt de gebruiker of dat die zeker is. Reset het reservatiesysteem en gaat Terug naar de startpagina.
        """
        msgbox = messagebox.askquestion("Reset", "Bent u zeker dat u wilt resetten?",
                                        icon='warning')
        if msgbox == "yes":
            self.sys.reset()
            messagebox.showinfo("Info", "Het systeem is gereset")
            self.switchFrame(StartFrame)

    def closeWindow(self):
        """
        Sluit het programma
        """
        msgbox = messagebox.askquestion("Reset", "Bent u zeker dat u het programma wil sluiten?\n" +
                                        "Alle wijzigingen gaan verloren.")
        if msgbox == "yes":
            self.sys.reset()
            self.destroy()


class StartFrame(tk.Frame):
    """
    Startpagina
    bevat:
        init knop
        maak log knop
    """
    def __init__(self, parent, sys, time, date):
        tk.Frame.__init__(self, parent)
        self.sys = sys
        self.time = time
        self.date = date
        tk.Label(self, text="Reservatiesysteem",
                 font=("Arial Bold", 30)).pack(side="top", fill="x", pady=10)

        tk.Button(self, text="Data", command=lambda: parent.switchFrame(DataFrame)).pack(pady=15)

        self.time_entry = tk.Entry(self, width=25)
        self.time_entry.pack()
        tk.Button(self, text="Verander tijd (uu:mm)", command=lambda: self.setTime()).pack(pady=5)

        self.date_entry = tk.Entry(self, width=25)
        self.date_entry.pack()
        tk.Button(self, text="Verander datum (dd/mm/yy)", command=lambda: self.setDate()).pack(pady=5)

        tk.Button(self, text="Reservatie toevoegen", command=lambda: parent.switchFrame(AddReservatieFrame)).pack(pady=10)
        tk.Button(self, text="Update aanwezigen", command=lambda: parent.switchFrame(UpdateAanwezigenFrame)).pack(pady=10)

        tk.Button(self, text="Maak log", command=lambda: self.createLog()).pack(pady=10)

        tk.Label(self, text="Huidige tijd:").pack(side="top")
        if len(str(self.time[1])) == 1:
            time = "0" + str(self.time[1])
        else:
            time = self.time[1]
        self.time_label = tk.Label(self, text=f"{self.time[0]}:{time}")
        self.time_label.pack(side="top", pady=2)

        tk.Label(self, text="Huidige datum:").pack(side="top", pady=2)
        self.date_label = tk.Label(self, text=f"{self.date[0]}/{self.date[1]}/{self.date[2]}")
        self.date_label.pack(side="top")

    def createLog(self):
        """
        Creëert een log en opent het in de standaard webbrowser.
        """
        if len(str(self.time[1])) == 1:
            time = "0" + str(self.time[1])
        else:
            time = self.time[1]
        self.time_label = tk.Label(self, text=f"{self.time[0]}:{time}")
        log_succes = self.sys.createLog(f"{self.time[0]}:{time}",
                                        f"{self.date[2]}-{self.date[1]}-{self.date[0]}")

        # open het logbestand
        if log_succes[1]:
            filename = os.path.abspath(log_succes[0])
            print(filename)
            webbrowser.open_new_tab(filename)
        elif log_succes[0] is None:
            messagebox.showinfo("Error", f"Geen vertoningen op {self.date[0]}/{self.date[1]}/{self.date[2]}",
                                icon='warning')

    def setTime(self):
        """
        Verandert de tijd van het systeem naar input van de gebruiker.
        :return: None
        """
        res = self.time_entry.get()
        try:
            res2 = res.split(":")
            self.time = [int(item) for item in res2]
            self.time_label.configure(text=f"{self.time[0]}:{self.time[1]}")
            print(self.time)
        except:
            messagebox.showinfo("Error", f"Ongeldige tijd", icon='warning')

    def setDate(self):
        """
        Verandert de datum van het systeem naar input van de gebruiker.
        :return: None
        """
        res = self.date_entry.get()
        try:
            res2 = res.split("/")
            self.date = [int(item) for item in res2]
            self.date_label.configure(text=f"{self.date[0]}/{self.date[1]}/{self.date[2]}")
            print(self.date)
        except:
            messagebox.showinfo("Error", f"Ongeldige datum", icon='warning')


class DataFrame(tk.Frame):
    """
    Initpagina
    bevat:
        zaalknop
        filmknop
        vertoningknop
        gebruikerknop
        reservatieknop
    """
    def __init__(self, parent, sys, time, date):
        tk.Frame.__init__(self, parent)
        self.sys = sys
        self.time = time
        self.date = date
        # tk.Label(self, text="Dit is de initpagina",
        #          font=("Arial Bold", 20)).pack(side="top", fill="x", pady=10)

        tk.Button(self, text="Zalen", command=lambda: parent.switchFrame(ZalenFrame)).pack(pady=10)
        tk.Button(self, text="Films", command=lambda: parent.switchFrame(FilmsFrame)).pack(pady=10)
        tk.Button(self, text="Vertoningen", command=lambda: parent.switchFrame(VertoningenFrame)).pack(pady=10)
        tk.Button(self, text="Gebruikers", command=lambda: parent.switchFrame(GebruikersFrame)).pack(pady=10)

        tk.Button(self, text="Terug", command=lambda: parent.switchFrame(StartFrame)).pack(pady=10)


class ZalenFrame(tk.Frame):
    def __init__(self, parent, sys, time, date):
        tk.Frame.__init__(self, parent)
        self.sys = sys
        self.time = time
        self.date = date
        self.zalen_lijst = scrolledtext.ScrolledText(self, width=80, height=20)
        self.zalen_lijst.pack(pady=10)
        self.updateZalenLijst()
        tk.Button(self, text="Zaal toevoegen", command=lambda: parent.switchFrame(AddZaalFrame)).pack(pady=10)
        tk.Button(self, text="Terug", command=lambda: parent.switchFrame(DataFrame)).pack(pady=10)

    def updateZalenLijst(self):
        """
        Toon alle zalen op het scherm
        :return: None
        """
        temp_list = []
        self.sys.zalen.traverseTable(temp_list.append)
        self.zalen_lijst.insert(tk.INSERT, "zaalnummer \tplaatsen")
        for zaal_nummer in temp_list:
            zaal = self.sys.zalen.tableRetrieve(zaal_nummer)[0]
            self.zalen_lijst.insert(tk.INSERT, f"\n{zaal_nummer}\t    {zaal.seats}")

        self.zalen_lijst.configure(state="disabled")


class AddZaalFrame(tk.Frame):
    def __init__(self, parent, sys, time, date):
        tk.Frame.__init__(self, parent)
        self.sys = sys
        self.time = time
        self.date = date

        tk.Label(self, text="Zaalnummer").pack(side="top", pady=10)
        self.zaalnummer_entry = tk.Entry(self, width=25)
        self.zaalnummer_entry.pack()

        tk.Label(self, text="Aantal plaatsen").pack(side="top", pady=10)
        self.seats_entry = tk.Entry(self, width=25)
        self.seats_entry.pack()

        tk.Button(self, text="Toevoegen", command=lambda: self.addZaal()).pack(pady=10)
        tk.Button(self, text="Terug", command=lambda: parent.switchFrame(ZalenFrame)).pack(pady=10)

    def addZaal(self):
        """
        Voegt een zaal toe aan het systeem.
        :return: None
        """
        try:
            zaalnummer = int(self.zaalnummer_entry.get())
        except:
            messagebox.showinfo("Error", "Ongeldige zaalnummer", icon='warning')
            return

        try:
            seats = int(self.seats_entry.get())
        except:
            messagebox.showinfo("Error", "Ongeldige seats", icon='warning')
            return

        self.sys.addZaal(zaalnummer, seats)
        messagebox.showinfo("Info", "Zaal toegevoegd!")


class FilmsFrame(tk.Frame):
    def __init__(self, parent, sys, time, date):
        tk.Frame.__init__(self, parent)
        self.sys = sys
        self.time = time
        self.date = date
        self.films_lijst = scrolledtext.ScrolledText(self, width=80, height=20)
        self.films_lijst.pack(pady=10)
        self.updateFilmsLijst()
        tk.Button(self, text="Film toevoegen", command=lambda: parent.switchFrame(AddFilmFrame)).pack(pady=10)
        tk.Button(self, text="Terug", command=lambda: parent.switchFrame(DataFrame)).pack(pady=10)

    def updateFilmsLijst(self):
        """
        Toon alle films op het scherm
        :return: None
        """
        temp_list = []
        self.sys.films.traverseTable(temp_list.append)
        self.films_lijst.insert(tk.INSERT, "id \ttitel \t\trating")
        for film_id in temp_list:
            film = self.sys.films.tableRetrieve(film_id)[0]
            self.films_lijst.insert(tk.INSERT, f"\n{film_id}\t{film.titel}\t\t{film.rating}")

        self.films_lijst.configure(state="disabled")


class AddFilmFrame(tk.Frame):
    def __init__(self, parent, sys, time, date):
        tk.Frame.__init__(self, parent)
        self.sys = sys
        self.time = time
        self.date = date

        tk.Label(self, text="Titel").pack(side="top", pady=10)
        self.titel_entry = tk.Entry(self, width=25)
        self.titel_entry.pack()

        tk.Label(self, text="Rating").pack(side="top", pady=10)
        self.rating_entry = tk.Entry(self, width=25)
        self.rating_entry.pack()

        tk.Button(self, text="Toevoegen", command=lambda: self.addFilm()).pack(pady=10)
        tk.Button(self, text="Terug", command=lambda: parent.switchFrame(FilmsFrame)).pack(pady=10)

    def addFilm(self):
        """
        Voegt een film toe aan het systeem.
        :return: None
        """
        # genereer een id voor de film
        film_id = self.sys.films.tableLength() + 1
        while True:
            if not self.sys.films.tableRetrieve(film_id)[1]:
                break
            film_id += 1

        film_titel = self.titel_entry.get()

        try:
            film_rating = float(self.rating_entry.get())
        except:
            messagebox.showinfo("Error", "Ongeldige filmrating", icon='warning')
            return

        if not film_titel:
            messagebox.showinfo("Error", "Lege titel", icon='warning')
            return

        self.sys.addFilm(film_id, film_titel, film_rating)
        messagebox.showinfo("Info", "Film toegevoegd!")


class VertoningenFrame(tk.Frame):
    def __init__(self, parent, sys, time, date):
        tk.Frame.__init__(self, parent)
        self.sys = sys
        self.time = time
        self.date = date
        self.vertoningen_lijst = scrolledtext.ScrolledText(self, width=80, height=20)
        self.vertoningen_lijst.pack(pady=10)
        self.updateVertoningenLijst()
        tk.Button(self, text="Vertoning toevoegen", command=lambda: parent.switchFrame(AddVertoningFrame)).pack(pady=10)
        tk.Button(self, text="Terug", command=lambda: parent.switchFrame(DataFrame)).pack(pady=10)

    def updateVertoningenLijst(self):
        """
        Toon alle vertoningen op het scherm
        :return: None
        """
        temp_list = []
        self.sys.vertoningen.traverseTable(temp_list.append)
        self.vertoningen_lijst.insert(tk.INSERT, "id\tzaal\tfilm\tslot\tdatum\t\tplaatsen " +
                                      "\taanwezig\tgestart")
        for vertoning_id in temp_list:
            vert = self.sys.vertoningen.tableRetrieve(vertoning_id)[0]
            self.vertoningen_lijst.insert(tk.INSERT, f"\n{vertoning_id}\t{vert.zaalnummer}\t{vert.film_id}" +
                                          f"\t{vert.sloten[vert.timeslot]}\t{vert.datum}" +
                                          f"\t\t{vert.aantal_vrije_plaatsen}\t  {vert.aanwezig}\t   {vert.gestart}")

        self.vertoningen_lijst.configure(state="disabled")


class AddVertoningFrame(tk.Frame):
    def __init__(self, parent, sys, time, date):
        tk.Frame.__init__(self, parent)
        self.sys = sys
        self.time = time
        self.date = date

        # zaal combobox
        tk.Label(self, text="Zaal").pack(side="top", pady=10)
        self.zaal_entry = Combobox(self)
        temp_list = []
        self.sys.zalen.traverseTable(temp_list.append)
        self.zaal_entry['values'] = temp_list
        self.zaal_entry.pack()

        # film combobox
        tk.Label(self, text="Film").pack(side="top", pady=10)
        self.film_entry = Combobox(self)
        temp_list = []
        self.sys.films.traverseTable(temp_list.append)
        temp_list2 = []
        self.film_dict = {}
        for film_id in temp_list:
            temp_list2.append(self.sys.films.tableRetrieve(film_id)[0].titel)
            self.film_dict[self.sys.films.tableRetrieve(film_id)[0].titel] = film_id
        self.film_entry['values'] = temp_list2
        self.film_entry.pack()

        # slot combobox
        tk.Label(self, text="slot").pack(side="top", pady=10)
        self.slot_entry = Combobox(self)
        self.slot_entry['values'] = Vertoning.sloten
        self.slot_entry.pack()

        # datum tekstbox
        tk.Label(self, text="Datum (yyyy-mm-dd)").pack(side="top", pady=10)
        self.date_entry = tk.Entry(self, width=25)
        self.date_entry.pack()

        tk.Button(self, text="Toevoegen", command=lambda: self.addVertoning()).pack(pady=10)
        tk.Button(self, text="Terug", command=lambda: parent.switchFrame(VertoningenFrame)).pack(pady=10)

    def addVertoning(self):
        """
        Voegt een vertoning toe aan het systeem.
        :return: None
        """
        # genereer een id voor de vertoning
        vertoning_id = self.sys.vertoningen.tableLength() + 1
        while True:
            if not self.sys.vertoningen.tableRetrieve(vertoning_id)[1]:
                break
            vertoning_id += 1

        vert_zaal = int(self.zaal_entry.get())
        vert_film = self.film_dict[self.film_entry.get()]
        vert_slot = Vertoning.sloten.index(self.slot_entry.get())
        vert_datum = self.date_entry.get()
        vert_plaatsen = self.sys.zalen.tableRetrieve(vert_zaal)[0].seats

        if not vert_datum:
            messagebox.showinfo("Error", "Lege datum", icon='warning')

        self.sys.addVertoning(vertoning_id, vert_zaal, vert_film, vert_slot, vert_datum, vert_plaatsen)
        messagebox.showinfo("Info", "Vertoning toegevoegd!")


class GebruikersFrame(tk.Frame):
    def __init__(self, parent, sys, time, date):
        tk.Frame.__init__(self, parent)
        self.sys = sys
        self.time = time
        self.date = date
        self.gebruikers_lijst = scrolledtext.ScrolledText(self, width=80, height=20)
        self.gebruikers_lijst.pack(pady=10)
        self.updateGebruikersLijst()
        tk.Button(self, text="Gebruiker toevoegen", command=lambda: parent.switchFrame(AddGebruikerFrame)).pack(pady=10)
        tk.Button(self, text="Terug", command=lambda: parent.switchFrame(DataFrame)).pack(pady=10)

    def updateGebruikersLijst(self):
        """
        Toon alle gebruikers op het scherm
        :return: None
        """
        temp_list = []
        self.sys.gebruikers.traverseTable(temp_list.append)
        self.gebruikers_lijst.insert(tk.INSERT, "id\tvoornaam\t\tachternaam\t\temail")
        for gebruiker_id in temp_list:
            gebruiker = self.sys.gebruikers.tableRetrieve(gebruiker_id)[0]
            self.gebruikers_lijst.insert(tk.INSERT, f"\n{gebruiker_id}\t{gebruiker.firstname}\t\t" +
                                         f"{gebruiker.surname}\t\t{gebruiker.email}")

        self.gebruikers_lijst.configure(state="disabled")


class AddGebruikerFrame(tk.Frame):
    def __init__(self, parent, sys, time, date):
        tk.Frame.__init__(self, parent)
        self.sys = sys
        self.time = time
        self.date = date

        tk.Label(self, text="Voornaam").pack(side="top", pady=10)
        self.firstname_entry = tk.Entry(self, width=25)
        self.firstname_entry.pack()

        tk.Label(self, text="Achternaam").pack(side="top", pady=10)
        self.surname_entry = tk.Entry(self, width=25)
        self.surname_entry.pack()

        tk.Label(self, text="Email").pack(side="top", pady=10)
        self.email_entry = tk.Entry(self, width=25)
        self.email_entry.pack()

        tk.Button(self, text="Toevoegen", command=lambda: self.addGebruiker()).pack(pady=10)
        tk.Button(self, text="Terug", command=lambda: parent.switchFrame(GebruikersFrame)).pack(pady=10)

    def addGebruiker(self):
        """
        Voegt een gebruiker toe aan het systeem.
        :return: None
        """
        # genereer een id voor de gebruiker
        gebruiker_id = self.sys.gebruikers.tableLength() + 1
        while True:
            if not self.sys.gebruikers.tableRetrieve(gebruiker_id)[1]:
                break
            gebruiker_id += 1

        if not self.firstname_entry.get() or not self.surname_entry.get() or not self.email_entry.get():
            messagebox.showinfo("Error", "Leeg veld", icon='warning')
            
        self.sys.addGebruiker(gebruiker_id, self.firstname_entry.get(), self.surname_entry.get(), self.email_entry.get())
        messagebox.showinfo("Info", "Gebruiker toegevoegd!")


class AddReservatieFrame(tk.Frame):
    def __init__(self, parent, sys, time, date):
        tk.Frame.__init__(self, parent)
        self.sys = sys
        self.time = time
        self.date = date

        self.vertoning_dict = {}

        # gebruiker combobox
        tk.Label(self, text="Gebruiker").pack(side="top", pady=10)
        self.gebruiker_entry = Combobox(self)
        temp_list = []
        self.sys.gebruikers.traverseTable(temp_list.append)
        temp_list2 = []
        self.gebruiker_dict = {}
        for gebruiker_id in temp_list:
            gebruiker = self.sys.gebruikers.tableRetrieve(gebruiker_id)[0]
            naam = gebruiker.firstname + " " + gebruiker.surname
            temp_list2.append(naam)
            self.gebruiker_dict[naam] = gebruiker_id
        self.gebruiker_entry['values'] = temp_list2
        self.gebruiker_entry.pack()

        # film combobox
        tk.Label(self, text="Film").pack(side="top", pady=10)
        self.film_entry = Combobox(self)
        temp_list = []
        self.sys.films.traverseTable(temp_list.append)
        temp_list2 = []
        self.film_dict = {}
        for film_id in temp_list:
            temp_list2.append(self.sys.films.tableRetrieve(film_id)[0].titel)
            self.film_dict[self.sys.films.tableRetrieve(film_id)[0].titel] = film_id
        self.film_entry['values'] = temp_list2
        self.film_entry.bind("<<ComboboxSelected>>", self.vertoningBoxUpdate)
        self.film_entry.pack()

        # Toon mogelijke datum tijd van vertoningen
        tk.Label(self, text="Vertoning").pack(side="top", pady=10)
        self.vertoning_entry = Combobox(self)
        self.vertoning_entry.pack()

        # plaatsen gereserveerd
        tk.Label(self, text="Aantal plaatsen").pack(side="top", pady=10)
        self.plaatsen_entry = tk.Entry(self, width=25)
        self.plaatsen_entry.pack()

        tk.Button(self, text="Toevoegen", command=lambda: self.addReservatie()).pack(pady=10)
        tk.Button(self, text="Terug", command=lambda: parent.switchFrame(StartFrame)).pack(pady=10)

    def vertoningBoxUpdate(self, event_object):
        # print(self.film_dict[self.film_entry.get()])
        # print(event_object)
        film_id = self.film_dict[self.film_entry.get()]
        temp_list = []
        vertoningen = self.sys.films.tableRetrieve(film_id)[0].vertoningen

        for vertoning_id in vertoningen:
            vertoning = self.sys.vertoningen.tableRetrieve(vertoning_id)[0]
            temp_list.append(f"{vertoning.datum}   {Vertoning.sloten[vertoning.timeslot]}")
            self.vertoning_dict[f"{vertoning.datum}   {Vertoning.sloten[vertoning.timeslot]}"] = vertoning_id
        self.vertoning_entry['values'] = temp_list

    def addReservatie(self):
        """
        Voegt een reservatie toe aan het systeem.
        :return: None
        """
        try:
            plaatsen = int(self.plaatsen_entry.get())
        except:
            messagebox.showinfo("Error", "Ongeldig aantal plaatsen", icon='warning')
            return

        self.sys.addReservatie(self.gebruiker_dict[self.gebruiker_entry.get()],
                               self.vertoning_dict[self.vertoning_entry.get()],
                               plaatsen, f"{self.time[0]}:{self.time[1]}",
                               f"{self.date[2]}-{self.date[1]}-{self.date[0]}")

        self.sys.updateReservaties()

        messagebox.showinfo("Info", "Reservatie toegevoegd!")


class UpdateAanwezigenFrame(tk.Frame):
    def __init__(self, parent, sys, time, date):
        tk.Frame.__init__(self, parent)
        self.sys = sys
        self.time = time
        self.date = date

        temp_list = []
        self.sys.vertoningen.traverseTable(temp_list.append)

        self.vertoning_dict = {}

        tk.Label(self, text="Vertoning").pack(side="top", pady=10)
        self.vertoning_entry = Combobox(self)
        self.vertoning_entry.pack()

        temp_list2 = []
        for vertoning_id in temp_list:
            vertoning = self.sys.vertoningen.tableRetrieve(vertoning_id)[0]
            temp_list2.append(f"{vertoning.datum}   {Vertoning.sloten[vertoning.timeslot]}")
            self.vertoning_dict[f"{vertoning.datum}   {Vertoning.sloten[vertoning.timeslot]}"] = vertoning_id
        self.vertoning_entry['values'] = temp_list2

        # aanwezigen
        tk.Label(self, text="Aantal aanwezigen").pack(side="top", pady=10)
        self.aanwezigen_entry = tk.Entry(self, width=25)
        self.aanwezigen_entry.pack()

        tk.Button(self, text="Update", command=lambda: self.updateAanwezigen()).pack(pady=10)
        tk.Button(self, text="Terug", command=lambda: parent.switchFrame(StartFrame)).pack(pady=10)

    def updateAanwezigen(self):
        """
        Update aantal aanwezige mensen in zaal.
        :return: None
        """
        try:
            aantal_aanwezigen = int(self.aanwezigen_entry.get())
        except:
            messagebox.showinfo("Error", "Ongeldig aantal aanwezigen", icon='warning')
            return

        self.sys.updateAanwezigen(self.vertoning_dict[self.vertoning_entry.get()],
                                  aantal_aanwezigen)
        messagebox.showinfo("Info", "Aantal aanwezigen geüpdatet!")


if __name__ == "__main__":
    program = ReservatiesysteemInterface()
