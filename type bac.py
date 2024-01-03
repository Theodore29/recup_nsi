def rendu(somme_a_rendre):
    n1=0  ## 5€
    n2=0  ## 2€
    n3=0  ## 1€
    li=[]
    monnaie = [5,2,1]
    indice = 0
    while somme_a_rendre > 0 :
        monnaie_test=monnaie[indice]
        if monnaie_test > somme_a_rendre :
            indice += 1
        else :
            if monnaie_test == 5 :
                n1 += 1
            if monnaie_test == 2 :
                n2 += 1
            if monnaie_test == 1 :
                n3 += 1


            somme_a_rendre -= monnaie_test
    li=[n1,n2,n3]
    return li


class AdresseIP:
    def __init__(self, adresse):
        self.adresse = adresse
    def liste_octet(self):
        return [int(i) for i in self.adresse.split(".")]
    def est_reservee(self):
        return self.adresse == "192.168.0.0" or self.adresse == "192.168.0.255"
    def adresse_suivante(self):
        if AdresseIP.liste_octet(self)[3] < 254:
            octet_nouveau = AdresseIP.liste_octet(self)[3] + 1
            return (AdresseIP('192.168.0.' + str(octet_nouveau)))
        else:
            return False

adresse1=AdresseIP("192.168.0.1")
adresse2=AdresseIP("192.168.0.2")
adresse3=AdresseIP("192.168.0.0")


