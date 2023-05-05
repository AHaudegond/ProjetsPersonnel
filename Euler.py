def Euler(n): #programme qui marche dans l'unique cas avec 1000 chiffres et l'on cherche le plus grand produit de 13 chiffre adjacent
    '''n:Nombre de 1000 chiffres
        sortie: liste des 13 chiffres adjacent dont le produit est le plus grand dans n'''
    LC=[]
    for x in list(str(n)):
        LC.append(int(x)) #transforme n en liste de chiffre qui le compose
    LR=[LC[0],LC[1],LC[2],LC[3],LC[4],LC[5],LC[6],LC[7],LC[8],LC[9],LC[10],LC[11],LC[12]] #donne une valeur de référence dans la liste qui est utilise pour la comparaison
    for i in range(988): #boucle pour tester toutes les suites de 13 chiffres possible
        if LC[i]*LC[i+1]*LC[i+2]*LC[i+3]*LC[i+4]*LC[i+5]*LC[i+6]*LC[i+7]*LC[i+8]*LC[i+9]*LC[i+10]*LC[i+11]*LC[i+12]>LR[0]*LR[1]*LR[2]*LR[3]*LR[4]*LR[5]*LR[6]*LR[7]*LR[8]*LR[9]*LR[10]*LR[11]*LR[12]: #test si la valeur d'une suite est plus grande que la valeur de référence
            LR=[LC[i],LC[i+1],LC[i+2],LC[i+3],LC[i+4],LC[i+5],LC[i+6],LC[i+7],LC[i+8],LC[i+9],LC[i+10],LC[i+11],LC[i+12]] # si la valeur testé est plus grande, on remplace la valeur de référence par la valeur testé pour garder la plus grande suite
    return LR

def Eulergen(n,d):# programme qui cherche à être plus généraliste que Euler3 avec des variables
    '''n:integer entier naturel
        d:nombre de chiffre adjcant souhaité, integer entier naturel différent de 0 et inférieure ou égale au nombre de chiffres de n
        sortie: liste des d chiffres adjacent dont le produit est le plus grand dans n'''
    LC=[]
    for x in list(str(n)):
        LC.append(int(x)) #transforme n en liste de chiffre qui le compose
    LI=[LC[0]]
    produit=LC[0]
    for i in range(1,d+1):
        LI.append(LC[i])
        produit=produit*LC[i] # construction d'une suite de référence
    LR=[]
    for i in range(len(list(str(n)))+1-d):#construction d'une suite testée
        LR=[LC[i]]
        test=LC[i]
        for j in range(1,d):
            LR.append(LC[j])
            test*=LC[j]#construction du produit des valeurs des d chiffres à la suite
        if test>produit:#comparaison de la suite de référence et suite testée
            produit=test#on garde le produit le plus grand
            LI=LR[:]# on garde en mémoires les chiffres qui donne le produit le plus grand
    return LI
