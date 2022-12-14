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
                if len(new_line) <= 2:
                    new_str = "{}.{}".format(new_line[0], new_line[1])
                    new_obj = storage.all()
                    if new_str in new_obj:
                        del(new_obj[new_str])
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
        if line is None or line == "":
            print("** class name is missing **")
        else:
            if new_line[0] in self.class_name:
                if len(new_line) >= 2:
                    ins_id = new_line[1]
                    new_obj = storage.all().get(key)
                    new_str = f"{new_line[0]}.{new_line[1]}"
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

    def do_count(self, line):
        '''Prints the number of instamces'''
        count = 0
        if line:
            for key, value in storage.all().items():
                if str(value.__class__.__name__) == line:
                    count += 1
        print (count)

    def splinter(self, line):
        '''To split the line'''
        sp = line
        sp = sp.replace("\"", "")
        sp = sp.replace("show(", "")
        sp = sp.replace("destroy(", "")
        sp = sp.replace("update(", "")
        sp = sp.replace(")", "")
        sp = sp.replace(",", "")
        sp = sp.split()
        args = ""
        for i in range(len(sp)):
            args += sp[i]
            if i - 1 != range(len(sp)):
                args += " "
        return(args)

    def default(self, line):
        """ Dafault function """
        new_line = line.split('.')
        if len(new_line) > 1:
            if new_line[1] == "count()":
                self.do_count(new_line[0])
            if new_line[1] == "all()":
                self.do_all(new_line[0])
            if new_line[1][:4] == "show":
                args = self.splinter(new_line[1])
                clas = new_line[0]
                self.do_show(clas + " " + args)
            if new_line[1][:7] == "destroy":
                args = self.splinter(new_line[1])
                clas = new_line[0]
                self.do_destroy(clas + " " + args)
            if new_line[1][:6] == "update":
                args = self.splinter(new_line[1])
                clas = new_line[0]
                self.do_update(clas + " " + args)
            else:
                cmd.Cmd.default(self, line)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
