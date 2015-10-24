def take_out_digits(number):
    list_of_digits = []
    for i in range(0, len(number)):
        list_of_digits.append(number[i])
    return list_of_digits


#digits = []
#digits = take_out_digits(number)
    
def isPalindrome(number):
    """

    :type number: int
    """
    answer = 0
    digits = take_out_digits(str(number))
    for i in range(0, len(digits)-1):
        if ( digits[i] == digits[len(digits)-1-i] ) :
            answer = 1
        else:
            answer = 0
    return answer

def largest_palindrome(number):
    answer = 0
    result = number**2
    for i in range(result,10000,-1):
        if(isPalindrome(i)):
            answer = i
            break
        else:
            continue   
    return answer

largest_three_digit_number = input("Enter largest 3 digit number: ")
result = largest_palindrome(int(largest_three_digit_number))
print (result)

        
    
