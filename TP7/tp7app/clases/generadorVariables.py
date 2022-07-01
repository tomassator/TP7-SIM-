import random
import math

#Modulo que devuelve un rnd con una determinada distribucion segun corresponda


def rnd_uniforme(li, ls):

    calculo = li + (random.random() * (ls-li))
    return round(calculo,3)



def rnd_exponencial(media):
    calculo = -media * math.log(1 - random.random())
    return round(calculo,3)