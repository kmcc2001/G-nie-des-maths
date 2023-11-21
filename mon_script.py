from random import randint

nbre1 = randint(0, 10)
nbre2 = randint(1, 10)  

resultat = nbre1 * nbre2  
quotient = int(resultat / nbre1)  

if resultat == quotient:
    print("Bravo!, vous êtes un génie des maths")
    
elif resultat == quotient + 1 or resultat == quotient - 1:
    print("Presque!")

elif resultat == quotient + 2:
    print("Raté, manque de concentration")