
R= int(input("Enter the number of rows:"))
C = int(input("Enter the number of columns:")) 
  
# Initialize matrix 
matrix = [] 
print("Enter the entries rowwise:") 
  
# For user input 
for i in range(R):          # A for loop for row entries 
    a =[] 
    for j in range(C):      # A for loop for column entries 
         a.append(int(input())) 
    matrix.append(a) 
  
# For printing the matrix 
print("MATRIX\n")
for i in range(R): 
    for j in range(C): 
        print(matrix[i][j], end=" ") 
    print() 

#to read the row and col that has to be flipped
r1=int(input("enter the row no: "))
c1=int(input("enter the col no: "))

#to flip the elements of corresponding row and corresponding col
print("FLIPPED MATRIX")
for r in range(R):
	#print(1-a[r])
	for c in range(C):
		if(r==r1 or c== c1):
			print(1-matrix[r][c], end=" ")
		else:
			print(matrix[r][c], end=" ")
		
	print()
