#!/usr/bin/env python


class Node(object):
   def __init__(self, data):
      self.data = data
      self.nextNode = None

class LinkedList(object):

   def __init__(self):
      self.head = None

   def insert(self, node):
      node.nextNode = self.head
      self.head = node

   def delete(self):
      if (self.head == None):
         return None
      returnNode = self.head
      self.head = self.head.nextNode
      return returnNode

   def delete(self, data):
      if (self.head == None):
         return None
      tempHead = self.head
      prevHead = None
      while(tempHead):
         if (tempHead.data == data):
            if prevHead:
               prevHead.nextNode = tempHead.nextNode
               tempHead.nextNode = None
            else:
               # Root node 
               self.head = tempHead.nextNode
            return tempHead
         prevHead = tempHead
         tempHead = tempHead.nextNode
      return None
   
   def isEmpty(self):
      return self.head == None

   def printList(self):
      tempHead = self.head
      while(tempHead):
         print tempHead.data,
         tempHead = tempHead.nextNode
      print "Done"

      
ll = LinkedList()
ll.insert(Node(1))
ll.insert(Node(4))
ll.insert(Node(5))
ll.insert(Node(6))
ll.printList()
y = ll.delete(1)
print y.data
ll.printList()
