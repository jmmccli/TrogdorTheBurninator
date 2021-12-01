# Lord Jeremy M. McClintock, CISSP

global curr_room  # Define a global variable to keep track of the current room the player is in.
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
    if (AttributeError == 'NoneType'):  # Error handling
        print(AttributeError.name)
    else:
        print('You are in the ' + curr_room + '.', end=' ')  # Print current room
        for direction, potential_room in room.items():  # Print available adjacent rooms
            print('You can go ' + str(direction) + " to the " + str(potential_room) + '.')


def get_curr_room_info():
    return curr_room


def move_room(direction):
    current_room = get_curr_room_info()  # Get current room's info
    room = rooms.get(current_room)  # Define room list
    for direct, potential_room in room.items():  # Iterate over the list, looking for direction & potential room
        if (direct.lower() == direction.lower()):  # Check to see if direction matches list
            current_room = potential_room  # Set current room to potential room
        elif (potential_room.lower() == direction.lower()):  # Check to see if potential room matches list
            current_room = potential_room  # Set current room to potential room
        else:
            continue  # If not a match, continue to the next iteration in the list

    return current_room


# Dictionary of items and people in each room
room_items = {
    'Great Hall': {'Jhonka': 'Villain'},
    'Cellar': {'Keeper of Trogdor': 'TrogHelmet'},
    'Village': {'Thatched Roof Cottages': 'Burninate'},
    'Dining Hall': {'Peasants': 'Burninate'},
    'Kitchen': {'Keeper of Trogdor': 'TrogShield'},
    'Throne Antechamber': {'Kerrek': 'Villain'},
    'Throne Room': {'Keeper of Trogdor': 'TrogSword'}
}


def print_room_items():
    room_item = room_items.get(curr_room)
    for person, item in room_item.items():
        if (item.lower() == 'villain'):
            print('You see a ' + str(person) + ". Better watch out!")
        else:
            continue  # If not a match, continue to the next iteration in the list


inventory = {
    'Thatched Roof Cottages': 'Mot Burninated',
    'Peasants': 'Not Burninated',
    'TrogHelmet': 'No',
    'TrogShield': 'No',
    'TrogSword': 'No'
}


def print_inventory():
    for item, has_item in inventory.items():
        print(str(item) + ': ' + str(has_item))


def get_item(item):
    for inv_item, has_item in inventory.items():
        if(inv_item.lower() == item):
            if has_item.lower() == 'not burninated':
                inventory.update(item, 'BURNINATED!')
            elif has_item.lower() == 'no':
                inventory.update(item, 'Yes')
            else:
                continue
        else:
            continue


def main():
    curr_room = 'Bedroom'  # Initialize the variable curr_room
    pot_room = 'Bedroom'  # Initialize the variable for potential rooms the player can move to based on current room.

    while ((pot_room.lower() != 'exit')):  # Make sure that the user isn't trying to exit the game.
        if((pot_room.lower()) == 'exit'):
            print('Trogdor the Burninator bids you farewell! Go forth & Burninate!')
            break

        else:

            print_curr_room()  # Print the current room that the player is in as well as the rooms they can move to.
            print_room_items()

            pot_room = input('Type Exit to quit. Type Inventory to view Inventory.' + '\n')
            # Get input from user (which room they want to move to).

            if(pot_room.lower() == 'inventory'):
                print_inventory()
            else:
                curr_room = move_room(pot_room)  # Move to the requested room.
    else:
        # Bid the user farewell and exit the game.
        print('Trogdor the Burninator bids you farewell! Go forth & Burninate!')


main()  # Run the game
