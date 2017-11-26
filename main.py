import matplotlib.pyplot as plt
from MathO import *

class Main(object):
    plt.xlabel("Значения X")
    plt.ylabel("плотность распределения p*")
    plt.title("Гистограмма плотности")

    plt.bar( Math1.otr,Math1.p, align='center', width=0.1, color = 'violet' )
    plt.grid(True)
    plt.show()
    print( len(Math1.otr), len(Math1.p), Math1.Pearson(Math1),np.sqrt(Math1.disp(Math1)),sum(Math1.n1), Math1.disp(Math1), Math1.n1,Math1.pint(Math1),sum(Math1.pint(Math1)) )