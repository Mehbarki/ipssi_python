#!/usr/bin/python3

from datetime import datetime

#Fonction qui affiche la multiplication du nombre que l'on veut avec les nombre
# d'itérations

def multiplication(nb, max):
    i = 0
    while i < max:
        print(i+1, "*", nb, "=", (i+1) * nb)
        i += 1

#fonction moyenne(nb1,nb2)
def avg(a, b):
    return (a+b)/2



#fonction estPair(nb)
def estPair():
    d = datetime.now()
    if d.day % 2 != 0:
       print("Le nombre est pair")
    else:
        print("Le nombre est impair")

multiplication(10,20)
print(avg(3,8))
estPair()
