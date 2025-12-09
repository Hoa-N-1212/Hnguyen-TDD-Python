from os import error
import pytest
from CirnosAPI import icestorm as StormSys

'''
Created in Sprint 4
'''
testStorm = StormSys.Storm("Chocolate",["Cherry","whipped Cream","storios"])

#%% getter tests

def test_AstormGetFlavor():
    '''should return Chocolate'''
    assert testStorm.get_flavor() == "chocolate"

def test_AstormGetToppings():
    '''should return list with cherry,whipped cream,storios'''
    assert testStorm.get_toppings() == ["cherry","whipped cream","storios"]

def test_AstormGetTotal():
    '''should return 4'''
    assert testStorm.get_total() == 4

def test_AstormGetTax():
    '''should return 2.9'''
    assert testStorm.get_tax() == 2.9

#%% setter tests

def test_BstormSetFlavor():
    '''flavor should change to vanilla bean'''
    testStorm.set_flavor("vanilla Bean")
    assert testStorm.get_flavor() == "vanilla bean"

def test_BstormSetToppings():
    '''toppings should be set to dig dogs'''
    testStorm.set_toppings(["dig dogs"])
    assert testStorm.get_toppings() == ["dig dogs"]

def test_BstormAddTopping():
    '''cookie dough should be added to the end of toppings list'''
    testStorm.add_topping("cookie dough")
    assert testStorm.get_toppings()[-1] == "cookie dough"
