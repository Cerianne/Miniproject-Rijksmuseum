from tkinter import *

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

Label(inloggebruiker, text='').grid(row=0, column=1, pady=20)
Label(inloggebruiker, text= 'Voer uw gegevens in:').grid(row=1, column=7, padx=50, pady=10)
Label(inloggebruiker, text= '').grid(row=2,column=3)
Label(inloggebruiker, text= 'Naam').grid(row=3,column=5)
Label(inloggebruiker, text= 'Email adres').grid(row=4,column=5)
Label(inloggebruiker, text= '').grid(row=5,column=3)
Button(inloggebruiker, text='Login', command= lambda: raise_frame(gebruiker)).grid(row=6,column=7)

e1 = Entry(inloggebruiker)
e2 = Entry(inloggebruiker)

e1.grid(row=3,column=7)
e2.grid(row=4,column=7)

Label(inloggebruiker, text= '').grid(row=7,column=3)
Button(inloggebruiker, text= 'Terug', command= lambda: raise_frame(main)).grid(row=8, column=7)

#inloggen galeriehouder
"""Invoer van de inloggegevens van de galeriehouder."""

Label(inloghouder, text='').grid(row=0, column=1, pady=20)
Label(inloghouder, text= 'Voer uw gegevens in:').grid(row=1, column=7, padx=50, pady=10)
Label(inloghouder, text= '').grid(row=2,column=3)
Label(inloghouder, text= 'Naam').grid(row=3,column=5)
Label(inloghouder, text= 'Wachtwoord').grid(row=4,column=5)
Label(inloghouder, text= '').grid(row=5,column=3)
Button(inloghouder, text='Login', command= lambda: raise_frame(houder)).grid(row=6, column=7)

e3 = Entry(inloghouder)
e4 = Entry(inloghouder)

e3.grid(row=3, column=7)
e4.grid(row=4, column=7)

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

Button(selectie, text= 'Terug', command= lambda: raise_frame(gebruiker)).grid()

#ticketscherm

Button(ticketscherm, text= 'Terug', command= lambda: raise_frame(gebruiker)).grid()

#galeriehouder
"""Het keuzemenu van de galeriehouder."""

Label(houder, text='').grid(row=0, column=1)
Label(houder, text= 'Maak een keuze:').grid(row=1, column=3, padx=125, pady=10)
Label(houder, text='').grid(row=2, column=2)
Button(houder, text= 'Overzicht niet geleende kunststukken', command= lambda: raise_frame(nietgeleend)).grid(row=3, column=3)
Label(houder, text='').grid(row=4, column=2)
Button(houder, text= 'Overzicht geleende kunststukken', command= lambda: raise_frame(geleend)).grid(row=5, column=3)
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
for line in range(101):                                         #hier moet lengte zijn van niet geleende dingen
   mylist.insert(END,str(line))

mylist.pack(expand=1, fill=BOTH)
scrollbar.config( command = mylist.yview )

Button(nietgeleend, text= 'Lenen').pack(pady=5)
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

