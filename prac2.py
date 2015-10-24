def take_out_digits(number):
    list = []
    for i in range(0, len(number)):
        list.append(number[i])
    return list

number = input("Enter a number: ")
result = take_out_digits(number)
print (result)
