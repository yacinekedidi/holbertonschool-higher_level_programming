#!/usr/bin/python3
"""Node class."""

class Node:
    """defines a node."""
    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, value):
        if value is None:
            self.__data = value
        elif not isinstance(value, int):
            raise TypeError("data must be an integer")
        else:
            self.__data = value

    @property
    def next_node(self):
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        if value is None:
            self.__next_node = value
        elif not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        else:
            self.__next_node = value

"""SinglyLinkedList class."""


class SinglyLinkedList:
    """ defines a SinglyLinkedList."""
    def __init__(self):
        self.__head = Node(None)

    def __str__(self):
        stR = ""
        tmp = self.__head
        if  tmp is None:
            return stR[:-1]
        else:
            while tmp is not None:
                stR += str(tmp.data)
                stR += "\n"
                tmp = tmp.next_node
            return stR[:-1]

    def sorted_insert(self, value):
        new = Node(value)
        tmp = self.__head
        if tmp is None:
            self.__head = new
        elif  tmp.data is None:
            tmp.data = value
        else:
            if value <= tmp.data:
                new.next_node = self.__head
                self.__head = new
            else:
                while tmp.next_node is not None:
                    if tmp.next_node.data >= value:
                        break
                    tmp = tmp.next_node
                new.next_node = tmp.next_node
                tmp.next_node = new
