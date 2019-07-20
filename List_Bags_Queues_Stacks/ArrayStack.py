class ArrayStack:
    """ LIFO Stack Implementation using a Python List as underlying storage """

    # --- Nested Exception Class
    class _Empty(Exception):
        """ Private Exception Class.
        Error attempting to access an element from an empty container
        """
        pass

    def __init__(self):
        """ Create an empty stack """
        self._data = []     # non public list members

    def __len__(self):
        """ Returning the number of elements in the stack """
        return len(self._data)

    def is_empty(self):
        """ Return True is the stack is empty """
        return len(self._data) == 0

    def push(self, e):
        """ Add element e to the top of the stack """
        self._data.append(e)            # new item stored at the end of the list

    def top(self):
        """ Return but donot remove the element at the top of the stack.
        Raise Empty Exception if the stack is empty
        """
        if self.is_empty():
            raise self._Empty('Empty stack.')
        return self._data[-1]         # last item in the stack

    def pop(self):
        """ Returns and Removes the top most element in the stack
        Raises Exception if Empty Stack
        """
        if self.is_empty():
            raise self._Empty('Empty Stack')
        return self._data.pop()        # remove the last item in the list
