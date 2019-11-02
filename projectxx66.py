from tkinter import *
from tkinter import messagebox

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
Label(main, text='').grid(row=2, column=3)
Button(main, text='Galeriehouder', command=lambda: raise_frame(inloghouder)).grid(row=3, column=3)
Label(main, text='').grid(row=4, column=2)
Button(main, text='Gebruiker', command=lambda: raise_frame(inloggebruiker)).grid(row=5, column=3)


#inloggen gebruiker
"""Invoeren van de gegevens van de gebruiker."""

Label(inloggebruiker, text='').grid(row=0, column=1, pady=20)
Label(inloggebruiker, text= 'Voer uw gegeven in:').grid(row=1, column=7, padx=50, pady=10)
Label(inloggebruiker, text= '').grid(row=2,column=3)
Label(inloggebruiker, text= 'Email-adres').grid(row=3,column=5)
Label(inloggebruiker, text='').grid(row=4, column=1)
Button(inloggebruiker, text='Inloggen', command= lambda: raise_frame(gebruiker)).grid(row=5,column=7)


e2 = Entry(inloggebruiker)

e2.grid(row=3,column=7)

Label(inloggebruiker, text= '').grid(row=7,column=3)
Button(inloggebruiker, text= 'Terug', command= lambda: raise_frame(main)).grid(row=8, column=7)

#inloggen galeriehouder
"""Invoer van de inloggegevens van de galeriehouder."""

Label(inloghouder, text='').grid(row=0, column=1, pady=20)
Label(inloghouder, text= 'Voer uw gegevens in:').grid(row=1, column=7, padx=50, pady=10)
Label(inloghouder, text= '').grid(row=2,column=3)
Label(inloghouder, text= 'Naam').grid(row=3,column=5)
Label(inloghouder, text= 'Wachtwoord').grid(row=4,column=5)
checkbox1 = Checkbutton(inloghouder, text="Onthoud mijn gegevens")
checkbox1.grid(row=5, column=7, pady=10)
Button(inloghouder, text='Inloggen', command= lambda: raise_frame(houder)).grid(row=6, column=7)

e3 = Entry(inloghouder)
e4 = Entry(inloghouder, show= '*')

e3.grid(row=3, column=7)
e4.grid(row=4, column=7)


Label(inloghouder, text= '').grid(row=7,column=3)
Button(inloghouder, text= 'Terug', command= lambda: raise_frame(main)).grid(row=8, column=7)

#gebruiker
"""Het keuze scherm van de gebruiker."""

Label(gebruiker, text='').grid(row=0, column=1, pady=20)
Label(gebruiker, text= 'Maak een keuze:').grid(row=1, column=3, padx=125, pady=10)
Label(gebruiker, text='').grid(row =2, column=2)
Button(gebruiker, text= 'Kunststukken', command= lambda: raise_frame(selectie)).grid(row=3, column=3)
Label(gebruiker, text='').grid(row=4, column=1)
Button(gebruiker, text= 'Ticket', command= lambda: raise_frame(ticketscherm)).grid(row=5, column=3)
Label(gebruiker, text='').grid(row=6, column=3, pady=10)

Button(gebruiker, text= 'Terug', command= lambda: raise_frame(main)).grid(row=7, column=3)

#selectie
"""Hier kan de bezoeker een kunststuk selecteren en mogelijk alvast een voorbeeld van zien"""

Label(selectie, text='Selecteren van een kunststuk:').pack(pady=20)
scrollbar = Scrollbar(selectie)
scrollbar.pack(side=RIGHT, fill=Y)

mylist = Listbox(selectie, yscrollcommand = scrollbar.set )
for line in range(101):            #hier moet lengte zijn van alle kunststukken
   mylist.insert(END,str(line))

mylist.pack(expand=1, fill=BOTH)
scrollbar.config( command = mylist.yview )

Button(selectie, text= 'Bekijk').pack(side=LEFT, pady=5)
Button(selectie, text= 'Selecteren').pack(side=RIGHT, pady=5)                   # message box met ticket nummer (of als de persoon al iets heeft gekozen?)
Label(selectie, text='').pack(fill=X)
Button(selectie, text= 'Terug', command= lambda: raise_frame(gebruiker)).pack()

selectmode = SINGLE

#ticketscherm

