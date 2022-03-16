#!/usr/bin/python3

import sys
import math

arlen = len(sys.argv) - 1


if (arlen == 0):
    sys.exit("No args")
elif (arlen < 7 and arlen != 0):
    sys.stderr.write("Too few args\n")
    sys.exit(84)
elif (arlen > 7):
    sys.stderr.write("Too much args\n")
    sys.exit(84)
else:

    x0 = float(sys.argv[1])
    y0 = float(sys.argv[2])
    z0 = float(sys.argv[3])
    x1 = float(sys.argv[4])
    y1 = float(sys.argv[5])
    z1 = float(sys.argv[6])
    n = int(sys.argv[7])

if (n < 0) :
    sys.stderr.write("Impossible time value\n")
    sys.exit(84)
    
def pong():
    
    velx = x1 - x0
    vely = y1 - y0
    velz = z1 - z0
    
    print("The velocity vector of the ball is:")
    print(f'({velx:.2f}, {vely:.2f}, {velz:.2f})')
    
    posx = x1 + (velx * n)
    posy = y1 + (vely * n)
    posz = z1 + (velz * n)

    print("At time t + {}, ball coordinates will be:".format(n))
    print(f'({posx:.2f}, {posy:.2f}, {posz:.2f})')

    norm = math.sqrt((velx*velx) + (vely*vely) + (velz*velz))
    angle = math.asin(velz/norm)
    angle = math.degrees(angle)
    angle = math.fabs(angle)
    print("The incidence angle is:")
    print(f'{angle:.2f}'+" degrees")
pong()

