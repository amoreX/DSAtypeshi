matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]


left,right=0,len(matrix)-1 

while left<right: # to go through every fucking shit in a layer untill left and right are the same
    for i in range(right-left): # to actually iterate over every fuckign element in a layer
        top,bottom=left,right #since square matrix so top and bottom are the same as left and right indexes
        
        
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
