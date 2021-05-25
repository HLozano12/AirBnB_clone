#!/usr/bin/python3
"""The module of a console"""


import cmd
import re

import models
from models import FileStorage
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    """the console of airbnb"""
    prompt = '(hbnb) '

    def default(self, line: str):
        command = re.search(r"^(\w*)\.(\w+)(\W+)", line)
        if command.group(1) and command.group(2) == 'all':
            self.do_all("{}".format(command.group(1)))
            return
        if command.group(1) and command.group(2) == 'count':
            print(FileStorage.count(self, command.group(1)))
            return
        command2 = re.search(r"^(\w*)\.(\w+)\((\S+)\)", line)
        if command2.group(2) == 'show':
            string = command2.group(1) + " " +\
                     command2.group(3).replace("\"", "", 2)
            self.do_show(string)
            return
        if command2.group(2) == "destroy":
            string1 = command2.group(1) + " " +\
                      command2.group(3).replace("\"", "", 2)
            self.do_destroy(string1)
            return
        # command3 = re.search(r"^(\w*)\.(\w+)(\s+)", line)
        # # if command3.group(2) == "update":
        # print(command3.group(1))
        # print(command3.group(2))
        # print(command3.group(3))
        # # command3 = re.search(r"^(\S*),(\S*),(\S*)")
        # # if command2.group(2) == 'update':
        # #     print(command3.group(1).replace("\"", "", 2))
        # #     print(command3.group(1).replace("\"", "", 2))
        # #     print(command3.group(1).replace("\"", "", 2))

    def do_quit(self, arg: str):
        'Quit command to exit the program\n'
        return True

    def do_EOF(self, arg: str):
        'Exit the program\n'
        return True

    def emptyline(self) -> bool:
        False

    def do_create(self, arg):
        'create a new instance\n'

        if arg:
            if arg in FileStorage.classes:
                if arg == "BaseModel":
                    nb = BaseModel()
                elif arg == "State":
                    nb = State()
                elif arg == "City":
                    nb = City()
                elif arg == "Amenity":
                    nb = Amenity()
                elif arg == "Place":
                    nb = Place()
                elif arg == "Review":
                    nb = Review()
                elif arg == "User":
                    nb = User()
                nb.save()
                print(nb.id)
                return
            else:
                print("** class doesn't exist **")
                return
        else:
            print("** class name missing **")
            return

    def do_show(self, arg):
        'Prints the string representation of an instance\
        based on the class name and id\n'

        if not arg:
            print("** class name missing **")
            return
        else:
            args = arg.split()
            if args[0] not in FileStorage.classes:
                print("** class doesn't exist **")
                return
            else:
                if len(args) == 1:
                    print("** instance id missing **")
                    return
                else:
                    if len(args) >= 2:
                        for key, val in models.storage.all().items():
                            if "{}.{}".format(args[0], args[1]) == key:
                                print(val)
                                return
                        else:
                            print("** no instance found **")
                            return

    def do_destroy(self, arg):
        """delete an instance by class name and id\n"""

        if not arg:
            print("** class name missing **")
            return
        else:
            args = arg.split()
            if args[0] in FileStorage.classes:
                if len(args) >= 2:
                    for key, val in models.storage.all().items():
                        if (args[1] in key.split(".")) and\
                           (args[0] in key.split(".")):
                            models.storage.all().pop(key)
                            models.storage.save()
                            return
                    else:
                        print("** no instance found **")
                        return
                else:
                    print("** instance id missing **")
                    return
            else:
                print("** class doesn't exist **")
                return

    def do_all(self, arg):
        """Prints all string representation of all instances\
        based or not on the class name\n"""
        if not arg:
            list_of_strings = []
            for val in models.storage.all().values():
                list_of_strings.append(str(val))
            print(list_of_strings)
            return
        else:
            args = arg.split()
            if args[0] not in FileStorage.classes:
                print("** class doesn't exist **")
                return
            else:
                list_of_strings = []
                for key, val in models.storage.all().items():
                    if arg in key.split("."):
                        list_of_strings.append(str(val))
                print(list_of_strings)
                return

    def do_update(self, arg):
        """update the information of an instance\n"""
        if not arg:
            print("** class name missing **")
            return
        args = arg.split()
        if args[0] not in FileStorage.classes:
            print("** class doesn't exist **")
            return
        if len(args) == 1:
            print("** instance id missing **")
            return
        if len(args) >= 2:
            for key, val in models.storage.all().items():
                if args[1] in key.split("."):
                    if len(args) == 2:
                        print("** attribute name missing **")
                        return
                    if len(args) == 3:
                        print("** value missing **")
                        return
                    if len(args) >= 4:
                        setattr(models.storage.all()[key], args[2], args[3])
                        val.save()
                        return
                else:
                    print("** no instance found **")
                    return

if __name__ == '__main__':
    HBNBCommand().cmdloop()
