from vpython import *
from exceptions import *
from utils import *
from __future__ import division, print_function
from math import *

def momentum_principle(dp: vec, Fnet: vec, dt: float):
    # dp = Fnet * dt

    if dp is not None and Fnet is not None:
        return Divide(dp, Fnet)
    elif dp is not None and dt is not None:
        return dp/dt
    elif dt is not None and Fnet is not None:
        return Fnet * dt
    else:
        raise not_enough_params(2)

def momentum_principle_scalar(dp, Fnet, dt: float):
    #dp = Fnet * dt

    if dp is not None and Fnet is not None:
        return dp/Fnet
    elif dp is not None and dt is not None:
        return dp/dt
    elif dt is not None and Fnet is not None:
        return Fnet * dt
    else:
        raise not_enough_params(2)

def vector_update(f: vec, i: vec, delta: vec, dt: float):
    # vf = vi + a * dt

    if i is not None and f is not None and delta is not None:
        return Divide(f - i, delta)
    elif f is not None and delta is not None and dt is not None:
        return f - delta * dt
    elif f is not None and i is not None and dt is not None:
        return (f - i)/dt
    elif i is not None and delta is not None and dt is not None:
        return i + delta * dt
    else:
        raise not_enough_params(3)

def scalar_update(f, i, delta, dt: float):
    # vf = vi + a * dt

    if i is not None and f is not None and delta is not None:
        return (f - i)/delta
    elif f is not None and delta is not None and dt is not None:
        return f - delta * dt
    elif f is not None and i is not None and dt is not None:
        return (f - i)/dt
    elif i is not None and delta is not None and dt is not None:
        return i + delta * dt
    else:
        raise not_enough_params(3)

def momentum(p: vec, m: float, v: vec):
    # p = m * v

    if p is not None and m is not None:
        return p/m
    elif m is not None and v is not None:
        return m * v
    elif p is not None and v is not None:
        return Divide(p/v)
    else:
        not_enough_params(2)


def force(F: vec, m: float, a: vec):
    # p = m * v

    if F is not None and m is not None:
        return F / m
    elif m is not None and a is not None:
        return m * a
    elif F is not None and a is not None:
        return Divide(F / a)
    else:
        not_enough_params(2)

def position_update_force(rf: vec, ri: vec, v: vec, dt: float, a: vec):
    # rf = ri + v * dt + 1/2 * a * dt**2

    if ri is not None and v is not None and dt is not None and a is not None:
        return ri + v * dt + 1/2 * a * dt**2
    elif ri is not None and rf is not None and v is not None and dt is not None:
        return (rf - ri - v * dt)/dt**2
    elif ri is not None and v is not None and dt is not None and a is not None:
        return (rf - ri - 1/2 * a * dt**2)/dt
    elif rf is not None and v is not None and dt is not None and a is not None:
        return rf - v * dt - 1/2 * a * dt**2
    elif rf is not None and ri is not None and v is not None and a is not None:
        return [
            Divide(-v + sqrt(Dot(v, v) - 4*Dot(a, ri)), 2*a),
            Divide(-v - sqrt(Dot(v, v) - 4 * Dot(a, ri)), 2 * a)
        ]
    else:
        return not_enough_params(4)