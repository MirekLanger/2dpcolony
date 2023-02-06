definitionFile = 'D:\\personal\\vsb\projekty\\aco_simulator\\2dpcolony\\colonie.xlsx'

import extractExcel
import colony as col


def main():
    colonieDefinition = extractExcel.getColonie(definitionFile)
    colony = col.Colony(colonieDefinition['environment'], colonieDefinition['agents'])
    step = 0
    steps = colonieDefinition['parameters']['steps']
    while step != steps:
        step += 1
        print(step)
        colony.colonyStep()


    print(colony.envMatrix)
    print(colony.agent[0].contents)
    print(colony.agent[0].coordinates)
    print(colony.agent[1].contents)
    print(colony.agent[1].coordinates)
    print(colony.agent[2].contents)
    print(colony.agent[2].coordinates)

main()