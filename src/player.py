# Write a class to hold player information, e.g. what room they are in
# currently.
from item import Item
class Player:

    def __init__(self, name, room):
         self.name = name
         self.room = room
         self.items=[]        

    def add_items(self,name, description):
        self.items.append(Item(name, description))
    
    def return_list(self):
        return self.items
    
    def __repr__(self):
        return self.items