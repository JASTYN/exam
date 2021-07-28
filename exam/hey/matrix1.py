# Python program for the above approach

# Initialize rows and columns
r, c = 0, 0;

# Store all 8 directions
dir = [[1, 0], [-1, 0], [0, 1], [0, -1],
	[-1, -1], [-1, 1], [1, 1], [1, -1]];

# Function to check if a cell
# (i, j) is valid or not
def valid(i, j):
	if (i >= 0 and j >= 0 and i < r and j < c):
		return True;

	return False;

# Function to find sum of adjacent cells
# for cell (i, j)
def find(i, j, v):

	# Initialize sum
	s = 0;

	# Visit all 8 directions
	for k in range(8):

		ni = i + dir[k][0];
		nj = j + dir[k][1];

		# Check if cell is valid
		if (valid(ni, nj)):
			s += v[ni][nj];

	# Return sum
	return s;

# Function to print sum of adjacent elements
def findsumofneighbors(M):

	# Stores the resultant matrix
	v = [[0 for i in range(c)] for j in range(r)];

	# Iterate each elements of matrix
	for i in range(r):
		for j in range(c):
		
			# Find adjacent sum
			v[i][j] = find(i, j, M);
			print(v[i][j], end=" ");

		print("");

# Driver code
if __name__ == '__main__':

	# Given matrix
	M = [[1, 4, 1], [2, 4, 5], [3, 1, 2]];

	# Size of matrix
	r = len(M[0]);
	c = len(M[1]);

	# Function call
	findsumofneighbors(M);

# This code is contributed by 29AjayKumar
