from Node import Node

class LinkedList:
	""" A class representing a linked list """

	def __init__(self):
		""" Initializes a new instance of {LinkedList} """
		self.head, self.tail = None, None
		self.count = 0
	
	def is_empty(self):
		""" Determines whether the linked list is empty """
		return self.count == 0
	def print(self):
		""" Prints the linked list """
		cur = self.head
		while cur:
			print(cur.value, end = '\u00ab\u00bb')
			cur = cur.next
		
		print('None')
	
	def insert(self, value):
		""" Appends the value towards the end of the linked list """
		node = Node(value)
		if self.head is None:
			self.head = self.tail = node

		# insert at tail
		self.tail.next = node
		node.prev = self.tail
		self.tail = node
		self.count += 1

# test
if __name__ == '__main__':
	ll = LinkedList()
	for i in range(1, 11):
		ll.insert(i)
	
	ll.print()
