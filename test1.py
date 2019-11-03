def randnum(code):
    while True:
        bezoekers = Jsonfiles.get_bezoekers
        for numbers in bezoekers['Persoonsgegevens']:
            value = random.randint(1000, 9999)
            if numbers['ticketnummer'] != value:
                numbers['ticketnummer'].append(value)
                bezoekers = json.dump(bezoekers, indent=2)
                with open('persoonsgegevens.json','w') as f:            #bij dit json bestand moet nog de ticketnummer worden toegevoegd
                    f.writelines(bezoekers)
                messagebox.showinfo('Uw ticketnummer is: ' + value)
                break
            else:
                continue


button_1 = Button(selectie, text= 'Selecteren').pack(side=RIGHT, pady=5)    #wordt aangepast in front
button_1.bind("<Button-1>",randnum)                                         #wordt toegevoegd er onder??
