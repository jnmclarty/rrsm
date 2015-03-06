"""
Creates the core objects of the Readable Runtime State Machine.

TODO : Implement all the other functionality of a state machine!

When ran as main, this script will set up a simple state machine."""

class StateTypeError(TypeError):
    """Custom error messages, just for instantiation"""
    def __init__(self, t, *args):
        messages = {}
        messages[dict] = "dictionary, "
        messages[list] = "list, "
        self.args = [a for a in args]
        tmp = ["When required state is a ", messages[type(t)], args[0], " RequiredStates = ", str(t)]
        self.msg = "".join(tmp)
    def __repr__(self):
        return self.msg
    def __str__(self):
        return repr(self)

class StateMachine(object):
    """
    The main class for a finite state machine created at run-time.
    
    It's initialized to the state with the lowest assigned value.  In the case
    of a list, that's 0.
    
    Example:
    
    Create a State Machine from a list of strings:
    >>> SM = StateMachine(['Initialized', 'Connected', 'Open'])
    
    Create a State Machine from a dictionary:
    >>> SM = StateMachine({'Initialized' : 10, 'Connected' : 20, 'Open' : 30})
    
    >>> SM.switch_to('Initialized')
    >>> SM == SM.Initialized
    True
    >>> SM.switch_to(20)
    >>> SM == SM.Connected
    True
    """
    
    def __init__(self, ReqStates,InitialState=None):
        
        if type(ReqStates) is dict:
            if not all([type(code) is int for code in ReqStates.values()]):
                raise StateTypeError(ReqStates,
                                     "values (codes) must all be integers.")
            if not all([type(state) in (str,unicode) for state in ReqStates.keys()]):
                raise StateTypeError(ReqStates,
                                     "keys (states) must all be strings.")
            if not len(ReqStates.values()) == len(list(set(ReqStates.values()))):
                raise StateTypeError(ReqStates,
                                     "values (codes) must form a unique set.")
           
            #states are { int : str }
            self._states = dict((code, state) for state, code in ReqStates.items())
            #states are { str : int }
            self._scodes = ReqStates
            
        elif type(ReqStates) is list:
            if not all([type(state) is str for state in ReqStates]):
                raise StateTypeError(ReqStates,
                                     "the elements must all be strings.")
            if not len(ReqStates) == len(list(set(ReqStates))):
                raise StateTypeError(ReqStates,
                                     "the elements must form a unique set of strings.")        
            self._states = dict((code, state) for code, state in enumerate(ReqStates))
            self._scodes = dict((state, code) for code, state in enumerate(ReqStates))
        
        if InitialState is not None:
            self._curcode = InitialState
        else:
            self._curcode = min(self._scodes.values())
        
        for code, state in self._states.items():
            self.__setattr__(state, code)
    def __getitem__(self,key):
        if key in self._states:
            return self._states[key]
        elif key in self._scodes:
            return self._scodes[key]
        else:
            raise KeyError("State {} does not exist".format(key))
    def __repr__(self):
        keys = self.all_states
        vals = [self._scodes[k] for k in keys]
        odict = ", ".join(["'{}' : {}".format(k,v) for k,v in zip(keys,vals)])
        odict = "{{{}}}".format(odict)
        msg = ["StateMachine(", odict, ", InitialState=", str(self._curcode), ")"]
        return "".join(msg)
    def __call__(self, newstate):
        self.switch_to(newstate)
    def switch_to(self, newstate):
        """Switch to a new state
        
        newstate : int or string
            Can be either the value of the state, or the label of the state"""
        if type(newstate) is int:
            if newstate in self._states:
                self._curcode = newstate
            else:
                raise Exception("The state value " + str(newstate) + " does not exist.")            
        else:
            if newstate in self._scodes:
                self._curcode = self._scodes[newstate]
            else:
                raise Exception("The state " + newstate + " does not exist.")
    @property
    def current_state(self):
        """Gets the current state of the state machine, as a string"""
        return self._states[self._curcode]
    @property
    def current_code(self):
        """Gets the current code of the state machine, as an integer"""
        return self._curcode
    @property
    def all_states(self):
        tmp = list(self._states.values())
        tmp.sort()
        return tmp
    @property
    def all_codes(self):
        tmp = list(self._states.keys())
        tmp.sort()
        return tmp
    def __eq__(self, other):
        if type(other) in (str,unicode):
            return self.current_state == other
        elif type(other) == int:
            return self.current_code == other
        elif isinstance(other, StateMachine):
            return self.current_code == other.current_code
        else:
            raise TypeError("Cannot compare {} to StateMachine".format(type(other)))
    def __ne__(self, other):
        return not (self == other)
            
if __name__ == '__main__':
    SM = StateMachine(['A', 'B', 'C'])
    SM('B')
    print SM.current_code
    if SM != 2:
        raise Exception("Problem changing state")    
    