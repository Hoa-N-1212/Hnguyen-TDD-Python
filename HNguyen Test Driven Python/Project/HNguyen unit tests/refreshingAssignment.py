from os import error

baseChoices = ["water", "sbrite", "pokeacola", "mr. salt", "hill fog", "leaf wine"]
flavorChoices = ["lemon", "cherry", "strawberry", "mint", "blueberry", "lime"]
# --- --- ---
# forced to interpret several getter functions as the instructions for them are vague and don't go into detail
# what they do or how much something would cost
# each choice above should be paired with a price in an object and the rest of the assignment would have to be reworked
# --- --- --- 

#%% Order class
class Order:
    '''contains a list of Drink'''
    _items = []

    def __init__(self,drinks):
        if not isinstance(drinks,list):
            raise error("items must be in a list")
        self._items=drinks
        

#getters
    def get_item(self,index):
        '''returns the drink item at the index'''
        return self._items[index]
    
    def get_all_items(self):
        '''returns all items in the list as a list'''
        return self._items
    
    def get_num_items(self):
        '''returns the number of items in the list'''
        return len(self._items)
    
    # vague instructions assuming total means each base and flavor choice has a set price through the POS system
    def get_total(self):
        '''returns how much the order will cost'''
        print("not implemented as it requires what each base and flavor would cost")
        raise NotImplementedError
        #total = 0
        #for item in self._items:
        #    # iterate through each base and add the price for whichever base is given
        #    if item.get_base == :
        #       total += 
        #   #iterate through all flavors in list and add to total
        #   for item in self._items:
        #      for flavor in item.get_flavors():
        #         match flavor:
        #                case water:
        #                    total +=
        #return total
        

    def get_reciept(self):
        '''returns a string that describes every item'''
        recieptString = ""
        for item in self._items:
            recieptString = recieptString + item.get_base() + " with " + ", ".join(item.get_flavors()) + "\n"
        return recieptString

#setters
    def add_item(self, drink):
        '''adds a drink item to the order object'''
        if not isinstance(drink,Drink):
            raise error(f"{drink} is not a drink instance")
        self._items.append(drink)
    
    def remove_item(self,index):
        self._items.pop(index)

#%% Drink class
class Drink:
    '''contains a base and a list of flavors'''
    _base = str
    _flavors = []
    def __init__(self,base,flavors):
        if base not in baseChoices:
            raise error(f"base not in base choices {base}")
        for item in flavors:
            if item not in flavorChoices:
                raise error(f"flavor not in flavor choices: {item}")
        self._base = base
        self._flavors = flavors

    #getters
    def get_base(self):
        '''returns the base drink'''
        return self._base
    
    def get_flavors(self):
        '''returns all flavors of drink'''
        return self._flavors
    
    def get_num_flavors(self):
        '''returns the number of flavors in drink'''
        return len(self._flavors)
    
    #setters
    def set_base(self,newBase):
        '''sets the base as a new base, refuses if the new base is not one of the choices'''
        if newBase not in baseChoices:
            raise error(f"base not in base choices {self._base}")
        self._base = newBase

    #checks for duplicate in the array, skips intruction if does
    def set_flavors(self,flavorArray):
        '''set all flavors as new list of flavors'''
        for item in flavorArray:
            if item not in flavorChoices:
                raise error(f"flavor not in flavor choices: {item}")
        if duplicateCheck(flavorArray):
            raise error(f"duplicate of {item} in given list")
        self._flavors = flavorArray

    def add_flavors(self,flavor):
        '''adds another flavor to the end of the list, rejects if its already included'''
        if flavor in self._flavors:
            raise error(f"flavor already in list: {flavor}")
        if flavor not in flavorChoices:
                raise error(f"flavor not in flavor choices: {flavor}")
        self._flavors.append(flavor)

# misc 
def duplicateCheck(list):
    '''checks duplicates in list'''
    already_seen = {}  
    for item in list:
        if item in already_seen:
            return True
        already_seen[item] = 0
    return False

# --- --- ---
# no interactivity was required on the assignment, only if the getters and setters are correct
# tests are not required for this assignment
# assignment forced to be either in text or web URL, cannot be sent as file
# --- --- ---
