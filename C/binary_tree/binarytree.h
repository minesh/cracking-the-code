#include <stdlib.h>
#include "node.h"


Node *newNode(int data) {
   Node *newNode = (Node *)malloc(sizeof(Node));
   newNode->data = data;
   newNode->left = NULL;
   newNode->right = NULL;
   return newNode;
}

/*
 * root -> ptr -> Node[5]
     (5)
    /  \
  (3)  (7)

  So now we can change what ptr points to
*/

void insert(Node **root, data) {
   if (*root == NULL) {
      *root = newNode(data);
   } else if ((*root)->data > data) {
      insert(&(*root)->left, data);
   } else {
      insert(&(*root)->right, data);
   }
}

Node* find(Node *root, int data) {
   if (root == NULL) {
      return NULL;
   } else if (root->data == data) {
      return root;
   } else if (root->data > data) {
      return find(root->left, data);
   } else {
      return find(root->right, data);
   }
}
