==============================
Readable Runtime State Machine
==============================

.. image:: https://travis-ci.org/jnmclarty/rrsm.svg?branch=master
    :target: https://travis-ci.org/jnmclarty/rrsm
    
.. image:: https://coveralls.io/repos/jnmclarty/rrsm/badge.svg 
    :target: https://coveralls.io/r/jnmclarty/rrsm

Enables a finite state machine to be created **at run-time** *AND* leverage simple attribute syntax creating **self documenting code**.

Normally these concepts are mutually exclusive, and in any finished design can hard coded.  This module is handy during prototyping.

Usage
=====

.. code:: python

    >>> from rrsm import StateMachine
    
    >>> #Instantiation works with a list of the form ['state', ...] 
    ... #or a dictionary of the form {'state' : value, ...}
    ... SM = StateMachine(['cool', 'off', 'on', 'warm'])   

    >>> #checking state works against strings or integers:
    ... SM == 'cool'
    True
    
    >>> #Change the state
    ... SM('warm')
    
    >>> #using attributes to check state:
    ... SM == SM.cool
    False
    >>> SM == SM.warm
    True
    >>> SM.current_state
    'warm'
    >>> SM.current_code
    3
     
For hardcoded finite state machines, the Super State Machine project seems like a more promising solution.

This implementation has no dependencies, nor does it import any of the standard library. It should work on any python version, but it's tested with 2.6, 2.7, 3.3 and 2.4. Some exceptions probably apply to the exception handling.  Pun intended.

Install
=======

The easiest way to install is::

    pip install smuggle