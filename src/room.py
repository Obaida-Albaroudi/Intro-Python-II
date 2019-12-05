# Implement a class to hold room information. This should have name and
# description attributes.
from item import Item

class Room:
    def __init__(self, name, description):
         self.name=name
         self.description=description
         self.itemss=[]

    def add_items(self,name, description):
        self.itemss.append(Item(name, description))
    
    # def drop_items(self, name):
    #     for key, value in items.items():
    #         if name in key:
    #         return key

