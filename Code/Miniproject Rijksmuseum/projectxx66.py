from tkinter import *
from tkinter import messagebox
import Jsonfiles
import json

ingelogd = ""
listboxplaceholder = Listbox()

#functies

def login_galerij(naam, wachtwoord):
    '''checkt of de gallerijhouder bestaat, en de juiste inloggegevens heeft. Data word uit een .json gehaald.'''
    galerijdata = Jsonfiles.get_galerijdata()
    for galerij in galerijdata['Gallerijhouders']:
        if galerij['Gebruikersnaam'] == naam and galerij['Wachtwoord'] == wachtwoord:
            global ingelogd
            ingelogd = naam
            raise_frame(houder)

'''Leent een beschikbaar item uit aan een galerijhouder, en zet deze daarna op uitgeleend.'''
def leen_item(kunststuk, listbox):
    galerijdata = Jsonfiles.get_galerijdata()
    for galerij in galerijdata['Gallerijhouders']:
        if galerij['Gebruikersnaam'] == ingelogd:
            galerij['Kunst'].append(kunststuk)
            galerijdata = json.dumps(galerijdata,indent=2)
            with open('galleries.json','w') as f:
                f.writelines(galerijdata)
            kunstdata = Jsonfiles.get_kunstdata()
            for item in kunstdata:
                if item['Naam'] == kunststuk:
                    item['Available'] = False
            with open('KunstUitleen.json','w') as f:
                kunstdata = json.dumps(kunstdata,indent=2)
                f.writelines(kunstdata)
            listbox.delete(0, END)
            for kunstwerk in Jsonfiles.get_kunstdata():
                if kunstwerk['Available'] == True:
                    listbox.insert(END, kunstwerk['Naam'])
            messagebox.showinfo("Success!","Het lenen is gelukt!")

def get_geleende_items(listbox,gebruiker):
    listbox.delete(0,END)
    galerijdata = Jsonfiles.get_galerijdata()
    for galerij in galerijdata["Gallerijhouders"]:
        if gebruiker == galerij["Gebruikersnaam"]:
            for kunststuk in galerij["Kunst"]:
                listbox.insert(END, kunststuk)


'''logt de gebruiker in. checkt enkel op een 'valide' mailadres.'''
def login_gebruiker(email):
    global ingelogd
    persoondata = Jsonfiles.get_persoondata()
    for persoon in persoondata["Persoonsgegevens"]:
        if email == persoon['Email']:
            ingelogd = email
            raise_frame(gebruiker)
            return
    if '@' in email and ('.com' or '.nl' in email):
        ingelogd = email
        persoondata["Persoonsgegevens"].append({"Naam" : "", "Email": email, "Kunststukken": []})
        with open ('persoonsgegevens.json', 'w') as f:
            persoondata = json.dumps(persoondata,indent=2)
            f.writelines(persoondata)
        raise_frame(gebruiker)
    else:
        messagebox.showinfo("Helaas","Dit is geen geldig mailadres. Probeer het nog eens!")
    
def get_ticket(kunststuk,gebruiker):
    gebruikers = Jsonfiles.get_persoondata()
    for persoongegevens in gebruikers["Persoonsgegevens"]:
        if persoongegevens["Email"] == gebruiker:
            persoongegevens["Kunststukken"].append(kunststuk)
            gebruikers = json.dumps(gebruikers, indent=2)
            with open("persoonsgegevens.json", "w") as file:
                file.writelines(gebruikers)

#Framework
def raise_frame(frame):
    frame.tkraise()

root = Tk()


main = Frame(root)
inloghouder = Frame(root)
inloggebruiker = Frame(root)
gebruiker = Frame(root)
houder = Frame(root)
nietgeleend = Frame(root)
geleend = Frame(root)
bezoekers = Frame(root)
controle = Frame(root)
selectie = Frame(root)
ticketscherm = Frame(root)

"""Hier loopt hij door de frames heen die er zijn."""

for frame in(main, inloghouder, inloggebruiker, gebruiker, houder, nietgeleend, geleend, bezoekers, controle, selectie, ticketscherm):
    frame.grid(row=0, column=0, sticky='news')


#mainscreen
"""Het hoofdscherm met buttons om te kiezen tussen gebruiker of galeriehouder."""


Label(main, text='').grid(row=0, column=1, pady=20)
Label(main, text='Maak een keuze:').grid(row=1, column=3, padx=125, pady=10)
Label(main, text='').grid(row=2, column=1)
Button(main, text='Galeriehouder', command=lambda: raise_frame(inloghouder)).grid(row=3, column=3)
Label(main, text='').grid(row=4, column=2)
Button(main, text='Gebruiker', command=lambda: raise_frame(inloggebruiker)).grid(row=5, column=3)


