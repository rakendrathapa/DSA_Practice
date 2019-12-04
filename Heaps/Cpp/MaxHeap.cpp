#include <iostream>
#include <vector>
#include <algorithm>
#include <stdexcept>

using namespace std;

class MaxHeap
{
private:
	vector<int> heap;

	int __parent(int i){
		return (i-1)/2;
	}

	int __left(int i){
		return (2*i + 1);
	}

	int __right(int i){
		return (2*i + 2);
	}

	// Heapify Down Algorithm.
	// The node at index i and its 2 children 
	// violates the heap property.
	void __heapify_down(int i)
	{
		int left = this->__left(i);
		int right = this->__right(i);

		int largest = i;

		// compare heap(i) with left and right child.
		// to find the largest value
		if(left < size() && heap.at(left) > heap.at(largest)){
			largest = left;
		}

		if(right < size() && heap.at(right) > heap.at(largest)){
			largest = right;
		}

		// swap with largest child having greater value
		// and call heapify down the child.
		if (largest != i){
			swap(heap[i], heap[largest]);
			__heapify_down(largest);
		}
	}

	// Recursively Heapify-up algorithm
	void __heapify_up(int i)
	{
		// Check if the node at index i and its parent violates the heap property.
		if (i && heap.at(__parent(i)) < heap.at(i))
		{
			swap(heap[i], heap[__parent(i)]);

			// call Heapify-up on the parent
			__heapify_up(__parent(i));
		}
	}

public:
	MaxHeap(vector<int> tempHeap = {})
	{
		this->heap = tempHeap;
	}

	// Size of the heap
	int size()
	{
		return heap.size();
	}
	
	// Check heap empty or not
	bool empty()
	{
		return this->size() == 0;
	}

	// Function return element with highest priority (without deleting)
	int top()
	{
		try{
			// if heap has n elements, throw an exception.
			if (this->empty()){
				throw out_of_range("Vector<X>::at() : "
				"index is out of range(Heap underflow)");
			}			
		}
		catch(const out_of_range& oor){
			std::cout << "\n" << oor.what() << std::endl;
		}
		return this->heap.at(0); 	// or heap[0]
	}

	int pop()
	{
		int top_element = 0;
		try{
			// if heap has no element, throw an exception
			if(this->empty()){
				throw out_of_range("Vector<X>::at() : index out of range(Heap Underflow)");
			}

			// replace the root of the heap with the last element of the vector.
			top_element = this->heap.at(0);
			heap[0] = heap.back();
			heap.pop_back();

			// Calling heapify down on root node.
			this->__heapify_down(0);
		}
		// catch and print the exception.
		catch (const out_of_range& oor){
			std::cout << "\n" << oor.what() << std::endl;
		}

		return top_element;
	}

	// Insert key into the heap
	void push(int key)
	{
		// insert the new key to the end of the vector
		this->heap.push_back(key);

		// get the element index and call heapify-up procedure
		int index = this->heap.size() - 1;
		this->__heapify_up(index);
	}

	// Print the heap value.
	void printHeap()
	{
		try{
			if (this->empty()){
				throw out_of_range("Vector<X>::at() : index out of range(Heap Underflow)");
			}

			vector<int>::iterator it = heap.begin();
			while(it != heap.end()){
				std::cout << *(it++) << " " << std::endl;
			}
		}
		catch (const out_of_range& oor){
			std::cout << "\n" << oor.what() << std::endl;
		}
	}
};

int main()
{
	std::cout << "Hello World\n" << std::endl;
	MaxHeap *h = new MaxHeap();

	std::cout << "Empty Heap:";
	h->printHeap();

	// priority is determined by element's value
	h->push(3);
	h->push(2);
	h->push(15);

	std::cout << "Heap:"; h->printHeap();
	std::cout << "Heap Size = " << h->size() << std::endl;
	std::cout << h->pop() << std::endl;

	h->push(5);
	h->push(4);
	h->push(45);

	std::cout << std::endl << "Size is " << h->size() << std::endl;
	
	std::cout << h->top() << " ";
	h->pop();
	std::cout << h->pop() << " ";
	std::cout << h->pop() << " ";
	std::cout << h->pop() << " ";
	std::cout << h->pop() << " ";
	
	std::cout << std::endl << std::boolalpha << h->empty();
	
	h->top();	// top operation on an empty heap
	h->pop();	// pop operation on an empty heap

	delete h;
	return 0;

}