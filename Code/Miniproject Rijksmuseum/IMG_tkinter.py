import io
from PIL import Image, ImageTk
import tkinter as tk
from urllib.request import urlopen
import Rijks_API_laad as api
import Jsonfiles as files


def showIMG(invoer):
    """" Haalt via de Rijksmuseum API de afbeelding op van het geselecteerde kunststuk"""
    root = tk.Tk()
    url = str(api.imgKunstwerk(invoer))
    image_bytes = urlopen(url).read()
    data_stream = io.BytesIO(image_bytes)
    pil_image = Image.open(data_stream)
    pil_image = pil_image.resize((350, 300), Image.BILINEAR)
    fname = "Gallerij"
    sf = "{}".format(fname)
    root.title(sf)
    tk_image = ImageTk.PhotoImage(pil_image, master=root)

    naam = ""
    adres = ""
    plaats = ""

    galerijdata = files.get_galerijdata()
    for galleries in galerijdata["Gallerijhouders"]:
        if invoer not in galleries["Kunst"]:
            adres = "Dit Kunstwerk is in het Rijksmuseum"

        else:
            naam = galleries["Gebruikersnaam"]
            adres = galleries["Straatnaam"] + " " + galleries["Huisnr"]
            plaats = galleries["Stad"]
            break

    textLabel = tk.Label(root, text=str("{}\n"
                                        "{}\n"
                                        "{}".format(naam, adres, plaats)), padx=10, pady=10)
    textLabel.pack()

    label = tk.Label(root, image=tk_image, bg='white')
    label.pack(padx=5, pady=5)
    root.geometry("360x360")
    root.mainloop()
