from vpython import *
from exceptions import *
from utils import *
from math import *
from enum import Enum

class Accuracy(Enum):
    LOW = 1
    HIGH = 2

class Equations:

    accuracy: Accuracy

    def __init__(self, accuracy: Accuracy = Accuracy.LOW):
        self.accuracy = accuracy

    def momentum_principle(self, dp: vec = None, Fnet: vec = None, dt: float = None):
        if dp is not None and Fnet is not None:
            raise cannot_divide_vectors()
        elif dp is not None and dt is not None:
            return dp / dt
        elif dt is not None and Fnet is not None:
            return Fnet * dt
        else:
            raise not_enough_params(2)


    def momentum_principle(self, dp: float = None, Fnet: float = None, dt: float = None):
        # dp = Fnet * dt

        if dp is not None and Fnet is not None:
            return dp / Fnet
        elif dp is not None and dt is not None:
            return dp / dt
        elif dt is not None and Fnet is not None:
            return Fnet * dt
        else:
            raise not_enough_params(2)


    def pdate(self, f: vec = None, i: vec = None, delta: vec = None, dt: float = None):
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


    def update(self, f: float = None, i: float = None, delta: float = None, dt: float = None):
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


    def momentum(self, p: vec = None, m: float = None, v: vec = None):
        # p = m * v

        if p is not None and m is not None:
            return p / m
        elif m is not None and v is not None:
            return m * v
        elif p is not None and v is not None:
            raise cannot_divide_vectors()
        else:
            raise not_enough_params(2)


    def force(self, F: vec = None, m: float = None, a: vec = None):
        # Fnet = m * a

        if F is not None and m is not None:
            return F / m
        elif m is not None and a is not None:
            return m * a
        elif F is not None and a is not None:
            raise cannot_divide_vectors()
        else:
            raise not_enough_params(2)

    def force(self, F: float = None, m: float = None, a: float = None):
        # Fnet = m * a

        if F is not None and m is not None:
            return F/m
        elif F is not None and a is not None:
            return F/a
        elif m is not None and a is not None:
            return m * a
        else:
            raise not_enough_params(2)

    def position_update(self, rf: vec = None, ri: vec = None, v: vec = None, dt: float = None, a: vec = None):
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

    def position_update(self, rf: float = None, ri: float = None, v: float = None, dt: float = None, a: float = None):
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

    def y(self, y: float = None, v: vec = None):
        c = 299792458 if self.accuracy == Accuracy.HIGH else 3e8

        if v is not None:
            return 1/sqrt(1 - (mag(v)/c)**2)
        elif y is not None:
            return sqrt(1 - (1/y**2)) * c
        else:
            raise not_enough_params(1)

    def y(self, y: float = None, v: float = None):
        c = 299792458 if self.accuracy == Accuracy.HIGH else 3e8

        if v is not None:
            return 1/sqrt(1 - (mag(v)/c)**2)
        elif y is not None:
            return sqrt(1 - (1 / y ** 2)) * c
        else:
            raise not_enough_params(1)


    def gamma_momentum_principle(self, p: vec = None, y: float = None, m: float = None, v: vec = None):

        if y is not None and m is not None and v is not None:
            return y * m * v
        elif m is not None and v is not None:
            c = 299792458
            y = y(v=v)

            return y * m * v
        elif p is not None and m is not None and y is not None:
            return p/(m * y)
        else:
            raise not_enough_or_invalid(3)

    def gamma_momentum_principle(self, p: float = None, y: float = None, m: float = None, v: float = None):

        if y is not None and m is not None and v is not None:
            return y * m * v
        elif m is not None and v is not None:
            c = 299792458
            y = y(v=v)

            return y * m * v
        elif p is not None and m is not None and y is not None:
            return p/(m * y)
        elif p is not None and y is not None and v is not None:
            return p/(y * v)
        elif p is not None and m is not None and v is not None:
            return p/(m * v)
        else:
            raise not_enough_params(3)

    def gravity(self, Fgrav: vec = None, m1: float = None, m2: float = None, r: vec = None):
        # Fgrav = -G * m1*m2/|r|^2 * rhat
        G = 6.674 * 10**-11 if self.accuracy == Accuracy.HIGH else 6.7 * 10 ** -11

        if m1 is not None and m2 is not None and r is not None:
            return -G * m1*m2/(mag(r)**2) * hat(r)
        elif Fgrav is not None and m1 is not None and m2 is not None:
            raise invalid_param_combination()
        elif Fgrav is not None and m1 is not None and r is not None:
            raise cannot_divide_vectors()
        elif Fgrav is not None and m2 is not None and r is not None:
            raise cannot_divide_vectors()
        else:
            raise not_enough_or_invalid(3)

    def gravity(self, Fgrav: float = None, m1: float = None, m2: float = None, r: float = None):
        # Fgrav = -G * m1*m2/r**2
        G = 6.674e-11 if self.accuracy == Accuracy.HIGH else 6.7e-11

        if m1 is not None and m2 is not None and r is not None:
            return -G * m1*m2/r**2
        elif Fgrav is not None and m1 is not None and m2 is not None:
            return sqrt(Fgrav/(m1*m2))
        elif Fgrav is not None and m1 is not None and r is not None:
            return Fgrav * r**2/m1
        elif Fgrav is not None and m2 is not None and r is not None:
            return Fgrav * r**2/m2
        else:
            raise not_enough_params(3)