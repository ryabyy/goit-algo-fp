class Node:
	def __init__(self, data=None):
		self.data = data
		self.next = None

class LinkedList:
	def __init__(self):
		self.head = None

	def insert_at_beginning(self, data):
		new_node = Node(data)
		new_node.next = self.head
		self.head = new_node

	def insert_at_end(self, data):
		new_node = Node(data)
		if self.head is None:
			self.head = new_node
		else:
			cur = self.head
			while cur.next:
				cur = cur.next
			cur.next = new_node

	def insert_after(self, prev_node: Node, data):
		if prev_node is None:
			print("Previous node does not exist.")
			return
		new_node = Node(data)
		new_node.next = prev_node.next
		prev_node.next = new_node

	def delete_node(self, key: int):
		cur = self.head
		if cur and cur.data == key:
			self.head = cur.next
			cur = None
			return
		prev = None
		while cur and cur.data != key:
			prev = cur
			cur = cur.next
		if cur is None:
			return
		prev.next = cur.next
		cur = None

	def search_element(self, data: int) -> Node | None:
		cur = self.head
		while cur:
			if cur.data == data:
				return cur
			cur = cur.next
		return None

	def print_list(self):
		current = self.head
		while current:
			print(current.data)
			current = current.next

	def insertion_sort(self):
		if not self.head or not self.head.next:
			return

		sorted_list = None

		current = self.head

		while current:
			next_node = current.next

			if not sorted_list or sorted_list.data >= current.data:
				current.next = sorted_list
				sorted_list = current
			else:
				sorted_current = sorted_list
				while sorted_current.next and sorted_current.next.data < current.data:
					sorted_current = sorted_current.next

				current.next = sorted_current.next
				sorted_current.next = current

			current = next_node

		self.head = sorted_list

def reverse_linked_list(linked_list):
	if linked_list.head is not None:
		previous = None
		current = linked_list.head
		while current is not None:
			next_node = current.next
			current.next = previous
			previous = current
			current = next_node
		linked_list.head = previous

def merge_sorted_lists(list1, list2):
	dummy_head = Node(0)

	current = dummy_head

	head1 = list1.head
	head2 = list2.head

	while head1 and head2:
		if head1.data <= head2.data:
			current.next = head1
			head1 = head1.next
		else:
			current.next = head2
			head2 = head2.next
		current = current.next

	if head1:
		current.next = head1
	else:
		current.next = head2

	merged_list = LinkedList()
	merged_list.head = dummy_head.next
	return merged_list

llist = LinkedList()

llist.insert_at_beginning(5)
llist.insert_at_beginning(10)
llist.insert_at_beginning(15)

llist.insert_at_end(20)
llist.insert_at_end(25)

llist.delete_node(10)

llist.print_list()


reverse_linked_list(llist)
llist.print_list()

llist.insertion_sort()
llist.print_list()

llist1 = LinkedList()

llist1.insert_at_beginning(7)
llist1.insert_at_beginning(13)
llist1.insert_at_beginning(9)

llist1.insertion_sort()
llist1.print_list()

c_list = merge_sorted_lists(llist, llist1)
c_list.print_list()