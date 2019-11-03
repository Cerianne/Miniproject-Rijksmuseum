def getCode(self, numbers, item, kunststuk):

    while True:

        config = json.loads(open('KunstUitleen.json').read()
        for item in config:
            if item['Available'] == True:
                messagebox.showinfo('U kunt dit kunstwerk zien in het Rijksmuseum')
                break

            else:
                kunstdata = Jsonfiles.get_kunstdata
                persoonsdata = Jsonfiles.get_persoonsdata

                for galerij in persoonsdata['Persoonsgegevens']:
                    for item in kunstdata:
                        if item['Naam'] == kunsstuk:
                            galerij['Kunststukken'].append(kunststuk)

                for numbers in persoonsdata['Persoonsgegevens']:
                    value = random.randint(1000, 9999)
                    if numbers['Ticketnummer'] != value:
                        numbers['Ticketnummer'].append(value)
                        persoonsdata = json.dump(persoonsdata, indent=2)
                        with open('persoonsgegevens.json','w') as f:            #bij dit json bestand moet nog de ticketnummer worden toegevoegd
                            f.writelines(persoonsdata)
                        messagebox.showinfo('Uw ticketnummer is: ' + value)
                        break
                    else:
                        continue


button_1 = Button(selectie, text= 'Selecteren').pack(side=RIGHT, pady=5)    #wordt aangepast in front
button_1.bind('<Button-1>',getCode)                                         #wordt toegevoegd er onder
                                                                            #gedaan kan zelf niet testen of dit alles werkt!!!
