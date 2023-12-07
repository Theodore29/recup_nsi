import sqlite3

conn=sqlite3.connect('magasin7.db')
cur=conn.cursor()

ex_2_client="CREATE TABLE client(identifiant INT PRIMARY KEY,nom VARCHAR(100),prenom VARCHAR(100),adresse VARCHAR(100),cp INT,ville VARCHAR(100),date_naissance DATE,num_carte INT);"
ex_2_ticket="CREATE TABLE ticket(num_ticket INT PRIMARY KEY, date DATE, heure TIME, mode_reg VARCHAR(100));"
ex_2_produit="CREATE TABLE produit(code_prod INT PRIMARY KEY, nom_prod VARCHAR(100), prix REAL);"
ex_2_possede="CREATE TABLE possede(identifiant INT REFERENCES client(identifiant), num_ticket INT REFERENCES ticket(num_ticket), PRIMARY KEY(identifiant,num_ticket) );"
ex_2_achat="CREATE TABLE achat(num_ticket INT REFERENCES ticket(num_ticket), code_produit INT REFERENCES produit(code_produit), qte INT, PRIMARY KEY(num_ticket,code_produit) );"

cur.execute(ex_2_client)
cur.execute(ex_2_ticket)
cur.execute(ex_2_produit)
cur.execute(ex_2_possede)
cur.execute(ex_2_achat)

ex_3_client1="INSERT INTO client VALUES (14,'Hamelin', 'Jules','42 rue des forges',25660,'VEZE','1986-12-30',900000236)"
ex_3_client2="INSERT INTO client VALUES (53,'Bertrand','Patrice','18 avenue du general Leclerc',25000,'BESANCON','1986-12-30',900000083)"
ex_3_client3="INSERT INTO client VALUES (80, 'Ciel','Leila','1 grande rue',39100,'DOLE','1976-07-24',900000001)"
ex_3_client4="INSERT INTO client VALUES (115, 'Dupont','Amelie','3 rue des acacias',25660,'MORRE','1980-02-16',9000000115)"
ex_3_client5="INSERT INTO client VALUES (134, 'Marcheur','Luc','1 grande rue',25000,'BESANCON','1977-06-17',9000000023)"
ex_3_client6="INSERT INTO client VALUES (168, 'Sombre','Hector','8 rue de lhopital',25300,'PONTARLIER','1952-05-24',9000000142)"

cur.execute(ex_3_client1)
cur.execute(ex_3_client2)
cur.execute(ex_3_client3)
cur.execute(ex_3_client4)
cur.execute(ex_3_client5)
cur.execute(ex_3_client6)


ex_3_ticket1="INSERT INTO ticket VALUES (2132, '2019-10-19', '14:32:00', 'CB')"
ex_3_ticket2="INSERT INTO ticket VALUES (3143, '2019-10-20', '09:22:00', 'ESPECE')"
ex_3_ticket3="INSERT INTO ticket VALUES (3542, '2019-10-20', '17:54:00', 'CB')"
ex_3_ticket4="INSERT INTO ticket VALUES (6192, '2019-10-21', '11:15:00', 'CHEQUE')"
ex_3_ticket5="INSERT INTO ticket VALUES (6369, '2019-10-21', '14:24:00', 'CHEQUE')"
ex_3_ticket6="INSERT INTO ticket VALUES (7193, '2019-10-22', '18:15:00', 'CB')"

cur.execute(ex_3_ticket1)
cur.execute(ex_3_ticket2)
cur.execute(ex_3_ticket3)
cur.execute(ex_3_ticket4)
cur.execute(ex_3_ticket5)
cur.execute(ex_3_ticket6)


