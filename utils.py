from vpython import *


def Divide(vec1: vec, vec2: vec):
    return mag(vec1) / mag(vec2)


def Dot(vec1: vec, vec2: vec):
    return vec1.x * vec2.x + vec1.y * vec2.y + vec1.z * vec2.z


def Mag(val):
    if type(val) is float:
        return val
    elif type(val) is int:
        return val
    else:
        return mag(val)


class Answer:
    answer = None
    units: str

    def __init__(self, answer, units: str):
        self.answer = answer
        self.units = units

    def __str__(self):
        return f'{self.answer} {self.units}'

    def __repr__(self):
        return self.answer
