class LinkedBag:
    """ Bag implementation using a singly linked list for storage """

    # ----- Nested _Node class --------
    class _Node:
        """ Lightweight, non public class for storing the singly linked node """
        __slots__ = '_element', '_next'  # streamline the memory usage

        def __init__(self, element, next):
            self._element = element
            self._next = next

    # ---------- Bag Class --------------
    def __init__(self):
        self._head = None
        self._size = 0

    def size(self):
        """ Returns the number of elements in the Bag"""
        return self._size

    def is_empty(self):
        """ Returns True is the Bag is empty """
        return self.size() == 0

    def add_element(self, e):
        """ Add element e to the Bag """
        self._head = self._Node(e, self._head)
        self._size += 1
