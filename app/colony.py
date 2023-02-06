import random

class Colony:
    def __init__(self, environment, agents):
        self.envMatrix = environment['matrix']
        self.rowsEnv = len(self.envMatrix)
        self.colsEnv = len(self.envMatrix[0])
        self.envRules = environment['rules']
        self.numAgents = len(agents)
        self.toConcat2env = []
        self.agent = [self.Agent(self, agents[i]['contents'], agents[i]['programs'],agents[i]['coordinates']) for i in range(self.numAgents)]

    def initComputationalStep(self):
        self.toConcat2env = []

    def getApplicableRules(self, i, j):
        contents = self.envMatrix[i][j][:]
        applicableRules = []
        for rule in self.envRules:
            allSymbols = 1
            for symbol in rule['left']:
                if symbol in contents:
                    contents.remove(symbol)
                else:
                    allSymbols = 0
                    break
            if allSymbols:
                applicableRules.append(rule)
        return applicableRules

    def evolveEnvironmet(self):
        for i in range(self.rowsEnv):
            for j in range(self.colsEnv):
                applicableRules = self.getApplicableRules(i,j)
                if applicableRules:
                    cell = self.envMatrix[i][j]
                    applyRule = applicableRules[random.randrange(len(applicableRules))]
                    for symbol in applyRule['left']:
                        cell.remove(symbol)
                    cell = cell + applyRule['right']
                    self.envMatrix[i][j] = cell

    def add2environment(self):
        for element in self.toConcat2env:
            self.envMatrix[element['position']['i']][element['position']['j']] += element['symbol']

    def agentsAct(self):
        agentIndexList = [i for i in range(self.numAgents)]
        while agentIndexList:
            agentIndex = agentIndexList.pop(random.randrange(len(agentIndexList)))
            self.agent[agentIndex].applyProgram()

    def colonyStep(self):
        self.initComputationalStep()
        self.agentsAct()
        self.evolveEnvironmet()
        self.add2environment()

    class Agent:
        def __init__(self, col, contents, programs, coordinates):
            self.contents = contents
            self.programs = programs
            self.coordinates = coordinates
            self.vicinityLength = 9
            self.colony = col

        def getVicinity(self):
            vicinity = []
            for i in range(self.coordinates['i'] - 1, self.coordinates['i'] + 2):
                for j in range(self.coordinates['j'] - 1, self.coordinates['j'] + 2):
                    vicinity.append(self.colony.envMatrix[i][j])
            return vicinity

        def getEnvironmentContent(self):
            return self.colony.envMatrix[self.coordinates['i']][self.coordinates['j']]

        def getApplicablePrograms(self):
            aplicablePorgrams = []
            for program in self.programs:
                allRulesAplicable = 1
                innerObjects = self.contents[:]
                envContent = self.getEnvironmentContent()[:]
                for rule in program:
                    #get type of a rule
                    #motion
                    if rule['operator'] in ['u', 'd', 'r', 'l']:
                        vicinity = self.getVicinity()
                        for i in range(self.vicinityLength):
                            if not(rule['left'][i] in (vicinity[i]+['e'])):
                                allRulesAplicable = 0
                                break
                    #evolving
                    elif (rule['operator'] == '>'):
                        if (rule['left'] in innerObjects):
                            innerObjects.remove(rule['left'])
                            #innerObjects += rule['right'] #can I develop and exchange the developped object in one program?
                        else:
                            allRulesAplicable = 0
                    #exchange
                    elif (rule['operator'] =='<>'):
                        if (rule['left'] in innerObjects) and (rule['right'] in envContent + ['e']):
                            innerObjects.remove(rule['left'])
                            if rule['right'] != 'e':
                                envContent.remove(rule['right'])
                            #innerObjects += rule['right'] # can I exchange and develop exchanged object in one program?
                        else:
                            allRulesAplicable = 0
                if allRulesAplicable:
                    aplicablePorgrams.append(program)
            return aplicablePorgrams

        def applyProgram(self):
            applycablePrograms = self.getApplicablePrograms()
            if applycablePrograms:
                for rule in applycablePrograms[random.randrange(len(applycablePrograms))]:
                    # get type of a rule
                    # motion
                    if rule['operator'] == 'u':
                        self.coordinates['i'] -= 1
                    elif rule['operator'] == 'd':
                        self.coordinates['i'] += 1
                    elif rule['operator'] == 'l':
                        self.coordinates['j'] -= 1
                    elif rule['operator'] == 'r':
                        self.coordinates['j'] += 1
                    # evolving
                    elif rule['operator'] == '>':
                        self.contents.remove(rule['left'])
                        self.contents += rule['right']
                    # exchange
                    elif rule['operator'] == '<>':
                        self.contents.remove(rule['left'])
                        self.contents += rule['right']
                        if rule['right'] != 'e':
                            self.colony.envMatrix[self.coordinates['i']][self.coordinates['j']].remove(rule['right'])
                        insert2env = {
                            'position':self.coordinates,
                            'symbol':rule['left']
                        }
                        self.colony.toConcat2env.append(insert2env)

