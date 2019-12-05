from room import Room
from player import Player

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Main
#

player = Player("Obaida", "outside")
player.add_items("flashlight","Used to help light up the passage ways.")
player.add_items("flashlight","Used to help light up the passage ways.")
# print(player.__repr__())
# for i in player.items:
#     print(i)

def search(myDict, lookup):
    for key, value in myDict.items():
        if key in lookup:
            return key

def dry(direction):
    direction=search(room, direction)
    print("\n")
    print(f"Current Room: {direction} \n")
    print(f"Description of Room: {room[direction].description}\n")   
    player.room=direction
        

# Make a new player object that is currently in the 'outside' room.

user = str(input("[n] North  [e] East  [s] South [w] West [q] Quit\n"))
# Write a loop that:
while user!="q":
    if user=="n":
        try:
            direction=str(room[player.room].n_to.name).lower()
            dry(direction)
        except:
             print("No room exists in that location. Wrong move.")
        
    elif user=="e":
        try:
            direction=str(room[player.room].e_to.name).lower()
            dry(direction)
        except:
             print("No room exists in that location. Wrong move.") 
    elif user=="s":
        try:
            direction=str(room[player.room].s_to.name).lower()
            dry(direction)
        except:
            print("No room exists in that location. Wrong move.")
    elif user=="w":
        try:
            direction=str(room[player.room].w_to.name).lower()
            dry(direction)
        except:
             print("No room exists in that location. Wrong move.")
    user = str(input("[n] North  [e] East  [s] South [w] West [q] Quit\n"))
       


#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.
