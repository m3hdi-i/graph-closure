#
#	a simple pyhton script to calculate the Closure of a graph
#
#	Author : Mehdi I.
#

def get_degree_of_node(mat,n):
	d=0
	for row in mat:
		d=d+row[n]
	return d


def get_closure(adj_matrix,lenght):
	mat=adj_matrix
	changes=0
	for i in range(lenght):
		for j in range(i,lenght):
			if i!=j:
				if mat[i][j]!=1:
					d1=get_degree_of_node(mat,i)
					d2=get_degree_of_node(mat,j)
					print(f"node {i + 1} and node {j + 1} :  {d1}+{d2} >= {lenght} , Connecting node {i + 1} and {j + 1}")
					if d1+d2>=lenght:
						print(f"node {i+1} and node {j+1} :  {d1}+{d2} >= {lenght} , Connecting node {i+1} and {j+1}")
						mat[i][j]=1
						mat[j][i]=1
						changes+=1

	if changes==0:
		return mat
	else:
		return get_closure(mat,lenght)


if __name__ == '__main__':

	# adjacency_matrix = [
	# 	[0, 1, 1, 0, 1, 0],
	# 	[1, 0, 0, 1, 0, 1],
	# 	[1, 0, 0, 1, 1, 0],
	# 	[0, 1, 1, 0, 0, 1],
	# 	[1, 0, 1, 0, 0, 0],
	# 	[0, 1, 0, 1, 0, 0],
	# ]

	adjacency_matrix = []

	# Specifying adjacency matrix of graph
	nodes_count = int(input("Enter your graph's nodes count : "))
	for i in range(nodes_count):
		row = []
		print('Enter values for row ' + str(i + 1) + ' of adjacency matrix : ')
		for j in range(nodes_count):
			row.append(int(input()))

		adjacency_matrix.append(row)


	print('\n Your Adjacency Matrix : \n')
	for r in adjacency_matrix:
		print(" ".join(map(str, r)))

	print("----------")

	cl=get_closure(adjacency_matrix,len(adjacency_matrix))
	print("\n Closure graph's Adjacency matrix : \n")
	for r in cl:
		print(" ".join(map(str, r)))
