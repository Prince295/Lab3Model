import matplotlib.pyplot as plt
from Table import *
from MathO import *

class Main(object):
    fig = plt.figure( 1 )
    plt.xlabel("Значения X")
    plt.ylabel("плотность распределения p*")
    plt.title("Гистограмма плотности функции распределения")
    plt.bar( Math1.otr,Math1.p, align='center', width=0.1, color = 'violet' )
    plt.grid(True)


    fig2 = plt.figure( 2 )
    plt.xlabel( "Значения X" )
    plt.ylabel( "плотность распределения p*" )
    plt.title( "Гистограмма плотности по распределению Пирсона" )
    plt.bar( Math1.pint(Math1), Math1.p , align='center', width=0.1, color='violet' )
    plt.grid( True )
    plt.show()

    if Math1.Pearson(Math1) < tabl_value[Math1.m - 1]:
        print("Теоретическое распределение согласуется с выборочным" )
    else:
        print("Теоретическое распределение не согласуется с выборочным")