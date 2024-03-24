from tkinter import messagebox



class Message_erreur:
    def __init__(self,titre,contenu):
        self.titre=titre
        self.contenu=contenu



    def attention(self):
        self.attention = messagebox.showwarning(self.titre, self.contenu)

    def rejouer(self):
        self.rejouer = messagebox.askquestion(self.titre, self.contenu)

    def gagner(self) :
        self.rejouer = messagebox.showinfo(self.titre,self.contenu)

