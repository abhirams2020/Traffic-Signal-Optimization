import csv
import os

n_points = 6

os.chdir(r'C:\Users\abhiram\Downloads\Traffic-Signal-Optimization\ACO')
file = open('location.csv')
type(file)

nodes = {}

count = 1
for line in file:
    if(count > n_points):
        break
    (key,lat,lon) = line.split(",")
    nodes[str(key)] = (float(lat),float(lon),int(count))
    count += 1

for keys,values in nodes.items():
    print(keys)
    print(values)

print(list(nodes)[0])