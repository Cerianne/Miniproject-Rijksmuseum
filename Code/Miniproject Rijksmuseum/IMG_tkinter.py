import io
from PIL import Image, ImageTk
import tkinter as tk
from urllib.request import urlopen
import Rijks_API_laad as api

root = tk.Tk()
# url is zoekfunctie via RijksAPI(de nachtwacht, vervangen)
url = str(api.imgKunstwerk("de nachtwacht"))
image_bytes = urlopen(url).read()
data_stream = io.BytesIO(image_bytes)
pil_image = Image.open(data_stream)
pil_image = pil_image.resize((350, 300), Image.BILINEAR)
fname = "Gallerij"
sf = "{}".format(fname)
root.title(sf)
tk_image = ImageTk.PhotoImage(pil_image)
# link naar galerijhouder
textLabel = tk.Label(root, text= str("NAAM\n"
                                     "ADRES 123\n"
                                     "PLAATS, 1234AB"), padx=10, pady=10)
textLabel.pack()


label = tk.Label(root, image=tk_image, bg='white')
label.pack(padx=5, pady=5)
root.geometry("360x360")
root.mainloop()