Label(ticketscherm, text='').grid(row=0, column=1, pady=15)
Label(ticketscherm, text='Email-adres').grid(row=1, column=3, padx=135)                           #hier moet ingevoerde email-adres inkomen
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

Label(houder, text='').grid(row=0, column=1)
Label(houder, text= 'Maak een keuze:').grid(row=1, column=3, padx=125, pady=10)
Label(houder, text='').grid(row=2, column=2)
Button(houder, text= 'Niet geleende kunststukken', command= lambda: raise_frame(nietgeleend)).grid(row=3, column=3)
Label(houder, text='').grid(row=4, column=2)
Button(houder, text= 'Geleende kunststukken', command= lambda: raise_frame(geleend)).grid(row=5, column=3)
Label(houder, text='').grid(row=6, column=2)
Button(houder, text= 'Bezoekers',command= lambda: raise_frame(bezoekers)).grid(row=7, column=3)
Label(houder, text='').grid(row=8, column=2)
Button(houder, text= 'Ticket controle', command= lambda: raise_frame(controle)).grid(row=9, column=3)
Label(houder, text='').grid(row=10, column=3, pady=10)
Button(houder, text= 'Terug', command= lambda: raise_frame(main)).grid(row= 11, column=3)


#nietgeleend
"""Overzicht van alle niet geleende kunststukken, mogelijkheid tot lenen."""

Label(nietgeleend, text='Overzicht niet geleende kunststukken:').pack(pady=20)
scrollbar = Scrollbar(nietgeleend)
scrollbar.pack(side=RIGHT, fill=Y)

mylist = Listbox(nietgeleend, yscrollcommand = scrollbar.set )
for line in range(101):                                         #hier moet lengte zijn van niet geleende dingen
   mylist.insert(END,str(line))

mylist.pack(expand=1, fill=BOTH)
scrollbar.config( command = mylist.yview )

Button(nietgeleend, text= 'Lenen', command=lambda: messagebox.showinfo("Success!","Het lenen is gelukt!")).pack(pady=10) # message box of gelukt is of niet dus
Button(nietgeleend, text= 'Terug', command= lambda: raise_frame(houder)).pack(pady=5)
selectmode = SINGLE

#geleend
"""Overzicht van alle geleende kunststukken."""

Label(geleend, text='Overzicht geleende kunststukken:').pack(pady=20)
scrollbar = Scrollbar(geleend)
scrollbar.pack(side=RIGHT, fill=Y)

mylist = Listbox(geleend, yscrollcommand = scrollbar.set )
for line in range(101):                                     #hier moet lengte van lijst van geleende dingen zijn
   mylist.insert(END, str(line))

mylist.pack(expand=1, fill=BOTH)
scrollbar.config( command = mylist.yview )

Button(geleend, text= 'Terug', command= lambda: raise_frame(houder)).pack(pady=10)
selectmode = SINGLE

#bezoekers
"""Overzicht van alle bezoekers."""

Label(bezoekers, text='Overzicht van bezoekers:').pack(pady=20)
scrollbar = Scrollbar(bezoekers)
scrollbar.pack(side=RIGHT, fill=Y)

listbox= Listbox(bezoekers)
listbox.pack(expand=1, fill=BOTH)

for i in range(1001):                  #hier moet len van de lijst zijn, dus eerst regels opvragen
    listbox.insert(END, i)

listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=listbox.yview)

Button(bezoekers, text= 'Terug', command= lambda: raise_frame(houder)).pack(pady=10)


#controle
"""Hier kunnen de afgegeven codes van het ticketscherm worden gecontroleerd."""

Label(controle, text= '').grid(row=1, column=0, pady=20)
Label(controle, text='Voer hier de code in:').grid(row=2, column=3, padx=120, pady=10)
e1 = Entry(controle)
e1.grid(row=3, column=3, pady=10)
Button(controle, text='Controleren').grid(row=4, column=3)      #message box als het klopt of als het niet voorkomt

Label(controle, text= '').grid(row=5, column=0)
Button(controle, text= 'Terug', command= lambda: raise_frame(houder)).grid(row=6, column=3)


root.title('Thuisgalerie')

""""De geometry geeft aan hoe groot het frame moet zijn."""
root.geometry('360x360')

"""Zorgt dat het mainscreen altijd als eerste wordt geopend"""
raise_frame(main)

"""Zorgt dat ervoor dat de frames werken"""
root.mainloop()



