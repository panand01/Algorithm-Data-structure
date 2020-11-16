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

# list1.pop()
# list1.pop()
# out = list1.pop()
# print(out)

# out = list1.shift()
# print(list1.length)
# out = list1.get(2)
# print(out)

# list1.set(2,100)
# print(list1.get(2))

# list1.insert(3,200)
# print(list1.length)

list1.reverse()
cur = list1.head
print(cur.value)
for i in range(1, list1.length):
	cur = cur.next
	print(cur.value)
