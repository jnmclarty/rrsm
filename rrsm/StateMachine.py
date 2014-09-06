class StateMachineException(Exception):
    def __init__(self, t, *args):
        Messages = {}
        Messages[dict] = " dictionary, "
        Messages[list] = " list, "
        self.args = [a for a in args]
        self.msg = "When RequiredStates is a" + Messages[type(t)] + args[0] + "  RequiredStates = " + str(t)
    def __repr__(self):
        return self.msg
    def __str__(self):
        return repr(self)

class StateMachine(object):
    def __init__(self,RequiredStates,InitialState=0):

    
        if type(RequiredStates) is dict:
            if not all([type(code) is int for code in RequiredStates.values()]):
                raise StateMachineException(RequiredStates,"values (codes) must all be integers.")
            if not all([type(state) is str for state in RequiredStates.keys()]):
                raise StateMachineException(RequiredStates,"keys (states) must all be strings.")
            if not len(RequiredStates.values()) == len(list(set(RequiredStates.values()))):
                raise StateMachineException(RequiredStates,"values must form a unique set.")
            self.States = dict([(code,state) for state,code in RequiredStates.iteritems()]) # This is done for speed of the rest of the class
            self.StateCodes = RequiredStates
        elif type(RequiredStates) is list:
            if not all([type(state) is str for state in RequiredStates]):
                raise StateMachineException(RequiredStates,"the elements must all be strings.")
            if not len(RequiredStates) == len(list(set(RequiredStates))):
                raise StateMachineException(RequiredStates,"the elements must form a unique set of strings.")        
            self.States = dict([(code,state) for code,state in enumerate(RequiredStates)])
            self.StateCodes = dict([(state,code) for code,state in enumerate(RequiredStates)])

        self.SwitchTo(InitialState)
        
        for code,state in self.States.iteritems():
            setattr(StateMachine,state,code)
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
        
SM = StateMachine(['A',1])
SM = StateMachine(['A','A','B'])
SM2 = StateMachine({'A' : 0, 2 : 1})
SM2 = StateMachine({'A' : 0, 'B' : '1'})
SM2 = StateMachine({'A' : 0, 'B' : 0})