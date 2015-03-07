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
    >>> SM = StateMachine(['COOL', 'OFF', 'ON', 'WARM'])
    >>> #using strings
    >>> SM == 'cool':
    True
    >>> #Change the state
    >>> SM('warm')
    >>> #using attributes
    >>> SM == SM.cool
    False
    >>> SM == SM.warm
    True

Install
=======

The easiest way to install is::

    pip install smuggle
    
For hardcoded finite state machines, the Super State Machine project seems like a more promising solution.

This implementation has no dependencies, nor does it import any of the standard library. It should work on any python version, some exceptions probably apply to the exception handling.  Pun intended.