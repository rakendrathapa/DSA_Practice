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
        self.curr_node = None

    def __iter__(self):
        return self

    def __next__(self):
        curr_node = self.curr_node
        if curr_node is None:
            self.curr_node = self._head
            raise StopIteration
        val = curr_node._element
        self.curr_node = self.curr_node._next
        return val

    def get_element(self):
        curr_node = self._head
        while True:
            if curr_node is not None:
                yield curr_node._element
                curr_node = curr_node._next
            else:
                break

    def size(self):
        """ Returns the number of elements in the Bag"""
        return self._size

    def is_empty(self):
        """ Returns True is the Bag is empty """
        return self.size() == 0

    def add_element(self, e):
        """ Add element e to the Bag """
        self._head = self._Node(e, self._head)
        self.curr_node = self._head
        self._size += 1
