'''reverse linked lists'''

class singleNode:

	def __init__(self,data):
		self.data = data
		self.next = None

class LinkedList:

	def __init__(self):
		self.head = None

	def printlist(self):
		temp = self.head
		while(temp):
			print(temp.data,end=" --> ")
			temp = temp.next
		print("None")

	def reverse_list(self):
		temp = self.head
		prev = None
		current = temp
		while(temp):
			temp = current.next
			current.next = prev
			prev = current
			current = temp
		self.head = prev



ll = LinkedList()
ll.head = singleNode(0)
data = ll.head
for i in range(1,11):
	data.next = singleNode(i)
	data = data.next
ll.printlist()
ll.reverse_list()
ll.printlist()


class doubleNode:
	def __init__(self,data):
		self.data = data
		self.prev = None
		self.next = None

class DoubleLlist:
	def __init__(self):
		self.head = None

	def printlist(self):
		temp = self.head

		while(temp):
			print (temp.data,end=" <--> ")
			temp = temp.next
		print ("None")

	def reverse(self):
		temp = None
		current = self.head
		while(current):
			# if temp:
			# 	print(temp.data)
			temp = current.prev
			current.prev = current.next
			current.next = temp
			current = current.prev
			# print(current.prev.data,current.data,current.next.data)

		if temp is not None: 
			self.head = temp.prev

	def push(self, new_data): 
   
		# 1. Allocates node 
		# 2. Put the data in it 
		new_node = doubleNode(new_data) 
   
		# 3. Make next of new node as head and 
		# previous as None (already None) 
		new_node.next = self.head 
   
		# 4. change prev of head node to new_node 
		if self.head is not None: 
			self.head.prev = new_node 
   
		# 5. move the head to point to the new node 
		self.head = new_node 


print("\n\n\n\nDouble LinkedList test\n")
ll = DoubleLlist()
# ll.head = doubleNode(0)
for i in range(1,11):
	ll.push(i)

ll.printlist()
ll.reverse()
ll.printlist()



class CirculerList:

	def __init__(self):
		self.head = None

	def push(self,item):
		data = singleNode(item)
		temp = self.head
		data.next = self.head 

		if self.head:
			while(temp.next != self.head):
				temp = temp.next
			temp.next = data
		else:
			data.next = data
		self.head = data


	def printlist(self):
		temp = self.head
		if temp:
			while(True):
				print (temp.data,end=" <--> ")
				temp = temp.next
				if(temp == self.head):
					break
			print(temp.data)

	def reverse_list(self):
		temp = self.head
		prev = None
		current = temp
		while(temp):
			temp = current.next
			current.next = prev
			prev = current
			current = temp
		self.head = prev


print("\n\n\nCirculer LinkedList test\n")
Cl = CirculerList()
for i in range(1,11):
	Cl.push(i)

Cl.printlist()
Cl.reverse_list()
Cl.printlist()