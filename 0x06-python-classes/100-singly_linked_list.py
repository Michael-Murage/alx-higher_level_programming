#!/usr/bin/python3


class Node:
    """Define class Node of a singly linked list"""

    @property
    def data(self):
        """Return private instance data"""
        return self.__data

    @data.setter
    def data(self, value):
        """Sets the value of data"""
        if type(value) is int:
            self.__data = value
        else:
            raise TypeError("data must be an integer")

    @property
    def next_node(self):
        """Returns the next node"""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """Sets the next_node value"""
        if value is not None and type(value) is not Node:
            raise TypeError("next_node must be a Node object")
        else:
            self.__next_node = value

    def __init__(self, data, next_node=None):
        """Initialize a node"""
        self.data = data
        self.next_node = next_node


class SinglyLinkedList:
    """A singly linked list class"""

    def __init__(self):
        """Initializes a singly linked list"""
        self.__head = None

    def sorted_insert(self, value):
        """Inserts a node into a linked list"""
        if self.__head is None:
            self.__head = Node(value, None)
        elif value <= self.__head.data:
            new_node = Node(value, self.__head)
            self.__head = new_node
        else:
            ptr = self.__head
            while ptr.next_node is not None and ptr.next_node.data <= value:
                ptr = ptr.next_node

            tmp = ptr.next_node
            ptr.next_node = Node(value, tmp)

    def __str__(self):
        """Printable representation of a linked list"""
        ptr = self.__head
        to_print = ""
        while ptr is not None:
            to_print = to_print + str(ptr.data) + '\n'
            ptr = ptr.next_node
        return to_print[:-1]
