# def yes_or_no(string):
#     """(str) -> bool

#     Given a string that begins with either an uppercase or lowercase 'Y",
#     return True, otherwise return False.

#     >>> yes_or_no('Olivet')
#     False

#     >>> yes_or_no('Yes')
#     True

#     >>> yes_or_no('yesorno')
#     True
#     """
#     if string.startswith('y') or string.startswith('Y'):
#         return True
#     else:
#         return False


def dark_cave():
    """ () -> bool

    Asks if you'd like to enter the Adelphic house.
    """
    print('Welcome to The Adelphic Adventure Game!')
    print()
    print('INSTRUCTIONS: In order to move around within the game, type the ' +
          'letter N – to walk forward, S – to turn around and head back, ' +
          'E – to walk to the right, or W – to walk to the left. ' +
          'If there are stairs, type the letter U - to go up and ' +
          'D - to go down.')
    print()
    print('INTRODUCTION: You are facing a massive green house with a long ' +
          'stone walkway that leads to concrete steps. Small lanterns on ' +
          'each side of the walkway create an eerie glow, and are your only ' +
          'source of light. Long vines encase the house, hanging down to ' +
          'conceal most of the porch. The steps lead to a heavy wooden door ' +
          'that sits back in the shadows of the archway.')
    print()
    print('You hear muffled sounds coming from the house.')
    choice = input('Do you want to go into the house? If so, continue ' +
                   'walking North. ')
    letter = ''
    while letter in choice:
        if letter == 'N':
            huge_chamber()
        if letter == 'S':
            print('Your poor decision to cross the road without looking results ' +
                  'in you being struck by a school bus. Consequently, you hit ' +
                  'your head on the pavement causing cerebral edema. As a ' +
                  'result, you experience amnesia and cannot remember how to ' +
                  'operate a computer and cannot finish the game.')
        if letter == 'E':
            print('You succumb to your hunger and decide to walk to the Kirk ' +
                  'Center to chow down and refuel your emaciated body.')
        if letter == 'W':
            print('You decide that you do not want to investigate the noise ' +
                  'and stoll the town of Olivet.')
        if letter != 'N' or 'S' or 'E' or 'W':
            print('I do not recognize this command.')
            choice = input('Do you want to go into the house? If so, continue ' +
                           'walking North. ')


def huge_chamber():
    """ () -> bool

    Asks if you want to explore a passage?
    """
    print('You walk through the front door and are standing in the foyer.')
    look = str('To the right of you there is a staircase. In front of you ' +
               'there is a closed door that possibly leads to a room. ' +
               'To the left there is a dimly lit round room. Behind ' +
               'you is the front, which is your only exit from the house.')
    choice = input('What do you wish to do? ')
    if choice == 'look':
        print(look)
        choice == input('What do you wish to do? ')
        if choice == 'W':
            up_or_down = input('Do you wish to go up the stairs or go ' +
                               'down and into the dark abyss? ')
            if up_or_down == 'U':
                print('You are now on the second floor of the house.')
                second_floor()
            if up_or_down == 'D':
                print('You are now in the basement. You have the visibility ' +
                      'of a bat, minus the sonar (of course).')
                basement()
        if choice == 'N':
            print('You tempt fate and slide open the pocket doors unvieling ' +
                  'a beautiful room. Large paddles decorate the walls with ' +
                  'names of former and current Adelphics.')
            chapter_room()
        if choice == 'E':
            print('You are now in the first floor round room.')
            first_floor_round()
        if choice == 'S':
            print('You chickened out and left the house screaming like a ' +
                  '12-year-old at a Justin Beiber concert.')
    if choice == 'W':
        up_or_down = input('Do you wish to go up the stairs or go down and ' +
                           'into the dark abyss? ')
        if up_or_down == 'U':
            second_floor()
        if up_or_down == 'D':
            basement()
    if choice == 'N':
        print('You tempt fate and slide open the pocket doors unvieling a ' +
              'beautiful room. Large paddles decorate the walls with names ' +
              'of former and current Adelphics.')
        chapter_room()
    if choice == 'E':
        print('You are now in the first floor round room.')
        first_floor_round()
    if choice == 'S':
        print('You chickened out and left the house screaming like a ' +
              '12-year-old at a Justin Beiber concert.')


def smaller_cave():
    """ () -> bool

    Asks if you want to take a swim?
    """
    print('You are in a smaller cave with a waterfall.')
    choice = input('Would you like to take a swim (y/n)? ')
    if choice == 'y':
        return True
    else:
        return False


def strange_noise():
    """ () - > bool

    Asks if you want to check out the strange noise?
    """
    print('You hear a strange noise.')
    choice = input('Check it out (y/n)? ')
    if choice == 'y':
        return True
    else:
        return False


def monster_noise():
    """ () -> bool

    Asks if you should run after you hear monster noises while standing in the
    dark?
    """
    print('You start to hear monster noises.')
    choice = input('Run (y/n)? ')
    if choice == 'y':
        return True
    else:
        return False


def reason_with_monster():
    """() -> bool

    Asks if you should try and reason with the monster?
    """
    print('You run right into the monster\'s arms... er paws.')
    choice = input('Try and reason with it (y/n)? ')
    if choice == 'y':
        return True
    else:
        return False


def walk_towards_light():
    """() -> bool

    Asks if you should walk towards the light?
    """
    print('You wait to see what the monster will do and notice a light.')
    choice = input('Walk towards it (y/n)? ')
    if choice == 'y':
        return True
    else:
        return False


# def second_floor():
#     """() -> bool

#     Depicts the second floor.
#     """


# def basement():


# Main Program

# def main():
#     torch = dark_cave()
#     if torch:
#         explore = huge_chamber()
#         if explore:
#             swim = smaller_cave()
#             if swim:
#                 print('You were eaten by a cave fish!')
#             else:
#                 print('Your wise decision has saved your life. ' +
#                       'You leave the cave in one piece!')
#         else:
#             print('You decide to stay put, but here a strange noise.')
#             strange = strange_noise()
#             if strange:
#                 print('You discover the noise is a underground rave and ' +
#                       'dance until dawn!')
#             else:
#                 print('A strong wind suddenly blows by, and your torch ' +
#                        'goes out! You are lost forever...')
#     else:
#         print('You stand in the dark.')
#         monster = monster_noise()
#         if monster:
#             reason = reason_with_monster()
#             if reason:
#                 print('You explain to the monster how it shouldn\'t eat ' +
#                        'you and you are so long-winded that the monster ' +
#                        'falls asleep!')
#             else:
#                 print('You try and fight off the monster to no avail. ' +
#                       'You\'re now a small smudge on the cave floor.')
#         else:
#             walk = walk_towards_light()
#             if walk:
#                 print('The monster tricked you! You\'ve been eaten by a ' +
#                        'giant kitten!')
#             else:
#                 print('The monster has mistaken you for a stalagmite. ' +
#                        'You are saved!')

# if __name__ == '__main__':
#     main()
