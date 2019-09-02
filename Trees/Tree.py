"""
Tree Abstract base class
"""

from collections import deque


class Tree:
    """
    Abstract base class representing a tree structure
    """

    # Nested Postion class
    class Postion:
        """ Abstraction representing the location of single element """

        def element(self):
            """ Return element stored at this Position """
            raise NotImplementedError('must be implemented by subclass')

        def __eq__(self, other):
            """ Return True if other position represents the same location """
            raise NotImplementedError('must be implemented by subclass')

        def __ne__(self, other):
            """ Returns True, if other does not represent the same location """
            return not (self == other)

    # Abstract methods that concrete subclasses must support
    def root(self):
        """ Return Position representing the tree's root (or None if empty) """
        raise NotImplementedError('must be implemented by the subclass')

    def parent(self, p):
        """ Return Position representing p parent """
        raise NotImplementedError('must be implemented by subclass')

    def num_children(self, p):
        """ Return the number of children that Position p has """
        raise NotImplementedError('must be implemented by subclass')

    def children(self, p):
        """ Generate Iteration of Position representing P's children """
        raise NotImplementedError('must be implemented by subclass')

    def __len__(self):
        """ Return the total number of elements of the tree """
        raise NotImplementedError('must be implemented by subclass')

    # Concrete method implemented by this class
    def is_root(self, p):
        """ Return True if Position p represents root of the tree """
        return self.root() == p

    def is_leaf(self, p):
        """ Return True if Position p does not have any children """
        return self.num_children(p) == 0

    def is_empty(self):
        """ Return True if the tree is empty """
        return len(self) == 0

    def depth(self, p):
        """ Returns the number of levels separating Position p from the root """
        if self.is_root(p):
            return 0
        else:
            1 + self.depth(self.parent(p))

    def __height1(self, p):
        """ Return the height of tree. Runs in O(n^2) """
        return max(self.depth(p) for p in self.positions() if self.is_leaf(p))

    def __height2(self, p):
        """ Returns the height of subtree rooted at position p. Runs in O(n) """
        if self.is_leaf(p):
            return 0
        else:
            return 1 + max(self.__height2(c) for c in self.children(p))

    def height(self, p=None):
        """
        Return the height of the subtree rooted at Position p
        If p==None, returns the height of the entire tree
        """
        if p is None:
            p = self.root()
        return self.__height2(p)

    def __iter__(self):
        """ Generate an iteration of tree's element """
        for p in self.positions():
            yield p.element()

    def preorder(self):
        """ Generate a preorder iteration of positions in the tree """
        if not self.is_empty():
            for p in self._subtree_preorder(self.root()):
                yield p

    def _subtree_preorder(self, p):
        """ Generate a preorder iteration of positions in subtree rooted at p """
        yield p
        for c in self.children(p):
            for other in self._subtree_preorder(c):  # do preorder of c's subtree
                yield other  # yielding each to our caller

    def postorder(self, p):
        """ Generate a postorder iteration of positions in the tree """
        if self.is_empty():
            return
        for p in self._subtree_postorder(self.root()):
            yield p

    def _subtree_postorder(self, p):
        """ Generate a postorder iteration of positions in subtree rooted at p """
        for c in self.children(p):
            for other in self._subtree_postorder(c):
                yield other
        yield p

    def breadthfirst(self):
        """ Generate a breadth first iteration of the positions of the tree """
        if self.is_empty():
            return

        fringe = deque()
        fringe.appendleft(self.root())
        while len(fringe):
            p = fringe.pop()
            yield p
            for c in self.children(p):
                fringe.appendleft(c)

    def positions(self):
        """ Generate an iterations of the tree's position """
        return self.preorder()


class BinaryTree(Tree):
    """ Abstract base class representing a binary tree structure """

    # Additional abstract methods
    def left(self, p):
        """
        Return a Position representing p's left child
        Return None if p does not have a left child
        """
        raise NotImplementedError('must be implemented by subclass')

    def right(self, p):
        """
        Return a position representing p's right child
        Return None if p does not have a right child
        """
        raise NotImplementedError('must be implemented by subclass')

    # concrete methods implemented in this class
    def sibling(self, p):
        """
        Return a position representing p's sibling
        """
        parent = self.parent(p)
        if parent is None:
            return None
        else:
            if p == self.left(parent):
                return self.right(parent)
            else:
                return self.left(parent)

    def children(self, p):
        """
        Generate an iteration of Positions representing p's children
        """
        if self.left(p) is not None:
            yield self.left(p)
        if self.right(p) is not None:
            yield self.right(p)

    def _subtree_inorder(self, p):
        """
        Generate an inorder iteration of position of the tree
        """
        if self.left(p) is not None:
            for other in self._subtree_inorder(self.left(p)):
                yield other
        yield p
        if self.right(p) is not None:
            for other in self._subtree_inorder(self.right(p)):
                yield other

    def inorder(self):
        """ Generate an inorder iteration of positions in the tree """
        if not self.is_empty():
            for p in self._subtree_inorder(self.root()):
                yield p

    # Override inherited version to make inorder the default
    def positions(self):
        """ Generate an iteration of tree position """
        return self.inorder()  # Make inorder the default


