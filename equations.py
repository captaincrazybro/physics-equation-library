from vpython import *
from exceptions import *
from utils import *
from math import *

def momentum_principle(dp: vec = None, Fnet: vec = None, dt: float = None):
    if dp is not None and Fnet is not None:
        raise cannot_divide_vectors()
    elif dp is not None and dt is not None:
        return dp / dt
    elif dt is not None and Fnet is not None:
        return Fnet * dt
    else:
        raise not_enough_params(2)


def momentum_principle(dp: float = None, Fnet: float = None, dt: float = None):
    # dp = Fnet * dt

    if dp is not None and Fnet is not None:
        return dp / Fnet
    elif dp is not None and dt is not None:
        return dp / dt
    elif dt is not None and Fnet is not None:
        return Fnet * dt
    else:
        raise not_enough_params(2)


def pdate(f: vec = None, i: vec = None, delta: vec = None, dt: float = None):
    # vf = vi + a * dt

    if i is not None and f is not None and delta is not None:
        raise cannot_divide_vectors()
    elif f is not None and delta is not None and dt is not None:
        return f - delta * dt
    elif f is not None and i is not None and dt is not None:
        return (f - i) / dt
    elif i is not None and delta is not None and dt is not None:
        return i + delta * dt
    else:
        raise not_enough_params(3)


def update(f: float = None, i: float = None, delta: float = None, dt: float = None):
    # vf = vi + a * dt

    if i is not None and f is not None and delta is not None:
        return (f - i) / delta
    elif f is not None and delta is not None and dt is not None:
        return f - delta * dt
    elif f is not None and i is not None and dt is not None:
        return (f - i) / dt
    elif i is not None and delta is not None and dt is not None:
        return i + delta * dt
    else:
        raise not_enough_params(3)


def momentum(p: vec = None, m: float = None, v: vec = None):
    # p = m * v

    if p is not None and m is not None:
        return p / m
    elif m is not None and v is not None:
        return m * v
    elif p is not None and v is not None:
        raise cannot_divide_vectors()
    else:
        raise not_enough_params(2)


def force(F: vec = None, m: float = None, a: vec = None):
    # Fnet = m * a

    if F is not None and m is not None:
        return F / m
    elif m is not None and a is not None:
        return m * a
    elif F is not None and a is not None:
        raise cannot_divide_vectors()
    else:
        raise not_enough_params(2)

def force(F: float = None, m: float = None, a: float = None):
    # Fnet = m * a

    if F is not None and m is not None:
        return F/m
    elif F is not None and a is not None:
        return F/a
    elif m is not None and a is not None:
        return m * a
    else:
        raise not_enough_params(2)

def position_update(rf: vec = None, ri: vec = None, v: vec = None, dt: float = None, a: vec = None):
    # rf = ri + v * dt + 1/2 * a * dt**2

    if ri is not None and v is not None and dt is not None and a is not None:
        return ri + v * dt + 1 / 2 * a * dt ** 2
    elif ri is not None and rf is not None and v is not None and dt is not None:
        return (rf - ri - v * dt) / dt ** 2
    elif ri is not None and v is not None and dt is not None and a is not None:
        return (rf - ri - 1 / 2 * a * dt ** 2) / dt
    elif rf is not None and v is not None and dt is not None and a is not None:
        return rf - v * dt - 1 / 2 * a * dt ** 2
    elif rf is not None and ri is not None and v is not None and a is not None:
        raise cannot_divide_vectors()
    else:
        raise not_enough_params(4)

def position_update(rf: float = None, ri: float = None, v: float = None, dt: float = None, a: float = None):
    # rf = ri + v * dt + 1/2 * a * dt**2

    if ri is not None and v is not None and dt is not None and a is not None:
        return ri + v * dt + 1 / 2 * a * dt ** 2
    elif ri is not None and rf is not None and v is not None and dt is not None:
        return (rf - ri - v * dt) / dt ** 2
    elif ri is not None and v is not None and dt is not None and a is not None:
        return (rf - ri - 1 / 2 * a * dt ** 2) / dt
    elif rf is not None and v is not None and dt is not None and a is not None:
        return rf - v * dt - 1 / 2 * a * dt ** 2
    elif rf is not None and ri is not None and v is not None and a is not None:
        return [
            (-v + sqrt(v**2 - 4 * a * ri))/(2 * a),
            (-v - sqrt(v**2 - 4 * a * ri))/(2 * a)
        ]
    else:
        raise not_enough_params(4)