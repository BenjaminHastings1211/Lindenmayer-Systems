class RuleSystem:
    def __init__(self,variables,axiom,rules):
        self.variables = variables
        self.axiom = axiom
        self.rules = rules

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
            self.variables[step]()
