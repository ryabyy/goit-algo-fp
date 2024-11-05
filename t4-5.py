import uuid
import networkx as nx
import matplotlib.pyplot as plt
from collections import deque

class Node:
	def __init__(self, key, color="skyblue"):
		self.left = None
		self.right = None
		self.val = key
		self.color = color
		self.id = str(uuid.uuid4())

def add_edges(graph, node, pos, x=0, y=0, layer=1):
	if node is not None:
		graph.add_node(node.id, color=node.color, label=node.val)
		if node.left:
			graph.add_edge(node.id, node.left.id)
			l = x - 1 / 2 ** layer
			pos[node.left.id] = (l, y - 1)
			l = add_edges(graph, node.left, pos, x=l, y=y - 1, layer=layer + 1)
		if node.right:
			graph.add_edge(node.id, node.right.id)
			r = x + 1 / 2 ** layer
			pos[node.right.id] = (r, y - 1)
			r = add_edges(graph, node.right, pos, x=r, y=y - 1, layer=layer + 1)
	return graph

def draw_tree(tree_root):
	tree = nx.DiGraph()
	pos = {tree_root.id: (0, 0)}
	tree = add_edges(tree, tree_root, pos)

	colors = [node[1]['color'] for node in tree.nodes(data=True)]
	labels = {node[0]: node[1]['label'] for node in tree.nodes(data=True)}

	plt.figure(figsize=(8, 5))
	nx.draw(tree, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=colors)
	plt.show()

root = Node(0)
root.left = Node(4)
root.left.left = Node(5)
root.left.right = Node(10)
root.right = Node(1)
root.right.left = Node(3)

draw_tree(root)

def insert(root, key):
	if root is None:
		return Node(key)
	else:
		if key < root.val:
			root.left = insert(root.left, key)
		else:
			root.right = insert(root.right, key)
	return root

def make_tree(root):
	if root is None:
		return None

	new_root = None

	queue = deque([root])

	while queue:
		current = queue.popleft()
		new_root = insert(new_root, current.val)

		if current.left:
			queue.append(current.left)
		if current.right:
			queue.append(current.right)

	return new_root

bst = make_tree(root)
draw_tree(bst)

def bfs_traversal(root, total=None):
	if root is None:
		return None
	count = 0

	queue = deque([root])
	while queue:
		node = queue.popleft()
		count += 1
		print(node.val)
		if total is not None and total > 0:
			color_part = hex(50 + count * (150 // total))[2:].zfill(2)
			node.color = '#' + color_part * 3
		if node.left:
			queue.append(node.left)
		if node.right:
			queue.append(node.right)
	return count

def dfs_traversal(root, total=None):
	if root is None:
		return None
	count = 0

	stack = deque([root])
	while stack:
		node = stack.pop()
		count += 1
		print(node.val)
		if total is not None and total > 0:
			color_part = hex(50 + count * (150 // total))[2:].zfill(2)
			node.color = '#' + color_part * 3
		if node.right:
			stack.append(node.right)
		if node.left:
			stack.append(node.left)
	return count

count = bfs_traversal(bst)
if count is not None:
	print('BFS:')
	bfs_traversal(bst, count)
	draw_tree(bst)

	print('DFS:')
	dfs_traversal(bst, count)
	draw_tree(bst)
