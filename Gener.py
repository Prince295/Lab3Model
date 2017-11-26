import numpy as np
from MathO import *


class Gen(object):
    e = np.exp(1)
    z = 0
    zmax = e - 1
    f1 = np.random.random()

    def function(self,f1):
        x = 1/(f1+1)
        return x


    def recursive_function(self,f1):
        self.z = pow(self.e, f1) - 1
        return self.z

    def array_of_func(self, n):
        array = []
        for i in range(n):
            f1 = np.random.random()
            array.append(self.recursive_function(self,f1))
        array.sort()
        return array

    def cut(self,l1,l2,x,n):
        xone=0
        xtwo=0
        i=0
        j=0
        while l1 > x[i]:
            xone = i
            i += 1
            if i > n-1:
                break
        while l2 > x[j]:
            xtwo = j
            j+=1
            if j>n-1:
                break

        return xone,xtwo


