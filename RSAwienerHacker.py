'''
Created on Dec 14, 2011

@author: pablocelayes
'''

import ContinuedFractions, Arithmetic, RSAvulnerableKeyGenerator, decryptor

def hack_RSA(e,n):
    '''
    Finds d knowing (e,n)
    applying the Wiener continued fraction attack
    '''
    frac = ContinuedFractions.rational_to_contfrac(e, n)
    convergents = ContinuedFractions.convergents_from_contfrac(frac)
    
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
                    print "-------------------------"
                    return d

# TEST functions

def test_hack_RSA():
    print("Testing Wiener Attack")
    
    with open('2.2_public_key.hex') as pub:
        e = int(pub.read(), 16)
    pub.close()
    with open('2.2_modulo.hex') as mod:
        n = int(mod.read(), 16)
    mod.close()

    print "(e,n) is (", e, ", ", n, ")"
    print "d = ?" 

    hacked_d = hack_RSA(e, n)
    msg = decryptor.decrypt(hacked_d)
    print "The message:\n"+str(msg)+"\n"
    
    print "hacked_d = ", hacked_d 
    print "-------------------------"
    
if __name__ == "__main__":
    #test_is_perfect_square()
    #print("-------------------------")
    test_hack_RSA()


    


        
    
