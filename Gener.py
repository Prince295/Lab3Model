import numpy as np
from MathO import *


class Gen(object):
    e = np.exp(1)
    z = 0
    zmax = e - 1

    def recursive_function(self):
        f1 = np.random.random()
        self.z = pow(self.e, f1) - 1
        return self.z

    def array_of_func(self, n):
        array = []
        for i in range(n):
            array.append(self.recursive_function(self))
        array.sort()
        return array

    def cut(self,l1,l2,x):
        xone=0
        xtwo=len(x)
        for i in range(len(x)):
            if l1<=x[i]:
                xone = i
                break
        for j in range(len(x)):
            if l2<=x[i]:
                xtwo = x[i-1]
                break

        return xone,xtwo


