def Euler(n):
    '''n: entier naturel différent de 0
        Renvoie le plus grand facteur premier de n'''
    r=0
    facteur=[]
    while n%2==0: #je compte la puissance de 2 dans n pour diminuer les calculs dans la partie suivante
        n=n/2
        r=r+1
    if n==1:
        return 2
    for i in range(3,int(M.sqrt(n))): #je cherche dans l'ordre croissant les diviseurs de mon nouveau n
        while n%i==0: #j'utilise une boucle while pour ne pas ajouter i si i n'est pas un diviseur (comme un if) et l'ajouter plusieurs fois si il apparait plusieurs fois (ex: 25=5*5)
            facteur.append(i)
            n=n/i
    for i in range(r):
        facteur=[2]+facteur
    return facteur[-1]
