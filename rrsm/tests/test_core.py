from rrsm import StateMachine, StateTypeError

from unittest import TestCase

import nose

class StateMachineTests(TestCase):
  
    def setUp(self):
        pass
        
    def tearDown(self):
        pass
        
    def test_good_list(self):
        SM = StateMachine(['A','B','C'])
        SM2 = StateMachine(['A','D','E'])
        if SM != 'A':
            raise Exception("Should have instantiated at 'A'")
        if SM != 0:
            raise Exception("Should have instantiated at 0")
        if SM['B'] != 1:
            raise Exception("Problem with getting state")
        if SM[2] != 'C':
            raise Exception("Problem with getting code")
        SM('B')
        if SM != 1:
            raise Exception("Problem changing state")            
        SM(2)
        if SM != 'C':
            raise Exception("Problem changing state, using code")   

    def test_good_dict(self):
        
        SM = StateMachine(dict(zip(['A','B','C'],[10,20,30])))
        if SM != 'A':
            raise Exception("Should have instantiated at 'A'")
        if SM != 10:
            raise Exception("Should have instantiated at 10")
        if SM['B'] != 20:
            raise Exception("Problem with getting state")
        if SM[30] != 'C':
            raise Exception("Problem with getting code")
        SM('B')
        if SM != 20:
            raise Exception("Problem changing state")            
        SM(30)
        if SM != 'C':
            raise Exception("Problem changing state, using code")  

    def test_all_sc(self):
        SM = StateMachine(['A','B','C'])
        if SM.all_states != ['A','B','C']:
            raise Exception("Problem with states")
        if SM.all_codes != [0,1,2]:
            raise Exception("Problem with codes")
    def test_repr(self):
        SM = StateMachine(['A','B','C'])
        if repr(SM) != "StateMachine({'A' : 0, 'B' : 1, 'C' : 2}, InitialState=0)":
            raise Exception("Problem with repr")
    
    def test_two_statemachines(self):
        SM = StateMachine(['A','B','C'], InitialState=2)
        SM2 = StateMachine(['Z','Y','C'], InitialState=2)

        if SM != SM2:
            raise Exception("Problem comparing State Machines")
            
    def test_bad_instatiations(self):
        
        try:
            StateMachine([1])
        except StateTypeError as e:
            if e.msg != "When required state is a list, the elements must all be strings. RequiredStates = [1]":
                raise Exception("Problem with required states")
    #TODO
        #Examples of error cases:
    #SM = StateMachine(['A', 1])
    #SM = StateMachine(['A', 'A', 'B'])
    #SM2 = StateMachine({'A' : 0,  2 : 1})
    #SM2 = StateMachine({'A' : 0,  'B' : '1'})
    #SM2 = StateMachine({'A' : 0,  'B' : 0})
            
if __name__ == '__main__':
    nose.runmodule(argv=[__file__, '-vvs', '-x'],exit=False) #, '--pdb-failure'],