ex_3_produit1 = "INSERT INTO produit VALUES (31, '1L Jus Pom. Brt',3.56)"
ex_3_produit2 = "INSERT INTO produit VALUES (34, '2Kg Orange Jus ',3.49)"
ex_3_produit3 = "INSERT INTO produit VALUES (35, '1,5KG orange esp', 2.25)"
ex_3_produit4 = "INSERT INTO produit VALUES (37, 'Baguette Rust', 0.9)"
ex_3_produit5 = "INSERT INTO produit VALUES (39,  'Bsc Ptt LycÃ©en', 2.45)"
ex_3_produit6 = "INSERT INTO produit VALUES (40,'Bsc Dino', 2.89)"
ex_3_produit7 = "INSERT INTO produit VALUES (44,'Dent. TpWhite', 1.08)"
ex_3_produit8 = "INSERT INTO produit VALUES (47,'Galette Rois', 7.5)"
ex_3_produit9 = "INSERT INTO produit VALUES (51, 'Huile 5W30 3l', 15.95 )"
ex_3_produit10 = "INSERT INTO produit VALUES (50, 'Lave Glace E 5l', 2.0)"
ex_3_produit11 = "INSERT INTO produit VALUES (54, 'Lave glace H 5l', 2.5)"
ex_3_produit12 = "INSERT INTO produit VALUES (59, 'Mgrt Canard', 7.52)"
ex_3_produit13 = "INSERT INTO produit VALUES (61, 'N&N-S 250g', 3.49)"
ex_3_produit14 = "INSERT INTO produit VALUES (70, 'Pain Ã©pice miel', 6.16)"
ex_3_produit15 = "INSERT INTO produit VALUES (71, 'Semoule Kebab', 2.94)"
ex_3_produit16 = "INSERT INTO produit VALUES (83, 'Buche citron', 9.42)"
cur.execute(ex_3_produit1)
cur.execute(ex_3_produit2)
cur.execute(ex_3_produit3)
cur.execute(ex_3_produit4)
cur.execute(ex_3_produit5)
cur.execute(ex_3_produit6)
cur.execute(ex_3_produit7)
cur.execute(ex_3_produit8)
cur.execute(ex_3_produit9)
cur.execute(ex_3_produit10)
cur.execute(ex_3_produit11)
cur.execute(ex_3_produit12)
cur.execute(ex_3_produit13)
cur.execute(ex_3_produit14)
cur.execute(ex_3_produit15)
cur.execute(ex_3_produit16)


ex_3_possede1 = "INSERT INTO possede VALUES (80,2132)"
ex_3_possede2 = "INSERT INTO possede VALUES (14,3143)"
ex_3_possede3 = "INSERT INTO possede VALUES (115, 3542)"
ex_3_possede4 = "INSERT INTO possede VALUES (134, 6192)"
ex_3_possede5 = "INSERT INTO possede VALUES (53, 6369)"
ex_3_possede6 = "INSERT INTO possede VALUES (168, 7193)"
cur.execute(ex_3_possede1)
cur.execute(ex_3_possede2)
cur.execute(ex_3_possede3)
cur.execute(ex_3_possede4)
cur.execute(ex_3_possede5)
cur.execute(ex_3_possede6)


ex_3_achat1 = "INSERT INTO achat VALUES (2132, 39, 1)"
ex_3_achat2 = "INSERT INTO achat VALUES (2132, 61, 1)"
ex_3_achat3 = "INSERT INTO achat VALUES (2132, 83, 2)"
ex_3_achat4 = "INSERT INTO achat VALUES (2132, 71, 1)"
ex_3_achat5 = "INSERT INTO achat VALUES (2132, 44, 1)"
ex_3_achat6 = "INSERT INTO achat VALUES (3143, 70, 3)"
ex_3_achat7 = "INSERT INTO achat VALUES (3143, 37, 1)"
ex_3_achat8 = "INSERT INTO achat VALUES (3143, 59, 1)"
ex_3_achat9 = "INSERT INTO achat VALUES (3143, 34, 1)"
ex_3_achat10 = "INSERT INTO achat VALUES (3542, 31, 2)"
ex_3_achat11 = "INSERT INTO achat VALUES (3542, 39, 2)"
ex_3_achat12 = "INSERT INTO achat VALUES (3542, 44, 1)"
ex_3_achat13 = "INSERT INTO achat VALUES (3542, 70, 1)"
ex_3_achat14 = "INSERT INTO achat VALUES (6192, 47, 1)"
ex_3_achat15 = "INSERT INTO achat VALUES (6192, 37, 1)"
ex_3_achat16 = "INSERT INTO achat VALUES (6192, 31, 2)"
ex_3_achat17 = "INSERT INTO achat VALUES (6192, 51, 1)"
ex_3_achat18 = "INSERT INTO achat VALUES (6192, 54, 1)"
ex_3_achat19 = "INSERT INTO achat VALUES (6369, 35, 3)"
ex_3_achat20 = "INSERT INTO achat VALUES (6369, 37, 2)"
ex_3_achat21 = "INSERT INTO achat VALUES (6369, 59, 1)"
ex_3_achat22 = "INSERT INTO achat VALUES (6369, 71, 1)"
ex_3_achat23 = "INSERT INTO achat VALUES (6369, 83, 2)"
ex_3_achat24 = "INSERT INTO achat VALUES (7193, 61, 2)"
ex_3_achat25 = "INSERT INTO achat VALUES (7193, 70, 1)"
ex_3_achat26 = "INSERT INTO achat VALUES (7193, 47, 4)"
cur.execute(ex_3_achat1)
cur.execute(ex_3_achat2)
cur.execute(ex_3_achat3)
cur.execute(ex_3_achat4)
cur.execute(ex_3_achat5)
cur.execute(ex_3_achat6)
cur.execute(ex_3_achat7)
cur.execute(ex_3_achat8)
cur.execute(ex_3_achat9)
cur.execute(ex_3_achat10)
cur.execute(ex_3_achat11)
cur.execute(ex_3_achat12)
cur.execute(ex_3_achat13)
cur.execute(ex_3_achat14)
cur.execute(ex_3_achat15)
cur.execute(ex_3_achat16)
cur.execute(ex_3_achat17)
cur.execute(ex_3_achat18)
cur.execute(ex_3_achat19)
cur.execute(ex_3_achat20)
cur.execute(ex_3_achat21)
cur.execute(ex_3_achat22)
cur.execute(ex_3_achat23)
cur.execute(ex_3_achat24)
cur.execute(ex_3_achat25)
cur.execute(ex_3_achat26)


