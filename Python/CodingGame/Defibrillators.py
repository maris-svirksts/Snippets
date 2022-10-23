# https://www.codingame.com/training/easy/defibrillators

import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

def to_float(variable):
    return float(variable.replace(',', '.'))

closest = None
name    = ''

lon = to_float(input())
lat = to_float(input())

n = int(input())
for i in range(n):
    _, def_name, _, _, def_lon, def_lat = input().split(';')

    def_lon = to_float(def_lon)
    def_lat = to_float(def_lat)

    x = (def_lon - lon) * math.cos((lat + def_lat)/2)
    y = def_lat - lat
    d = math.sqrt(x ** 2 + y ** 2) * 6371

    if closest == None or d < closest:
        closest = d
        name = def_name


# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)

print(name)
