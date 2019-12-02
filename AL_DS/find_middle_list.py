'''find out midle element of the linked list'''

class Node:

	def __init__(self,data=None):
		self.data = data
		self.next = None


class LinkedList:
	def __init__(self):
		self.head = None

	def printlist(self):
		temp = self.head
		while(temp):
			print (temp.data,end = " ")
			temp = temp.next

	def middle_element(self):
		middle = self.head
		temp = self.head
		if not temp:
			return "no element in list"
		while(temp.next):
			temp = temp.next
			if (temp.next):
				middle = middle.next
				temp = temp.next
		return middle.data


ll = LinkedList()
print ("middle element 1st : ",ll.middle_element())
ll.head = Node(0)
data = ll.head
print ("middle element 2st : ",ll.middle_element())
for i in range(1,11):
	data.next = Node(i)
	data = data.next

print ("middle element 3st : ",ll.middle_element())
ll.printlist()