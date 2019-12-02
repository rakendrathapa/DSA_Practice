class LinkedStack:
    """ LIFO Stack implementation using a singly linked list """

    # ------- Nested Empty Exception Class -----
    class _Empty(Exception):
        """ non public exception class for this stack. """
        pass

    # ------- Nested __Node class ----------
    class _Node:
        """ Lightweight, non public class for storing singly linked list """
        __slots__ = '_element', '_next'  # streamline memory usage

        def __init__(self, element, next):  # initialize the node fields
            self._element = element  # reference to user's element
            self._next = next  # reference to next node

    # -------- Stack methods ----------------
    def __init__(self):
        """ Create a empty stack """
        self._head = None  # reference to the head node
        self._size = 0  # number of the stack element

    def size(self):
        """ Returns the number of elements in the stack """
        return self._size

    def is_empty(self):
        """ Returns True is the stack is empty """
        return self._size == 0

    def push(self, e):
        """ Add element e to the top of the stack"""
        self._head = self._Node(e, self._head)  # create and link a new node
        self._size += 1

    def top(self):
        """ Return the top most element of the stack. Donot delete.
         Raise exception if the Stack is empty.
         """
        if self.is_empty():
            raise self._Empty('Stack is empty')
        return self._head.elment

    def pop(self):
        """ Returns and removes the top most element of the stack.
        Raise Empty Exception if the stack is empty.
        """
        if self.is_empty():
            raise self._Empty('Stack is empty')

        answer = self._head.elment
        self._head = self._head._next  # By pass the former topnode
        self._size -= 1
        return answer
