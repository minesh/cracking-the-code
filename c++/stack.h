#include <node.h>

#define STACK_SIZE 1024

class Stack {
   int size;
   Node *stack[STACK_SIZE];
   public:
      Stack();
      void push(Node *);
      bool isEmpty();
      bool isFull();
      Node *pop();

Stack::Stack() {
   size = -1;
}

bool Stack::isEmpty() {
   return (size == -1);
}

bool Stack::isFull() {
   return (size == STACK_SIZE);
}

void Stack::push(Node *newNode) {
   if (!isFull()) {
      stack[++size] = newNode;
   }
}

Node* Stack::pop() {
   if (!isEmpty()) {
      return stack[size--];
   }
}


