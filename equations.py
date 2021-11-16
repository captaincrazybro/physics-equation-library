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
            return Answer(dp / dt, "N")
        elif dt is not None and Fnet is not None:
            return Answer(Fnet * dt, "kg*m/s")
        else:
            raise not_enough_params(2)


    def momentum_principle(self, dp: float = None, Fnet: float = None, dt: float = None):
        # dp = Fnet * dt

        if dp is not None and Fnet is not None:
            return Answer(dp / Fnet, "s")
        elif dp is not None and dt is not None:
            return Answer(dp / dt, "N")
        elif dt is not None and Fnet is not None:
            return Answer(Fnet * dt, "kg*m/s")
        else:
            raise not_enough_params(2)


    def update(self, f: vec = None, i: vec = None, delta: vec = None, dt: float = None):
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
            return Answer(p / m, "m/s")
        elif m is not None and v is not None:
            return Answer(m * v, "kg*m/s")
        elif p is not None and v is not None:
            raise cannot_divide_vectors()
        else:
            raise not_enough_params(2)

    def momentum(self, p: float = None, m: float = None, v: float = None):
        # p = m * v

        if p is not None and m is not None:
            return Answer(p / m, "m/s")
        elif m is not None and v is not None:
            return Answer(m * v, "kg*m/s")
        elif p is not None and v is not None:
            return Answer(p / v, "kg")
        else:
            raise not_enough_params(2)

    def force(self, F: vec = None, m: float = None, a: vec = None):
        # Fnet = m * a

        if F is not None and m is not None:
            return Answer(F / m, "m/s^2")
        elif m is not None and a is not None:
            return Answer(m * a, "N")
        elif F is not None and a is not None:
            raise cannot_divide_vectors()
        else:
            raise not_enough_params(2)

    def force(self, F: float = None, m: float = None, a: float = None):
        # Fnet = m * a

        if F is not None and m is not None:
            return Answer(F/m, "m/s^2")
        elif F is not None and a is not None:
            return Answer(F/a, "kg")
        elif m is not None and a is not None:
            return Answer(m * a, "N")
        else:
            raise not_enough_params(2)

    def position_update(self, rf: vec = None, ri: vec = None, v: vec = None, dt: float = None, a: vec = None):
        # rf = ri + v * dt + 1/2 * a * dt**2

        if ri is not None and v is not None and dt is not None and a is not None:
            return Answer(ri + v * dt + 1 / 2 * a * dt ** 2, "m")
        elif ri is not None and rf is not None and v is not None and dt is not None:
            return Answer((rf - ri - v * dt) / dt**2, "m/s^2")
        elif ri is not None and v is not None and dt is not None and a is not None:
            return Answer((rf - ri - 1 / 2 * a * dt ** 2) / dt, "m/s")
        elif rf is not None and v is not None and dt is not None and a is not None:
            return Answer(rf - v * dt - 1 / 2 * a * dt ** 2, "m")
        elif rf is not None and ri is not None and v is not None and a is not None:
            raise cannot_divide_vectors()
        else:
            raise not_enough_params(4)

    def position_update(self, rf: float = None, ri: float = None, v: float = None, dt: float = None, a: float = None):
        # rf = ri + v * dt + 1/2 * a * dt**2

        if ri is not None and v is not None and dt is not None and a is not None:
            return Answer(ri + v * dt + 1 / 2 * a * dt ** 2, "m")
        elif ri is not None and rf is not None and v is not None and dt is not None:
            return Answer((rf - ri - v * dt) / dt ** 2, "m/s^2")
        elif ri is not None and v is not None and dt is not None and a is not None:
            return Answer((rf - ri - 1 / 2 * a * dt ** 2) / dt, "m/s")
        elif rf is not None and v is not None and dt is not None and a is not None:
            return Answer(rf - v * dt - 1 / 2 * a * dt ** 2, "m")
        elif rf is not None and ri is not None and v is not None and a is not None:
            return Answer([
                (-v + sqrt(v**2 - 4 * a * ri))/(2 * a),
                (-v - sqrt(v**2 - 4 * a * ri))/(2 * a)
            ], "s")
        else:
            raise not_enough_params(4)

    def y(self, y: float = None, v: vec = None):
        c = 299792458 if self.accuracy == Accuracy.HIGH else 3e8

        if v is not None:
            return 1/sqrt(1 - (mag(v)/c)**2)
        elif y is not None:
            return Answer(sqrt(1 - (1/y**2)) * c, "m/s")
        else:
            raise not_enough_params(1)

    def y(self, y: float = None, v: float = None):
        c = 299792458 if self.accuracy == Accuracy.HIGH else 3e8

        if v is not None:
            return 1/sqrt(1 - (mag(v)/c)**2)
        elif y is not None:
            return Answer(sqrt(1 - (1 / y ** 2)) * c, "m/s")
        else:
            raise not_enough_params(1)


    def gamma_momentum(self, p: vec = None, y: float = None, m: float = None, v: vec = None):

        if y is not None and m is not None and v is not None:
            return Answer(y * m * v, "kg*m/s")
        elif m is not None and v is not None:
            c = 299792458
            y = self.y(v=v)

            return Answer(y * m * v, "kg*m/s")
        elif p is not None and m is not None and y is not None:
            return Answer(p/(m * y), "m/s")
        else:
            raise not_enough_or_invalid(3)

    def gamma_momentum(self, p: float = None, y: float = None, m: float = None, v: float = None):

        if y is not None and m is not None and v is not None:
            return Answer(y * m * v, "kg*m/s")
        elif m is not None and v is not None:
            c = 299792458
            y = self.y(v=v)

            return Answer(y * m * v, "kg*m/s")
        elif p is not None and m is not None and y is not None:
            return Answer(p/(m * y), "m/s")
        elif p is not None and y is not None and v is not None:
            return Answer(p/(y * v), "kg")
        elif p is not None and m is not None and v is not None:
            return p/(m * v)
        else:
            raise not_enough_params(3)

    def gravity(self, Fgrav: vec = None, m1: float = None, m2: float = None, r: vec = None):
        # Fgrav = -G * m1*m2/|r|^2 * rhat
        G = 6.674 * 10**-11 if self.accuracy == Accuracy.HIGH else 6.7 * 10 ** -11

        if m1 is not None and m2 is not None and r is not None:
            return Answer(-G * m1*m2/(mag(r)**2) * hat(r), "N")
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
            return Answer(-G * m1*m2/r**2, "N")
        elif Fgrav is not None and m1 is not None and m2 is not None:
            return Answer(sqrt(Fgrav/(m1*m2)), "m")
        elif Fgrav is not None and m1 is not None and r is not None:
            return Answer(Fgrav * r**2/m1, "kg")
        elif Fgrav is not None and m2 is not None and r is not None:
            return Answer(Fgrav * r**2/m2, "kg")
        else:
            raise not_enough_params(3)

    def spring_force(self, Fspring: vec = None, k: float = None, s: float = None, rHat: vec = None):
        # Fspring = -k * s * rHat

        if k is not None and s is not None and rHat is not None:
            return Answer(-k * s * rHat, "N")
        elif Fspring is not None and k is not None and rHat is not None:
            raise cannot_divide_vectors()
        elif Fspring is not None and k is not None and s is not None:
            return Fspring/(-k * s)
        elif Fspring is not None and s is not None and rHat is not None:
            raise cannot_divide_vectors()
        else:
            raise not_enough_params(3)

    def spring_force(self, Fspring: float = None, k: float = None, s: float = None):
        # Fspring = -k * s

        if k is not None and s is not None:
            return Answer(-k * s, "N")
        elif Fspring is not None and k is not None:
            return Answer(Fspring/k, "m")
        elif Fspring is not None and s is not None:
            return Answer(Fspring/s, "N/m")
        else:
            raise not_enough_params(2)

    def electric_force(self, Felectric: vec = None, q1: float = None, q2: float = None, r: vec = None):
        # Felectric = k * q1 * q2/|r|**2 * rHat
        k = 1/(4 * pi * 8.854187817e-12) if self.accuracy == Accuracy.HIGH else 9e9

        if q1 is not None and q2 is not None and r is not None:
            return Answer(k * q1*q2/(mag(r))**2 * hat(r), "N")
        elif q1 is not None and Felectric is not None and r is not None:
            raise cannot_divide_vectors()
        elif q2 is not None and Felectric is not None and r is not None:
            raise cannot_divide_vectors()
        elif Felectric is not None and q2 is not None and q1 is not None:
            invalid_param_combination()
        else:
            raise not_enough_params(3)

    def electric_force(self, Felectric: float = None, q1: float = None, q2: float = None, r: float = None):
        # Felectric = k * q1 * q2/|r|**2 * rHat
        k = 1/(4 * pi * 8.854187817e-12) if self.accuracy == Accuracy.HIGH else 9e9

        if q1 is not None and q2 is not None and r is not None:
            return Answer(k * q1*q2/r**2, "N")
        elif q1 is not None and Felectric is not None and r is not None:
            raise Answer(Felectric * r**2/(k*q1), "C")
        elif q2 is not None and Felectric is not None and r is not None:
            raise Answer(Felectric * r**2/(k*q2), "C")
        elif Felectric is not None and q2 is not None and q1 is not None:
            return Answer(sqrt(q1*q2/Felectric), "m")
        else:
            raise not_enough_params(3)

    def perp_force(self, Fperp: float = None, m: float = None, v: float = None, R: float = None):
        # Fperp = m * v**2/R

        if m is not None and v is not None and R is not None:
            return Answer(m * v**2/R, "N")
        elif Fperp is not None and m is not None and v is not None:
            return Answer(m * v**2/Fperp, "m")
        elif Fperp is not None and m is not None and R is not None:
            return Answer(sqrt(Fperp * R/m), "m/s")
        elif Fperp is not None and R is not None and v is not None:
            return Answer(Fperp * R/v**2, "kg")
        else:
            raise not_enough_params(3)
