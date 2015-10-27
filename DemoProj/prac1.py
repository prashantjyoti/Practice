# def take_out_digits(number):
#     list = []
#     for i in range(0, len(number)):
#         list.append(number[i])
#     return list
#
# def isPalindrome(number):
#     answer = False
#     digits = take_out_digits(number)
#     for i in range(0, len(digits)-1):
#         if ( digits[i] == digits[len(digits)-1-i] ) :
#             answer = True
#         else:
#             answer = False
#     return answer
#
# number = input("Enter a number: ")
# bool1 = isPalindrome(number)
# print (bool1)

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