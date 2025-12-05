from os import error
import pytest
from CirnosAPI import food as FoodSys

'''
Created tests for Food module in Sprint 3
'''

testFood = FoodSys.Food("hotdog", "chili")

#%% food getter tests
def test_foodGetFood():
    assert testFood.get_food() == "hotdog"

def test_foodGetTopping():
    assert testFood.get_topping() == "chili"

def test_foodGetTotal():
    assert testFood.get_total() == 2.9

def test_foodGetTax():
    assert testFood.get_tax() == .21025

#%% food setter tests
def test_foodSetFood():
    testFood.set_food("ice cream")
    assert testFood.get_food() == "ice cream"

def test_foodSetTopping():
    testFood.set_topping("caramel sauce")
    assert testFood.get_topping() == "caramel sauce"