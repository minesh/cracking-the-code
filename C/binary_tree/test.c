#include <stdio.h>


int main(void) {
   int x = 10;
   int y = 2;
   int *ptr;
   int **pptr;

   ptr = &x;
   pptr = &ptr;

   printf("Addr of &x: %p\n", &x); 
   printf("Addr of ptr: %p\n", ptr); 
   printf("Addr of &ptr: %p\n", &ptr); 
   printf("Addr of *ptr: %d\n", *ptr); 
   printf("\nAddr of &y: %p\n", &y); 
   printf("Addr of pptr: %p\n", pptr); 
   printf("Addr of &pptr: %p\n", &pptr); 
   printf("Addr of *pptr: %p\n", *pptr); 
}
