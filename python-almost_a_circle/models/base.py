#!/usr/bin/python3
"""
Module contains class Base
Contains private class __nb_objects, and class constructor __init__
"""


import json
import csv


class Base():
    """
    defines class Base
    Class Attributes:
        __nb_objects
    Methods:
        __init__(self, id=None)
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        Initialize id, increment class attribute if no id and set as id
        """
        if id:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = self.__nb_objects

    @classmethod
    def save_to_file(cls, list_objs):
        """
        Save json strings of all instances into file
        """
        objs = []
        if list_objs is not None:
            for o in list_objs:
                objs.append(cls.to_dictionary(o))
        filename = cls.__name__ + ".json"
        with open(filename, "w") as f:
            f.write(cls.to_json_string(objs))

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Save json strings of all instances into file
        """
        if list_dictionaries is None:
            list_dictionaries = []
        return json.dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string):
        """Returns Python obj of JSON string representation"""
        if json_string is None or len(json_string) == 0:
            json_string = "[]"
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
        Returns instance with attributes already set
        """
        if cls.__name__ == "Square":
            dummy = cls(1)
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """
        Returns list of instances
        """
        fn = cls.__name__ + ".json"
        l = []
        try:
            with open(fn, "r") as f:
                instances = cls.from_json_string(f.read())
            for i, dic in enumerate(instances):
                l.append(cls.create(**instances[i]))
        except:
            pass
        return l
