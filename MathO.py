import Generator
import numpy as np
class MathO():
    n=500
    m=30
    deltax=(Generator.e-1)/m
    x = Generator.array_of_func( n )
    v=[]
    nj=[]
    p=[]
    for j in range(m-1):
        v.append((x[int(j*n/m)]+x[int((j+1)*n/m)])/2)
        nj.append(len(x[int(j*n/m):int((j+1)*n/m)]))
        p.append(nj[j]/n)

    def dispersy(self):

    def oj(self):