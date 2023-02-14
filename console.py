#!/usr/bin/python3
"""A program that contains the entry point of the command interpreter"""
import cmd
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review
from models.engine.file_storage import FileStorage


class HBNBCommand(cmd.Cmd):
    """Contains the entry point of the command interpreter"""

    prompt = "(hbnb) "
    all_classes = {
        'BaseModel': BaseModel,
        'User': User,
        'State': State,
        'City': City,
        'Amenity': Amenity,
        'Place': Place,
        'Review': Review
      }

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

    def do_create(self, arg):
        """Usage: create <class>
        Create a new class instance and print its id.
        """
        if not arg:
            print("** class name missing **")
        elif arg not in HBNBCommand.all_classes:
            print("** class doesn't exist **")
        else:
            print(eval(arg)().id)
            storage.save()

    def do_show(self, arg):
        """Usage: show <class> <id> or <class>.show(<id>)
        Display the string representation of a class instance of a given id.
        """
        argl = arg.split()
        objdict = storage.all()
        if len(arg) == 0:
            print("** class name missing **")
        elif argl[0] not in HBNBCommand.all_classes:
            print("** class doesn't exist **")
        elif len(argl) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(argl[0], argl[1]) not in objdict.keys():
            print("** no instance found **")
        else:
            print(objdict["{}.{}".format(argl[0], argl[1])])

    def do_destroy(self, arg):
        """Usage: destroy <class> <id> or <class>.destroy(<id>)
        Delete a class instance of a given id."""
        argl = arg.split()
        objdict = storage.all()
        if len(arg) == 0:
            print("** class name missing **")
        elif argl[0] not in HBNBCommand.all_classes:
            print("** class doesn't exist **")
        elif len(argl) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(argl[0], argl[1]) not in objdict.keys():
            print("** no instance found **")
        else:
            del objdict["{}.{}".format(argl[0], argl[1])]
            storage.save()

    def do_all(self, arg):
        """Usage: all or all <class> or <class>.all()
        Display string representations of all instances of a given class.
        If no class is specified, displays all instantiated objects."""
        argl = arg.split()
        if len(argl) > 0 and argl[0] not in HBNBCommand.all_classes:
            print("** class doesn't exist **")
        else:
            objl = []
            for obj in storage.all().values():
                if len(argl) > 0 and argl[0] == obj.__class__.__name__:
                    objl.append(obj.__str__())
                elif len(argl) == 0:
                    objl.append(obj.__str__())
            print("\n".join(objl))

    def default(self, arg):
        """
        Method called on an input line when command prefix isn't recognized.

        Usage: <class>.all()
        Retrieve all instances of a class

        Usage: <class>.count()
        Retrieve the number of instances of a given class.

        Usage: <class>.show(<id>)
        Retrieve an instance of a given class based on its ID.

        Usage: <class>.destroy(<id>)
        Destroy an instance based on his ID
        Usage: <class>.update(<id>, <dictionary representation>)
        Update an instance based on his ID with a dictionary representation
        """
        count = 0
        objdict = storage.all()
        line = arg.split('.')
        if line[1] == 'count()':
            for key in objdict.keys():
                obj = key.split('.')
                if obj[0] == line[0]:
                    count += 1
            print(count)
        elif line[1] == 'all()':
            self.do_all(line[0])
        elif line[1].startswith('show'):
            cmid = line[1].split('("')
            cmid[1] = cmid[1].replace('")', '')
            self.do_show("{} {}".format(line[0], cmid[1]))
        elif line[1].startswith('destroy'):
            cmid = line[1].split('("')
            cmid[1] = cmid[1].replace('")', '')
            self.do_destroy("{} {}".format(line[0], cmid[1]))

    def do_update(self, arg):
        """Usage: update <class> <id> <attribute_name> <attribute_value> or
        <class>.update(<id>, <attribute_name>, <attribute_value>) or
        <class>.update(<id>, <dictionary>)
        Update a class instance of a given id by adding or updating
        a given attribute key/value pair or dictionary."""
        argl = arg.split()
        objdict = storage.all()

        if len(arg) == 0:
            print("** class name missing **")
            return False
        if argl[0] not in HBNBCommand.all_classes:
            print("** class doesn't exist **")
            return False
        if len(argl) == 1:
            print("** instance id missing **")
            return False
        if "{}.{}".format(argl[0], argl[1]) not in objdict.keys():
            print("** no instance found **")
            return False
        if len(argl) == 2:
            print("** attribute name missing **")
            return False
        if len(argl) == 3:
            print("** value missing **")
            return False

        obj = objdict["{}.{}".format(argl[0], argl[1])]

        if len(argl) == 4:
            setattr(obj, argl[2], eval(argl[3]))
        else:
            if type(eval(argl[2])) == dict:
                for k, v in eval(argl[2]).items():
                    setattr(obj, k, v)
            else:
                print("** invalid syntax **")
                return False

        storage.save()
        print(obj)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
