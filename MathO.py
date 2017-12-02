import numpy as np
from Gener import *


class Math1(object):

    n = int(input("ВВедите n "))
    m = int(n/17)

    if n>=500:
        m=30
    P=0.01
    deltax = (np.exp(1) - 1) / m
    x = Gen.array_of_func(Gen,n)
    v = []
    p = []
    n1=[]
    otr = [0]
    num=[]
    x1 = 0
    a =np.sum(x)/n


    for j in range( m ):
        otr.append(x1 + deltax)
        x1 = otr[j+1]

        xone,xtwo = Gen.cut(Gen,otr[j], otr[j+1],x,n)
        v.append( (otr[j]+otr[j+1]) / 2 )
        num.append((xone,xtwo))
        n1.append(xtwo-xone)
        p.append( n1[j] / n )
    otr.pop(otr[0])


    def pint(self):
        sigma = np.sqrt( self.disp( self ) )
        p1=[]
        for i in range(len(self.p)):
            xone,xtwo=self.num[i]
            fp = (self.x[int(xone)]-self.expected_value(self))/sigma
            sp = (self.x[int(xtwo)]-self.expected_value(self))/sigma
            ffp=Gen.recursive_function(Gen,sp) - Gen.recursive_function(Gen,fp)
            p1.append(ffp)
        return p1

    def expected_value(self):
        sum=0
        for i in range(len(self.p)):
            sum=sum+self.n1[i]*self.v[i]
        return sum/self.n

    def disp(self):
        sum=0
        ma=self.expected_value(self)
        for i in range(len(self.n1)):
            sum=sum+self.p[i]*(self.v[i]-ma)*(self.v[i]-ma)
        return sum


    def Pearson(self):
        XI=0
        p1=self.pint(self)
        for i in range(len(self.n1)):
            XI=XI+(self.n1[i]-self.n*p1[i])*(self.n1[i]-self.n*p1[i])/(self.n*p1[i])
        return XI*self.P
