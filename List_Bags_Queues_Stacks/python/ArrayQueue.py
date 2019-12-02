class ArrayQueue:
    """ FIFO queue implementation using a Python list as underlying storage """
    DEFAULT_CAPACITY = 10

    class _Empty(Exception):
        """ Private Exception Class.
        Error attempting to access an element from an empty container
        """
        pass

    def __init__(self):
        """ Create an empty queue """
        self._data = [None] * ArrayQueue.DEFAULT_CAPACITY
        self._size = 0
        self._front = 0

    def __len__(self):
        """ Return the number of elements in the queue """
        return self._size

    def is_empty(self):
        """ Return TRUE if empty queue """
        return self._size == 0

    def first(self):
        """ Return but donot remove element at the front of the queue
         Raise exception if queue is empty
        """
        if self.is_empty():
            raise self._Empty('Empty Queue')
        return self._data[self._front]

    def dequeue(self):
        """ Remove and Return the first element of the queue
        Raise exception if the queue is empty
        """
        if self.is_empty():
            raise self._Empty('Empty Queue')

        value = self._data[self._front]
        self._data[self._front] = None          # help garbage collection
        self._front = (self._front + 1) % len(self._data)
        self._size -= 1
        return value

    def enqueue(self, e):
        """ Add an element in the back of the queue """
        if self._size == len(self._data):
            self.resize(2 * len(self._data))    # double the size of the queue
        avail = (self._front + self._size) % len(self._data)
        self._data[avail] = e
        self._size += 1

    def _resize(self, cap):
        """ Resize to new list of capacity >= len(self)  """
        old = self._data                        # Keep track of the existing list
        self._data = [None] * cap               # allocate list with new capacity
        walk = self._front
        for k in range(self._size):             # consider only existing elements
            self._data[k] = old[walk]           # intentionally shift indices
            walk = (1 + walk) % len(old)        # use old size as modulus
        self._front = 0                         # realign the front

