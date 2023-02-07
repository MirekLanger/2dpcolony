from matplotlib import pyplot, colors
from matplotlib.widgets import Button
from matplotlib.patches import Rectangle
import matplotlib.patches as mpatches
import numpy
import sys

animation_delay = 0.915 # pause between displaying new iteration in seconds [default: 0.15]

def initPopulation(rows, cols, acoordinates):
    popData = [[0.0 for j in range(0,cols)] for i in range(0,rows)]
    for coordinates in acoordinates:
        coord_i = coordinates.get("j")-1 #switch j and i
        coord_j = coordinates.get("i")-1
        if coord_i in range (0,rows) and coord_j in range (0,cols):
            popData[coord_i][coord_j]=1.0 #Agent is not out of the env
    return popData

def updatePlot(initplot,popData, animation_delay): # function to update 2D plot
    initplot.set_data(popData)
    rect=mpatches.Rectangle((3-0.5,3-0.5),1,1, fill = False, color = "red",linewidth = 1)
    pyplot.gca().add_patch(rect)
    pyplot.pause(animation_delay)
    [p.remove() for p in reversed(pyplot.gca().patches)]
"""    
    for i in range(1,x_dim):
        for j in range(1,y_dim):
            if environmentSymbols[i][j].value == 'P':
                clrs = {0:"aquamarine", 1:"mediumaquamarine", 2:"lightgreen", 3:"greenyellow", 4:"yellowgreen", 5:"olivedrab", 6:"seagreen",7:"darkgreen", 8:"olive"};
                clr = "black"
                sz = int(environmentSymbols[i][j].size)
                if 0 <= sz <= 5:
                    clr = clrs[sz]
                rect=mpatches.Rectangle((int(j)-0.5,int(i)-0.5),1,1, fill = False, color = clr,linewidth = 1)
                pyplot.gca().add_patch(rect)
                if environmentSymbols[i][j].size < 1:
                    environmentSymbols[i][j].value = 'e'
                else:
                    environmentSymbols[i][j].size -= rmFI
            if environmentSymbols[i][j].value == 'p':
                clrs = {0:"lightpink", 1:"pink", 2:"plum", 3:"violet", 4:"orchid", 5:"darkorchid"};
                clr = "purple"
                sz = int(environmentSymbols[i][j].size)
                if 0 <= sz <= 5:
                    clr = clrs[sz]
                rect=mpatches.Rectangle((int(j)-0.5,int(i)-0.5),1,1, fill = False, color = clr,linewidth = 1)
                pyplot.gca().add_patch(rect)
            elif (environmentSymbols[i][j].value == 'L' or environmentSymbols[i][j].value == 'R' or environmentSymbols[i][j].value == 'U' or environmentSymbols[i][j].value == 'D'):
                clrs = {0:"aquamarine", 1:"mediumaquamarine", 2:"lightgreen", 3:"greenyellow", 4:"yellowgreen", 5:"olivedrab", 6:"seagreen",7:"darkgreen", 8:"olive"};
                clr = "darkgreen"
                sz = int(environmentSymbols[i][j].size)
                if 0 <= sz <= 5:
                    clr = clrs[sz]
                rect=mpatches.Rectangle((int(j)-0.5,int(i)-0.5),1,1, fill = False, color = clr,linewidth = 1)
                pyplot.gca().add_patch(rect)
                if environmentSymbols[i][j].size < 1:
                    environmentSymbols[i][j].value = 'e'
                else:
                    environmentSymbols[i][j].size -= rmFI

    #for prey in preylist:
    #    rect=mpatches.Rectangle((int(prey[1])-0.5,int(prey[0])-0.5),1,1, fill = False, color = "purple",linewidth = 1)
    #    pyplot.gca().add_patch(rect)
    pyplot.pause(animation_delay)
    [p.remove() for p in reversed(pyplot.gca().patches)]
"""

testagent =	{
  "i": 5,
  "j": 2,
}

def initVizualiser():
    # using colors from matplotlib, define a color map
    colormap = colors.ListedColormap(["lightgrey","green","blue"])
    # define figure size using pyplot
    fig = pyplot.figure("Model Visualization")
    # using pyplot add a title
    pyplot.title("Iteration 0",
                fontsize = 24)
    pyplot.suptitle("Simulation is running...", fontsize = 16, ha='center', va='center')
    # using pyplot add x and y labels
    pyplot.xlabel("x coordinates", fontsize = 20)
    pyplot.ylabel("y coordinates", fontsize = 20)
    # adjust x and y axis ticks, using pyplot
    pyplot.xticks(fontsize = 16)
    pyplot.yticks(fontsize = 16)
    # use .imshow() method from pyplot to visualize agent locations
    initplot = pyplot.imshow(X = initPopulation(10,7,[testagent]),
                cmap = colormap)
    def keypress(keyEvent):
        character = str(keyEvent.key)
        print (character)
        if (character == "c"):
            sys.exit(0)
        if (character == "p"):
            pyplot.pause(5)

    fig.canvas.mpl_connect('key_press_event', keypress)
    pyplot.draw()
    #pyplot.pause(0.85)
    return initplot

def endOfVisualization(initplot, popData):
    initplot.set_data(popData)
    #END
    itercount = 1
    n_iterations = 2
    #End of simulation
    newtitle = "Iteration " + str(itercount - 1) + " of " + str(n_iterations) + " [end]"
    pyplot.title(newtitle, fontsize = 24)
    pyplot.suptitle("Click anywhere to exit.", fontsize = 16, ha='center', va='center')
    pyplot.waitforbuttonpress(0)
    pyplot.draw()
    print ("[Info] End of simulation")
    return "a"

initVizualiser()
#pyplot.draw()
#endOfVisualization()