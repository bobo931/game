import tkinter as tk
from PIL import Image, ImageTk
from random import shuffle

def program():
    PAHARE = ["X", 'O', "X"]

    def shuffle_list(PAHARE):
        shuffle(PAHARE)
        return PAHARE

    def player_ghiceste():
        ghiceste = ''
        while ghiceste not in ['0', '1', '2']:
            ghiceste = int(text.get())
            return int(ghiceste)

    def check_guess(PAHARE, ghiceste):
        if PAHARE[ghiceste] == 'O':
            print('SUPER , AI CASTIGAT!')
            label3.config(text="SUPER , AI CASTIGAT")
        else:
            print('GRESIT, AI PIERDUT !', '\n''MAI BAGA O FISA!')
            label3.config(text="GRESIT, AI PIERDUT !','\n''MAI BAGA O FISA!")

    mixedup_list = shuffle_list(PAHARE)
    ghiceste = player_ghiceste()
    check_guess(mixedup_list, ghiceste)


window = tk.Tk()

img = ImageTk.PhotoImage(Image.open("imagine.jpg"))
label10 = tk.Label(window, image=img)
label10.pack()

text = tk.StringVar()
entry = tk.Entry(window, textvariable=text)
entry.pack()
label = tk.Label(text="SALUT!").pack()
label2 = tk.Label(text="UNDE CREZI CA ESTE BILA ALBA ? '\nALEGE UNU DIN PAHARELE : [0], [1], SAU [2]").pack()
label3 = tk.Label(window, text="")
label3.pack()


def clear_labels():
    label3.config(text="")


window.geometry("450x250")

INCEARCA = tk.Button(window, text="INCEARCA", command=program)
RESETARE = tk.Button(window, text="RESETARE", command=clear_labels)
INCEARCA.pack()
RESETARE.pack()
window.mainloop()