class LinkedBinaryTree(BinaryTree):
    """
    Linked Representation of a binary tree structure
    """

    class _Node:
        __slots__ = '_element', '_parent', '_left', '_right'

        def __init__(self, element, parent=None, left=None, right=None):
            self._element = element
            self._parent = parent
            self._left = left
            self._right = right

    class Position(BinaryTree.Postion):
        """
        An abstraction representing the location of a single element
        """

        def __init__(self, container, node):
            """ Constructor should not be invoked by the user """
            self._container = container
            self._node = node

        def element(self):
            """ Returns the element stored at this Position """
            return self._node._element

        def __eq__(self, other):
            """ Return True if other is a Position representing the same location """
            return type(other) is type(self) and other._node is self._node

    def _validate(self, p):
        """ Return associated node, if the position is valid """
        if not isinstance(p, self.Postion):
            raise TypeError('p must be a proper Position type')
        if p._container is not self:
            raise ValueError('p does not belong to this container')
        if p._node._parent is p._node:
            raise ValueError('p is no longer valid')
        return p._node

    def _make_position(self, node):
        """ Return Position instance for a given node (or None if no node)"""
        return self.Position(self, node) if node is not None else None

    # Binary Tree contructor
    def __init__(self):
        """ Create an initial empty tree """
        self._root = None
        self._size = 0

    # public accessor
    def __len__(self):
        """ Return the total number of elements in the tree """
        return self._size

    def root(self):
        """ Return the root postion of the tree (None if tree is empty """
        return self._make_position(self._root)

    def parent(self, p):
        """ Return the Position of p's parent (or None is p is root)"""
        node = self._validate(p)
        return self._make_position(node._parent)

    def left(self, p):
        """ Return the position of p's left child (or None is no left child )"""
        node = self._validate(p)
        return self._make_position(node._left)

    def right(self, p):
        """ Return the position of p's right child (or None is no right child) """
        node = self._validate(p)
        return self._make_position(node._right)

    def num_children(self, p):
        """ Return the number of child of postion p """
        node = self._validate(p)
        count = 0
        if node._left is not None:  # left child exists
            count += 1
        if node._right is not None:  # right child exists
            count += 1
        return count

    def _add_root(self, e):
        """
        Place element e at the root of an empty tree and return new position
        Raise ValueError is tree is nonempty
        """
        if self._root is not None: raise ValueError('Root exists')
        self._size = 1
        self._root = self._Node(e)
        return self._make_position(self._root)

    def _add_left(self, p, e):
        """
        Create a left child for Position p, storing element e
        Return position of new node
        Raise ValueError if Position p is invalid or p already has a left child
        """
        node = self._validate(p)
        if node._left is not None: raise ValueError('Left child exisits')
        self._size += 1
        node._left = self._Node(e, node)  # node is its parent
        return self._make_position(node._left)

    def _add_right(self, p, e):
        """
        Create a new right child of Position p storing element e
        Return the new position of the element
        Raise ValueError is Position is invalid or p already has a right child
        """
        node = self._validate(p)
        if node._right is not None: raise ValueError('Right child exists')
        self._size += 1
        node._right = self.Node(e, node)
        return self._make_position(node._right)

    def _replace(self, p, e):
        """ Replace the element at position p with e, return the old value """
        node = self._validate(p)
        oldvalue = node._element
        node._element = e
        return oldvalue

    def _delete(self, p):
        """
        Delete the node at Position p, and replace it with its child, if any.
        Return the element that had been previously stored at position p
        Raise ValueError is Position p is invalid or p has two children
        """
        node = self._validate(p)
        if self.num_children(p) == 2: raise ValueError('p has 2 children')
        child = node._left if node._left else node._right
        if child is not None:
            child._parent = node._parent
        if node is self._root:
            self._root = child
        else:
            parent = node._parent
            if node is parent._left:
                parent._left = child
            else:
                parent._right = child
        self._size -= 1
        node._parent = node
        return node._element

    def attach(self, p, t1, t2):
        """
        Attach trees t1 and t2 as left and right subtrees of external p
        """
        node = self._validate(p)
        if not self.is_leaf(p): raise ValueError('Position must be left')
        if not type(self) is type(t1) is type(t2):  # All 3 Tress must be of same type
            raise TypeError('Tree Type must match')
        self._size += len(t1) + len(t2)
        if not t1.is_empty():  # Attach t1 as left subtree
            t1._root._parent = node
            node._left = t1._root
            t1._root = None
            t1._size = 0
        if not t2.is_empty():  # Attach t2 as right subtree
            t2._root._parent = node
            node._right = t2._root
            t2._root = None
            t2._size = 0
