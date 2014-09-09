==============================
Readable Runtime State Machine
==============================

Enables a finite state machine to be created at run-time AND leverage simple attribute syntax creating self documenting code.

Normally these concepts are mutually exclusive, and in any protocol you likely can hard code the states.  This module is handy during prototyping.

For hardcode able finite state machines, the Super State Machine project seems like a more promising solution.

This implementation has no dependencies, nor does it import any of the standard library. It should work on any python version, some exceptions probably apply to the exception handling.  Pun intended.