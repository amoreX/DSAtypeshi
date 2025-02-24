row=3
col=7
mat=[[0 for _ in range(col)] for _ in range(row)]

for i in range(row-1,-1,-1):
	for j in range(col-1,-1,-1):
		if (i+1) in range(row) and (j+1) in range(col):
			mat[i][j]=mat[i+1][j]+mat[i][j+1]
		elif (i+1) not in range (row) and (j+1) not in range(col):
			mat[i][j]=1
		elif (j+1) not in range (col):
			mat[i][j]=mat[i+1][j]+0
		else:
			mat[i][j]=mat[i][j+1]+0
			
print(mat)