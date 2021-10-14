import numpy as np, random, operator, pandas as pd
from ga import *
from presets import cities, nodes, no_of_cities, popSize, eliteSize, mutationRate, generations, connection
from plot import plot

cityList = []
for i in range (0,no_of_cities):
    cityList.append(City(x=int(cities[i][0]), y=int(cities[i][1])))

print('Route of all the ants at the end :')
route, solution = geneticAlgorithm(cityList, popSize, eliteSize, mutationRate, generations)

points = []
for pt in nodes:
    points.append((int(nodes[pt][0]),int(nodes[pt][1])))

path = []
for i in range(0,len(route)):
    path.append(route[i].st)

print('The best route is: {}'.format(path))
print('Total distance of: {:.4f}'.format(solution))
print('Points : {}'.format(points))

plot(points, path, solution)