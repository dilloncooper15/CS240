import cmd
from room import get_room
import textwrap
import shutil
import tempfile


class Game(cmd.Cmd):
    def __init__(self):
        cmd.Cmd.__init__(self)

        self.dbfile = tempfile.mktemp()
        shutil.copyfile("game.db", self.dbfile)

        self.loc = get_room(1, self.dbfile)
        # self.look()

    def move(self, dir):
        newroom = self.loc._neighbor(dir)
        if newroom is None:
            print("you can't go that way!")
        else:
            self.loc = get_room(newroom, self.dbfile)
            print(self.loc.name)
            print(self.loc.visited)
            if self.loc.visited is False:
                self.loc.visited = True
                print(self.loc.visited)
            
                print()
                for line in textwrap.wrap(self.loc.description, 72):
                    print(line)

    def look(self):
        print(self.loc.name)
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
        self.look('look')

    def do_save(self, args):
        """Saves the game"""
        shutil.copyfile(self.dbfile, args)
        print("The game was saved to {0}".format(args))

if __name__ == "__main__":
    g = Game()
    g.cmdloop()
