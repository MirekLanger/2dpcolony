import extractExcel
import colony as col
import visualize
import sys
import os


def main(args=sys.argv[1:]):
    if len(args):
        definitionFile = str(args[0])
    else:
        pyDir = os.path.dirname(os.path.realpath(__file__)) #Get directory of the current .py script
        definitionFile = pyDir + '\\colony.xlsx'
    colonyDefinition = extractExcel.getColony(definitionFile)
    colony = col.Colony(colonyDefinition['environment'], colonyDefinition['agents'],
                        colonyDefinition['parameters']['jokerSymbols']
                        )
    print(colonyDefinition)
    step = 0
    steps = colonyDefinition['parameters']['steps']
    agentCoords = [o.coordinates for o in colony.agent]
    initplot = visualize.initVizualiser(steps, colony.rowsEnv, colony.colsEnv, agentCoords)
    
    while step != steps:
        step += 1
        #print(step)
        colony.colonyStep(True)
        agentCoords = [o.coordinates for o in colony.agent]
        popData = visualize.initPopulation(colony.rowsEnv, colony.colsEnv, agentCoords)
        visualize.updatePlot(step, initplot, popData, colony.envMatrix,
                             colonyDefinition['parameters']['animationDelay'],
                             colonyDefinition['parameters']['colorSettings']
                             )

    visualize.endOfVisualization(initplot, popData)

    #print(colony.envMatrix)
    #for a in colony.agent: #Print the last configuration of the agent / can be commented
        #print("Agent:")
        #print(a.contents)
        #print(a.coordinates.get("i"), a.coordinates.get("j"))
    #print(colony.agent[0].contents)
    #print(colony.agent[0].coordinates)
    #print(colony.agent[1].contents)
    #print(colony.agent[1].coordinates)
    #print(colony.agent[2].contents)
    #print(colony.agent[2].coordinates)
main()