
def lower(matrix, row, col):

	
	for i in range(0, row):
	
		for j in range(0, col):
		
			if (i < j):
			
				print("0", end = " ");
			
			else:
				print(matrix[i][j],
					end = " " );
		
		print(" ");
def upper(matrix, row, col):

	for i in range(0, row):
	
		for j in range(0, col):
		
			if (i > j):
				print("0", end = " ");
			
			else:
				print(matrix[i][j],
					end = " " );
		
		print(" ");
matrix = [[1, 2, 3],
		[4, 5, 6],
		[7, 8, 9]];
row = 3;
col = 3;
	
print("Lower triangular matrix: ");
lower(matrix, row, col);
	
print("Upper triangular matrix: ");
upper(matrix, row, col);

