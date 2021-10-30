from vpython import *

def Divide(vec1: vec, vec2: vec):
    return mag(vec1)/mag(vec2)

def Dot(vec1: vec, vec2: vec):
    return vec1.x * vec2.x + vec1.y * vec2.y + vec1.z * vec2.z