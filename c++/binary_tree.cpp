#include <iostream>
#include <node.h>


class BinaryTree {
   private:
      Node *root;
      void insert(Node **root, int data);
      void printPreOrder(Node *root);
   public:
      BinaryTree();
      void insert(int data);
      void printTree();
      void printPreOrder();
      void printPreOrderIteratively();
};

BinaryTree::BinaryTree() {
   root = NULL;
}

void BinaryTree::printTree() {
   int screenWidth = 80;

}

void BinaryTree::printPreOrder(Node *root) {
   if (root != NULL) {
      printf("Data: %d\n", root->data);
      printPreOrder(root->left);
      printPreOrder(root->right);
   }
}

void BinaryTree::printPreOrder() {
   printPreOrder(root);
}

void BinaryTree::printPreOrderIteratively() {
   while(root != NULL) {
      printf("Data: %d\n", root->data);
   }
}

void BinaryTree::insert(Node **root, int data) {
   if (*root == NULL) {
      *root = new Node(data);
   } else {
      if ((*root)->data > data) {
         insert(&(*root)->left, data);
      } else {
         insert(&(*root)->right, data);
      }
   }
}

void BinaryTree::insert(int data) {
   insert(&root, data);
}

int main() {
   BinaryTree *tree = new BinaryTree();
   tree->insert(6);
   tree->insert(3);
   tree->insert(4);
   tree->insert(2);
   tree->insert(1);
   tree->insert(8);
   tree->printPreOrder();
   delete tree;
}


//Pre-order traversal
