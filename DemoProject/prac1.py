def take_out_digits(number):
    list = []
    for i in range(0, len(number)):
        list.append(number[i])
    return list

def isPalindrome(number):
    answer = False
    digits = take_out_digits(number)
    for i in range(0, len(digits)-1):
        if ( digits[i] == digits[len(digits)-1-i] ) :
            answer = True
        else:
            answer = False
    return answer

number = input("Enter a number: ")
bool1 = isPalindrome(number)
print (bool1)
