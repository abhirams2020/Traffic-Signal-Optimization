# nodes : Dictionary of nodes and their coordinate positions.
# p : Constant used during local phermeone calculation.
# evaporation : Evaporation constant rho used when updating pheremone matrix.
# alpha : Constant to control the impact of the pheremone levels in the probability computation.
# beta : Constant to control the effect of local preference matrix H.
# n_ants : Number of ants used per iteration.
# iterations : Number of iterations.
nodes = {'A':(4,2), 'B':(5,1), 'C':(6,3), 'D':(2,5), 'E':(1,1)}

p = 100
evaporation = 0.5
alpha = 1
beta = 1
n_ants = 100
iterations = 20
connection = [  [0,0,1,1,1],
                [0,0,1,1,1],
                [1,1,0,1,1],
                [1,1,1,0,0],
                [1,1,1,0,0]]



