from __future__ import annotations

from abc import abstractmethod, ABC


class Shape:

    def __init__(self):
        self.shape = None


class Color:

    def __init__(self):
        self.color = None


class Figure:
    def __init__(self):
        self.__color: Color = None
        self.__shape: Shape = None

    def who_i_am(self):
        print(f"My color is {self.__color.color}")
        print(f"My shape is {self.__shape.shape}")

    def set_color(self, color):
        self.__color = color

    def set_shape(self, shape):
        self.__shape = shape


class Director:

    def __init__(self):
        self._builder = None

    def set_builder(self, builder: Builder):
        self._builder = builder

    def get_figure(self):
        figure = Figure()

        color = self._builder.get_color()
        figure.set_color(color)

        shape = self._builder.get_shape()
        figure.set_shape(shape)

        return figure


class Builder(ABC):
    """
    Specify an abstract interface for creating parts of a Product
    object.
    """

    @abstractmethod
    def get_color(self):
        raise NotImplementedError

    @abstractmethod
    def get_shape(self):
        raise NotImplementedError


class BlueCircleBuilder(Builder):

    def get_color(self):
        color = Color()
        color.color = "blue"
        return color

    def get_shape(self):
        shape = Shape()
        shape.shape = "Circle"
        return shape


class RedLineBuilder(Builder):
    def get_color(self):
        color = Color()
        color.color = "red"
        return color

    def get_shape(self):
        shape = Shape()
        shape.shape = "Line"
        return shape


if __name__ == "__main__":

    builder = BlueCircleBuilder()
    director = Director()
    director.set_builder(builder)

    figure = director.get_figure()

    figure.who_i_am()
    print("Next Figure")
    director.set_builder(RedLineBuilder())
    figure = director.get_figure()
    figure.who_i_am()