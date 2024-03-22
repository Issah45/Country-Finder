import wikipedia, pycountry
from tkinter import *
from PIL import ImageTk, Image

country = input("What is the country? ")

try:
    country_code_upper = pycountry.countries.get(name=country).alpha_2
except:
    if country == "Russia": country_code_upper = "RU"
    else:
        country_code_upper = "NON"

country_code = country_code_upper.lower()

root = Tk()

canvas = Canvas(root, width = 256, height = 256)
canvas.grid(row=1, column=1)

_summary = wikipedia.summary(country, auto_suggest=False, sentences=4)
summary = Label(root, text=_summary, wraplength=500)
summary.grid(row=2, column=1)

map_image = PhotoImage(file=f"maps/all/{country_code}/256.png")
flag_image = PhotoImage(file=f"flags/{country_code_upper}.png")

canvas.create_image(0, 0, anchor=NW, image=map_image)
canvas.create_image(0, 0, anchor=NW, image=flag_image)

root.mainloop()
