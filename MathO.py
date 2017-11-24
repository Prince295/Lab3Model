import numpy as np
from Gener import *


class Math1(object):

    n = 500
    m = 30
    deltax = (np.exp(1) - 1) / m
    x = Gen.array_of_func( Gen, n )
    v = [0]
    p = [0]
    n1=[0]
    otr = [0]
    x1 = 0

    for j in range( m - 1 ):
        otr.append(x1 + deltax)
        x1 = otr[j]
        v.append( (otr[j-1]+otr[j]) / 2 )
        xone,xtwo = Gen.cut(Gen,otr[j-1], otr[j],x)
        n1.append(xtwo-xone)
        p.append( n1[j] / n )



    def expected_value(self):
        sum=0
        for i in range(len(self.p)):
            sum=sum+self.p[i]*self.v[i]
        return sum/2

print (Math1.expected_value(Math1), len(Math1.p), len(Math1.v), Math1.x)