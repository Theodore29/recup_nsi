class ABR(object):
    def __init__(self,c,g=None,d=None):
        if v is not None :
            self.valeur = v
        else :
            raise ValueError("La clé ne peut pas etre None")
        if g is None or type(g) is ABR :
            self.filsg = g
        else :
            raise ValueError("Un fils est un arbre_bin ou None")

        if d is none or type(d) is ABR :
            self.filsd = d
        else :
            raise ValueError("Un fils est un arbre_bin ou None")


    def ajouter(self, elt):
        if elt == self.v :
            self.v = elt
        if elt < self.v :
            self.g == elt
            ajouter(elt)
        if elt > self.v :
            self.d == elt
            ajouter(elt)



