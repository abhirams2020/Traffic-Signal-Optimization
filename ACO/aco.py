import numpy as np
import math
from presets import n_ants, iterations

class ant_colony:
   
   #Create an instance of ant colony optimisation.
    def __init__(self, nodes, p, evaporation, alpha, beta, n_ants, iterations, connection):
        self.nodes = nodes
        self.p = p
        self.evaporation = evaporation
        self.alpha = alpha
        self.beta = beta
        self.n_ants = n_ants
        self.iterations = iterations
        self.connection = connection
        
    #function to calculate distance from start node to end node
    def get_distance(self, start, end):
        x = start[0] - end[0]
        y = start[1] - end[1]
        dist = (x**2) + (y**2)
        return (np.sqrt(dist))

    #Function to intialise the adjacency and visibility matrices, calculated from the input dictionary of nodes.
    def get_adjacency(self):
        nodes = self.nodes
        adjacency = np.zeros((len(nodes), len(nodes)))
        for i in range(len(nodes)):
            for j in range(len(nodes)):
                adjacency[i,j] = self.get_distance(list(nodes.values())[i],
                                                   list(nodes.values())[j])
        self.adjacency = adjacency
        self.visibility = np.divide(1, adjacency, out=np.zeros_like(adjacency), where=adjacency!=0)
        
    # Function to calculate the total distance of a given route
    def get_total_distance(self, route):
        nodes = self.nodes
        dist = 0
        for i in range(len(route)-1):
            current_node_index = list(nodes.keys()).index(route[i])
            
            next_node_index = list(nodes.keys()).index(route[i+1])
            
                
            dist += self.adjacency[current_node_index][next_node_index]
        
        # total_distance = dist

        # modified total distance to add the distance back to A
        total_distance = dist + self.adjacency[list(nodes.keys()).index(route[len(route)-1])][list(nodes.keys()).index('A')]
        return total_distance
                
    # Function to initialise the pheremone matrix
    def initialise_pheromone(self):
        pheromone = np.ones((self.adjacency.shape[0],self.adjacency.shape[0]))
        np.fill_diagonal(pheromone, 0)
        self.pheromone = pheromone
        
    #Function to intialise the route. For each ant, this includes selecting the starting node and generating a list of unvisited nodes.
    def initialise_route(self):
        self.unvisited_nodes = list(self.nodes)
        self.start_node = self.unvisited_nodes[0]
        self.start_node_index = self.initial_route.index(self.start_node)
        self.unvisited_nodes.remove(self.start_node)
    
    #Function to calculate the probabilities used in selecting the next node to visit.             
    def get_probabilities(self, start_node_index, unvisited_nodes):
        probabilities = []
        for node in range(len(unvisited_nodes)):
            next_node = unvisited_nodes[node] 
            next_node_index = self.initial_route.index(next_node)
            denominator = 0
            for i in range(len(unvisited_nodes)):
                n = unvisited_nodes[i]
                n_index = self.initial_route.index(n)
                denominator += (self.pheromone[start_node_index][n_index]**self.alpha
                                *self.visibility[start_node_index][n_index]**self.beta)
            probability = ((self.pheromone[start_node_index][next_node_index]**self.alpha
                            *self.visibility[start_node_index][next_node_index]**self.beta)/denominator)
            probabilities.append(probability)
        self.probabilities = probabilities

    # Function to calculates probability and chooses the appropriate route. Also updates the pheromones
    def optimise(self):
        self.get_adjacency()
        self.initialise_pheromone()
        self.initial_route = list(self.nodes)
        # self.route_best = self.initial_route
        self.route_best = []
        self.distance_best = math.inf
        for i in range(iterations):
            local_pheromone = np.zeros((self.adjacency.shape[0],self.adjacency.shape[0]))
            for b in range(n_ants):
                self.initialise_route()
                route = list(self.start_node)
                current_node_index = self.start_node_index
                templist = self.unvisited_nodes
                while len(self.unvisited_nodes) != 0:
                    self.get_probabilities(current_node_index,templist)
                    next_node = np.random.choice(templist,p=self.probabilities)
                    next_node_index = self.initial_route.index(next_node)
                    if self.connection[current_node_index][next_node_index]==0:
                        templist.remove(next_node)
                    else:
                        route.append(next_node)
                        current_node_index = self.initial_route.index(next_node)
                        self.unvisited_nodes.remove(next_node)
                self.route_best
                distance = self.get_total_distance(route)
                new_pheromone = np.zeros((self.adjacency.shape[0],self.adjacency.shape[0]))
                for node in range(len(route)):
                    current_node = route[node]
                    i = self.initial_route.index(current_node)
                    try:
                        next_node = route[node+1]
                    except:
                        next_node = route[0]
                    j = self.initial_route.index(next_node) 
                    new_pheromone[i][j] = self.p/distance
                if (distance < self.distance_best) and (len(route)==len(self.nodes)):
                    self.route_best, self.distance_best = route, distance
                local_pheromone = local_pheromone + new_pheromone
            print(route + ['A'], np.round(distance,4))
            self.pheromone = ((1-self.evaporation)*self.pheromone + local_pheromone)

        # appended A to the final route
        self.route_best.append('A')

        return self.route_best, self.distance_best