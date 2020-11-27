class node:

	def __init__(self, val):
		self.value = val
		self.next = None

first = node(27)
# first.next = node(28)
# first.next.next = node(32)
# first.next.next.next = node(50)

class SingleLinkedList:

	def __init__(self):
		self.head = None
		self.tail = None
		self.length = 0

	def push(self, element):
		new_node = node(element)

		if(self.head == None):
			self.head = new_node
			self.tail = self.head
		else:
			self.tail.next  =  new_node
			self.tail = new_node
			self.tail.next = None 

		self.length = self.length + 1
		return self

	def pop(self):
		cur = self.head
		temp = cur.next

		while temp.next != None:
			cur = cur.next
			temp = cur.next

		self.tail = cur
		cur.next = None
		self.length = self.length - 1
		return self

	def shift(self):
		first = self.head

		cur = first.next
		self.head = cur
		del first
		self.length = self.length - 1
		if(self.length == 0):
			self.tail = None
		return self

	def unshift(self, element):
		new_node = node(element)

		new_node.next = self.head
		self.head = new_node
		self.length = self.length + 1
		return self

	def get(self, index):
		cur = self.head

		for i in range(1, index):
			cur = cur.next

		return cur.value

	def set(self, index, val):
		cur = self.head

		for i in range(1,index):
			cur = cur.next

		cur.value = val

		return self

	def insert(self, index, val):
		new_node = node(val)
		cur = self.head

		for i in range(1, (index - 1)):
			cur = cur.next

		new_node.next = cur.next
		cur.next = new_node
		self.length = self.length + 1 

		return self

	def reverse(self):
		cur = self.head
		self.tail = cur
		Next = cur.next

		for i in range(1, self.length):
			Prev = cur
			cur = Next
			Next = cur.next

			cur.next = Prev

		self.head = cur
		Tail = self.tail
		Tail.next = None

		return self



list1 = SingleLinkedList()

out = list1.push(10)
print(out)
out = list1.push(30)
out = list1.push(70)
out = list1.push(80)
out = list1.push(88)
out = list1.push(96)
print(out)

list1.pop()
list1.pop()
out = list1.pop()
print(out)

out = list1.shift()
print(list1.length)
out = list1.get(2)
print(out)

list1.set(2,100)
print(list1.get(2))

list1.insert(3,200)
print(list1.length)

list1.reverse()
cur = list1.head
print(cur.value)
for i in range(1, list1.length):
	cur = cur.next
	print(cur.value)


DoublyLinkedList is almost same as SingleLinkedList 

class node:
	def __init__(self,val):
		self.value = val
		self.next = None

class stack:

	def __init__(self):
		self.start = None
		self.end = None
		self.size = 0

	def push(self, val):
		NewNode = node(val)

		if(self.start == None):
			self.start = NewNode
			self.end = self.start
		else:
			NewNode.next = self.start
			self.start = NewNode

		self.size = self.size + 1

		return self.size

	def pop(self):
		if(self.start == None):
			return None

		if(self.size == 1):
			cur = self.start
			val = cur.value
			self.start = None
			self.end = None
			self.size = 0
			del cur

			return val

		if(self.size > 1):
			cur = self.start
			val = cur.value
			self.start = cur.next
			self.size = self.size - 1
			del cur

			return val

# push & pop is of constant time in stack

stack1 = stack()
stack1.push(2)
print(stack1.push(20))
print(stack1.push(19))
print(stack1.push(29))
print(stack1.push(98))

print(stack1.pop())
print(stack1.pop())

class node:

	def __init__(self, val):
		self.value = val
		self.next = None

class queues:

	def __init__(self):
		self.start = None
		self.end = None
		self.size = 0

	def enqueue(self, val):
		NewNode = node(val)

		if(self.start == None):
			self.start = NewNode
			self.end = self.start
		else:
			last = self.end
			last.next = NewNode
			self.end = NewNode

		self.size = self.size + 1

		return self.size

	def dequeue(self):
		if(self.start == None):
			return None

		if(self.size == 1):
			cur = self.start
			val = cur.value
			self.start = None
			self.end = None
			self.size = 0
			del cur 
			return val

		if(self.size > 1):
			first = self.start
			val = first.value
			self.start = first.next
			self.size = self.size - 1
			del first

			return val

queue = queues()
out = queue.enqueue(23)
print(out)
print(queue.enqueue(21))
print(queue.enqueue(5))
print(queue.enqueue(65))
print(queue.enqueue(76))

print(queue.dequeue())

class node:

	def __init__(self, val):
		self.value = val
		self.left = None
		self.right = None

class BinarySearchTree:

	def __init__(self):
		self.root = None

	@staticmethod 
	def left(element, parent):
		if(parent.left == None):
			NewNode = node(element)
			parent.left = NewNode
			return True
		else:
			parent = parent.left
			if(element < parent.value):
				return BinarySearchTree.left(element, parent)
			elif(element > parent.value):
				return BinarySearchTree.right(element, parent)
			else:
				return False

	@staticmethod
	def right(element, parent):
		if(parent.right == None):
			NewNode = node(element)
			parent.right = NewNode
			return True
		else:
			parent = parent.right
			if(element < parent.value):
				return BinarySearchTree.left(element, parent)
			elif(element > parent.value):
				return BinarySearchTree.right(element, parent)
			else:
				return False

	def insert(self, element):
		if(self.root == None):
			NewNode = node(element)
			self.root = NewNode
			return True

		parent = self.root
		if(element < parent.value):
			return BinarySearchTree.left(element, parent)
		elif(element > parent.value):
			return BinarySearchTree.right(element, parent)
		else:
			return False

	def BFS(self):
		Node = self.root
		data = []
		queue = []
		queue.append(Node)

		while (len(queue) != 0):
			Node = queue[0]
			queue = queue[1:]
			data.append(Node.value)
			if(Node.left != None):
				queue.append(Node.left)

			if(Node.right != None):
				queue.append(Node.right)

		return data

	def DFS(self):
		Node = self.root
		data = []

		def helper(vertex):
			data.append(vertex.value)

			if(vertex.left != None):
				helper(vertex.left)

			if(vertex.right != None):
				helper(vertex.right)

		helper(Node)
		return data


