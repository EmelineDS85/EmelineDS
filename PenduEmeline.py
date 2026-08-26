# fini
from turtle import* #importation de l'extension
reset() #permet de remettre tout le programme a 0

mot = str(input("mot: ")) #demander le mot
mot_secret = list(mot) #transformer le mot en liste
mot_cache = [] #initialiser la variable mot_cache
reponse = [] #initialiser la variable reponse
compteur = 0 #mettre le compteur a 0
faux = [] #initialiser la variable faux


def pendu(compteur) : #definir la fonction pendu
    hideturtle()
    if compteur == 1 : #si le compteur est a 1 alors...
        penup() #lever son stylo
        goto(-200, -250) #permet de se teleporter aux coordonnees demandees
        pendown() #baisser son stylo
        forward(400) #aller tout droit sur 400 pixels
        
    elif compteur == 2 : #si le compteur est a 2 alors...
        penup() #lever son stylo
        goto(-100, -250) #permet de se teleporter aux coordonnees demandees
        left(90) #tourner de 90 degres a gauche
        pendown() #baisser son stylo
        forward(300) #aller tout droit sur 300 pixels
        
    elif compteur == 3 : #si le compteur est a 3 alors...
        penup() #lever son stylo
        goto(-100, 50) #permet de se teleporter aux coordonnees demandees
        right(90) #tourner de 90 degres a droite
        pendown() #baisser son stylo
        forward(250) #aller tout droit sur 250 pixels
        
    elif compteur == 4 : #si le compteur est a 4 alors...
        penup() #lever son stylo
        goto(150, 50) #permet de se teleporter aux coordonnees demandees
        right(90) #tourner de 90 degres a droite
        pendown() #baisser son stylo
        forward(50) #aller tout droit sur 50 pixels
        
    elif compteur == 5 : #si le compteur est a 5 alors...
        penup() #lever son stylo
        goto(120, -30) #permet de se teleporter aux coordonnees demandees
        pendown() #baisser son stylo
        circle(30) #faire un cercle de 30 de rayon
        
    elif compteur == 6 : #si le compteur est a 6 alors...
        penup() #lever son stylo
        goto(150, -60) #permet de se teleporter aux coordonnees demandees
        pendown() #baisser son stylo
        forward(100) #aller tout droit sur 100 pixels
        
    elif compteur == 7 : #si le compteur est a 7 alors...
        penup() #lever son stylo
        goto(110, -100) #permet de se teleporter aux coordonnees demandees
        left(90) #tourner de 90 degres a gauche
        pendown() #baisser son stylo
        forward(80) #aller tout droit sur 80 pixels
        
    elif compteur == 8 : #si le compteur est a 8 alors...
        penup() #lever son stylo
        goto(150, -160) #permet de se teleporter aux coordonnees demandees
        right(45) #tourner de 45 degres a droite
        pendown() #baisser son stylo
        forward(45) #aller tout droit sur 45 pixels
        left(180) #tourner de 180 degres a gauche
        forward(45) #aller tout droit sur 45 pixels
        left(90) #tourner de ... degres a gauche
        forward(45) #aller tout droit sur 45 pixels

def demande_mot(mot_secret, mot_cache, letres_fausses): #verifie si lettre mot

    lettre = str(input())#demander la lettre
    compteur_lettre = -1 #initialiser le compteur de lettres
    trouve = False #mettre la variable trouve sur False
    for j in mot_secret: #pour j dans le mot_secret
        compteur_lettre += 1 #ajouter 1 au compteur_lettre
        if lettre == j: #si lettre est egal a j
            mot_cache[compteur_lettre] = lettre #ajouter la lettre a mot_cache
            trouve = True #mettre a trouver : True 
        elif lettre not in letres_fausses and lettre not in mot_secret:
        #sinon si la letre n'est ni dans letre fausse ni dans mot secret
                    letres_fausses.append(lettre)
                    #ajouter letre a la liste de letres fausses 
    return mot_cache, trouve, letres_fausses 
    #renvoyer les lsites mot cacher trouve et letre fausse 



for i in range(len(mot_secret)):#eloigne le mot et cree une liste 
    print(".")#eloigner le mot pour qi' il ne soit pas decouvert
    mot_cache.append("_")#cree la liste ou on feras aparaitre le mot
print(mot_cache)#afficher mot cache
while  mot_secret != reponse and compteur<8:
    #tant que reponse n'est pas egale a reponse et compteur<8
    reponse, trouve, faux = demande_mot(mot_secret, mot_cache, faux)
    #donner les valeurs de reponse, trouve et faux
    if trouve == False: #si trouve est egal a Faux
        compteur += 1 #alors ajouter 1 au compteur
        print (pendu(compteur)) #Afficher pendu avec compteur
    print(reponse) #afficher reponse
    print("lettres deja utiliees:", faux) 
    #afficher les lettres deja utilisees
if compteur<8: #si le compteur<8
    print("TU AS GAGNe!!! le mot etait bien:", mot) 
    #alors afficher "TU AS GAGNe!!! le mot etait bien:" suivi du mot
else: #sinon
    print("tu a perdu :,( le mot etait :", mot)
    #afficher "tu a perdu :,( le mot etait :" suivi du mot
