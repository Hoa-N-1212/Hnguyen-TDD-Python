from os import error, path
from pathlib import Path
import csv

from _pytest.stash import D

optionsDir = Path(__file__).parent.parent.joinpath("Order_Options")

with open(optionsDir.joinpath("Storm_Flavors.csv"), newline='') as flavorsFile:
    flavorReader = csv.DictReader(flavorsFile)
    flavorChoices = dict()
    for row in flavorReader:
        flavorChoices = row
with open(optionsDir.joinpath("Storm_Toppings.csv"), newline='') as toppingFile:
    toppingReader = csv.DictReader(toppingFile)
    toppingChoices = dict()
    for row in toppingReader:
        toppingChoices = row
'''
Created in Sprint 4
'''
class Storm:
    _flavor = ""
    _toppings = []

    def __init__(self, flavor, toppings):
        tempToppingList = []
        flavor = flavor.casefold()
        if flavor not in flavorChoices.keys():
            raise error(f"flavor:{flavor} not in icestorm flavor choices")
        self._flavor = flavor
        if not isinstance(toppings,list):
            raise error(f"toppings should be in a list")
        for topping in toppings:
            topping = topping.casefold()
            if topping not in toppingChoices.keys():
                raise error(f"topping:{topping} not in icestorm topping choices")
            tempToppingList.append(topping)
        self._toppings = tempToppingList.copy()
        tempToppingList.clear()
            
        
       
#%% getters
    
    def get_flavor(self):
        '''returns the flavor of the icestorm'''
        return self._flavor

    def get_toppings(self):
        '''returns all toppings as a list of the icestorm'''
        return self._toppings

    def get_total(self):
        '''returns the total cost of the ice storm'''
        total = float(flavorChoices.get(self.get_flavor()))
        for topping in self.get_toppings():
            total += float(toppingChoices.get(topping))
        return total

    def get_tax(self):
        return self.get_total()*0.725
#%% setters
    
    def set_flavor(self, flavor):
        '''sets the flavor of icestorm to given string'''
        flavor = flavor.lower()
        if flavor not in flavorChoices.keys():
            raise error("flavor not in icestorm flavor choices")
        self._flavor = flavor
    
    def set_toppings(self, toppings):
        '''sets the toppings of ice storm to given list of strings'''
        if not isinstance(toppings,list):
            raise error("toppings should be in a list")
        for topping in toppings:
            topping = topping.lower()
            if topping not in toppingChoices.keys():
                raise error("topping not in icestorm topping choices")
        self._toppings = toppings

    def add_topping(self, topping):
        '''adds a topping to the end of the toppings list of ice storm'''
        topping = topping.lower()
        if topping not in toppingChoices.keys():
            raise error("topping not in icestorm topping choices")
        self._toppings.append(topping)
