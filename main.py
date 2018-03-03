from functools import reduce

import matplotlib.pyplot as plt
import numpy as np
import math

def sumProizv(xCollection, yCollection):
    return reduce(lambda x, y: x + y, [xCollection[i] * yCollection[i] for i in range(0, len(xCollection) if (len(xCollection) <= len(yCollection)) else len(yCollection))])

def sumQuard(collection):
    return sum(map(lambda x: x**2, collection))

def average(collection):
    sum = 0
    for i in collection:
        sum += i
    return sum/len(collection)

if __name__ == "__main__":

    file = open("./data.txt")
    rows = file.readlines()
    file.close()

    rawdata = [i.split(",") for i in rows]
    coordinate1 = [float(i[0]) for i in rawdata]
    coordinate2 = [float(i[2]) for i in rawdata]


    #coordinate1 = coordinate1[:LENGTH]
    #coordinate2 = coordinate2[:LENGTH]
    tTabl = 2.0
    COUNT = len(coordinate1)

    coordinate1 = sorted(coordinate1)
    print(coordinate1)

    MATOZHX = sum(coordinate1) / COUNT
    DISPERSX = sum([(i - MATOZHX) ** 2 for i in coordinate1]) / COUNT
    print(DISPERSX)
    STANDOTKLX = sum([(i - MATOZHX) ** 2 for i in coordinate1]) / (COUNT - 1)
    QUARDOTKLX = math.sqrt(DISPERSX)
    print("quardotkl = " + str(QUARDOTKLX))
    MARKQUARDOTKLX = math.sqrt(STANDOTKLX)
    DELTAX = tTabl * (MARKQUARDOTKLX / math.sqrt(COUNT))

    MATOZHY = sum(coordinate2) / COUNT
    DISPERSY = sum([(i - MATOZHY) ** 2 for i in coordinate2]) / COUNT
    STANDOTKLY = sum([(i - MATOZHY) ** 2 for i in coordinate2]) / (COUNT - 1)

    Tn = (MATOZHX - MATOZHY)/math.sqrt(DISPERSX/COUNT + DISPERSY/COUNT)
    print("Tn = " + str(Tn))

    #level of important
    a = 0.95
    print("Известная дисперсия:")
    if abs(Tn) > DISPERSX/DISPERSY : # Fisher
        print("Гипотеза опровергнута")
    else:
        print("Гипотеза подтверждена")

    Ssmesh = (((COUNT - 1) * STANDOTKLX + (COUNT - 1) * STANDOTKLY) / (COUNT + COUNT - 2)) * (2 / COUNT)

    Tun = (MATOZHX - MATOZHY) / math.sqrt(Ssmesh)

    Tkr = math.sqrt(-2 * math.log(math.sqrt(2*math.pi) * (1 - a)))

    print("Неизвестная дисперсия:")

    print("T = " + str(Tun))
    print("Tkrit = " + str(Tkr))

    if (abs(Tun) > Tkr) :
        print("Гипотеза опровергнута")
    else:
        print("Гипотеза подтверждена")
    print("INTERVAL: ( " + str(MATOZHX) + " - " + str(DELTAX) + "; " + str(MATOZHX) + " + " + str(DELTAX) + ")")
