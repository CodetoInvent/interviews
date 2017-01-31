import numpy

matrix = numpy.random.random_integers(0, 10, (3, 3))
print matrix


top = 0
right = len(matrix)-1
bottom = len(matrix[0])-1
left = 0

while top <= bottom and left <= right:

    for i in range(left, right+1):
        print matrix[top][i]
    top += 1

    for i in range(top, bottom+1):
        print matrix[i][right]
    right -= 1

    for i in range(right, left-1, -1):
        print matrix[bottom][i]
    bottom -= 1

    for i in range(bottom, top-1, -1):
        print matrix[i][left]        
    left += 1



