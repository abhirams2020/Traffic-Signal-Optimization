import operator
from presets import nodes
import matplotlib.pyplot as plt

def plot(points, path: list, solution):
    x = []
    y = []
    for point in points:
        x.append(point[0])
        y.append(point[1])
   
    # y = list(map(operator.sub, [max(y) for i in range(len(points))], y)) 

    plt.plot(x, y, 'co')

    plt.title('Total distance of: {:.4f}'.format(solution))

    for _ in range(1, len(path)):
        i = ord(path[_ - 1])-65 # to convert A,B.. to 0,1..
        j = ord(path[_])-65
        plt.arrow(x[i], y[i], x[j] - x[i], y[j] - y[i], color='r', length_includes_head=True)

    for a,b in zip(x,y):
        for i in nodes:
            if(nodes[i][0]==a and nodes[i][1]==b):
                pt = i
        #uncomment below line to add coordinates
        # label = pt + " ({:.1f},{:.1f})".format(a,b) 
        label = pt

        plt.annotate(label, # this is the text
                    (a,b), # these are the coordinates to position the label
                    textcoords="offset points", # how to position the text
                    xytext=(0,10), # distance from text to points (x,y)
                    ha='center') # horizontal alignment can be left, right or center

    plt.xlim(0, max(x) * 1.1)
    plt.ylim(0, max(y) * 1.1)
    plt.show()