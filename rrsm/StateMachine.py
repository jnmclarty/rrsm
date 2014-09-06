class StateMachine(object):
    def __init__(self,RequiredStates,InitialState=0):

    
        if type(RequiredStates) is dict:
            assert all([type(state) is int for state in RequiredStates.values()]), "When RequiredStates is a dictionary, it's values must all be of type integer"
            assert len(RequiredStates.values()) == len(list(set(RequiredStates.values()))), "When RequiredStates is a dictionary, it's values must form a unique set"
            self.States = RequiredStates
            self.StateCodes = dict([(code,state) for state,code in RequiredStates.iteritems()]) # This is done for speed of the rest of the class
        elif type(RequiredStates) is list:
            assert len(RequiredStates) == len(list(set(RequiredStates))), "RequiredStates must be list of unique strings"
            self.States = dict([(code,state) for code,state in enumerate(RequiredStates)])
            self.StateCodes = dict([(state,code) for code,state in enumerate(RequiredStates)])

        self.SwitchTo(InitialState)
        
        for StateCodes,States in self.States.iteritems():
            setattr(StateMachine,States,StateCodes)
    def __repr__(self):
        return "StateMachine(" + str(self.StateCodes) + ",InitialState=" + str(self.CurrentCode) + ")"
    def SwitchTo(self,NewState):
        if type(NewState) is int:
            self.CurrentCode = NewState
        else:
            self.CurrentCode = self.StateCodes[NewState]
    def CurrentState(self):
        return self.States[self.CurrentCode]
    def __eq__(self,other):
        return self.CurrentCode == other
        
SM = StateMachine(['A','B'])
SM2 = StateMachine({'A' : 0,'B' : 1})