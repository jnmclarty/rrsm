class StateMachine(object):
    def __init__(self,RequiredStates,InitialState=0):
    
        if type(RequiredStates) is dict:
            self.States = RequiredStates
            self.StateCodes = dict([(code,state) for state,code in RequiredStates.iteritems()]) # This is done for speed of the rest of the class
        elif type(RequiredStates) is list:
            self.States = dict([(code,state) for code,state in enumerate(RequiredStates)])
            self.StateCodes = dict([(state,code) for code,state in enumerate(RequiredStates)])

        self.SwitchTo(InitialState)
        
        for StateCodes,States in self.States.iteritems():
            setattr(StateMachine,States,StateCodes)
            
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