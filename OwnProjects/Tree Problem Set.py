#  1) Write following functions body. A nested dictionary is passed as parameter. You need to
#  print all keys with their depth.
#  Sample Input:
d = {
	'key1': 1,
	'key2': {
			'key3': 1,
			'key4': {
					'key5': 4
					}
			}
	}

# Sample Output:
# key1 1
# key2 1
# key3 2
# key4 2
# key5 3

def print_depth(data):
	#  Write function body
	pass
	
	
# print_depth(data)

# You may write additional function.
# 2) Write following functions body. 2 Nodes are passed as parameter. You need to find Least
# Common Ancestor and print its value. Node structure are as following:

# class Node{
# 	value;
# 	parent;
# 	}

# Ancestor Definition:
# 1) Any node falls under parent chain till root node.
# 2) A node is ancestor of itself.
# For example: if we consider Node 7 it’s ancestors will be 1, 3, and 7.
# All nodes values are unique for this tree.
# You function needs to find least common ancestor (closest common ancestor).

def lca(node1, node2):
	#  Write function body
	pass
# You may write additional function.
# # Explain Runtime and Memory requirement for your solution.