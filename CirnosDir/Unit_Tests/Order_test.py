from os import error
import pytest
from CirnosAPI import order as OrderSys, drink as DrinkSys, food as FoodSys

'''
Added Order Tests in Sprint 2
'''

testDrink = DrinkSys.Drink("hill fog",["blueberry","lime"],"small")
testDrink2 = DrinkSys.Drink("water",["cherry"],"medium")
testFood = FoodSys.Food("hotdog", "chili")
testOrder = OrderSys.Order([testDrink,testDrink2,testFood])

#%% order getter tests
def test_orderGetAllItem():
    '''
    should return type Drink (1)
    should return type List (2)
    '''
    assert isinstance(testOrder.get_all_items()[0],DrinkSys.Drink)
    assert isinstance(testOrder.get_all_items(),list)

def test_orderGetItem():
    '''should return the first drink object'''
    assert testOrder.get_item(0) == testDrink

def test_orderGetNumItems():
    '''should return number of drinks in testOrder'''
    assert testOrder.get_num_items() == len(testOrder.get_all_items())

def test_orderGetReciept():
    '''should return a string // formatting depends on the user and should be adjusted as needed'''
    assert isinstance(testOrder.get_reciept(),str)

def test_orderGetTotal():
    '''returns the price of the order, small(1.5) and two flavors(.3)'''
    testOrder2 = OrderSys.Order([DrinkSys.Drink("water",["cherry","strawberry"],"small"), FoodSys.Food("tater tots", "bacon bits")])
    assert testOrder2.get_total() == 3.8

def test_orderGetTax():
    '''should return tax of the order'''
    testOrder2 = OrderSys.Order([DrinkSys.Drink("water",["cherry","strawberry"],"small"),FoodSys.Food("ice cream","caramel sauce")])
    assert testOrder2.get_tax() == testOrder2.get_total()*.0725

#%% order setter tests
def orderAddItemError():
    '''forces an error from add_item'''
    testOrder.add_item("blahbalbh")

def test_orderAddItem():
    '''adds a second instance of the first order'''
    testOrder.add_item(testDrink)
    assert testOrder.get_item(-1) == testDrink
    with pytest.raises(OSError):
        orderAddItemError()