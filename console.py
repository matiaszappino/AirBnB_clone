#!/usr/bin/python3
"""Console File"""
import cmd
import json
from collections import namedtuple
from models.base_model import BaseModel
from models.user import User
from models.city import City
from models.review import Review
from models.place import Place
from models.state import State
from models import storage


class HBNBCommand(cmd.Cmd):
    """The console of the Airbnb project"""
    prompt = "(hbnb) "

    class_list = ["BaseModel", "User", "City", "State", "Amenity", "Place", "Review"]
    class_ls = {"BaseModel": BaseModel, "City": City}
    
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
            """new_inst = HBNBCommand.class_dict[line]
            new_inst.save()
            print(new_inst.id)"""
            print("** class doesn't exist **")
    
    """def do_show(self, line):
        Prints the string representation of an instance 
            based on the class name and id
        objs = storage.all()
        if line != "":
            args = line.split()
            if args[0] != "BaseModel":
                print("** class doesn't exist **")
            if len(args) == 1:
                print("** instance id missing **")
            if len(args) == 2:
                key = args[0] + "." + args[1]
                if key in objs:
                    new_obj = BaseModel(objs[key])
                    print(new_obj)
                else:
                    print("** no instance found **")
        else:
            print("** class name missing **")"""

    """def do_all(self, line):
        Prints all string representation of all instances
        based or not on the class name
        new_list = []
        for dic in storage.all().values():
            print(dic.__str__())"""
    def do_show(self, line):
        """Prints the string representation of an instance
        based on the class name and id"""
        if not line:
            print('** class name missing **')
        else:
            arg = line.split()
            if not arg[0] in class_ls:
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
        if len(arg) == 0:
            for val in storage.all().values():
                new_list.append(str(val))
            print(new_list)
        elif arg[0] in class_ls:
            for class_key in storage.all():
                if arg[0] in class_key:
                    new_list.append(str(storage.all()[class_key]))
            print(new_list)
        else:
            print('** class doesn\'t exist **')
    
    def do_destroy(self, line):
        """Deletes an instance 
        based on the class name and id"""
        objs = storage.all()
        if line != "":
            args = line.split()
            if args[0] != "BaseModel":
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
        if line != "":
            args = line.split()
            if args[0] != "BaseModel":
                print("** class doesn't exist **")
            if len(args) == 1:
                print("** instance id missing **")
            if len(args) == 2:
                print("** attribute name missing **")
            if len(args) == 3:
                print("** value missing **")
            if len(args) >= 4:
                key = args[0] + "." + args[1]
                if key in objs:
                    if args[2] in objs[key] and args[2] != "id" and args[2] != "created_at":
                        setattr(args[0], args[2], args[3])
                    else:
                        print("No se puede editar")
                else:
                    print("** no instance found **")
        else:
            print("** class name missing **")

if __name__ == '__main__':
    HBNBCommand().cmdloop()
