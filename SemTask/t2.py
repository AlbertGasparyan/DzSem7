from math import pi
orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]

def find_farthest_orbit(orbits):
    return max(orbits,key=lambda x:(x[0]!=x[1])*pi*x[0]*x[1])
print(find_farthest_orbit(orbits))
