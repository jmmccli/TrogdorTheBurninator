# Lord Jeremy M. McClintock, CISSP

# A dictionary for the Trogdor the Burninator text game
# The dictionary links a room to other rooms.
rooms = {
    'Great Hall': {'South': 'Bedroom', 'West': 'Village', 'East': 'Dining Hall', 'North': 'Throne Antechamber'},
    'Bedroom': {'North': 'Great Hall', 'East': 'Cellar'},
    'Cellar': {'West': 'Bedroom'},
    'Village': {'East': 'Great Hall'},
    'Dining Hall': {'West': 'Great Hall', 'North': 'Kitchen'},
    'Kitchen': {'South': 'Dining Hall'},
    'Throne Antechamber': {'South': 'Great Hall', 'East': 'Throne Room'},
    'Throne Room': {'West': 'Throne Antechamber'}
}


def print_curr_room():
    room = rooms.get(curr_room)  # Get the current room from the Dictionary
    if AttributeError == 'NoneType':  # Error handling
        print(AttributeError.name)
    else:
        print('You are in the ' + curr_room + '.', end=' ')  # Print current room
        for direction, potential_room in room.items():  # Print available adjacent rooms
            print('You can go ' + str(direction) + " to the " + str(potential_room) + '.')


def move_room(direction):
    current_room = curr_room  # Get current room's info
    room = rooms.get(curr_room)  # Define room list
    for direct, potential_room in room.items():  # Iterate over the list, looking for direction & potential room
        if direct.lower() == direction.lower():  # Check to see if direction matches list
            current_room = potential_room  # Set current room to potential room
            break
        elif potential_room.lower() == direction.lower():  # Check to see if potential room matches list
            current_room = potential_room  # Set current room to potential room
            break
        else:
            continue  # If not a match, continue to the next iteration in the list
    else:
        print('Invalid Entry. Enter the direction you would like to go.')

    return current_room


# Dictionary of items and people in each room
room_items = {
    'Great Hall': {'Jhonka': 'Villain'},
    'Cellar': {'Keeper of Trogdor': 'TrogHelmet'},
    'Village': {'Thatched Roof Cottages': 'Burninate'},
    'Dining Hall': {'Peasants': 'Burninate'},
    'Kitchen': {'Keeper of Trogdor': 'TrogShield'},
    'Throne Antechamber': {'Kerrek': 'Villain'},
    'Throne Room': {'Keeper of Trogdor': 'TrogSword'},
    'Bedroom': {'Nothing': 'Nothing'}
}


def print_room_items():
    room_item = room_items.get(curr_room)

    for person, item in room_item.items():
        if item.lower() == 'villain':
            print('You see a ' + str(person) + ". Better watch out!")
        elif item.lower() == 'burninate':
            print('You see some ' + person + "... Perhaps you should do what you do best and " + item.upper() + "?!?")
        elif item.lower() == 'nothing':
            print(item + ' to see here. Let\'s get to burninating!')
        elif person.lower() == 'keeper of trogdor':
            print('You see a ' + person + '. Perhaps you should talk to them.')
        else:
            continue  # If not a match, continue to the next iteration in the list


# Small dictionary for inventory items
inventory = {
    'Thatched Roof Cottages': 'Mot Burninated',
    'Peasants': 'Not Burninated',
    'TrogHelmet': 'No',
    'TrogShield': 'No',
    'TrogSword': 'No'
}


# Print the inventory items
def print_inventory():
    for item, has_item in inventory.items():  # Iterate over each key in the dictionary
        print(str(item) + ': ' + str(has_item))  # Print each key, item pair


# FIXME #Get logic in main to work, then verify functionality
def get_item(item):
    for inv_item, has_item in inventory.items():
        if inv_item.lower() == item:
            if has_item.lower() == 'not burninated':
                inventory[inv_item] = 'BURNINATED!!!'
                continue
            elif has_item.lower() == 'no':
                inventory[inv_item] = 'Yes'
                continue
            else:
                continue
        else:
            continue


def main():
    global curr_room  # Define a global variable to keep track of the current room the player is in.

    curr_room = 'Bedroom'  # Initialize the variable curr_room
    pot_room = 'Bedroom'  # Initialize the variable for potential rooms the player can move to based on current room.

    while pot_room.lower() != 'exit':  # Make sure that the user isn't trying to exit the game.
        if (pot_room.lower()) == 'exit':
            print('Trogdor the Burninator bids you farewell! Go forth & Burninate!')
            break

        elif pot_room.lower().__contains__('burninate'):
            if pot_room.lower().__contains__('peasants'):
                get_item('peasants')
            elif pot_room.lower().__contains__('cottages'):
                get_item('thatched roof cottages')
            else:
                continue

        else:

            print_curr_room()  # Print the current room that the player is in as well as the rooms they can move to.
            print_room_items()  # Print people/items in each of the rooms.

            pot_room = input('Type Exit to quit. Type Inventory to view Inventory.' + '\n')
            # Get input from user (which room they want to move to).

            if pot_room.lower() == 'inventory':
                print_inventory()
            else:
                curr_room = move_room(pot_room)  # Move to the requested room.
    else:
        # Bid the user farewell and exit the game.
        print('Trogdor the Burninator bids you farewell! Go forth & Burninate!')


main()  # Run the game
