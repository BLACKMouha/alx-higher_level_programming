#!/usr/bin/python3
"""Represents the structure of a node belonging a singly linked list"""


class Node:
    """Define the Node"""

    def __init__(self, data, next_node=None):
        """Initializes self
            Args:
                data (int): the data field of the node
                next_node (Node): points to the next node"""
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """Getting the data of an Node instance
            Usage : instance.data
            Return: the value of the attribute data"""
        return self.__data

    @data.setter
    def data(self, value):
        """Set value to the attribute data
            Args:
                value (int): integer to be hold by the data field
            Raises:
                TypeError: if value is not an integer"""
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """Getting the next node of an Node instance
            Usage : instance.next_node
            Return: the value of the attribute next_node"""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """Set value to the attribute data
            Args:
                value (Node): Node instance of the next node
            Raises:
                TypeError: if value is not None or Node type"""
        if not isinstance(value, type(None)) and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


"""Generates a singly linked list"""


class SinglyLinkedList:
    """Define a Singly List List."""

    def __init__(self):
        """Initializes a singly linked list"""
        self.__head = None

    def sorted_insert(self, value):
        """Inserts in a sorted way a new node
            Args:
                value: data to be insert"""
        new_node = Node(value)
        if self.__head is None:
            self.__head = new_node
            return

        if value < self.__head.data:
            new_node.next_node = self.__head
            self.__head = new_node
            return

        tmp = self.__head
        while value >= tmp.data:
            prev = tmp
            if tmp.next_node:
                tmp = tmp.next_node
            else:
                tmp.next_node = new_node
                return
        prev.next_node = new_node
        new_node.next_node = tmp

    def __str__(self):
        """Return str(self)"""
        s = ""
        tmp = self.__head
        while tmp:
            s += str(tmp.data) + "\n"
            tmp = tmp.next_node
        return s[:-1]
