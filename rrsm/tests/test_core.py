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
        if SM != 'A':
            raise Exception("Should have instantiated at 'A'")
        if SM != 0:
            raise Exception("Should have instantiated at 0")
        if SM['B'] != 1:
            raise Exception("Problem with getting state")
        if SM[2] != 'C':
            raise Exception("Problem with getting code")
        SM('B')
        if SM != 2:
            raise Exception("Problem changing state")            
        SM(3)
        if SM != 'C':
            raise Exception("Problem changing state, using code")   


    def test_good_dict(self):
        
        SM = StateMachine(dict(zip(['A','B','C'],[10,20,30])))
        if SM != 'A':
            raise Exception("Should have instantiated at 'A'")
        if SM != 0:
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
            
if __name__ == '__main__':
    nose.runmodule(argv=[__file__, '-vvs', '-x'],exit=False) #, '--pdb-failure'],