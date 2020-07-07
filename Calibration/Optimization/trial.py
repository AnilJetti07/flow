import numpy as np
import random, csv, time
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style

x = np.array([1,2,3,4,53,21])

def eror(vals, isCounts, stdv):
    if isCounts:
        y = np.round(np.random.normal(vals,stdv))
        return np.where(y<0, 0, y) 
    else:
        y = np.random.normal(vals,stdv)
        return np.where(y<0, 0, y) 

#print(eror(x, True, 3))
#print(eror(x, False, 4))

def plotErrors(error):
    timestr = time.strftime("%Y%m%d_%H%M%S")
    csvName = "error" + ".csv"
    with open(csvName, "a") as file:
        writer = csv.writer(file)
        writer.writerow([error])

plotErrors(12)
plotErrors(123)
plotErrors(3)
plotErrors(10)


def animate():
    graph_data = open('error.csv','r').read()
    lines = graph_data.split('\n')
    xs = []
    ys = []
    i = 0
    for line in lines:
        i += 1
        if len(line) > 1:
            x = float(line)
            xs.append(float(x))
            ys.append(i)
    plt.plot(ys, xs)
    plt.ylabel("Error")
    plt.xlabel("Iteration")
    plt.show()

animate()
