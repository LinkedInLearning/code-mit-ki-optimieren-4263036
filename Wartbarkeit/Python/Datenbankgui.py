import tkinter as tk
from tkinter import messagebox
import sqlite3
import os

class Database:
    def __init__(self):
        self.db_file = 'sqldb.db'
    
    def initialize(self):
        if not os.path.exists(self.db_file):
            connection = sqlite3.connect(self.db_file)
            cursor = connection.cursor()
            cursor.execute('''CREATE TABLE personen(name TEXT, vorname TEXT)''')
            connection.close()
            return "Datenbank erstellt"
        else:
            return "Datenbank vorhanden"
    
    def read(self):
        db_string = ""
        counter = 0
        if os.path.exists(self.db_file):
            connection = sqlite3.connect(self.db_file)
            cursor = connection.cursor()
            cursor.execute('''SELECT * FROM personen''')
            rows = cursor.fetchall()
            for row in rows:
                counter += 1
                db_string += row[0] + ", " + row[1] + "\n"
            connection.close()
            return db_string, str(counter)
        else:
            return "Datenbank nicht vorhanden"
    
    def write(self, n, v):
        if os.path.exists(self.db_file):
            connection = sqlite3.connect(self.db_file)
            cursor = connection.cursor()
            cursor.execute('''INSERT INTO personen VALUES (?, ?)''', (n, v))
            connection.commit()
            connection.close()
            return "Daten geschrieben: " + n + ", " + v
        else:
            return "Datenbank nicht vorhanden"

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.grid(padx=20, pady=20)
        self.create_widgets()
        
    def create_widgets(self):
        tk.Label(self, text="Personendatenbank").grid(row=0, column=0)
        tk.Label(self, text="").grid(row=0, column=1)
        tk.Label(self, text="Nachname").grid(row=1)
        tk.Label(self, text="Vorname").grid(row=2)

        self.nname = tk.Entry(self)
        self.vname = tk.Entry(self)
        self.nname.grid(row=1, column=1)
        self.vname.grid(row=2, column=1)
        
        tk.Button(self, text='Eintrag DB', width=20, command=self.handle_entry).grid(row=3, column=0, sticky=tk.W, pady=4)
        tk.Button(self, text='Ende', width=20, command=self.master.destroy).grid(row=3, column=1, sticky=tk.W, pady=4)

        self.anzeige = tk.Text(self, height=4, width=40)
        self.anzeige.grid(row=4, columnspan=2)
        self.anzeige.configure(state='disabled')
        
        self.status = tk.Label(self, text="")
        self.status.grid(row=5, columnspan=2)

        self.datensaetze = tk.Label(self, text="")
        self.datensaetze.grid(row=6, columnspan=2)

        menu_bar = tk.Menu(self.master)
        self.master.config(menu=menu_bar)
        
        file_menu = tk.Menu(menu_bar)
        file_menu.add_command(label="Öffnen", command=self.master.destroy)
        file_menu.add_command(label="Exit", command=self.master.destroy)
        
        help_menu = tk.Menu(menu_bar)
        help_menu.add_command(label="About...", command=self.master.destroy)
        
        menu_bar.add_cascade(label="File", menu=file_menu)
        menu_bar.add_cascade(label="Hilfe", menu=help_menu)

        self.initialize_db()
        self.update_display()

    def initialize_db(self):
        db = Database()
        self.status['text'] = db.initialize()
    
    def update_display(self):
        db = Database()
        result = db.read()
        self.anzeige.configure(state='normal')
        self.anzeige.delete('1.0', tk.END)
        self.anzeige.insert(tk.END, result[0])
        self.anzeige.configure(state='disabled')
        self.datensaetze['text'] = "Anzahl Datensätze: " + result[1]
    
    def handle_entry(self):
        nn = self.nname.get()
        vn = self.vname.get()
        if nn == "" or vn == "":
            messagebox.showwarning('Fehler beim Speichern', 'Beide Felder müssen gefüllt werden.')
            return
        db = Database()
        self.status['text'] = db.write(nn, vn)
        self.update_display()

if __name__ == "__main__":
    root = tk.Tk()
    app = Application(master=root)
    app.mainloop()