##Question 4:
ex4_q1="SELECT nom,prenom FROM client WHERE cp = 25000" # Les personnes qui habitent Ã  Besancon sont Bertrand Patrice et Marcheur Luc
cur.execute(ex4_q1)

ex4_q2="SELECT prix FROM produit WHERE nom_prod ='Baguette Rust'" # Une baguette Rust coute 0,9â‚¬
cur.execute(ex4_q2)

ex4_q3="UPDATE produit SET prix=0.95 WHERE code_prod=37"
cur.execute(ex4_q3)

ex4_q4="SELECT num_carte FROM client WHERE nom='Ciel' AND prenom='Leila' " # le numÃ©ro de client de Leila Ciel est 900000001
cur.execute(ex4_q4)

ex4_q5="SELECT date_naissance FROM client WHERE nom='Hamelin' AND prenom='Jules' " #La date de naissance de Jules Hamelin est 1986-12-30 (30/12/1986)
cur.execute(ex4_q5)

ex4_q6="SELECT * FROM client ORDER BY nom " #La table client est dÃ©sormais triÃ©e par nom
cur.execute(ex4_q6)

ex4_q7="SELECT COUNT(*) mode_reg FROM ticket WHERE mode_reg='CB' " #Il y a 3 clients qui ont rÃ©glÃ©s en CB
cur.execute(ex4_q7)

ex4_q8="SELECT COUNT(*) mode_reg FROM ticket WHERE mode_reg <> 'CHEQUE'" #Il y a 4 client qui n'ont pas payÃ© en chÃ¨que
cur.execute(ex4_q8)

ex4_q9="SELECT ticket.heure FROM client JOIN possede ON client.identifiant=possede.identifiant JOIN ticket ON possede.num_ticket = ticket.num_ticket WHERE client.nom='Dupont' "
cur.execute(ex4_q9) #Madame Dupont Ã  fait ses courses Ã  17h54


ex4_q10="SELECT client.nom, client.prenom FROM client JOIN possede ON client.identifiant = possede.identifiant JOIN ticket ON possede.num_ticket = ticket.num_ticket JOIN achat ON ticket.num_ticket = achat.num_ticket JOIN produit ON achat.code_produit = produit.code_prod WHERE produit.nom_prod ='Baguette Rust' "
cur.execute(ex4_q10) #Les clients qui ont achÃ©tÃ©s uen Baguette Rust sont Hamelin Jules, Marcheur Luc et Bertrand Patrice.


ex4_q11="SELECT produit.nom_prod FROM produit JOIN possede ON client.identifiant = possede.identifiant JOIN ticket ON possede.num_ticket = ticket.num_ticket JOIN achat ON achat.code_produit = produit.code_prod WHERE nom = 'Ciel'  "
cur.execute(ex4_q11)


ex4_q12="SELECT achat.qte FROM achat JOIN possede ON client.identifiant = possede.identifiant JOIN achat ON possede.num_ticket = achat.num_ticket JOIN produit ON achat.code_produit = produit.code_prod WHERE client.nom = 'Sombre' "
cur.execute(ex4_q12)

affichage="SELECT * FROM client"
##cur.execute(affichage)


for i in cur:
    print(i)


conn.commit()
cur.close()
conn.close