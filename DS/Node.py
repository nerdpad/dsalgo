class Node:
	""" A class representing a single node in a linked list """

	def __init__(self, value):
		""" Initlizes a new node """
		self.data = value
		self.next = None
		self.prev = None
