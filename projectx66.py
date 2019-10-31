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

for frame in(main, inloghouder, inloggebruiker, gebruiker, houder, nietgeleend, geleend, bezoekers, controle, selectie, ticketscherm):
    frame.grid(row=0, column=0, sticky='news')

#mainscreen

Label(main, text='Maak een keuze:').pack(padx=275, pady=15)
Button(main, text='Galeriehouder', command=lambda: raise_frame(inloghouder)).pack(pady=15)
Button(main, text='Gebruiker', command=lambda: raise_frame(inloggebruiker)).pack()


#inloggen gebruiker
Label(inloggebruiker, text= 'Voer uw gegevens in:').grid(row=1, column=7)
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
Label(inloghouder, text= 'Voer uw gegevens in:').grid(row=1, column=7)
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

Label(gebruiker, text= 'Maak een keuze:').pack(pady= 15, padx=275)
Button(gebruiker, text= 'Kunststuk selectie', command= lambda: raise_frame(selectie)).pack(pady=15)
Button(gebruiker, text= 'Ticket scherm', command= lambda: raise_frame(ticketscherm)).pack()

Button(gebruiker, text= 'Terug', command= lambda: raise_frame(main)).pack(pady=30)

#selectie

Button(selectie, text= 'Terug', command= lambda: raise_frame(gebruiker)).pack()

#ticketscherm

Button(ticketscherm, text= 'Terug', command= lambda: raise_frame(gebruiker)).pack()

#galeriehouder

Label(houder, text= 'Maak een keuze:').pack(pady= 15, padx=275)
Button(houder, text= 'Overzicht niet geleende kunststukken', command= lambda: raise_frame(nietgeleend)).pack(pady=10)
Button(houder, text= 'Overzicht geleende kunststukken', command= lambda: raise_frame(geleend)).pack(pady=10)
Button(houder, text= 'Overzicht van bezoekers',command= lambda: raise_frame(bezoekers)).pack(pady=10)
Button(houder, text= 'Ticketnummer controle', command= lambda: raise_frame(controle)).pack(pady=10)

Button(houder, text= 'Terug', command= lambda: raise_frame(main)).pack(pady=30)


#nietgeleend

scrollbar = Scrollbar(nietgeleend)
scrollbar.pack(padx= 275, pady=20)

mylist = Listbox(nietgeleend, yscrollcommand = scrollbar.set )
for line in range(101):
   mylist.insert(END,str(line))

mylist.pack(pady=20, padx=275)
scrollbar.config( command = mylist.yview )

Button(nietgeleend, text= 'Terug', command= lambda: raise_frame(houder)).pack()

#geleend

scrollbar = Scrollbar(geleend)
scrollbar.pack(padx= 275, pady=20)

mylist = Listbox(geleend, yscrollcommand = scrollbar.set )
for line in range(101):
   mylist.insert(END,str(line))

mylist.pack(pady=20, padx=275)
scrollbar.config( command = mylist.yview )

Button(geleend, text= 'Terug', command= lambda: raise_frame(houder)).pack()

#bezoekers

scrollbar = Scrollbar(bezoekers)
scrollbar.pack(padx= 275, pady=20)

mylist = Listbox(bezoekers, yscrollcommand = scrollbar.set )
for line in range(1000):
   mylist.insert(END,str(line))

mylist.pack(pady=20, padx=275)
scrollbar.config( command = mylist.yview )

Button(bezoekers, text= 'Terug', command= lambda: raise_frame(houder)).pack()

#controle
Label(controle, text='Voer hier de code in:').grid(row=2, column=2)
e1 = Entry(controle)
e1.grid(row=2, column=3)
Button(controle, text='Check').grid(column=3)

Button(controle, text= 'Terug', command= lambda: raise_frame(houder)).grid()

root.title('')
root.geometry('640x360')
raise_frame(main)
root.mainloop()

