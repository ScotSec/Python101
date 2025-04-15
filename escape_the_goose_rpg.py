print(r'''

   ____   ____  _____   ___    ___    ____      ______   __ __   ____       _____  ____   ____    ____   ____
  / __/  / __/ / ___/  / _ |  / _ \  / __/     /_  __/  / // /  / __/      / ___/ / __ \ / __ \  / __/  / __/
 / _/   _\ \  / /__   / __ | / ___/ / _/        / /    / _  /  / _/       / (_ / / /_/ // /_/ / _\ \   / _/  
/___/  /___/  \___/  /_/ |_|/_/    /___/       /_/    /_//_/  /___/       \___/  \____/ \____/ /___/  /___/                                                                                                                                                                                         

''')
print("You are being chased through a castle by a dangerous and deadly goose.")
print("Your objective is to escape by any means.")

room_one_complete = False
room_two_complete = False
room_three_complete = False

start = input("Type 'BEGIN' to Start.\n")
if start.lower() == "begin":
    print("---")
    response = input(
        "You find yourself running down a long corridor, You hear a terrible honk behind you.\nYou stop as you come to a fork in the path.\nYou can hear the goose approaching.\nWhich path will you choose? 'LEFT' or 'RIGHT'\n")
    if response.lower() != "left":
        print("As you enter the corridor you find it is a dead end.\nOh dear... You have died.")
        exit()
    else:
        print("---")
        print("You successfully zip into the corridor before the goose notices.")
        room_one_complete = True

if room_one_complete == True:
    print("---")
    print(
        "After choosing the left path you find yourself in a grand hall of mirrors.\nIt's getting closer.\nThe corners of the room are in darkness and you may be able to hide.\nAs you turn your head you notice a strange glint behind one of the mirrors it looks like there is something behind it.")
    response = input("Do you 'HIDE' or 'BREAK' the mirror?\n")
    if response.lower() != "break":
        print("The goose instantly locates you.\nOh dear... You have died.")
        exit()
    else:
        print("---")
        print("You brace yourself ready to smash through the mirror... but there was no impact, it was an illusion!")
        room_two_complete = True

if room_one_complete == True and room_two_complete == True:
    print("---")
    print(
        "After tumbling through the illusionary mirror you find yourself looking at a spiral staircase.\nOne path leads to the rooftop and the other leads down into the dungeons.")
    response = input("Do you go 'UP' the staircase or 'DOWN'?\n")
    if response.lower() != "up":
        print(
            "You trip trying to go down the stairs, Landing in a crumpled heap at the bottom\nOh dear... You have died.")
        exit()
    else:
        print("---")
        print("You climb up the staircase until you read the roof, There is a rickety rope bridge leading to another tower.\nThinking quickly you sprint across, hearing the goose close behind.\nAs you reach the other tower you hear the ropes snap behind you.")
        print("You hear an echoing honk of rage as the goose falls out of sight.")
        room_three_complete = True

    if room_three_complete == True:
        print("---")
        print(r'''
 __  __  ____   __  __        ____  __  __   ___   _   __   ____  _   __   ____   ___    __
 \ \/ / / __ \ / / / /       / __/ / / / /  / _ \ | | / /  /  _/ | | / /  / __/  / _ \  / /
  \  / / /_/ // /_/ /       _\ \  / /_/ /  / , _/ | |/ /  _/ /   | |/ /  / _/   / // / /_/ 
  /_/  \____/ \____/       /___/  \____/  /_/|_|  |___/  /___/   |___/  /___/  /____/ (_)  

        ''')
        exit()

if start.lower() != "begin":
    print("If you can't type 'BEGIN' how are you planning to escape the goose?")
    print("The goose catches you.\nOh dear... You have died.")
    exit()
