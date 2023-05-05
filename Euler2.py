def Euler2(n):  #y'a une erreur dénoncé, ça doit donner un résultat entier positif différent de 0 car sinon, -2520 est plus petit que 2520 et 0 est plus petit que 2520
    '''n: entier naturel différent de 0
    Renvoie le plus petit entier positif différent de 0 qui est divisible par tout les entiers naturelle de 1 à n'''
    pnd=1
    r=1
    while True: #c'est pas stupide si ça marche
        while pnd%r==0:
            if r==n:
                return(pnd)
            r+=1
        r=1
        pnd=pnd+1
