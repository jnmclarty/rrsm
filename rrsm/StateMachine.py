class StateMachine(object):
    def __init__(self,RequiredStates,InitialState=0):
    
        self.States = RequiredStates
        self.StateCodes = dict([(v,k) for k,v in RequiredStates.iteritems()]) # This is done for speed of the rest of the class
        
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
        