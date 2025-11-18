from os import error
import pytest
import refreshingAssignment as OrderSys


testDrink = OrderSys.Drink("hill fog",["blueberry","lime"])
testDrink2 = OrderSys.Drink("water",["cherry"])
testOrder = OrderSys.Order([testDrink,testDrink2])

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
    testDrink.set_flavors("cherry")

def test_drinkSetFlavors():
    '''should set the flavors to ["mint","blueberry]'''
    testDrink.set_flavors(["mint", "blueberry"])
    assert testDrink.get_flavors() == ["mint","blueberry"]
    with pytest.raises(OSError):
        drinkSetFlavorsError()

#%% order getter tests
def test_orderGetAllItem():
    '''
    should return type Drink (1)
    should return type List (2)
    '''
    assert isinstance(testOrder.get_all_items()[0],OrderSys.Drink)
    assert isinstance(testOrder.get_all_items(),list)

def test_orderGetItem():
    '''should return the first drink object'''
    assert testOrder.get_item(0) == testDrink

def test_orderGetNumItems():
    '''should return number of drinks in testOrder'''
    assert testOrder.get_num_items() == 2

def test_orderGetReciept():
    '''should return a string // formatting depends on the user and should be adjusted as needed'''
    assert isinstance(testOrder.get_reciept(),str)

# remove and retest once implemeted
def orderGetTotalError():
    '''replace when specified'''
    testOrder.get_total()

def test_orderGetTotal():
    '''replace when specified'''
    with pytest.raises(NotImplementedError):
        orderGetTotalError()

#%% order setter tests
def orderAddItemError():
    '''forces an error from add_item'''
    testOrder.add_item("blahbalbh")

def test_orderAddItem():
    '''adds a second instance of the first order'''
    testOrder.add_item(testDrink)
    assert testOrder.get_item(2) == testDrink
    with pytest.raises(OSError):
        orderAddItemError()