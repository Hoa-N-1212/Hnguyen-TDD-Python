from os import error
from CirnosAPI import drink as DrinkSys
from CirnosAPI import food as FoodSys
'''
Created Order object in Sprint 1
Added get_tax and get_reciept in Sprint 2 additions
Implemented the Food module into the order Class in Sprint 3
'''
tax = .0725

#%% Order class
class Order:
    '''contains a list of Drink and Food'''
    _items = []

    def __init__(self,items):
        if not isinstance(items,list):
            raise error("items must be in a list")
        self._items=items
        

# getters
    def get_item(self,index):
        '''returns the drink item at the index'''
        return self._items[index]
    
    def get_all_items(self):
        '''returns all items in the list as a list'''
        return self._items
    
    def get_num_items(self):
        '''returns the number of items in the list'''
        return len(self._items)
    
    # extra credit (2), can be called as the order is init, live calculate
    def get_total(self):
        '''returns how much the order will cost'''
        sizeCost = 0
        flavorCost = 0
        foodCost = 0
        for item in self._items:
            if isinstance(item,DrinkSys.Drink):
                # iterate through each size and add the price for whichever base is given
                sizeCost += item.get_size_cost()
                # add .15 for each flavor
                flavorCost += item.get_flavor_cost()
            if isinstance(item,FoodSys.Food):
                foodCost = item.get_total()
        return sizeCost+flavorCost+foodCost

    def get_tax(self):
        '''returns total tax of the order'''
        return self.get_total()*tax

        

    def get_reciept(self):
        '''returns a string that describes every item'''
        recieptString = ""
        for item in self._items:
            if isinstance(item,DrinkSys.Drink):
                recieptString = f"{recieptString} {item.get_base()} with {", ".join(item.get_flavors())}:: ${round(item.get_total()+item.get_tax(),2)} (${round(item.get_tax(),2)})tax \n"
            if isinstance(item,FoodSys.Food):
                recieptString = f"{recieptString} {item.get_food()} with {item.get_topping()}:: ${round(item.get_total()+item.get_tax(),2)} (${round(item.get_tax(),2)})tax \n"
        return recieptString+f"\nTotal:${round(self.get_total()+self.get_tax(),2)} (${round(self.get_tax(),2)})tax"

    # extra credit addon (1)
    def print_reciept(self):
        '''prints the reciept of the order'''
        print(self.get_reciept())
# setters
    def add_item(self, drink):
        '''adds a drink item to the order object'''
        if not isinstance(drink,DrinkSys.Drink):
            raise error(f"{drink} is not a drink instance")
        self._items.append(drink)
    
    def remove_item(self,index):
        self._items.pop(index)


