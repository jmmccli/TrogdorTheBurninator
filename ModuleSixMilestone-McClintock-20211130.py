# Lord Jeremy M. McClintock, CISSP

# A dictionary for the Trogdor the Burninator text game
# The dictionary links a room to other rooms.
import random

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
        print('Invalid Entry.')

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

    for person, item in room_item.items():  # Iterate over possible room items (dictionary)
        if item.lower() == 'villain':  # If item is a villain print "Better watch out!"
            print('You see a ' + str(person) + ". Better watch out!")
        elif item.lower() == 'burninate':
            if inventory.get(person) == 'BURNINATED!!!':  # If burninatable item, see if already burninated.
                print('You see some ' + person + "... they look pretty BURNINATED!!!")
            else:
                print('You see some ' + person + "... Perhaps you should do what you do best and " + item.upper() +
                      "?!?")
        elif item.lower() == 'nothing':
            print(item + ' to see here. Let\'s get to burninating!')
        elif person.lower() == 'keeper of trogdor':  # Suggest talking to Keeper of Trogdor.
            print('You see a ' + person + '. Perhaps you should talk to them.')
        else:
            continue  # If not a match, continue to the next iteration in the list


# Small dictionary for inventory items
inventory = {
    'Thatched Roof Cottages': 'Not Burninated',
    'Peasants': 'Not Burninated',
    'TrogHelmet': 'No',
    'TrogShield': 'No',
    'TrogSword': 'No'
}


# Print the inventory items
def print_inventory():
    for item, has_item in inventory.items():  # Iterate over each key in the dictionary
        print(str(item) + ': ' + str(has_item))  # Print each key, item pair


def get_item(item, curr_room):
    for inv_item, has_item in inventory.items():  # Iterate over the inventory
        if inv_item.lower() == item.lower():  # Check to see if the item is already in possession
            if has_item.lower() == 'not burninated':  # If not burninated, then burninate
                inventory[inv_item] = 'BURNINATED!!!'
                print('TROGDOR STRIKES AGAIN!!! You sure burninated them ' + item + ' good, ole buddy!')
            elif has_item.lower() == 'no':  # If don't have item, update inventory to has item
                inventory[inv_item] = 'Yes'

                # Make the Keeper of Trogdor "disappear" after you talk to them.
                room_items[curr_room] = {'Nothing': 'Nothing'}

            else:
                continue
        else:
            continue


def smite(curr_room):
    if inventory.get('TrogSword') == 'No':
        print('You can\'t smite anything without a mighty weapon! You must find the TrogSword!')
        return 'no'
    elif inventory.get('TrogShield') == 'No':
        print('You can\'t smite anything without some mighty protection! You must find the TrogShield!')
        return 'no'
    elif inventory.get('TrogHelmet') == 'No':
        print('You can\'t smite anything without a safe nugget! You must find the TrogHelmet!')
        return 'no'
    elif inventory.get('Peasants') == 'Not Burninated':
        print('I saw some peasants back there, perhaps you should warm-up by burninating them!')
        return 'no'
    elif inventory.get('Thatched Roof Cottages') == 'Not Burninated':
        print('I saw some thatched roof cottages back there, perhaps you should warm-up by burninating them!')
        return 'no'
    elif curr_room == 'Great Hall' or curr_room == 'Throne Antechamber':
        room_item = room_items.get(curr_room)

        for person, item in room_item.items():
            if person.lower() == 'jhonka':
                print('You can\'t smite The Jhonka. Block with your shield and run away!')
                return 'no'
            elif person.lower() == 'kerrek':
                print('It was an epic battle. Trogdor breathing flame and striking in a frenzy with the TrogSword!!! \n'
                      'But Trogdor emerges victorious and the Kerrek falls! ... And Trogdor smote the Kerrek and '
                      'everything was laid to BURNINATIONNNNNNN!')
                print('CONGRATULATIONS! YOU HAVE WON THE GAME!')
                return 'win'
            else:
                return 'no'

    else:
        print('Nothing to smite yet!')
        return 'no'


