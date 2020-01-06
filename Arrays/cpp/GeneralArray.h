/**
 * Array as an Abstract Data Type
 * An array is intuitively a set of pairs <index, value>, such that index is defined as value associated with it.
 * We define an Abstract Class, GeneralArray, that is more flexible about the composition of the index set
 */

template <class T>
class GeneralArray {
// A set of pairs <index, value> where for each value of index in IndexSet
// there is a value of type T. IndexSet is a finite ordered set of one or more
// dimensions, for example {0, . . . ., n-1} for one dimension, {(0,0), (0,1),
// (0,2), . . ., (2,2)} for 2 dimensions, etc.
public:
    GeneralArray(int j, RangeList list, T initValue=defaultValue);
    // This constructor creates a j dimensional array of floats; the
    // range of the kth dimension is given by the kth element of list.
    // For each index i n the index set, insert <i, initValue> into the array.

    T Retrieve(index i);
    // If i is in the index set of the array, return the T associated with i
    // in the array, otherwise throw an exception.

    void Store(index i, T x);
    // If i is in the index set of the array, replace the old value associated
    // with i by x; otherwise throw an exception.
};