#inloggen gebruiker
"""Invoeren van de gegevens van de gebruiker."""

e1 = Entry(inloggebruiker)
e2 = Entry(inloggebruiker)

e1.grid(row=3,column=7)
e2.grid(row=4,column=7)

Label(inloggebruiker, text='').grid(row=0, column=1, pady=20)
Label(inloggebruiker, text= 'Voer uw gegevens in:').grid(row=1, column=7, padx=50, pady=10)
Label(inloggebruiker, text= '').grid(row=2,column=3)
Label(inloggebruiker, text= 'Naam').grid(row=3,column=5)
Label(inloggebruiker, text= 'Email adres').grid(row=4,column=5)
Label(inloggebruiker, text= '').grid(row=5,column=3)
Button(inloggebruiker, text='Login', command= lambda: login_gebruiker(e2.get())).grid(row=6,column=7)

Label(inloggebruiker, text= '').grid(row=7,column=3)
Button(inloggebruiker, text= 'Terug', command= lambda: raise_frame(main)).grid(row=8, column=7)

#inloggen galeriehouder
"""Invoer van de inloggegevens van de galeriehouder."""
e3 = Entry(inloghouder)
e4 = Entry(inloghouder)

e3.grid(row=3, column=7)
e4.grid(row=4, column=7)

Label(inloghouder, text='').grid(row=0, column=1, pady=20)
Label(inloghouder, text= 'Voer uw gegevens in:').grid(row=1, column=7, padx=50, pady=10)
Label(inloghouder, text= '').grid(row=2,column=3)
Label(inloghouder, text= 'Naam').grid(row=3,column=5)
Label(inloghouder, text= 'Wachtwoord').grid(row=4,column=5)
Label(inloghouder, text= '').grid(row=5,column=3)
Button(inloghouder, text='Login', command= lambda:  login_galerij(e3.get(),e4.get())).grid(row=6, column=7)

Label(inloghouder, text= '').grid(row=7,column=3)
Button(inloghouder, text= 'Terug', command= lambda: raise_frame(main)).grid(row=8, column=7)

#gebruiker
"""Het keuze scherm van de gebruiker."""

Label(gebruiker, text='').grid(row=0, column=1, pady=20)
Label(gebruiker, text= 'Maak een keuze:').grid(row=1, column=3, padx=125, pady=10)
Label(gebruiker, text='').grid(row =2, column=2)
Button(gebruiker, text= 'Kunststuk selectie', command= lambda: raise_frame(selectie)).grid(row=3, column=3)
Label(gebruiker, text='').grid(row=4, column=1)
Button(gebruiker, text= 'Ticket scherm', command= lambda: raise_frame(ticketscherm)).grid(row=5, column=3)
Label(gebruiker, text='').grid(row=6, column=3, pady=10)

Button(gebruiker, text= 'Terug', command= lambda: raise_frame(main)).grid(row=7, column=3)

#selectie
"""Hier kan de bezoeker een kunststuk selecteren en mogelijk alvast een voorbeeld van zien"""

Label(selectie, text='Selecteren van een kunststuk:').pack(pady=20)
scrollbar = Scrollbar(selectie)
scrollbar.pack(side=RIGHT, fill=Y)

mylist3 = Listbox(selectie, yscrollcommand = scrollbar.set )
for kunstwerk in Jsonfiles.get_kunstdata():
    mylist3.insert(END, kunstwerk['Naam'])

mylist3.pack(expand=1, fill=BOTH)
scrollbar.config( command = mylist3.yview )

Button(selectie, text= 'Bekijk').pack(side=LEFT, pady=5)
Button(selectie, text= 'Selecteren', command=lambda: get_ticket(mylist3.get(mylist3.curselection()),ingelogd)).pack(side=RIGHT, pady=5)
#Button(nietgeleend, text= 'Lenen', command= lambda: leen_item(mylist.get(mylist.curselection()))).pack(pady=5)
Label(selectie, text='').pack(fill=X)
Button(selectie, text= 'Terug', command= lambda: raise_frame(gebruiker)).pack()
selectmode = SINGLE

#ticketscherm

Label(ticketscherm, text='').grid(row=0, column=1, pady=15)
Label(ticketscherm, text='naam').grid(row=1, column=3, padx=150)                           #hier moet ingevoerde naam inkomen
Label(ticketscherm, text='').grid(row=2, column=2)
Label(ticketscherm, text='code').grid(row=3, column=3, pady=10)                           #hier moet de code komen
Label(ticketscherm, text='').grid(row=4, column=0)
Label(ticketscherm, text='Geselecteerde kunststuk:').grid(row=5, column=3)
Label(ticketscherm, text='').grid(row=6, column=3)
Label(ticketscherm, text='naam kunststuk').grid(row=7, column=3)                                    #hier moet de naam van het kunststuk komen


