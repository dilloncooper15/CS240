import cmd
from room import load_db
import textwrap
import shutil
import tempfile


class Game(cmd.Cmd):
    def __init__(self):
        cmd.Cmd.__init__(self)

        self.inv = []
        self.dbfile = tempfile.mktemp()
        shutil.copyfile("game.db", self.dbfile)

        self.room_dict = load_db(self.dbfile)
        # room_dict = {1: room, 2: room, 3: room}

        self.loc = self.room_dict[1]
        self.look()

    def move(self, dir):
        newroom = self.loc._neighbor(dir)
        if newroom is None:
            print("you can't go that way!")
        else:
            print()
            self.loc = self.room_dict[newroom]
            self.look()
            # print(self.loc.name)
            # print(self.loc.visited)
            if self.loc.visited is False:
                self.loc.visited = True
                # print(self.loc.visited)
                # print()
                # for line in textwrap.wrap(self.loc.description, 72):
                #     print(line)

    def look(self):
        # print(self.loc.name)
        print()
        for line in textwrap.wrap(self.loc.description, 72):
            print(line)

    def do_up(self, args):
        """Go up"""
        self.move('up')

    def do_down(self, args):
        """Go down"""
        self.move('down')

    def do_n(self, args):
        """Go north"""
        self.move('n')

    def do_s(self, args):
        """Go south"""
        self.move('s')

    def do_e(self, args):
        """Go east"""
        self.move('e')

    def do_w(self, args):
        """Go west"""
        self.move('w')

    def do_quit(self, args):
        """Leaves the game"""
        print("Thank you for playing!")
        return True

    def do_look(self, args):
        """Lets the user look around"""
        self.look()

    def do_save(self, args):
        """Saves the game"""
        shutil.copyfile(self.dbfile, args)
        print("The game was saved to {0}".format(args))

    def do_get(self, args):
        """Transfers an item from the room to the player's inventory."""
        for item in self.loc.inv:
            if item.name == args:
                self.inv.append(item)
                self.loc.inv.remove(item)
                print('\n{} is now in your inventory.\n'.format(args))
                break
        else:
            print('\nThere is no {} here!\n'.format(args))

    def do_drop(self, args):
        """Removes an item from the player's inventory."""
        for item in self.inv:
            if item.name == args:
                self.loc.inv.append(item)
                self.inv.remove(item)
                print('\nThe deed is done.\n')
                break
        else:
            print('\nYou cannot remove something you do not possess.\n')

    def do_inventory(self, args):
        """Displays what is in the player's inventory."""
        output = ''
        if self.inv:
            for item in self.inv:
                output += str(item)
        if output:
            output = '\nItems in your inventory:\n' + output
        else:
            output = '\nYou do not currently possess any items in your\
 inventory.\n'
        print(output)

if __name__ == "__main__":
    g = Game()
    g.cmdloop()
