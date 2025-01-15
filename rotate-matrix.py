matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]


left,right=0,len(matrix)-1 #square matrix

while left<right:
    for i in range(right-left):
        top,bottom=left,right
        
        # print(top,bottom,i)
        topleft=matrix[top][left+i]
        
        #bottom left to top left
        matrix[top][left+i]=matrix[bottom-i][left]

        #bottom right to bottom left
        matrix[bottom-i][left]=matrix[bottom][right-i]
        
        #top right to bottom right
        matrix[bottom][right-i]=matrix[top+i][right]
        
        #top left to top right
        matrix[top+i][right]=topleft
    print(matrix)
    left+=1
    right-=1 

print(matrix)
