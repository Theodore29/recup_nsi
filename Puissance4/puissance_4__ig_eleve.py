from tkinter import *
from tkinter import messagebox
import webbrowser
from datetime import *
import compteur
import message_erreur





##Docstring
## traduire gagner


class Pion():
    def __init__(self,colonne,ligne,couleur):
        self.colonne = colonne-1
        self.ligne = ligne
        self.couleur=couleur


    def affiche_pions(self):
        print("colonne",self.colonne+1)



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
        self.liste_pions=[]



    def switch_joueur(self,pion):
        if  self.pions_couleur==[]:
            prochain_tour.set("C'est au tour du Rouge")
            pion.couleur = "yellow"

        elif self.pions_couleur[-1] == "yellow":
            prochain_tour.set("C'est au tour du Jaune")
            pion.couleur='red'

        elif self.pions_couleur[-1] == "red":
            prochain_tour.set("C'est au tour du Rouge ")
            pion.couleur = 'yellow'



    def check_winner(self,grille):
        directions = [(1, 0), (0, 1), (1, 1), (-1, 1)]  # Right, Up, Diagonal Up-Right, Diagonal Up-Left
        for pion in grille.pions:
            for dx, dy in directions:
                compteur = 1  # Count for consecutive pieces of the same color
                x, y = pion.colonne, pion.ligne
                for i in range(3):  # Check in both directions
                 x, y = x + dx, y + dy
                 if (0 <= x < 7 and 0 <= y < 6 and len(grille.colonnes) > x and len(grille.colonnes[x]) > y and grille.colonnes[x][y] and grille.colonnes[x][y].couleur == pion.couleur):
                    compteur += 1
                 else:
                     break
                if compteur == 4:
                    return True
        return False

    def renitialiser(self):
        self.pions.clear()
        self.pions_couleur.clear()
        self.colonnes = [[] for i in range(7)]




    def ajouter_pions(self,pion):
        n=1
        col=self.colonnes[pion.colonne]


        if len(col) >= 6:
            mess_err=message_erreur.Message_erreur("Attention","données invalide vous êtes sortie de la grille")
            mess_err.attention()
            nombre1.set("")

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



def renitialiser_jeu():
    reset=message_erreur.Message_erreur("Rejouer ?","Voulez vous rejouer ?")
    reset.rejouer()
    if reset.rejouer == "yes":
        grille.renitialiser()
        initialisation()
        compteur1.stop()
        effacer_entree()
        compteur1.reset()
        return True
    else :
        Mafenetre.destroy()
        return False




def effacer_entree():
    nombre1.set("")


compteur1 = compteur.Timer(Mafenetre)



grille=Grille()
n1_verif=nombre1.get()


def jouer():
    n1=int(nombre1.get())
    if n1 > 7 :
        mess_err=message_erreur.Message_erreur("Attention",f"données invalide ({n1}) : Veuillez entrez une colonne comprise entre 1 et 7 ")
        nombre1.set("")
        mess_err.attention()



    print("colonne",n1)

    initialisation()

    pion1=Pion(n1,0,0)
    grille.ajouter_pions(pion1)
    grille.afficher(Canevas)

    if grille.check_winner(grille):
        compteur1.reset()
        gagner=message_erreur.Message_erreur("Victoire",f"Le joueur {pion1.couleur} a gagné !")
        gagner.gagner()
        renitialiser_jeu()

    effacer_entree()




def jouer_touche(event):
    jouer()

def pub():
    webbrowser.open('https://youtu.be/dQw4w9WgXcQ?feature=shared')

def aide():
    messagebox.showinfo("Aide", "Puissance 4, 2 joueurs, première couleur = Jaune", icon="info")



initialisation()


Mafenetre.bind('<Return>', jouer_touche)
Mafenetre.iconbitmap('icone.ico')

prochain_tour=StringVar()
prochain_tour.set("C'est au tour du Jaune")
label_tour=Label(Mafenetre,textvariable=prochain_tour)


BoutonJouer=Button(Mafenetre, text='Jouer', fg ='red', command=jouer)
BoutonJouer.pack(padx=10, pady=10)


BoutonQuitter=Button(Mafenetre, text='Quitter', fg = 'red' ,command = Mafenetre.destroy)
Canevas.pack(padx=10, pady=10)

label_tour.pack()
BoutonAide=Button(Mafenetre, text='?', command=aide)
BoutonPub=Button(Mafenetre, text='Afficher la publicité', command=pub)
BoutonRejouer = Button(Mafenetre, text='Rejouer',fg = 'blue', command=renitialiser_jeu)



BoutonAide.pack(side = RIGHT, padx=10, pady=10)
BoutonPub.pack(side=RIGHT, padx=10, pady=10)
BoutonRejouer.pack(side=RIGHT, padx=10, pady=10)
BoutonQuitter.pack(side=RIGHT, padx=10, pady=10)

Mafenetre.mainloop()


