import operator
from presets import no_of_cities
import matplotlib.pyplot as plt

def plot(nodes, cities, path: list, solution):
    x = []
    y = []
    for point in cities:
        x.append(point[0])
        y.append(point[1])
   
    x.append(cities[0][0])
    y.append(cities[0][1])
    # y = list(map(operator.sub, [max(y) for i in range(len(points))], y)) 

    plt.plot(x, y, 'co')

    plt.title('Total distance of: {:.4f} km,  Path : {}'.format(solution,path))

    for _ in range(1, no_of_cities+1):
        i = nodes[path[_ - 1]][2] # to convert A,B.. to 0,1..
        j = nodes[path[_]][2]
        plt.arrow(x[i], y[i], x[j] - x[i], y[j] - y[i], color='r', length_includes_head=True)

    for a,b in zip(x,y):
        for i in nodes:
            if(nodes[i][1]==a and nodes[i][0]==b):
                pt = i
        #uncomment below line to add coordinates
        # label = pt + " ({:.1f},{:.1f})".format(a,b) 
        label = pt

        plt.annotate(label, # this is the text
                    (a,b), # these are the coordinates to position the label
                    textcoords="offset points", # how to position the text
                    xytext=(0,10), # distance from text to points (x,y)
                    ha='center') # horizontal alignment can be left, right or center

    plt.xlim(min(min(x),-1) * 1.5, max(x) * 1.5)
    plt.ylim(min(min(y),-1) * 1.5, max(y) * 1.5)
    plt.show()