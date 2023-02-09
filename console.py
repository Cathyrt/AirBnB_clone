#!/usr/bin/python3
"""A program that contains the entry point of the command interpreter"""
import cmd


class HBNBCommand(cmd.Cmd):
    """Contains the entry point of the command interpreter"""

    prompt = "(hbnb) "

    def do_EOF(self, line):
        """exit the program"""
        print()
        return True

    def do_quit(self, line):
        """Quit command to exit the program"""
        return True

    def emptyline(self):
        """ does not execute anything"""
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