Label(ticketscherm, text='').grid(row=8, column=3, pady=10)
Button(ticketscherm, text= 'Terug', command= lambda: raise_frame(gebruiker)).grid(row=9, column=3)

#galeriehouder
"""Het keuzemenu van de galeriehouder."""

def imBadAtNames(geleend, listbox, gebruiker):
    raise_frame(geleend)
    get_geleende_items(listbox, gebruiker)

Label(houder, text='').grid(row=0, column=1)
Label(houder, text= 'Maak een keuze:').grid(row=1, column=3, padx=125, pady=10)
Label(houder, text='').grid(row=2, column=2)
Button(houder, text= 'Overzicht niet geleende kunststukken', command= lambda: raise_frame(nietgeleend)).grid(row=3, column=3)
Label(houder, text='').grid(row=4, column=2)
#Button(houder, text= 'Overzicht geleende kunststukken', command= lambda: raise_frame(geleend)).grid(row=5, column=3)
Button(houder, text= 'Overzicht geleende kunststukken', command= lambda: imBadAtNames(geleend, listboxplaceholder, ingelogd)).grid(row=5, column=3)
#Button(houder, text= 'Overzicht geleende kunststukken', command= lambda: raise_frame(geleend)).grid(row=5, column=3)
Label(houder, text='').grid(row=6, column=2)
Button(houder, text= 'Overzicht van bezoekers',command= lambda: raise_frame(bezoekers)).grid(row=7, column=3)
Label(houder, text='').grid(row=8, column=2)
Button(houder, text= 'Ticketnummer controle', command= lambda: raise_frame(controle)).grid(row=9, column=3)
Label(houder, text='').grid(row=10, column=2, pady=10)
Button(houder, text= 'Terug', command= lambda: raise_frame(main)).grid(row= 11, column=3)


#nietgeleend
"""Overzicht van alle niet geleende kunststukken, mogelijkheid tot lenen."""

Label(nietgeleend, text='Overzicht niet geleende kunststukken:').pack(pady=20)
scrollbar = Scrollbar(nietgeleend)
scrollbar.pack(side=RIGHT, fill=Y)

mylist = Listbox(nietgeleend, yscrollcommand = scrollbar.set )
for kunstwerk in Jsonfiles.get_kunstdata():
    if kunstwerk['Available'] == True:
        mylist.insert(END, kunstwerk['Naam'])

mylist.pack(expand=1, fill=BOTH)
scrollbar.config( command = mylist.yview )

Button(nietgeleend, text= 'Lenen', command= lambda: leen_item(mylist.get(mylist.curselection()),mylist)).pack(pady=5)
Button(nietgeleend, text= 'Terug', command= lambda: raise_frame(houder)).pack(pady=5)
selectmode = SINGLE

#geleend
"""Overzicht van alle geleende kunststukken."""

Label(geleend, text='Overzicht geleende kunststukken:').pack(pady=20)
scrollbar = Scrollbar(geleend)
scrollbar.pack(side=RIGHT, fill=Y)

mylist2 = listboxplaceholder
#mylist2 = Listbox(geleend, yscrollcommand = scrollbar.set )

get_geleende_items(mylist2,ingelogd)

mylist2.pack(expand=1, fill=BOTH)
scrollbar.config( command = mylist2.yview )

Button(geleend, text= 'Terug', command= lambda: raise_frame(houder)).pack(pady=10)
selectmode = SINGLE

#bezoekers
"""Overzicht van alle bezoekers."""

Label(bezoekers, text='Overzicht van bezoekers:').pack(pady=20)
scrollbar = Scrollbar(bezoekers)
scrollbar.pack(side=RIGHT, fill=Y)

listbox= Listbox(bezoekers)
listbox.pack(expand=1, fill=BOTH)

for i in range(1001):                  #ToDo hier moet len van de lijst zijn, dus eerst regels opvragen
    listbox.insert(END, i)

listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=listbox.yview)

Button(bezoekers, text= 'Terug', command= lambda: raise_frame(houder)).pack(pady=10)


#controle
"""Hier kunnen de afgegeven codes van het ticketscherm worden gecontroleerd."""

Label(controle, text= '').grid(row=1, column=0, pady=20)
Label(controle, text='Voer hier de code in:').grid(row=2, column=3, padx=125, pady=10)
e1 = Entry(controle)
e1.grid(row=3, column=3)
Label(controle, text= '').grid(row=4, column=0)
Button(controle, text='Check').grid(row=5, column=3)

Label(controle, text= '').grid(row=6, column=0)
Button(controle, text= 'Terug', command= lambda: raise_frame(houder)).grid(row=7, column=3)


root.title('')
root.geometry('360x360')
raise_frame(main)
root.mainloop()

