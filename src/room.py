# Implement a class to hold room information. This should have name and
# description attributes.
from item import Item

class Room(Item):
    def __init__(self, name, description):
         self.name=name
         self.description=description
         self.items=[]

    def add_items(self,name, description):
        self.items.append(Item(name, description))
    
    def remove_items(self,name):
        for i in self.items:
            if i.name==name:
                print("test")
                self.items.remove(i)

    def __repr__(self):
        for i in self.items:
            print(f"{i.name} {i.description}")
