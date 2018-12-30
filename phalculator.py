import math
def dPos(t, a, vx0):
    changeInPos = (vx0 * t) + (0.5 * a * t ** 2)
    return changeInPos


def fVel(vx0, a, x, x0):
    finalVel = vx0 ** 2 + (2 * a * (x - x0))
    return finalVel

def comp(solveFor, num1, num2):
    if(solveFor is 1):
        return f"Vertical Component: {split(num1, num2)[0]}, " \
               f"Horizontal Component: {split(num1, num2)}"
    if(solveFor is 2):
        return f"Magnitude: {condense(num1, num2)}[0]" \
               f"Angle: {condense(num1, num2)}[1])"

def condense(hor, ver):
    return (hor**2 + ver**2), math.degrees(math.atan(ver/hor))

def split(angle, mag):
    return (mag * math.degrees(math.sin(angle))), \
           (mag * math.degrees(math.cos(angle)))