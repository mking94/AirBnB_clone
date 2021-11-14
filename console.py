#!/usr/bin/python3
"""
console module
"""

import cmd
from datetime import datetime
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """
    HBNBCommand class
    """
    prompt = "(hbnb) "

    classes = ["BaseModel", "User", "Amenity",
               "State", "City", "Place", "Review"]

    @classmethod
    def count(self, class_name, objects_dict):
        """ count the number of instance"""
        counter = 0
        for key in objects_dict.keys():
            if class_name in key:
                counter += 1
        print(counter)

    def do_quit(self, args):
        """
        exit program
        """
        return True

    def do_EOF(self, args):
        """
        Quit command to exit the program
        """
        return True

    def emptyline(self):
        """
        empty line + ENTER shouldn’t execute anything
        """
        pass

    def do_help(self, args):
        """
        help command
        """
        cmd.Cmd.do_help(self, args)

    def do_create(self, args):
        """
        creates a new instances of BaseModel
        saves it and prints the id
        """
        args = args.split(" ")
        if args == "":
            print("** class name missing **")
            return
        if args[0] not in self.classes:
            print("** class doesn't exist **")
            return
        else:
            new = eval("{}()".format(args[0]))
            new.save()
            print(new.id)

    def do_show(self, args):
        """
        Prints the string representation of an
        instance based on the class name and id
        """
        args = args.split()
        if len(args) == 0:
            print("** class name missing **")
            return
        try:
            eval(args[0])
        except Exception:
            print("** class doesn't exist **")
            return
        if len(args) == 1:
            print("** instance id missing **")
        else:
            storage.reload()
            container_obj = storage.all()
            key_id = args[0] + "." + args[1]
            if key_id in container_obj:
                value = container_obj[key_id]
                print(value)
            else:
                print("** no instance found **")

    def do_destroy(self, args):
        """
        Deletes an instance based on the class name and id
        """
        if not args:
            print("** class name missing **")
            return
        tokens = args.split(" ")
        objects = storage.all()

        if tokens[0] in self.classes:
            if len(tokens) < 2:
                print("** instance id missing **")
                return
            name = tokens[0] + "." + tokens[1]
            if name not in objects:
                print("** no instance found **")
            else:
                obj = objects[name]
                if obj:
                    objs = storage.all()
                    del objs["{}.{}".format(type(obj).__name__, obj.id)]
                    storage.save()
        else:
            print("** class doesn't exist **")

    def do_all(self, args):
        """
        Prints all string representation of all instances
        based or not on the class name
        """
        args = args.split()
        dict_obj = storage.all()
        list = []
        if len(args):
            class_name = args[0]
            if class_name not in self.classes:
                print("** class doesn't exist **")
                return
            for k, v in dict_obj.items():
                if class_name in k:
                    list.append((dict_obj[k].__str__()))
        else:
            for k, v in dict_obj.items():
                list.append((dict_obj[k].__str__()))
        print(list)

    def do_update(self, args):
        """
        Updates an instance based on the class
        name and id by adding or updating attribute
        """
        args = args.split()
        if not args:
            print("** class name missing **")
            return
        if args[0] not in self.classes:
            print("** class doesn't exist **")
            return
        try:
            args[1]
        except Exception:
            print("** instance id missing **")
            return
        objects_dict = storage.all()
        my_key = args[0] + "." + args[1]
        if my_key not in objects_dict:
            print("** no instance found **")
            return
        try:
            args[2]
        except Exception:
            print("** attribute name missing **")
            return
        try:
            args[3]
        except Exception:
            print("** value missing **")
            return
        if args[3]:
            setattr(objects_dict[my_key], args[2], args[3])
            my_obj = objects_dict[my_key]
            my_obj.updated_at = datetime.now()
            storage.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
