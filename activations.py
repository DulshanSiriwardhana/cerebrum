import math

def normal(x):
    return x/(x+1)

def sin(x):
    return math.abs(math.sin(x))

def cos(x):
    return math.abs(math.cos(x))

def exp(x):
    return math.exp(-x)

def piStep(x):
    ret = x/(x+1)
    if ret <1/math.pi:
        return 0
    return 1