from rjs.datenbank import *
from tkinter import *
from tkinter import messagebox

class Application(Frame):
   
    def __init__(self,master=None):
        Frame.__init__(self, master)
        self.grid(padx=20, pady=20)
        Label(master,text="Personendatenbank").grid(row=0,column=0)
        Label(master,text="").grid(row=0,column=1)
        
        Label(master,text="Nachname").grid(row=1)
        Label(master,text="Vorname").grid(row=2)

        self.nname = Entry(master)
        self.vname = Entry(master)
        Button(master,text='Eintrag DB',width=20,command=self.action).grid(
            row=3, column=0, sticky=W, pady=4)

        Button(master,text='Ende',width=20,command=self.ende).grid(
            row=3, column=1, sticky=W, pady=4)

        self.nname.grid(row=1, column=1)
        self.vname.grid(row=2, column=1)
        self.anzeige = Text(master, height=4, width=40)
        self.status=Label(master,text="")
        self.status.grid(row=6, columnspan=2)

        menubar = Menu(self.master)
        self.master.config(menu=menubar)
        
        fileMenu = Menu(menubar)
        fileMenu.add_command(label="Öffnen", command=self.ende)
        fileMenu.add_command(label="Exit", command=self.ende)
        helpMenu = Menu(menubar)
        helpMenu.add_command(label="About...", command=self.ende)
        menubar.add_cascade(label="File", menu=fileMenu)
        menubar.add_cascade(label="Hilfe", menu=helpMenu)
        db = DB()

        self.status['text']=db.initDB()
        result = db.leseDB()
        self.anzeige.insert(END, result[0])
        self.anzeige.grid(row=4, columnspan=2)
        self.anzeige.configure(state='disabled')
        self.datensaetze=Label(master,text="")
        self.datensaetze.grid(row=5, columnspan=2)
        self.datensaetze['text'] = "Anzahl Datensätzer: " + result[1]
        
    def action(self):
        nn = self.nname.get()
        vn = self.vname.get()
        if nn == "" or vn == "":
            messagebox.showwarning('Fehler beim Speichern', 'Beide Felder müssen gefüllt werden.')
            return
        db = DB()
        self.status['text'] =""
        db.schreibDB(nn, vn)
        self.anzeige.configure(state='normal')
        result = db.leseDB()
        self.anzeige.delete(1.0,END)
        self.anzeige.insert(END, result[0])
        self.anzeige.configure(state='disabled')
        self.datensaetze['text'] = "Anzahl Datensätzer: " + result[1]
    def ende(self):
        if messagebox.askokcancel('Ende','Programm beenden?'):
            root.destroy()
  
root=Tk()
app=Application(master=root)
app.mainloop()

















