# nodes : Dictionary of nodes and their coordinate positions.
# cities = [[4,2], [5,1], [6,3], [2,5], [1,1]]
import os

n_points = 5

os.chdir(r'C:\Users\abhiram\Downloads\Traffic-Signal-Optimization\GA')
file = open('location.csv')
type(file)

nodes = {}
cities = []
city_name = []

count = 0
for line in file:
    if(count >= n_points):
        break
    (key,lat,lon) = line.split(",")
    nodes[str(key)] = (float(lat),float(lon),int(count))
    cities.append((float(lat),float(lon)))
    city_name.append(key)
    count += 1

# cities = [(4,2), (5,1), (6,3), (2,5), (1,1)]
# city_name = ['A', 'B', 'C', 'D', 'E']
# nodes = {'A':(4,2), 'B':(5,1), 'C':(6,3), 'D':(2,5), 'E':(1,1)}
no_of_cities = len(cities)
popSize=100
eliteSize=20
mutationRate=0.01
generations=10

connection = [  [0,1,1,1,1],
                [1,0,1,1,1],
                [1,1,0,1,1],
                [1,1,1,0,1],
                [1,1,1,1,0]]
# connection = [  [0,0,1,1,1],
#                 [0,0,1,1,1],
#                 [1,1,0,1,1],
#                 [1,1,1,0,0],
#                 [1,1,1,0,0]]