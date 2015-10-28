"""make a list
for any given number, find all the products, append them in a list
find max of list, store index of number and its max product(if greater than prev max)
in any direction in global variables """

#def initializeMatrix():
f = open('data_11.txt', 'r')
    #print (f)
    #for line in f:
    #print (line)
list_file_data = list(f)
    #print(list_file_data[0])
    #print(list_file_data)
    #str = list_file_data[0]
    # for i in range(len(list_file_data)):
    #     listA = list_file_data[i].split()
    #     print(listA)
    #     print(listA[0])
    #print (list_file_data[0].split())
    #print(len(abc))

    #[[0 for x in range(cols_count)] for x in range(rows_count)]
Matrix = [[0 for x in range(20)] for x in range(20)]

for i in range(20):
    list_numbers_in_a_line = list_file_data[i].split()
    for j in range(20):
        Matrix[i][j] = list_numbers_in_a_line[j]

    #print (Matrix)
#for i in range(20):
    #print(Matrix[i])

def hasLtoR(index1, index2):
    ret = True
    if index2>=17:
        ret = False
    return ret

def hasRtoL(index1, index2):
    ret = True
    if index2<=3:
        ret = False
    return ret

def hasUtoB(index1, index2):
    ret = True
    if index1>=17:
        ret = False
    return ret

def hasBtoU(index1, index2):
    ret = True
    if index1<3:
        ret = False
    return ret

def hasRightLowerDiag(index1, index2):
    ret = True
    if index1>16 or index2>16:
        ret = False
    return ret

def hasLeftUpperDiag(index1, index2):
    ret = True
    if index1<3 or index2<3:
        ret = False
    return ret

def hasLeftLowerDiag(index1, index2):
    ret = True
    if index1>16 or index2<3:
        ret = False
    return ret

def hasRightUpperDiag(index1, index2):
    ret = True
    if index1<3 or index2>16:
        ret = False
    return ret

def right_lower_diagonal_product(Matrix, index1, index2):
    if(hasRightLowerDiag(index1,index2)):
        product = 1
        j = index2
        for i in range(index1,index1+4):
            product *= int(Matrix[i][j])
            j += 1
        return product
    else:
        return 0

def right_upper_diagonal_product(Matrix, index1, index2):
    if(hasRightUpperDiag(index1,index2)):
        product =1
        j = index2
        for i in range(index1,index1-4,-1):
            product *= int(Matrix[i][j])
            j += 1
        return product
    else:
        return 0

def left_lower_diagonal_product(Matrix, index1, index2):
    if(hasLeftLowerDiag(index1,index2)):
        product = 1
        j = index2
        for i in range(index1,index1+4):
            product *= int(Matrix[i][j])
            j -= 1
        return product
    else:
        return 0

def left_upper_diagonal_product(Matrix, index1, index2):
    if(hasLeftUpperDiag(index1,index2)):
        product = 1
        j = index2
        for i in range(index1,index1-4,-1):
            product *= int(Matrix[i][j])
            j -= 1
        return product
    else:
        return 0

def LtoR_product(Matrix, index1, index2):
    if(hasLtoR(index1,index2)):
        product = 1
        for i in range(index2,index2+4):
            product *= int(Matrix[index1][i])
        return product
    else:
        return 0

def RtoL_product(Matrix, index1, index2):
    if(hasRtoL(index1,index2)):
        product = 1
        for i in range(index2,index2-4,-1):
            product *= int(Matrix[index1][i])
        return product
    else:
        return 0

def BtoU_product(Matrix, index1, index2):
    if(hasBtoU(index1,index2)):
        product = 1
        for i in range(index1,index1-4,-1):
            product *= int(Matrix[i][index2])
        return product
    else:
        return 0

def UtoB_product(Matrix, index1, index2):
    if(hasUtoB(index1,index2)):
        product = 1
        for i in range(index1,index1+4):
            product *= int(Matrix[i][index2])
        return product
    else:
        return 0

productList = []
for i in range(8):
    productList.append(0)
#print("pdl: ")
#print(productList)

ansList = []
for i in range(5):
    ansList.append(0)
#print("anl: ")
#print(ansList)

globalMax = 0

for i in range(len(Matrix)):
    for j in range(len(Matrix)):
        #print(Matrix)
        #print(i)
        #print(j)
        productList[0] = LtoR_product(Matrix,i,j)
        productList[1] = RtoL_product(Matrix,i,j)
        productList[2] = BtoU_product(Matrix,i,j)
        productList[3] = UtoB_product(Matrix,i,j)
        productList[4] = right_lower_diagonal_product(Matrix,i,j)
        productList[5] = right_upper_diagonal_product(Matrix,i,j)
        productList[6] = left_lower_diagonal_product(Matrix,i,j)
        productList[7] = left_upper_diagonal_product(Matrix,i,j)

        if(max(productList) > globalMax):
            globalMax = max(productList)
            ansList[0] = max(productList)
            ansList[1] = Matrix[i][j]
            ansList[2] = i
            ansList[3] = j
            ansList[4] = productList.index(globalMax)


#print("final step")
print (ansList)
