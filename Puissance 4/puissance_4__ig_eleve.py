from tkinter import *
from tkinter import messagebox
import webbrowser
from datetime import *


##Docstring

class Pion():
    def __init__(self,colonne,ligne,couleur):
        self.colonne = colonne-1
        self.ligne = ligne
        self.couleur=couleur


    def affiche_pions(self):
        print("et",self.colonne+1,"et",6-(self.ligne+6)%6)



    def afficher_gui(self,canvas):
        C = 70
        rayon = 30
        marge = 5
        x = (self.colonne + 0.5) * C
        y = (5-self.ligne + 0.5) * C
        canvas.create_oval(x - rayon, y-rayon, x + rayon, y + rayon, fill = self.couleur)




class Grille:
    def __init__(self):
        self.pions = []
        self.pions_couleur = []
        self.colonnes = [[] for i in range(7)]



    def switch_joueur(self,pion):
        if  self.pions_couleur==[]:
            pion.couleur = "yellow"

        elif self.pions_couleur[-1] == "yellow":
            pion.couleur='red'

        elif self.pions_couleur[-1] == "red":
            pion.couleur = 'yellow'






    def ajouter_pions(self,pion):
        n=1
        col=self.colonnes[pion.colonne]


        if len(col) >= 6:
            erreur_val_col()
            return

        for i in self.pions:
            if i.colonne == pion.colonne and i.ligne == pion.ligne+1 :
                self.pions.append(pion)
        self.switch_joueur(pion)
        self.pions.append(pion)


        self.pions_couleur.append(pion.couleur)
        col.append(pion)
        pion.ligne = len(col) - 1
        print(self.pions_couleur)


    def afficher(self,canvas):
        for i in self.pions:
            i.afficher_gui(canvas)




def initialisation() :
    C=70
    for i in range(7):
        for j in range(6):
            x1 = i * C + 5
            y1 = j * C + 5
            x2 = (i + 1) * C - 5
            y2 = (j + 1) * C - 5
            Canevas.create_oval(x1, y1, x2, y2, fill="snow")


Mafenetre = Tk()
Mafenetre.title('Puissance 4')
Mafenetre.geometry('650x755')
Largeur = 490
Hauteur = 420
couleur1 = "blue"

Canevas=Canvas(Mafenetre, width=Largeur, height=Hauteur, bg=couleur1 )



message1=StringVar()
message1.set("Colonne : ")
Label(Mafenetre, textvariable=message1).pack(padx=1,pady=1)
nombre1=StringVar()
saisie1=Entry(Mafenetre)
saisie1.configure(textvariable=nombre1,width=2)
saisie1.pack()





counter = timedelta(seconds=0)
running = False


def format_time(time):
    minutes, seconds = divmod(time.seconds, 60)
    return '{:02d}:{:02d}'.format(minutes, seconds)


def counter_label(label):
    def count():
        global counter
        if running:
            string = format_time(counter)
            label.config(text=string)
            counter += timedelta(seconds=1)
        label.after(1000, count)
    count()


def Start(label):
        global running
        running=True
        counter_label(label)
        start['state']='disabled'
        stop['state']='normal'
        reset['state']='normal'


def Stop():
    global running
    start['state']='normal'
    stop['state']='disabled'
    reset['state']='normal'
    running = False

def Reset(label):
    global counter
    counter=0

    if running==False:
        reset['state']='disabled'
        label['text']='Se tester'


    else:
        label['text']='Démarrage'




label = Label(Mafenetre, text="Se Tester !", fg="black", font="Verdana 30 bold")
label.pack()
f = Frame(Mafenetre)

start = Button(f, text="Start", width=6, command=lambda:Start(label))
stop = Button(f, text='Stop',width=6,state='disabled', command=Stop)
reset = Button(f, text='Reset',width=6, state='disabled', command=lambda:Reset(label))
f.pack(anchor = 'center',pady=5)
start.pack(side="left")
stop.pack(side ="left")
reset.pack(side="left")



def erreur_val_col():
    messagebox.showwarning("Alerte", "Entre une donnée valide (1 JAUNE, 2 ROUGE)")


grille=Grille()
def jouer():
    n1=int(nombre1.get())
    if n1 > 7 :
        erreur_val_col()



    print("et",n1,"et")

##    g=Grille()
##    print(g.pions)
    initialisation()

    pion1=Pion(n1,0,0)
    grille.ajouter_pions(pion1)
    grille.afficher(Canevas)



def jouer_touche(event):
    jouer()

def pub():
    webbrowser.open('https://youtu.be/dQw4w9WgXcQ?feature=shared')

def aide():
    messagebox.showinfo("Aide", "Ceci est un simple Puissance 4, le jeu que vous jouait lorsque vous étiez petit.", icon="info")



initialisation()

Mafenetre.bind('<Return>', jouer_touche)
Mafenetre.iconbitmap('icone.ico')

BoutonJouer=Button(Mafenetre, text='Jouer', fg ='red', command=jouer)
BoutonJouer.pack(padx=10, pady=10)



BoutonQuitter=Button(Mafenetre, text='Quitter', fg = 'red' ,command = Mafenetre.destroy)
Canevas.pack(padx=10, pady=10)
BoutonAide=Button(Mafenetre, text='?', command=aide)
BoutonPub=Button(Mafenetre, text='Afficher la publicité', command=pub)




BoutonAide.pack(side = RIGHT, padx=10, pady=10)
BoutonPub.pack(side=RIGHT, padx=10, pady=10)
BoutonQuitter.pack(side=RIGHT, padx=10, pady=10)

Mafenetre.mainloop()


