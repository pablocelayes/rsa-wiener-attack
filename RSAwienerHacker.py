'''
Created on Dec 14, 2011

@author: pablocelayes
'''

import ContinuedFractions, Arithmetic

def hack_RSA(e,n):
    '''
    Finds d knowing (e,n)
    applying the Wiener continued fraction attack
    '''
    _, convergents = ContinuedFractions.rational_to_contfrac(e, n)
    
    for (k,d) in convergents:
        
        #check if d is actually the key
        if k!=0 and (e*d-1)%k == 0:
            phi = (e*d-1)//k
            s = n - phi + 1
            # check if the equation x^2 - s*x + n = 0
            # has integer roots
            discr = s*s - 4*n
            if(discr>=0):
                t = Arithmetic.is_perfect_square(discr)
                if t!=-1 and (s+t)%2==0:
                    print("Hacked!")
                    return d


        
    