def villain(curr_room):
    room_item = room_items.get(curr_room)

    for person, item in room_item.items():
        if person.lower() == 'jhonka':
            stealth = random.randint(1,10)
            if stealth <= 5:
                print('The Jhonka sees you! He attacks!')
                if inventory.get('TrogShield').lower() == 'yes':
                    print('You successfully block with the TrogShield.')
                    return 'safe'
                elif inventory.get('TrogHelmet').lower() == 'yes':
                    hit = random.randint(0,1)
                    if hit == 0:
                        print('The Jhonka\'s attack glances off the TrogHelmet! You\'re safe for now!')
                        return 'safe'
                    elif hit == 1:
                        print('The Jhonka strikes true. You are dead.')
                        return 'dead'
                else:
                    hit = random.randint(0, 1)
                    if hit == 0:
                        print('The Jhonka\'s attack misses! You\'re safe for now!')
                        return 'safe'
                    elif hit == 1:
                        print('The Jhonka strikes true. You are dead.')
                        return 'dead'
            elif stealth > 5:
                print('The Jhonka doesn\'t see you, be stealthy!')
                return 'safe'
            else:
                return 'safe'
        elif person.lower() == 'kerrek':
            stealth = random.randint(1, 10)
            if stealth <= 5:
                print('The Kerrek sees you! He attacks!')
                if inventory.get('TrogShield').lower() == 'yes':
                    print('You successfully block with the TrogShield.')
                    return 'safe'
                elif inventory.get('TrogHelmet').lower() == 'yes':
                    hit = random.randint(0, 1)
                    if hit == 0:
                        print('The Kerrek\'s attack glances off the TrogHelmet! You\'re safe for now!')
                        return 'safe'
                    elif hit == 1:
                        print('The Kerrek strikes true. You are dead.')
                        return 'dead'
                else:
                    hit = random.randint(0, 1)
                    if hit == 0:
                        print('The Kerrek\'s attack misses! You\'re safe for now!')
                        return 'safe'
                    elif hit == 1:
                        print('The Kerrek strikes true. You are dead.')
                        return 'dead'
            elif stealth > 5:
                print('The Kerrek doesn\'t see you, be stealthy!')
                return 'safe'
            else:
                return 'safe'


def main():
    global curr_room  # Define a global variable to keep track of the current room the player is in.

    curr_room = 'Bedroom'  # Initialize the variable curr_room
    pot_room = 'Bedroom'  # Initialize the variable for potential rooms the player can move to based on current room.

    while pot_room.lower() != 'exit':  # Make sure that the user isn't trying to exit the game.

        print_curr_room()  # Print the current room that the player is in as well as the rooms they can move to.
        print_room_items()  # Print people/items in each of the rooms.
        if curr_room == 'Throne Antechamber' or curr_room == 'Great Hall':
            if villain(curr_room) == 'dead':
                break

        pot_room = input('Type Exit to quit. Type Inventory to view Inventory.' + '\n')

        if (pot_room.lower()) == 'exit':
            # Bid the user farewell and exit the game.
            print('Trogdor the Burninator bids you farewell! Go forth & Burninate!')
            break

        elif pot_room.lower().__contains__('burninate'):  # If input contains "burninate"
            if pot_room.lower().__contains__('peasants'):  # If input contains peasants
                get_item('peasants', curr_room)

            elif pot_room.lower().__contains__('cottages'):  # If input contains cottages
                get_item('thatched roof cottages', curr_room)

            else:
                # Else nothing to burninate here!
                print('What would you like to burninate? I don\'t see anything here to burninate...')

        # If input contains speak check for Keeper of Trogdor and talk to them.
        elif pot_room.lower().__contains__('talk') or pot_room.lower().__contains__('speak'):
            if curr_room == 'Cellar':
                print('Trogdor carries on a brief, but lovely conversation with the Keeper of Trogdor...')
                print('He gives you the TrogHelmet & disappears in a cloud of smoke!')
                get_item('troghelmet', curr_room)
            elif curr_room == 'Kitchen':
                print('Trogdor carries on a brief, but lovely conversation with the Keeper of Trogdor...')
                print('He gives you the TrogShield & disappears in a cloud of smoke!')
                get_item('trogshield', curr_room)
            elif curr_room == 'Throne Room':
                print('Trogdor carries on a brief, but lovely conversation with the Keeper of Trogdor...')
                print('He gives you the TrogSword & disappears in a cloud of smoke!')
                get_item('trogsword', curr_room)
            else:
                print('There\'s nobody else here, you\'re talking to yourself, bub!')

        elif pot_room.lower() == 'inventory':
            print_inventory()

        elif pot_room.lower().__contains__('smite'):
            if smite(curr_room) == 'win':
                break
            else:
                continue

        else:

            curr_room = move_room(pot_room)  # Move to the requested room.

    else:
        # Bid the user farewell and exit the game.
        print('Trogdor the Burninator bids you farewell! Go forth & Burninate!')


main()  # Run the game
