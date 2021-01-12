"""
Interface voor Reservatiesysteem.py

gebruikte bronnen:
https://likegeeks.com/python-gui-examples-tkinter-tutorial/
https://stackoverflow.com/questions/7546050/switch-between-two-frames-in-tkinter
https://riptutorial.com/tkinter/example/29713/grid--
https://en.wikipedia.org/wiki/Model%E2%80%93view%E2%80%93controller
"""
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
from Reservatiesysteem import Reservatiesysteem
from copy import deepcopy
import webbrowser
import os

# INSTELLINGEN
WIDTH = 500
HEIGHT = 500


class ReservatiesysteemInterface(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)

        # huidige frame
        self._frame = None

        # reservatiesysteem
        self.sys = Reservatiesysteem()
        self.time = [18, 0]
        self.date = [11, 1, 2021]

        # zet de windowsize en titel
        self.geometry(f"{WIDTH}x{HEIGHT}")
        self.title("Reservatiesysteem")

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
            for log in logs_succes[0]:
                filename = os.path.abspath(log)
                print(filename)
                webbrowser.open_new_tab(filename)

            messagebox.showinfo("Info", "Script werd succesvol verwerkt!")
        else:
            messagebox.showinfo("Error", "Script kon niet verwerkt worden", icon='warning')
            # Zet het oude reservatiesysteem terug
            self.sys = temp_sys
            return

        # ga terug naar de startpagina
        self.switchFrame(StartFrame)

    def reset(self):
        """
        Vraagt de gebruiker of dat die zeker is. Reset het reservatiesysteem en gaat terug naar de startpagina.
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
        tk.Button(self, text="Init", command=lambda: parent.switchFrame(InitFrame)).pack(pady=10)
        self.time_entry = tk.Entry(self, width=10)
        self.time_entry.pack()
        tk.Button(self, text="Zet tijd", command=lambda: self.setTime()).pack(pady=10)
        self.date_entry = tk.Entry(self, width=10)
        self.date_entry.pack()
        tk.Button(self, text="Zet datum", command=lambda: self.setDate()).pack(pady=10)
        tk.Button(self, text="Maak log", command=lambda: self.createLog()).pack(pady=10)

    def createLog(self):
        """
        Creëert een log en opent het in de standaard webbrowser.
        """
        log_succes = self.sys.createLog(f"{self.time[0]}:{self.time[1]}",
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
            self.time = res.split(":")
            self.time = [int(item) for item in self.time]
            print(self.time)
        except:
            messagebox.showinfo("Error", f"Geen geldige tijd", icon='warning')

    def setDate(self):
        """
        Verandert de datum van het systeem naar input van de gebruiker.
        :return: None
        """
        res = self.date_entry.get()
        try:
            self.date = res.split("/")
            self.date = [int(item) for item in self.date]
            print(self.date)
        except:
            messagebox.showinfo("Error", f"Geen geldige datum", icon='warning')


class InitFrame(tk.Frame):
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
        tk.Label(self, text="Dit is de initpagina",
                 font=("Arial Bold", 20)).pack(side="top", fill="x", pady=10)

        tk.Button(self, text="Zaal", command=lambda: parent.switchFrame(ZaalFrame)).pack()
        tk.Button(self, text="Film", command=lambda: parent.switchFrame(FilmFrame)).pack()
        tk.Button(self, text="Vertoning", command=lambda: parent.switchFrame(VertoningFrame)).pack()
        tk.Button(self, text="Gebruiker", command=lambda: parent.switchFrame(GebruikerFrame)).pack()
        tk.Button(self, text="Reservatie", command=lambda: parent.switchFrame(ReservatieFrame)).pack()

        tk.Button(self, text="terug", command=lambda: parent.switchFrame(StartFrame)).pack()


class ZaalFrame(tk.Frame):
    def __init__(self, parent, sys, time, date):
        tk.Frame.__init__(self, parent)
        self.sys = sys
        self.time = time
        self.date = date
        tk.Button(self, text="terug", command=lambda: parent.switchFrame(InitFrame)).pack()


class FilmFrame(tk.Frame):
    def __init__(self, parent, sys, time, date):
        tk.Frame.__init__(self, parent)
        self.sys = sys
        self.time = time
        self.date = date
        tk.Button(self, text="terug", command=lambda: parent.switchFrame(InitFrame)).pack()


class VertoningFrame(tk.Frame):
    def __init__(self, parent, sys, time, date):
        tk.Frame.__init__(self, parent)
        self.sys = sys
        self.time = time
        self.date = date
        tk.Button(self, text="terug", command=lambda: parent.switchFrame(InitFrame)).pack()


class GebruikerFrame(tk.Frame):
    def __init__(self, parent, sys, time, date):
        tk.Frame.__init__(self, parent)
        self.sys = sys
        self.time = time
        self.date = date
        tk.Button(self, text="terug", command=lambda: parent.switchFrame(InitFrame)).pack()


class ReservatieFrame(tk.Frame):
    def __init__(self, parent, sys, time, date):
        tk.Frame.__init__(self, parent)
        self.sys = sys
        self.time = time
        self.date = date
        tk.Button(self, text="terug", command=lambda: parent.switchFrame(InitFrame)).pack()


if __name__ == "__main__":
    program = ReservatiesysteemInterface()
