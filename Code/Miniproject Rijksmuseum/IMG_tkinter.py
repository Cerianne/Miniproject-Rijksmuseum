import io
from PIL import Image, ImageTk
import tkinter as tk
from urllib.request import urlopen
import Rijks_API_laad as api

root = tk.Tk()

url = str(api.imgKunstwerk(input("Naam van het kunstwerk: ")))
image_bytes = urlopen(url).read()
data_stream = io.BytesIO(image_bytes)
pil_image = Image.open(data_stream)
pil_image = pil_image.resize((500, 500), Image.BILINEAR)
fname = url.split('/')[-1]
sf = "{}".format(fname)
root.title(sf)
tk_image = ImageTk.PhotoImage(pil_image)

label = tk.Label(root, image=tk_image, bg='white')
label.pack(padx=5, pady=5)
root.geometry("500x500")
root.mainloop()
