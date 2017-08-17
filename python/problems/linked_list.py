class Node(object):
   def __init__(self, data):
      self.data = data
      self.nextNode = None

class LinkedList(object):
   def __init__(self):
      self.root = None
      self.nodeCount = 0

   def insert(self, data):
      node = Node(data)
      if (self.root == None):
         self.root = node
      else:
         node.nextNode = self.root
         self.root = node
      self.nodeCount += 1

   def getNodeCount(self):
      return self.nodeCount

   def getRoot(self):
      return self.root

   def printLinkedList(self):
      pointer = self.root
      while(pointer != None):
         print pointer.data
         pointer = pointer.nextNode



