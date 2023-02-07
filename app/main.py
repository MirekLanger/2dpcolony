import extractExcel
import colony as col
import visualize
import sys

def main(args = sys.argv[1:]):
    if len(args):
        definitionFile = str(args[0])
    else:
        definitionFile = 'colony.xlsx'
    colonieDefinition = extractExcel.getColonie(definitionFile)
    colony = col.Colony(colonieDefinition['environment'], colonieDefinition['agents'])
    step = 0
    steps = colonieDefinition['parameters']['steps']
    initplot = visualize.initVizualiser()
    while step != steps:
        step += 1
        print(step)
        colony.colonyStep()
        coords = [o.coordinates for o in colony.agent]
        popData = visualize.initPopulation(colony.rowsEnv, colony.colsEnv, coords)
        visualize.updatePlot(initplot,popData, colonieDefinition['parameters']['animationDelay'])
    visualize.endOfVisualization(initplot, popData)

    print(colony.envMatrix)
    coords = [o.coordinates for o in colony.agent]
    print(coords)
    res = (visualize.initPopulation(colony.rowsEnv, colony.colsEnv, coords))
    for i in res:
        print(i)
    for a in colony.agent:
        print("Agent:")
        print(a.contents)
        print(a.coordinates.get("i"), a.coordinates.get("j"))

    #print(colony.agent[0].contents)
    #print(colony.agent[0].coordinates)
    #print(colony.agent[1].contents)
    #print(colony.agent[1].coordinates)
    #print(colony.agent[2].contents)
    #print(colony.agent[2].coordinates)
main()