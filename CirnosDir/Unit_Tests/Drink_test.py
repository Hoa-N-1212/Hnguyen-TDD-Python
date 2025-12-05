from os import error
import pytest
from CirnosAPI import drink as DrinkSys

'''
Added Drink Tests in Sprint 2
Added tests for Drink_Sizes in Sprint 2
Added tests for get_tax and get_reciept in Sprint 2
'''

testDrink = DrinkSys.Drink("hill fog",["blueberry","lime"],"small")
testDrink2 = DrinkSys.Drink("water",["cherry"],"medium")
#%% drink getter tests
def test_drinkGetBase():
    '''should return "hill fog"'''
    assert testDrink.get_base() == "hill fog"

def test_drinkGetFlavor():
    '''
    should return "blueberry" (1)
    should return type list (2)
    '''
    assert testDrink.get_flavors()[0] == "blueberry"
    assert isinstance(testDrink.get_flavors(),list)

def test_drinkGetNumFlavor():
    '''should return the number of flavors in testOrder'''
    assert testDrink.get_num_flavors() == 2

def test_drinkGetFlavorCost():
    '''should return cost of all flavors'''
    assert testDrink.get_flavor_cost() == .3
    assert testDrink2.get_flavor_cost() == .15
   
def test_drinkGetSize():
    '''should return size of the drink'''
    assert testDrink.get_size() == "small"

def test_drinkGetTotal():
    '''should return cost of the drink, medium(1.75) one flavor(.15)'''
    assert testDrink2.get_total() == float(1.9)

def test_drinkGetTax():
    '''should return the tax amount of the drink'''
    taxedAmount = (1.9*.0725)
    assert testDrink2.get_tax() == taxedAmount

#%% drink setter tests
def drinkSetBaseError():
    '''creates set base error'''
    testDrink.set_base("blahblah")
    
def test_drinkSetBase():
    '''should change base to "water"'''
    testDrink.set_base("water")
    assert testDrink.get_base() == "water"
    with pytest.raises(OSError):
        drinkSetBaseError()

def drinkSetFlavorsError():
    '''creates set flavors error'''
    testDrink.set_flavors("cherry")
    
def test_drinkSetFlavors():
    '''should set the flavors to ["mint","blueberry]'''
    testDrink.set_flavors(["mint", "blueberry"])
    assert testDrink.get_flavors() == ["mint","blueberry"]
    with pytest.raises(OSError):
        drinkSetFlavorsError()

def drinkAddFlavors():
    '''should add another flavor to the order'''
    testDrink.add_flavors("strawberry")
    isTrue = bool
    if "strawberry" in testDrink.get_flavors():
        isTrue = True
    assert isTrue
    with pytest.raises(OSError):
        testDrink.add_flavors("strawberry")
    with pytest.raises(OSError):
        testDrink.add_flavors("wrong entry")

def test_drinkSetSize():
    '''should change drink size value'''
    testDrink.set_size("mega")
    assert testDrink.get_size() == "mega"
