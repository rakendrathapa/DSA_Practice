class LinkedQueue:
    """ FIFO queue implementation using a singly linked node """

    # ------ Nested Exception class -----
    class _Empty(Exception):
        """ non public exception class for this stack. """
        pass

    # ------ Nested _Node class ------
    class _Node:
        """ Lightweight, non public class for storing a singly linked node """
        __slots__ = '_element', '_next'         # streamline memory usage

        def __init__(self, element, next):
            self._element = element
            self._next = next

    # ------- Queue methods ----------
    def __init__(self):
        """ Create an empty queue """
        self._head = None
        self._tail = None
        self._size = 0              # Number of queue elements

    def __len__(self):
        """ Return the number of elements in the queue """
        return self._size

    def is_empty(self):
        """ Return True if the Queue is empty """
        return self._size == 0

    def first(self):
        """ Return but donot remove the First element of the queue
        Raise Exception if the queue is empty.
        """
        if self.is_empty():
            raise self._Empty('Empty Queue')
        return self._head._element      # Front aligned with the head of the list

    def dequeue(self):
        """ Return and Remove the first element of the queue
        Raise exception if the Queue is empty
        """
        if self.is_empty():
            raise self._Empty('Empty Queue')
        value = self._head._element
        self._head = self._head._next
        self._size -= 1
        if self.is_empty():         # Special case when the queue is empty
            self._tail = None
        return value

    def enqueue(self, e):
        """ Add an element to the back of the queue """
        newest = self._Node(e, None)            # Node will be a new tail node
        if self.is_empty():
            self._head = newest
        else:
            self._tail._next = newest
        self._tail = newest                     # Update Reference to the tail node
        self._size += 1



