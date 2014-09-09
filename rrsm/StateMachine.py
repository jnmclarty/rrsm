"""
This module sreates the core objects of the Readable Runtime State Machine.

TODO : Implement all the other functionality of a state machine!

When ran as main, this script will set up a simple state machine."""

class StateMachineException(Exception):
    """Custom error messages, just for setup"""
    def __init__(self, t, *args):
        messages = {}
        messages[dict] = "dictionary, "
        messages[list] = "list, "
        self.args = [a for a in args]
        tmp = ["When RequiredStates is a ", messages[type(t)], args[0], " RequiredStates = ", str(t)]
        self.msg = "".join(tmp)
    def __repr__(self):
        return self.msg
    def __str__(self):
        return repr(self)

class StateMachine(object):
    """
    The main class for a state machine.
    
    Example:
    
    Create a State Machine from a list of strings:
    >>> SM = StateMachine(['Initialized', 'Connected', 'Closed'])
    
    Create a State Machine from a dictionary:
    >>> SM = StateMachine({'Initialized' : 10, 'Connected' : 20, 'Closed' : 30})
    
    >>> SM.switch_to('Initialized')
    >>> SM == SM.Initialized
    True
    >>> SM.switch_to(20)
    >>> SM == SM.Connected
    True
    """
    
    def __init__(self, RequiredStates, InitialState=0):    
        if type(RequiredStates) is dict:

            if not all([type(code) is int for code in RequiredStates.values()]):
                raise StateMachineException(RequiredStates, 
                                            "values (codes) must all be integers.")
            if not all([type(state) is str for state in RequiredStates.keys()]):
                raise StateMachineException(RequiredStates,
                                            "keys (states) must all be strings.")
            if not len(RequiredStates.values()) == len(list(set(RequiredStates.values()))):
                raise StateMachineException(RequiredStates,
                                            "values must form a unique set.")
    
            self.states = dict([(code, state) for state, code in RequiredStates.iteritems()])
            self.scodes = RequiredStates
        elif type(RequiredStates) is list:
            if not all([type(state) is str for state in RequiredStates]):
                raise StateMachineException(RequiredStates,
                                            "the elements must all be strings.")
            if not len(RequiredStates) == len(list(set(RequiredStates))):
                raise StateMachineException(RequiredStates,
                                            "the elements must form a unique set of strings.")        
            self.states = dict([(code, state) for code, state in enumerate(RequiredStates)])
            self.scodes = dict([(state, code) for code, state in enumerate(RequiredStates)])

        self.switch_to(InitialState)
        
        for code, state in self.states.iteritems():
            self.__setattr__(state, code)
    def __repr__(self):
        msg = ["StateMachine(", str(self.scodes), ", InitialState=", str(self.curcode), ")"]
        return "".join(msg)
    def switch_to(self, newstate):
        """Switch to a new state
        
        newstate : int or string
            Can be either the value of the state, or the label of the state"""
        if type(newstate) is int:
            if newstate in self.scodes.values():
                self.curcode = newstate
            else:
                raise Exception("The state value " + str(newstate) + " does not exist,yet")            
            self.curcode = newstate
        else:
            if newstate in self.scodes:
                self.curcode = self.scodes[newstate]
            else:
                raise Exception("The state " + newstate + " does not exist,yet")
    def current_state(self):
        """Gets the current state of the machine, as a string"""
        return self.states[self.curcode]
    def __eq__(self, other):
        return self.curcode == other

if __name__ == '__main__':
    pass
    #SM = StateMachine(['A', 'B', 'C'])
    
    #Examples of error cases:
    #SM = StateMachine(['A', 1])
    #SM = StateMachine(['A', 'A', 'B'])
    #SM2 = StateMachine({'A' : 0,  2 : 1})
    #SM2 = StateMachine({'A' : 0,  'B' : '1'})
    #SM2 = StateMachine({'A' : 0,  'B' : 0})
    