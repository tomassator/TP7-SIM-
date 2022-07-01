import random
import math

#Modulo que devuelve un rnd con una determinada distribucion segun corresponda


def rnd_uniforme(li, ls):
    rnd = random.random()
    calculo = li + (rnd * (ls-li))
    return round(rnd, 3), round(calculo,3)



def rnd_exponencial(media):
    rnd = random.random()
    calculo = -media * math.log(1 - rnd)
    return round(rnd, 3), round(calculo,3)