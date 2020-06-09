#!/usr/bin/python3
"""Module.



"""
import json


class Base:
    """
    class.
    """
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(ld):
        """
        returns json string repr.
        """
        if ld is None or not ld:
            return "[]"
        return json.dumps(ld)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        json string repr to a file.
        """
        l = []
        with open("{}.json".format(cls.__name__), "w") as f:
            if list_objs is not None:
                for i in list_objs:
                    l.append(i.to_dictionary())
	    f.write(Base.to_json_string(l))

    @staticmethod
    def from_json_string(json_string):
        """
        returs list from json string
        """
        if json_string is None or not json_string:
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
        create instance
        """
        if cls.__name__ == "Rectangle":
            r = cls(10, 10)
        else:
            r = cls(10)
        r.update(**dictionary)
        return r

    @classmethod
    def load_from_file(cls):
        """
        returns list of instances
        """
        try:
            with open("{}.json".format(cls.__name__), "r") as f:
                y = cls.from_json_string(f.read())
                return [cls.create(**x) for x in y]
        except IOError:
            return []
