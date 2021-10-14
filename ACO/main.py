from aco import ant_colony
from presets import nodes, p, evaporation, alpha, beta, n_ants, iterations, connection
from plot import plot

points = []

print('Route of all the ants at the end :')
problem = ant_colony(nodes, p, evaporation, alpha, beta, n_ants, iterations, connection)
path, solution = problem.optimise()

for pt in nodes:
    points.append((int(nodes[pt][0]),int(nodes[pt][1])))
    #points.append((int(nodes[1]), int(nodes[2])))

print('The best route is: {}'.format(path))
print('Total distance of: {:.4f}'.format(solution))
# print('Cost: {:.4f}, Path: {}'.format(solution, path))
print('Points : {}'.format(points))
plot(points, path, solution)