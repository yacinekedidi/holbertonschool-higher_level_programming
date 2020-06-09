#!/usr/bin/python3
"""Module.



"""
import json
import csv
import turtle


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
            f.write(cls.to_json_string(l))

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

    @classmethod
    def save_to_file_csv(cls, lo):
        """save to csv file"""
        if lo is not None:
            if cls.__name__ in "Rectangle":
                ls = [[i.id, i.width, i.height, i.x, i.y] for i in lo]
            else:
                ls = [[i.id, i.size, i.x, i.y] for i in lo]
            with open("{}.csv".format(cls.__name__), "w", newline="") as f:
                w = csv.writer(f)
                for i in ls:
                    w.writerow(i)

    @classmethod
    def load_from_file_csv(cls):
        """load from csv file"""
        l = []
        with open("{}.csv".format(cls.__name__), "r", newline="") as f:
            r = csv.reader(f)
            for row in r:
                x = [int(y) for y in row]
                if len(x) == 5:
                    d = {'id': x[0], 'width': x[1], 'height': x[2],
                         'x': x[3], 'y': x[4]}
                else:
                    d = {'id': x[0], 'size': x[1],
                         'x': x[2], 'y': x[3]}
                l.append(cls.create(**d))

        return l

    @staticmethod
    def draw(lr, ls):
        """draw"""
        turtle.color("green")
        for i in lr:
            turtle.forward(i.height)
            turtle.left(90)
            turtle.forward(i.width)
            turtle.left(90)
            turtle.forward(i.height)
            turtle.left(90)
            turtle.forward(i.width)
            turtle.left(90)

        turtle.color("red")
        for i in ls:
            turtle.forward(i.size)
            turtle.left(90)
            turtle.forward(i.size)
            turtle.left(90)
            turtle.forward(i.size)
            turtle.left(90)
            turtle.forward(i.size)
            turtle.left(90)
            turtle.setheading(turtle.heading() + 90)
