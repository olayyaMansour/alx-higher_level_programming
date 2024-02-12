#!/usr/bin/python3

"""Defines a base model class."""
import json
import csv
import turtle


class BaseModel:
    """Base model.

    Represents the "base" for all other classes in project 0x0C*.

    Private Class Attributes:
        __nb_objects (int): Number of instantiated BaseModels.
    """

    __nb_objects = 0

    def __init__(self, identity=None):
        """Initialize a new BaseModel.

        Args:
            identity (int): The identity of the new BaseModel.
        """
        if identity is not None:
            self.id = identity
        else:
            BaseModel.__nb_objects += 1
            self.id = BaseModel.__nb_objects

    @staticmethod
    def to_json_string(list_of_dicts):
        """Return the JSON serialization of a list of dictionaries.

        Args:
            list_of_dicts (list): A list of dictionaries.
        """
        if list_of_dicts is None or list_of_dicts == []:
            return "[]"
        return json.dumps(list_of_dicts)

    @classmethod
    def save_to_file(cls, list_of_objs):
        """Write the JSON serialization of a list of objects to a file.

        Args:
            list_of_objs (list): A list of inherited BaseModel instances.
        """
        filename = cls.__name__ + ".json"
        with open(filename, "w") as jsonfile:
            if list_of_objs is None:
                jsonfile.write("[]")
            else:
                list_of_dicts = [obj.to_dictionary() for obj in list_of_objs]
                jsonfile.write(BaseModel.to_json_string(list_of_dicts))

    @staticmethod
    def from_json_string(json_str):
        """Return the deserialization of a JSON string.

        Args:
            json_str (str): A JSON str representation of a list of dicts.
        Returns:
            If json_str is None or empty - an empty list.
            Otherwise - the Python list represented by json_str.
        """
        if json_str is None or json_str == "[]":
            return []
        return json.loads(json_str)

    @classmethod
    def create(cls, **attrs):
        """Return a class instantiated from a dictionary of attributes.

        Args:
            **attrs (dict): Key/value pairs of attributes to initialize.
        """
        if attrs and attrs != {}:
            if cls.__name__ == "Rectangle":
                new_obj = cls(1, 1)
            else:
                new_obj = cls(1)
            new_obj.update(**attrs)
            return new_obj

    @classmethod
    def load_from_file(cls):
        """Return a list of classes instantiated from a file of JSON strings.

        Reads from `<cls.__name__>.json`.

        Returns:
            If the file does not exist - an empty list.
            Otherwise - a list of instantiated classes.
        """
        filename = str(cls.__name__) + ".json"
        try:
            with open(filename, "r") as jsonfile:
                list_of_dicts = BaseModel.from_json_string(jsonfile.read())
                return [cls.create(**d) for d in list_of_dicts]
        except IOError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_of_objs):
        """Write the CSV serialization of a list of objects to a file.

        Args:
            list_of_objs (list): A list of inherited BaseModel instances.
        """
        filename = cls.__name__ + ".csv"
        with open(filename, "w", newline="") as csvfile:
            if list_of_objs is None or list_of_objs == []:
                csvfile.write("[]")
            else:
                if cls.__name__ == "Rectangle":
                    fieldnames = ["id", "width", "height", "x", "y"]
                else:
                    fieldnames = ["id", "size", "x", "y"]
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                for obj in list_of_objs:
                    writer.writerow(obj.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        """Return a list of classes instantiated from a CSV file.

        Reads from `<cls.__name__>.csv`.

        Returns:
            If the file does not exist - an empty list.
            Otherwise - a list of instantiated classes.
        """
        filename = cls.__name__ + ".csv"
        try:
            with open(filename, "r", newline="") as csvfile:
                if cls.__name__ == "Rectangle":
                    fieldnames = ["id", "width", "height", "x", "y"]
                else:
                    fieldnames = ["id", "size", "x", "y"]
                list_of_dicts = csv.DictReader(csvfile, fieldnames=fieldnames)
                list_of_dicts = [dict([k, int(v)] for k, v in d.items())
                                 for d in list_of_dicts]
                return [cls.create(**d) for d in list_of_dicts]
        except IOError:
            return []

    @staticmethod
    def draw(rectangle_list, square_list):
        """Draw Rectangles and Squares using the turtle module.

        Args:
            rectangle_list (list): A list of Rectangle objects to draw.
            square_list (list): A list of Square objects to draw.
        """
        turt = turtle.Turtle()
        turt.screen.bgcolor("#b7312c")
        turt.pensize(3)
        turt.shape("turtle")

        turt.color("#ffffff")
        for rect in rectangle_list:
            turt.showturtle()
            turt.up()
            turt.goto(rect.x, rect.y)
            turt.down()
            for i in range(2):
                turt.forward(rect.width)
                turt.left(90)
                turt.forward(rect.height)
                turt.left(90)
            turt.hideturtle()

        turt.color("#b5e3d8")
        for sq in square_list:
            turt.showturtle()
            turt.up()
            turt.goto(sq.x, sq.y)
            turt.down()
            for i in range(2):
                turt.forward(sq.width)
                turt.left(90)
                turt.forward(sq.height)
                turt.left(90)
            turt.hideturtle()

        turtle.exitonclick()
