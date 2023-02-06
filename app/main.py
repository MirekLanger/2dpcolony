definitionFile = 'D:\\personal\\vsb\projekty\\aco_simulator\\2dpcolony\\colonie.xlsx'

import extractExcel
import colonie as col


def main():
    colonieDefinition = extractExcel.getColonie(definitionFile)
    #print(colonieDefinition)
    #agents = colonieDefinition['agents']
    #print(colonieDefinition['agents'])
    #print(len(colonieDefinition['agents']))

    #for i in range(len(colonieDefinition['agents'])):
        #print(agents[i]['contents'])
        #print(agents[i]['programs'])
        #print(agents[i]['coordinates'])

    #print(colonieDefinition['environment']['rules'])

    colonie = col.Colonie(colonieDefinition['environment'], colonieDefinition['agents'])
    colonie.colonieStep()
    print(colonie.envMatrix)
    print(colonie.agent[0].contents)
    print(colonie.agent[0].coordinates)
    print(colonie.agent[1].contents)
    print(colonie.agent[1].coordinates)
    print(colonie.agent[2].contents)
    print(colonie.agent[2].coordinates)

main()