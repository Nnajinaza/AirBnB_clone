#!/usr/bin/python3
'''A class HBNBCommand which will be used by the command interpreter'''
import cmd
from models.base_model import BaseModel
from models import storage
from models.engine.file_storage import FileStorage
from models.user import User
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.state import State


class HBNBCommand(cmd.Cmd):
    '''A custom prompt that displays '(hbnb)' when the file is executed'''
    prompt = '(hbnb) '
    class_name = {"BaseModel": BaseModel, "User": User, "Place": Place,
                  "city": City, "Amenity": Amenity, "Review": Review,
                  "State": State}

    def do_EOF(self, line):
        '''EOF command to exit the program'''
        return True

    def do_quit(self, line):
        '''quit command to exit the program'''
        return True

    def emptyline(self):
        '''emptyline + 'ENTER' shouldn't execute anything'''
        pass

    def do_create(self, line):
        '''create: Creates a new instance of BaseModel, saves it
        (JSON file) and prints the id'''
        if (line is None or line == ""):
            print("** class name missing **")

        else:
            if line:
                new_ins = eval(line + "()")
                new_ins.save()
                print(new_ins.id)
            else:
                print("** class doesn't exist **")

    def do_show(self, line):
        '''show: Prints the string representation of an instance based
        on the class name and an id'''
        if line is None or line == "":
            print("** class name missing **")
        else:
            new_line = line.split(" ")
            if new_line[0] in self.class_name:
                if len(new_line) == 2:
                    new_str = "{}.{}".format(new_line[0], new_line[1])
                    new_obj = storage.all()
                    if new_str in new_obj:
                        print(new_obj[new_str])
                    else:
                        print("** no instance found **")
                else:
                    print("** instance id missing **")
            else:
                ("** class doesn't exist **")

    def do_destroy(self, line):
        '''destroy: Deletes an instance based on the class name and id'''
        if line is None or line == "":
            print("** class name missing **")
        else:
            new_line = line.split(" ")
            if new_line[0] in self.class_name:
                if len(new_line) < 2:
                    print("** instance id missing **")
                    new_str = "{}.{}".format(new_line[0], new_line[1])
                    new_obj = storage.all()
                    if new_str in new_obj:
                        del(new_str)
                        storage.save()
                    else:
                        print("** no instance found **")
                else:
                    print("** instance id missing **")
            else:
                print("** class doesn't exist **")

    def do_all(self, line):
        '''all: Prints all string representation of all
        instances based or not on the class name'''
        new_str = []
        if line == "":
            print([str(value) for key, value in storage.all().items()])

        else:
            new_line = line.split(" ")
            if new_line[0] not in self.class_name:
                print("** class doesn't exist **")
            else:
                for key, value in storage.all().items():
                    keys = key.split(".")
                    if keys[0] == new_line[0]:
                        new_str.append(str(value))
                print(new_str)

    def do_update(self, line):
        '''update: Update an instance based on the class name
        and id by adding or updating attribute'''
        new_line = line.split(" ")
        new_obj = storage.all()
        new_str = "{}.{}".format(new_line[0], new_line[1])
        if line is None or line == "":
            print("** class name is missing **")
        else:
            if new_line[0] in self.class_name:
                if len(new_line) >= 2:
                    ins_id = new_line[1]
                    if new_str in new_obj:
                        obj = new_obj[new_str]
                        if len(new_line) >= 3:
                            attr_name = new_line[2]
                            if len(new_line) >= 4:
                                attr_value = new_line[3]
                                setattr(obj, attr_name, attr_value)
                                storage.new(obj)
                                obj.save()
                            else:
                                print("** value is missing **")
                        else:
                            print("** attribute name missing **")
                    else:
                        print("** no instance found **")
                else:
                    print("** instance id missing **")
            else:
                print("** class doesn't exist **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
