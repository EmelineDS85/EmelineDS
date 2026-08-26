from turtle import* #importation de l'extension
reset() #permet de remettre tout le programme à 0

def début() : #définir la fonction début
    penup() #lever son stylo
    goto(-200,-250) #permet de se téléporter aux coordonnées demandées
    pendown() #baisser son stylo
    forward(400) #aller tout droit sur 400 pixels


def vertical() : #définir la fonction vertical
    penup() #lever son stylo
    goto(-100,-250) #permet de se téléporter aux coordonnées demandées
    left(90) #tourner de 90 degrés à gauche
    pendown() #baisser son stylo
    forward(300) #aller tout droit sur 300 pixels


def horizontal() : #définir la fonction horizontal
    penup() #lever son stylo
    goto(-100,50) #permet de se téléporter aux coordonnées demandées
    right(90) #tourner de 90 degrés à droite
    pendown() #baisser son stylo
    forward(250) #aller tout droit sur 250 pixels
    

def corde() : #définir la fonction corde
    penup() #lever son stylo
    goto(150,50) #permet de se téléporter aux coordonnées demandées
    right(90) #tourner de 90 degrés à droite
    pendown() #baisser son stylo
    forward(50) #aller tout droit sur 50 pixels


def tete() : #définir la fonction tete
    penup() #lever son stylo
    goto(120, -30) #permet de se téléporter aux coordonnées demandées
    pendown() #baisser son stylo
    circle(30) #faire un cercle de 30 de rayon


def corps() : #définir la fonction corps
    penup() #lever son stylo
    goto(150,-60) #permet de se téléporter aux coordonnées demandées
    pendown() #baisser son stylo
    forward(100) #aller tout droit sur 100 pixels


def bras() : #définir la fonction bras
    penup() #lever son stylo
    goto(110,-100) #permet de se téléporter aux coordonnées demandées
    left(90) #tourner de 90 degrés à gauche
    pendown() #baisser son stylo
    forward(80) #aller tout droit sur 80 pixels


def jambes() : #définir la fonction jambes
    penup() #lever son stylo
    goto(150,-160) #permet de se téléporter aux coordonnées demandées
    right(45) #tourner de 45 degrés à droite
    pendown() #baisser son stylo
    forward(45) #aller tout droit sur 45 pixels
    left(180) #tourner de 180 degrés à gauche
    forward(45) #aller tout droit sur 45 pixels
    left(90) #tourner de ... degrés à gauche
    forward(45) #aller tout droit sur 45 pixels

nombre = int(input() #créer une variable nombre où l'on rentre notre nombre
if nombre == 1 : #si la variable nombre est égale à 1 alors...
    print (début()) #...afficher la fonction début
elif nombre == 2 : #si la variable nombre est égale à 2 alors...
    print(vertical()) #...afficher la fonction vertical
elif nombre == 3 : #si la variable nombre est égale à 3 alors...
    print (horizontal()) #...afficher la fonction horizontal
elif nombre == 4 : #si la variable nombre est égale à 4 alors...
    print (corde()) #...afficher la fonction corde
elif nombre == 5 : #si la variable nombre est égale à 5 alors...
    print (tete()) #...afficher la fonction tete
elif nombre == 6 : #si la variable nombre est égale à 6 alors...
    print (corps()) #...afficher la fonction corps
elif nombre == 7 : #si la variable nombre est égale à 7 alors...
    print (bras()) #...afficher la fonction bras
elif nombre == 8 : #si la variable nombre est égale à 8 alors...
    print (jambes()) #...afficher la fonction jambes