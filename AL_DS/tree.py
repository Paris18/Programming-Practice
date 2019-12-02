class NewNode:
	def __init__(self,val):
		self.left = None
		self.right = None
		self.val = val


def preorder(root):
	if root:
		print (root.val,end=" ")
		preorder(root.left)
		preorder(root.right)


def inorder(root):
	if root:
		inorder(root.left)
		print (root.val,end=" ")
		inorder(root.right)

def postorder(root):
	if root:
		postorder(root.left)
		postorder(root.right)
		print (root.val,end=" ")


def rightview(root,current_node,max_node):
	if root:
		if(current_node > max_node):
			print(root.val,end=" ")
			# print(root.val,current_node,max_node)
			max_node = current_node
		max_node = rightview(root.right,current_node+1,max_node)
		max_node = rightview(root.left,current_node+1,max_node)
	return max_node

def leftview(root,current_node,max_node):
	if root:
		if(current_node > max_node):
			print(root.val,end=" ")
			# print(root.val,current_node,max_node)
			max_node = current_node
		max_node = leftview(root.left,current_node+1,max_node)
		max_node = leftview(root.right,current_node+1,max_node)
	return max_node

def topvie(root):
	if root:
		print (root.val,end=" ")
		right_root = root.right
		while(right_root):
			print (right_root.val,end=" ")
			right_root = right_root.right

		left_root = root.left
		while(left_root):
			print (left_root.val,end=" ")
			left_root = left_root.left
	return 


def bfs(root):
	if not root:
		print ("No Nodes")
		return

	queue = []
	queue.append(root)

	while(len(queue) > 0):
		print(queue[0].val,end=" ")
		node = queue.pop(0)
		if node.left:
			queue.append(node.left)
		if node.right:
			queue.append(node.right)


def inorder_norecursion(root):

	stack = []
	current = root

	while True:
		if current:
			stack.append(current)
			current = current.left
		elif stack:
			data = stack.pop()
			print(data.val,end=" ")
			current = data.right
		else:
			break


def depth_node_print(root,d):
	if root:
		left_depth = depth_node_print(root.left,d)+1
		right_depth = depth_node_print(root.right,d)+1
		current_depth = max(left_depth,right_depth)
		if(current_depth == d):
			print (root.val,end=" ")
		return current_depth
	else:
		return -1

	

root = NewNode(1)
root.left = NewNode(2)
root.left.left = NewNode(3)
root.left.left.left = NewNode(8)
root.left.left.right = NewNode(10)
root.left.left.right.right = NewNode(11)
root.right = NewNode(4)
root.right.left = NewNode(5)
root.left.left.right.left = NewNode(5)
root.right.left.right = NewNode(9)
root.right.right = NewNode(6)

'''        
						   (1)
						   / \
						  /   \
						(2)   (4)
						/     / \
					   /     /   \
					 (3)    (5)  (6)
					 / \     \
					/   \     \
				  (8)   (10)  (9)
							\
							 \
							 (11)
				   
				   '''

print("\n\nPreorder")
preorder(root)

print("\n\npostorder")
postorder(root)

print ("\n\ninorder")
inorder(root)

print ("\n\ninorder norecursion")
inorder_norecursion(root)

print("\n\nRight View")
rightview(root,1,0)

print("\n\nleft view")
leftview(root,1,0)

print("\n\ntop View")
topvie(root)

print("\n\nbfs View")
bfs(root)

print("\nDepth print")
depth_node_print(root,1)
