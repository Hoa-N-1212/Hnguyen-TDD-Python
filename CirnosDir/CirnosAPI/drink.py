from os import error,path
import csv
from pathlib import Path
from string.templatelib import convert
optionsDir = Path(__file__).parent.parent.joinpath("Order_Options")
with open(optionsDir.joinpath("Drink_Bases.csv"), newline='') as baseFile:
    baseReader = csv.reader(baseFile)
    baseChoices = list()
    for i in baseReader:
        baseChoices.append(i[0])
with open(optionsDir.joinpath("Drink_Flavors.csv"), newline='') as flavorFile:
    flavorReader = csv.reader(flavorFile)
    flavorChoices = list()
    for i in flavorReader:
        flavorChoices.append(i[0])
with open(optionsDir.joinpath("Drink_Sizes.csv")) as sizeFile:
    sizeReader = csv.DictReader(sizeFile)
    sizeChoices = dict()
    for row in sizeReader:
        sizeChoices = row
    for item in sizeChoices:
        float(sizeChoices[item])

'''
Created Drink object in Sprint 1
Added Drink_Sizes to Drink in Sprint 2
'''     

class Drink:
    '''contains a base and a list of flavors'''
    _base = str
    _flavors = []
    _size = str

    def __init__(self,base,flavors,size):
        size.lower()
        base.lower()
        if base not in baseChoices:
            raise error(f"base not in base choices {base}")
        for item in flavors:
            item.lower()
            if item not in flavorChoices:
                raise error(f"flavor not in flavor choices: {item}")
        if size not in sizeChoices.keys():
            raise error(f"size not in size list")
        self._base = base
        self._flavors = flavors
        self._size = size

    # getters
    def get_base(self):
        '''returns the base drink'''
        return self._base
    
    def get_flavors(self):
        '''returns all flavors of drink'''
        return self._flavors
    
    def get_num_flavors(self):
        '''returns the number of flavors in drink'''
        return len(self._flavors)

    def get_flavor_cost(self):
        '''returns the cost of all flavors in this drink, tests not made'''
        return self.get_num_flavors() * .15

    def get_size(self):
        '''returns size of drink'''
        return self._size

    def get_size_cost(self):
        '''returns the cost of the size of the drink'''
        return float(sizeChoices.get(self.get_size()))

    # extra credit addon (2), can be called while the drink is init, live calculate
    def get_total(self):
        '''returns the total of the drink'''
        total = self.get_flavor_cost() + self.get_size_cost()
        return total

    def get_tax(self):
        '''returns the tax value of this drink'''
        return self.get_total() * .0725

    # extra credit addon
    def print_drink(self):
        '''prints the drink into the console'''
        print(f"{self.get_size} {self.get_base()} with {", ".join(self.get_flavors())}")
    
    # setters
    def set_base(self,newBase):
        '''sets the base as a new base, refuses if the new base is not one of the choices'''
        newBase.lower()
        if newBase not in baseChoices:
            raise error(f"base not in base choices {self._base}")
        self._base = newBase
        
    # checks for duplicate in the array, skips intruction if does
    def set_flavors(self,flavorArray):
        '''set all flavors as new list of flavors'''
        for item in flavorArray:
            item.lower()
            if item not in flavorChoices:
                raise error(f"flavor not in flavor choices: {item}")
        if duplicateCheck(flavorArray):
            raise error(f"duplicate of {item} in given list")
        self._flavors = flavorArray

    def add_flavors(self,flavor):
        '''adds another flavor to the end of the list, rejects if its already included'''
        flavor.lower()
        if flavor in self._flavors:
            raise error(f"flavor already in list: {flavor}")
        if flavor not in flavorChoices:
                raise error(f"flavor not in flavor choices: {flavor}")
        self._flavors.append(flavor)

    def set_size(self,size):
        '''checks if size is in dict, changes size to input size'''
        size.lower()
        if size not in sizeChoices.keys():
            raise error(f"size not in size list")
        self._size = size

# misc 
def duplicateCheck(list):
    '''checks duplicates in list'''
    already_seen = {}  
    for item in list:
        if item in already_seen:
            return True
        already_seen[item] = 0
    return False

