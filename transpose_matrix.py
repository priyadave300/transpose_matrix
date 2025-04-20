##here we can 2 ways transpose one is by creating another matrix by copying all elements of old mtatrix
##then just assign temp[i][j] with matrix[j][i] by transversing through for loop for row and col
def transpose1(matrix: list):
    temp =  [item[:] for item in matrix]
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            temp[i][j] = matrix[j][i]
    return temp

##another way is transversing through for loop for row and then running j for col from i so that previous
##elements are not changed and then using temp first assigning it with matrix[i][j] then matrix[i][j] equals
##matrix[j][i] then matrix[j][i] by temp and then printing matrix

def transpose(matrix: list):
    for i in range(len(matrix)):
        for j in range(i,len(matrix[i])):
            temp_var = matrix[i][j]
            matrix[i][j]= matrix[j][i]
            matrix[j][i] = temp_var
    print(matrix)

if __name__ == "__main__":
    matrix = [[1,2,3],[4,5,6],[7,8,9]]
    transpose(matrix)





