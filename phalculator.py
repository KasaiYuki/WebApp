import math


def dPos(t, a, vx0):
    changeInPos = (vx0 * t) + (0.5 * a * (t ** 2))
    return changeInPos


def fVel(vx0, a, x, x0):
    finalVel = math.sqrt(vx0 ** 2 + (2 * a * (x - x0)))
    return finalVel

def comp(solveFor, num1, num2):
    if(solveFor is 1):
        return split(num1, num2)[0] #v comp
    if(solveFor is 2):
        return pythag(num1, num2) #magnitude

def comp2(solveFor, num1, num2):
    if(solveFor is 1):
        return split(num1, num2)[1] #h comp
    if(solveFor is 2):
        return angle(num1, num2) #angle

def pythag(ver, hor):
    return round(math.sqrt(hor**2 + ver**2),2)

def angle(ver, hor):
    return round(math.degrees(math.atan(ver / hor)),2)


def split(mag, angle):
    rads = math.radians(angle)
    vcomp = round(math.sin(rads),2)
    hcomp = round(math.cos(rads),2)
    return mag*vcomp, mag*hcomp

def friction(coef: float, mass: float, angle: float, inc):
    fric = coef * (mass * 10)
    if(angle is not 0):
        if(inc == "l"):
            fric *= math.sin(math.radians(angle))
        elif(inc == "r"):
            fric *= math.cos(math.radians(angle))
    return round(fric,2)