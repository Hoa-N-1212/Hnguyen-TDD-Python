from os import error,path
from pathlib import Path
import csv
optionsDir = Path(__file__).parent.parent.joinpath("Order_Options")
with open(optionsDir.joinpath("Food_Choices.csv"), newline='') as foodFile:
    foodReader = csv.DictReader(foodFile)
    foodChoices = dict()
    for row in foodReader:
        foodChoices = row
with open(optionsDir.joinpath("Food_Toppings.csv"), newline='') as toppingFile:
    toppingReader = csv.DictReader(toppingFile)
    toppingChoices = dict()
    for row in toppingReader:
        toppingChoices = row

'''
Created the Food module in Sprint 3
'''

class Food: 
    '''contains the kind of food and its topping'''
    _food = str
    _topping = str

    def __init__(self, food, topping):
        food.lower()
        topping.lower()

        if food not in foodChoices.keys():
            raise error("food not a food option")
        if topping not in toppingChoices.keys():
            raise error("topping not a topping option")
        self._food = food
        self._topping = topping

    # getters

    def get_food(self):
        '''returns the kind of food'''
        return self._food
    
    def get_topping(self):
        '''returns food topping'''
        return self._topping

    def get_total(self):
        '''returns price of this food item'''
        total = float(foodChoices.get(self.get_food())) + float(toppingChoices.get(self.get_topping()))
        return total


    def get_tax(self):
        '''returns tax of this food item'''
        return self.get_total()*.0725

    # setters

    def set_food(self,food):
        '''changes food type to given food'''
        if food not in foodChoices.keys():
            raise error("food not a food option")
        self._food = food

    def set_topping(self,topping):
        '''changes topping to given topping'''
        if topping not in toppingChoices.keys():
            raise error("topping not a topping option")
        self._topping = topping