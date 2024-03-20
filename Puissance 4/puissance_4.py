from tkinter import *

Mafenetre = Tk()
Mafenetre.title('Puissance 4')
Mafenetre.geometry('650x755')
Largeur = 490
Hauteur = 420
couleur1 = "blue"

Canevas=Canvas(Mafenetre, width=Largeur, height=Hauteur, bg=couleur1 )

message=StringVar()
message.set("Couleur :")
Label(Mafenetre, textvariable=message).pack(padx=1,pady=1)
nombre0=StringVar()
saisie0=Entry(Mafenetre)
saisie0.configure(textvariable=nombre0,width=2)
saisie0.pack()

message1=StringVar()
message1.set("Colonne : ")
Label(Mafenetre, textvariable=message1).pack(padx=1,pady=1)
nombre1=StringVar()
saisie1=Entry(Mafenetre)
saisie1.configure(textvariable=nombre1,width=2)
saisie1.pack()

message2=StringVar()
message2.set("Ligne : ")
Label(Mafenetre, textvariable=message2).pack(padx=1,pady=1)
nombre2=StringVar()
saisie2=Entry(Mafenetre)
saisie2.configure(textvariable=nombre2,width=2)
saisie2.pack()


Mafenetre.iconbitmap('icone.ico')

BoutonJouer=Button(Mafenetre, text='Jouer', fg ='red')
BoutonJouer.pack(padx=10, pady=10)

BoutonQuitter=Button(Mafenetre, text='Quitter', fg = 'red' ,command = Mafenetre.destroy)
Canevas.pack(padx=10, pady=10)

BoutonQuitter.pack(side=RIGHT, padx=10, pady=10)


Mafenetre.mainloop()