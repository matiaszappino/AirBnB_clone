#!/usr/bin/python3
"""Console File"""
import cmd
import json
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """The console of the Airbnb project"""
    prompt = "(hbnb) "
    class_list = ["BaseModel", "User", "City", "State", "Amenity",
                  "Place", "Review"]
    attr_list = ["updated_at", "created_at", "id"]

    def do_quit(self, line):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, line):
        """Quit command to exit the program"""
        return True

    def emptyline(self):
        pass

    def do_create(self, line):
        """Creates a new instance of BaseModel, saves it (to the JSON file)"""
        if line is None or line == "":
            print("** class name missing **")
        elif line in HBNBCommand.class_list:
            klass = globals()[line]
            new_inst = klass()
            new_inst.save()
            print(new_inst.id)
        else:
            print("** class doesn't exist **")

    def do_show(self, line):
        """Prints the string representation of an instance
        based on the class name and id"""
        if not line:
            print('** class name missing **')
        else:
            arg = line.split()
            if not arg[0] in HBNBCommand.class_list:
                print('** class doesn\'t exist **')
            else:
                if len(arg) > 1:
                    class_key = ''
                    class_key = arg[0] + '.' + arg[1]
                    if class_key in storage.all():
                        print(storage.all()[class_key])
                    else:
                        print('** no instance found **')
                else:
                    print('** instance id missing **')

    def do_all(self, line):
        '''
        Prints all string representation of all instances
        based or not on the class name
        '''
        new_list = []
        arg = line.split()
        objs = storage.all()
        if len(arg) == 0:
            for val in objs.values():
                new_list.append(str(val))
            print(new_list)
        elif arg[0] in HBNBCommand.class_list:
            for class_key in objs:
                if arg[0] in class_key:
                    new_list.append(str(objs[class_key]).__str__())
            print(new_list)
        else:
            print('** class doesn\'t exist **')

    def do_destroy(self, line):
        """Deletes an instance
        based on the class name and id"""
        objs = storage.all()
        if line != "":
            args = line.split()
            if args[0] not in HBNBCommand.class_list:
                print("** class doesn't exist **")
            if len(args) == 1:
                print("** instance id missing **")
            if len(args) == 2:
                key = args[0] + "." + args[1]
                if key in objs:
                    objs.pop(key)
                else:
                    print("** no instance found **")
        else:
            print("** class name missing **")

    def do_update(self, line):
        """updates an instance based on the class name and id"""
        objs = storage.all()
        scape = ["\"", "\'"]
        if line != "":
            args = line.split()
            if args[0] not in HBNBCommand.class_list:
                print("** class doesn't exist **")
            if len(args) == 1:
                print("** instance id missing **")
            if len(args) == 2:
                key = args[0] + "." + args[1]
                if key in objs:
                    print("** attribute name missing **")
                else:
                    print("** no instance found **")
            if len(args) == 3:
                print("** value missing **")
            if len(args) >= 4:
                key = args[0] + "." + args[1]
                if key in objs:
                    if args[2] not in HBNBCommand.attr_list:
                        if args[3][0] in scape and args[3][-1] in scape:
                            setattr(objs[key], args[2], str(args[3][1:-1]))
                        else:
                            setattr(objs[key], args[2], str(args[3]))
                        storage.save()
                    else:
                        print("No se puede editar")
                else:
                    print("** no instance found **")
        else:
            print("** class name missing **")

    def count(self, line):
        """Return the amount of instances of the class"""
        count = 0
        objs = storage.all()
        if line in HBNBCommand.class_list:
            for class_key in objs:
                if line in class_key:
                    count += 1
            print(count)

    def default(self, line):
        """In case to not found the command this func is executed"""
        functions = {"all()": HBNBCommand.do_all, "count()": HBNBCommand.count}
        try:
            args = line.split(".")
            func = ""
            func_id = ""
            for index, letter in enumerate(args[1]):
                if letter == "(":
                    func = args[1][0:index] + "()"
                    func_id = args[1][index + 2: -2]
                    break
            if func in functions:
                functions[func](self, args[0])
            else:
                print("*** Unknown syntax: {}".format(line))
        except:
            print("*** Unknown syntax: {}".format(line))

if __name__ == '__main__':
    HBNBCommand().cmdloop()
