class RuleSystem:
    def __init__(self,variables,constants,axiom,rules):
        self.variables = variables
        self.constants = constants
        self.axiom = axiom
        self.rules = rules

        self.executeActions = self.variables | self.constants

        self.stack = []

    def generate(self,n):
        finalState = self.axiom
        for i in range(n):
            newState = ""
            for step in finalState:
                try:
                    newState += self.rules[step]
                except KeyError:
                    newState += step
            finalState = newState;
        return finalState;

    def execute(self,state):
        for step in state:
            self.executeActions[step]()
