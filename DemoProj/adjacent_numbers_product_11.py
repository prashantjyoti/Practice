if 00 comes in any direction then dont multiiply in that direction

def right_lower_diagonal_product(index1, index2):
  return product
  
def right_upper_diagonal_product(index1, index2):
  return product
  
def left_lower_diagonal_product(index1, index2):
  return product
  
def left_lower_diagonal_product(index1, index2):
  return product
  
def acrossLtoR_product(index1, index2):
  return product
  
def acrossRtoL_product(index1, index2):
  return product
  
def horizontalBtoU_product(index1, index2):
  return product
  
def horizontalUtoB_product(index1, index2):
  return product

make a list
for any given number, find all the products, append them in a list
find max of list, store index of number and its max product(if greater than prev max) in any direction in global variables

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
#
for i in range(20):
    list_numbers_in_a_line = list_file_data[i].split()
    for j in range(20):
         Matrix[i][j] = list_numbers_in_a_line[j]

#print (Matrix)
for i in range(20):
    print(Matrix[i])
