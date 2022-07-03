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
			print(cur.data, end = '\u00ab\u00bb')
			cur = cur.next
		
		print('None')
	
	def insert(self, value):
		""" Appends the value towards the end of the linked list """
		node = Node(value)
		if self.head is None:
			self.head = self.tail = node
			return

		# insert at tail
		self.tail.next = node
		node.prev = self.tail
		self.tail = node
		self.count += 1
	
	def delete(self, value):
		""" Delete the first node with the given {value} """ 
		cur = self.head

		while cur:
			if cur.data is value:
				# there is only one node
				if self.head is cur and self.head.next is None:
					self.head, self.tail = None, None
					return True
				
				# there are more than one node and last node is
				# to be deleted
				if self.tail is cur:
					self.tail = cur.prev
					self.tail.next = None
					return True
				
				# the node to be deleted is in between
				if cur.prev and cur.next:
					cur.prev.next, cur.next.prev = cur.next, cur.prev
					return True
			
			cur = cur.next

		return False

# test
if __name__ == '__main__':
	ll = LinkedList()
	for i in range(1, 11):
		ll.insert(i)
	
	ll.print()

	ll.delete(5)
	ll.print()

	ll = LinkedList()
	ll.insert(1)
	ll.print()
	ll.delete(1)
	ll.print()

	ll.delete(1)
	ll.print()