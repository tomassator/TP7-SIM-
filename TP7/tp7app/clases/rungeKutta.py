import math
import time

def funcion_secado(x0, y0):
    return ((31*y0) + 5)




def rk4_secado(x0, y0, h=0.001, para_mostrar=False):
    vectores = []

    while y0 <= 60 :
        k1 = h * (funcion_secado(x0, y0))
        k2 = h * (funcion_secado((x0 + h / 2), (y0 + k1 / 2)))
        k3 = h * (funcion_secado((x0 + h / 2), (y0 + k2 / 2)))
        k4 = h * (funcion_secado((x0 + h), (y0 + k3)))
        k = (k1 + 2 * k2 + 2 * k3 + k4) / 6
        yn = y0 + k

        if para_mostrar:
            vectores.append([x0, y0, k1, k2, k3, k4, yn])
        y0 = yn
        x0 = round(x0 + h, 5)

    if para_mostrar:
        vectores.append([x0, y0, "-", "-", "-", "-", "-"])
        return vectores


    return round(x0, 3)