tree = BinarySearchTree()
print(tree.insert(10))
print(tree.insert(6))
print(tree.insert(15))
print(tree.insert(3))
print(tree.insert(8))
print(tree.insert(20))
#print(tree.insert(43))

out = tree.BFS()
print(out)

out = tree.DFS()
print(out)

import math 
class MaxBinaryHeap:

	def __init__(self):
		self.value = []

	def insert(self, element):
		self.value.append(element)
		self.BubbleUp(self.value)

		return self.value

	def BubbleUp(self, values):
		element_index = len(values) - 1
		parent_index = math.floor((element_index - 1) / 2)

		if(parent_index < 0):
			return True

		while (values[parent_index] < values[element_index]):

			[values[parent_index],values[element_index]] = [values[element_index],values[parent_index]]
			element_index = parent_index
			parent_index = math.floor((element_index - 1) / 2)

			if(values[parent_index] > values[element_index] or parent_index < 0):
				return True

heap = MaxBinaryHeap()
out = heap.insert(41)
print(out)
out = heap.insert(39)
print(out)
out = heap.insert(33)
print(out)
out = heap.insert(18)
print(out)
out = heap.insert(27)
print(out)
out = heap.insert(12)
print(out)
out = heap.insert(55)
print(out)

class node:

	def __init__(self, val, priority):
		self.value = val
		self.priority = priority

class PriorityQueue:

	def __init__(self):
same as BinaryHeap

def Hash(astring, arange):
	total = 0
	for i in astring:
		value = ord(i)
		total = total + value

	total = total % arange

	return total

out = Hash("pink", 10)
print(out)

import numpy as np 
class HashTable:
	
	def __init__(self, size = 53):
		self.size = size
		self.KeyMap = [None] * self.size

	def hesh(self, key):
		total = 0
		weird_prime = 31

		for i in range(min(len(key), 100)):
			value = ord(key[i]) - 96
			total = (total * weird_prime + value) % self.size

		return total

	def set(self, key, val):
		index = self.hesh(key)

		if(self.KeyMap[index] == None):
			self.KeyMap[index] = []

		self.KeyMap[index].append([key, val])

	def get(self, key):
		index = self.hesh(key)

		if(self.KeyMap[index] != None):
			
			for i in range(len(self.KeyMap[index])):
				if(key == self.KeyMap[index][i][0]):
					return self.KeyMap[index][i][1]
		else:
			return "undefined"

ht = HashTable(17)
ht.set("mango", 20)
ht.set("apple", 26)
ht.set("physics", 11)
ht.set("maths", 2)
ht.set("statistics", 98)
ht.set("Numerical", 65)
ht.set("machine", 43)
ht.set("machine", 44)
def hesh(key):
	total = 0
	weird_prime = 31

	for i in range(min(len(key), 100)):
		value = ord(key[i]) - 96
		total = (total * weird_prime + value) % 53

	return total

out = hesh("pratik")
print(out)
out = hesh("nishi")
print(out)
out = hesh("bhavna")
print(out)
out = hesh("deepa")
print(out)
out = hesh("avinash")
print(out)

out = ht.get("machine")
print(out)

class Graph:

	def __init__(self):
		self.AdjacencyList = {}

	def AddVertex(self, vertex):

		if(self.AdjacencyList.get(vertex) == None):
			self.AdjacencyList[vertex] = []

	def AddEdge(self, vertex1, vertex2):
		self.AdjacencyList[vertex1].append(vertex2)
		self.AdjacencyList[vertex2].append(vertex1)

	def RemoveEdge(self, vertex1, vertex2):
		self.AdjacencyList[vertex1].remove(vertex2)
		self.AdjacencyList[vertex2].remove(vertex1)

	def DFS(self, vertex):
		result = []
		visited = {}
		adjacencyList = self.AdjacencyList

		def dfsHelper(vertex):
			visited[vertex] = True
			result.append(vertex)
			for v in adjacencyList[vertex]:
				if(visited.get(v) == None):
					return dfsHelper(v)

		dfsHelper(vertex)
		return result

	def BFS(self, start):
		queue = [start]
		result = []
		visited = {}

		while(len(queue))


g = Graph()
g.AddVertex("0")
g.AddVertex("1")
g.AddVertex("2")
g.AddVertex("3")
g.AddVertex("4")
g.AddVertex("5")

g.AddEdge("1","0")
g.AddEdge("1","3")
g.AddEdge("0","2")
g.AddEdge("2","4")
g.AddEdge("4","5")
g.AddEdge("3","5")
g.AddEdge("4","3")

print(g.AdjacencyList)
print(g.DFS("1"))