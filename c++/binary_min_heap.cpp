#include <iostream>
#include <math>
/* [don't use index 0, 4,5,6,7,8,9,10]
 */

class BinaryMinHeap {
   private:
      int *array;
      int size;
      int indexPtr;
      bool isEmpty();
      bool isFull();
      void heapify(int index);
      void swap(int a, int b);
   public:
      BinaryMinHeap(int size);
      void insert(int data);
      int remove();
      void printHeap();
};

BinaryMinHeap::BinaryMinHeap(int size) {
   this->size = size;
   array = new int[size]; 
   indexPtr = 1;
}

bool BinaryMinHeap::isEmpty() {
   return indexPtr == 1;
}

bool BinaryMinHeap::isFull() {
   bool full = false;
   if (indexPtr == size + 1) {
      printf("Heap is full\n");
      full = true;
   }
   return full;
}

void BinaryMinHeap::swap(int parentIndex, int index) {
   int temp = array[parentIndex];
   array[parentIndex] = array[index];
   array[index] = temp;
}

void BinaryMinHeap::heapify(int index) {
   int parentIndex = index / 2;
   if (array[parentIndex] > array[index] && parentIndex != 0) {
      swap(parentIndex, index);
      // parentIndex will contain the smallest number
      // since it got swapped
      heapify(parentIndex);
   }
}

void BinaryMinHeap::insert(int data) {
   if (!isFull()) {
      //add to end and heapify
      array[indexPtr] = data;
      heapify(indexPtr);
      indexPtr++;
   }
}
void BinaryMinHeap::bubbleDownRoot(int index) {
   int lChild = 2 * i;
   int rChild = 2 * i + 1;
   int minChild = array[lChild] > array[rightChild] ? rightChild:leftChild;
   if (array[index] > array[minChild] && lChild <= indexPtr && rChild <= indexPtr) {
      swap(index, minChild);
      // minChild holds the larger value
      bubbleDownRoot(minChild);
   }
}

int BinaryMinHeap::remove() {
   int returnValue = array[1];
   swap(1, indexPtr);
   --indexPtr;
   bubbleDownRoot(1);
}

void BinaryMinHeap::printHeap() {
   for( int i=1; i <= indexPtr; i++) {
      printf("Index %d = %d\n", i, array[i]);
   }
}

int main () {
   BinaryMinHeap heap = BinaryMinHeap(5);
   heap.insert(33);
   heap.insert(2);
   heap.insert(10);
   heap.insert(7);
   heap.printHeap();
   return 0;
}
