import webbrowser
import puissance_4__ig_eleve as fichier_principal

def jouer_touche(event):
    fichier_principal.jouer()

def pub():
    webbrowser.open('https://youtu.be/dQw4w9WgXcQ?feature=shared')

def aide():
    messagebox.showinfo("Aide", "Ceci est un simple Puissance 4, le jeu que vous jouait lorsque vous étiez petit.", icon="info")




