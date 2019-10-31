from tkinter import *

#mainscreen functie

def main_screen():
    screen = Tk()
    screen.geometry("300x300")
    screen.title("Inlogvenster")
    Label(text = "Inlogvenster", bg="white", width="300", height="2", font = ("Calibri,13")).pack()
    Label(text="").pack()
    Button(text="Galeriehouder", height= "2", width="30").pack()
    Label(text="").pack()
    Button(text="Gebruiker", height="2", width="30").pack()

    screen.mainloop()

#main_screen()

#vanaf hier alle galeriehouder functies

def houderinlog_screen():
    screen = Tk()
    screen.geometry("300x300")
    screen.title("Houder log in")
    Label(text="Name").grid(row=0)
    Label(text="Password").grid(row=1)


    e1 = Entry(screen)
    e2 = Entry(screen)

    e1.grid(row=0, column=1)
    e2.grid(row=1, column=1)

    screen.mainloop()

houderinlog_screen()

def houder_screen():
    screen = Tk()
    screen.geometry("300x300")
    screen.title("Galeriehouder")
    Label(text="Overzichten", bg="white", width="300", height="2", font=("Calibri,13")).pack()
    Label(text="").pack()
    Button(text="Overzicht niet geleende kunststukken", height="2", width="30").pack()
    Label(text="").pack()
    Button(text="Overzicht geleende kunststukken", height="2", width="30").pack()
    Label(text="").pack()
    Button(text="Overzicht van bezoekers", height="2", width="30").pack()
    Label(text="").pack()
    Button(text="Toegangscode bezoeker check", height="2", width="30").pack()

    screen.mainloop()

#houder_screen()


def nietgeleend_screen():
    print()


def geleend_screen():
    print()

def bekijken_screen():
    print()

def check_screen():
    print()

#vanaf hier alle functies van gebruiker

def gebruikerinlog_screen():
    screen = Tk()
    screen.geometry("300x300")
    screen.title("Gebruiker log in")
    Label(text="Email adres").grid(row=0)
    Label(text="Name").grid(row=1)


    e1 = Entry(screen)
    e2 = Entry(screen)

    e1.grid(row=0, column=1)
    e2.grid(row=1, column=1)

    screen.mainloop()

#gebruikerinlog_screen()


def gebruiker_screen():
    screen = Tk()
    screen.geometry("300x300")
    screen.title("Gebruiker")
    Label(text="Overzichten", bg="white", width="300", height="2", font=("Ariel,13")).pack()
    Label(text="").pack()
    Button(text="kunststuk selectie", height="2", width="30").pack()
    Label(text="").pack()
    Button(text="Ticket scherm", height="2", width="30").pack()

    screen.mainloop()


#gebruiker_screen()

def selectie_screen():
    print()

def ticket_screen():
    print()

