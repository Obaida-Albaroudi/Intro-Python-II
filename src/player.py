# Write a class to hold player information, e.g. what room they are in
# currently.
from item import Item
class Player(Item):

    def __init__(self, name, room):
         self.name = name
         self.room = room
         self.items=[]        

    def add_items(self,name, description):
        self.items.append(Item(name, description))
    
    def remove_items(self,name):
        for i in self.items:
            if i.name ==name:
                self.items.remove(i)
    
    def __repr__(self):
        for i in self.items:
            print(f"{i.name} {i.description}")
