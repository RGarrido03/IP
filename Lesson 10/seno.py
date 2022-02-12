import numpy as np
import math

def seno(x,terms=6): #by default uses 6 terms
    """ Approximates sin(x) using a given number of terms of
        the Maclaurin series
    """    
    # ...complete the function using np functions 
    n = np.arange(terms)
    fac = np.vectorize(math.factorial)
    soma = np.sum((-1)**n * x**(2*n+1)/fac(2*n+1))
    return soma

def seno2(x, terms=6):
    """ Approximates sin(x) using a given number of terms of
        the Maclaurin series
    """     
    soma = 0.0
    for n in range(terms):
        soma += ((-1)**n * x ** (2*n+1)) / math.factorial(2*n +1)
    return soma

def main():
    ntermos = 6
    angulo = np.pi/2
    print("seno2    :",seno2(angulo, ntermos))
    m = seno(angulo, ntermos)
    print(f"Macl seno: {m}\nMath.sin :{math.sin(angulo)}")

    #Gera um array de angulos e calcula array com os respetivos senos
    angulos = np.array([math.pi/4*n for n in range(0,6)])
    print(angulos)
    sen = np.vectorize(seno2)
    senos = sen(angulos)
    print(senos)
    np.set_printoptions(precision=4, suppress=True) 
    print(senos)
    #Formatar array para impressão
    #np.set_printoptions(precision=None, suppress=None) 
    #np.set_printoptions(formatter={'float': '{: 8.3f}'.format})
    
main()
