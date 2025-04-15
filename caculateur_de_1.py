from tkinter import *
from math import *
import random
from threading import Timer
import os

print("Répertoire parent du fichier actuel :", os.path.dirname(os.path.abspath(__file__)))

fenetre = Tk()

fenetre.configure(bg='deep sky blue')
#fenetre.state('zoomed')
fenetre.title("nombre entier calculateur")

# canvas
canvas = Canvas(fenetre, width=170, height=50, background='deep sky blue')
txt = canvas.create_text(85, 27, text="calculateur de 1", font="Arial 16 italic", fill="blue")
canvas.pack()
canvas.place(x=12, y=10)


# label
label = Label(fenetre, text="coup pour trouver 1 :", bg="deep sky blue")
label.pack()
label.place(x=10, y=70)

# label
label2 = Label(fenetre, text="votre nombre :", bg="deep sky blue")
label2.pack()
label2.place(x=10, y=110)

# label
label3 = Label(fenetre, text="résultat :", bg="deep sky blue")
label3.pack()
label3.place(x=10, y=90)


# entrée
string = StringVar()
string.set("")
entree = Entry(fenetre, textvariable=string, width=30)
entree.pack()
entree.place(x=10, y=130)

résultat=StringVar()
résultat.set("")
labelrésultat= Label(fenetre, textvariable=résultat,fg="red",bg="deep sky blue")
labelrésultat.pack()
labelrésultat.place(x=65, y=90)

coupnombre=StringVar()
coupnombre.set("aucun")
labelcoup= Label(fenetre, textvariable=coupnombre,fg="red",bg="deep sky blue")
labelcoup.pack()
labelcoup.place(x=130, y=70)

error=0
def exe():
    global error
    global résultat
    global coupnombre
    global autoposition
    réponse=entree.get()
    print(réponse)
    ok=0
    coup=0
    try:
        repint=int(réponse)
    except Exception:
        print("error1")
        ok=1
        résultat.set("error 1")
        labelrésultat.config(fg='red')
        if error==0:
            error=1
            info()
    if repint < 1:
        print("error2")
        ok=1
        résultat.set("error 2")
        labelrésultat.config(fg='red')
        if error==0:
            error=1
            info()
    if repint==1:
        ok=1
        coup=1
        coupnombre.set(coup)
        labelcoup.config(fg='black')
        résultat.set(repint)
        labelrésultat.config(fg='black')
    while ok != 1:
        if repint %2 ==0:
            try:
                repint=repint/2
            except Exception:
                ok=1
                résultat.set("error 3")
                labelrésultat.config(fg='red')
                autoposition='off'
                bouton2.config(bg='goldenrod')
                automate()
            coup=coup+1
        elif repint %2 !=0:
            try:
                repint=repint*3
            except Exception:
                ok=1
                résultat.set("error 3")
                labelrésultat.config(fg='red')
                autoposition='off'
                bouton2.config(bg='goldenrod')
                automate()
            repint=repint+1
            coup=coup+1
        if repint ==1:
            ok=1
            print('fini')
            print(coup)
            coupnombre.set(coup)
            labelcoup.config(fg='black')
            résultat.set(repint)
            labelrésultat.config(fg='black')
        if repint < 1:
            résultat.set("error 3")
            labelrésultat.config(fg='red')
            ok=1
            print('error3')
            coupnombre.set(coup)
            labelcoup.config(fg='red')
            if error==0:
                error=1
                info()

# bouton ok
bouton=Button(fenetre, text="ok / Enter", command=exe, bg='gold', activebackground='gold')
bouton.pack()
bouton.place(x=55, y=160)

autoposition='off'
def auto():
    global autoposition
    print(autoposition)
    if autoposition=='off':
        autoposition='on'
        bouton2.config(bg='green2')
    else:
        autoposition='off'
        bouton2.config(bg='goldenrod')
    automate()

def automate():
    global autoposition
    global string
    global entree
    if autoposition=='on':
        nombre=random.randint(0,9)
        nombre=str(nombre)
        avantnombre=entree.get()
        avantnombre=nombre+avantnombre
        string.set(avantnombre)
        exe()
        attente= Timer(0.3,automate)
        attente.start()


# auto bouton
bouton2=Button(fenetre, text="auto",command=auto, bg='goldenrod', activebackground='goldenrod')
bouton2.pack()
bouton2.place(x=115, y=160)

#touche enter pressé
def my(event):
    exe()

fenetre.bind('<Return>', my)

def suppr(event):
    global string
    string.set("")

fenetre.bind('<Delete>',suppr)

def info():
    global fondinfo
    global boutonclose
    global saisi1blocked
    fondinfo = Canvas(fenetre, width=187, height=200, background='white')
    fondinfo.pack()
    fondinfo.place(x=5, y=3)
    boutonclose=Button(fenetre, text="ok", command=infoclose,width = 10, height= 1, bg="cyan", activebackground="cyan")
    boutonclose.pack()
    boutonclose.place(x=61, y=165)
    saisi1blocked = Text(fenetre, width=20, height=9)
    saisi1blocked.pack()
    saisi1blocked.place(x=20, y=15)
    saisi1blocked.insert(INSERT,"Error :                                 Error 1 = ce n'est  pas un nombre entier                    Error 2 = nombre    inférieur à 1                           Error 3 = beug prog (impossible)                            INFO : opération =  si nombre est pair: nombre=nombre/2     si nombre impair :  nombre=nombre*3+1")
    saisi1blocked.configure(state='disabled',fg='red')

def infoclose():
    global fondinfo
    global boutonclose
    global saisi1blocked
    fondinfo.place_forget()
    boutonclose.place_forget()
    saisi1blocked.place_forget()

# bouton i
bouton=Button(fenetre, text="i", command=info)
bouton.pack()
bouton.place(x=187, y=1)


fenetre.mainloop()

