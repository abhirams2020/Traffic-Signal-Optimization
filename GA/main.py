import numpy as np, random, operator, pandas as pd
from ga import *
from presets import cities, nodes, no_of_cities, popSize, eliteSize, mutationRate, generations, connection
from plot import plot

cityList = []
for i in range (0,no_of_cities):
    cityList.append(City(x=float(cities[i][0]), y=float(cities[i][1])))

route, solution = geneticAlgorithm(cityList, popSize, eliteSize, mutationRate, generations)

points = []
for pt in nodes:
    points.append((float(nodes[pt][1]),float(nodes[pt][0])))

path = []
for i in range(0,len(route)):
    path.append(route[i].st)

print('The best route is: {}'.format(path))
print('Total distance of: {:.4f} km'.format(solution))
print('Points : {}'.format(points))

plot(nodes, points, path, solution)