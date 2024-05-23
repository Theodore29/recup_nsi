from graphviz import Digraph
import networkx as nx
import pylab

class Graphe():
    def __init__(self, noeuds = None):
        if noeuds is None :
            self.__noeuds = dict()
        else :
            self.__noeuds = noeuds

    def liste_noeuds(self):
        nds = list(self.__noeuds.keys())
        nds.sort()
        return nds

    def voisins(self,nd):
        if nd in self.liste_noeuds():
            return [a[0] for a in self.__noeuds[nd]]
        else :
            return []

    def voisins1(self,nd):
        if nd in self.liste_noeuds():
            return [(a[0],a[1]) for a in self.__noeuds[nd]]
        else :
            return []

    def __str__(self):
        result="Le graphe est defini par \n"
        for nd in self.liste_noeuds():
            result=result+str(nd)+'->'
            for elt in self.voisins1(nd):
                result = result+"("+str(elt[0])+","+str(elt[1])+")"+";"
            result=result+"\n"
        return result

    def ajouter_noeud(self,nd):
        if not nd in self.__noeuds :
            self.__noeuds[nd] = []


    def ajouter_arete(self, nd1,nd2, poids=1):
        self.ajouter_noeud(nd1)
        self.ajouter_noeud(nd2)
        self.__noeuds[nd1].append((nd2, poids))


    def arete(self,nd1,nd2):
        if nd2 not in self.voisins(nd1):
            return 0
        for a in self.__noeuds[nd1]:
            if a[0] == nd2 :
                return a[1]


    def matrice(self):
        L=[]
        for v in self.__noeuds.keys():
            L.append(v)
        L.sort()
        n=len(L)
        M=[]
        for i in range(n):
            M.append([])
            for j in range(n):
                M[i].append(0)

        for i in range(n):
            double_V=self.voisins1(L[i])
            for j in range(n):
                for k in range(len(double_V)):
                    if L[j]==double_V[k][0]:
                        M[i][j]=double_V[k][1]
        return M


    def affiche(self):
        G=nx.DiGraph()
        for nd in self.liste_noeuds():
            G.add_node(nd)
        for nd in self.liste_noeuds():
            for elt in self.voisins1(nd):
                G.add_edge(nd,elt[0], weight=elt[1])
        etiquettes=dict([((u,v),d["weight"]) for u,v,d in G.edges(data=True)])
        pos=nx.circular_layout(G)
        nx.draw(G, pos,node_color="#badbad", with_labels=True)
        nx.draw_networkx_edge_labels(G,pos,etiquettes,label_pos=0.4)
        pylab.draw()
        pylab.show()
        pylab.figure()

    def parcour_largeur(self,s):
        couleur=[]
        file=[]
        couleur.append(s)
        file.append(s)
        while len(file) != 0 :
            u=file.pop(0)
            print(u)


            for v in self.voisins(u):
                if v not in couleur :
                    couleur.append(v)
                    file.append(v)




    def parcours_profondeur(self, s):
        couleurs=[]
        pile=[]
        couleurs.append(s)
        pile.append(s)
        while len(pile) != 0 :
            u=pile.pop()
            print(u)

            for v in self.voisins(u):
                if v not in couleurs :
                    couleurs.append(v)
                    pile.append(v)













ex1= {'A' : [('M', 65), ('R', 90), ('T', 80)],
    'G' : [('L', 70)],
    'L' : [('G', 70), ('P', 230), ('T', 260)],
    'M' : [('A', 65), ('P', 95), ('R', 90), ('T', 55)],
    'P' : [('L', 23), ('M', 95), ('T', 130)],
    'R' : [('A', 90), ('M', 90)],
    'T' : [('A', 90), ('L', 260), ('M', 55), ('P', 130)]}





graphe = Graphe(ex1)
matrice_adj = graphe.matrice()
affiche = graphe.affiche()

print(matrice_adj, affiche)

##graphe1 = Graphe()
##
##
##
##graphe1.ajouter_noeud("A")
##graphe1.ajouter_noeud("B")
##graphe1.ajouter_arete("A","B",3)
##graphe1.ajouter_arete("B","A",3)
##
##graphe1.ajouter_noeud("C")
##graphe1.ajouter_arete("B","C",5)
##graphe1.ajouter_arete("C","B",5)
##graphe1.ajouter_arete("C","A",1)
##graphe1.ajouter_arete("A","C",1)
##
##graphe1.ajouter_noeud("D")
##graphe1.ajouter_arete("C","D",1)
##graphe1.ajouter_arete("D","C",1)
##graphe1.ajouter_arete("D","A",2)
##graphe1.ajouter_arete("A","D",2)
##
##graphe1.ajouter_noeud("E")
##graphe1.ajouter_arete("E","D",4)
##graphe1.ajouter_arete("D","E",4)
##
##graphe1.ajouter_noeud("F")
##graphe1.ajouter_arete("F","E",2)
##graphe1.ajouter_arete("E","F",2)
##graphe1.ajouter_arete("F","D",3)
##graphe1.ajouter_arete("D","F",3)
##graphe1.ajouter_arete("F","C",4)
##graphe1.ajouter_arete("C","F",4)
##graphe1.ajouter_arete("F","A",6)
##graphe1.ajouter_arete("F","A",6)
##
##
##
##
##
##
##
##
##
##
##
##matrice_adj = graphe1.matrice()
##affiche = graphe1.affiche()
##
##print(matrice_adj, affiche)

