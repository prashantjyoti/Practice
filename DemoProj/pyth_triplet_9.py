__author__ = 'Prashant'

from math import sqrt

def findPythTriplet(list):
    pythTripletList = []
    for i in range(len(list)):
        for j in range(i,len(list)):
            k = list[i] + list[j]
            for x in range(j,len(list)):
                if k==list[x]:
                    val1 = int(sqrt(k))
                    val2 = int(sqrt(list[i]))
                    val3 = int(sqrt(list[j]))
                    #print(val2,val3,val1)
                    if(val1+val2+val3==1000):
                        pythTripletList.append(val2)
                        pythTripletList.append(val3)
                        pythTripletList.append(val1)

    return pythTripletList

def isPerfectSquare(number):
    if sqrt(number) == int(sqrt(number)):
        return True
    return False

perfectSquaresList =[]

for i in range(1,1000**2):
    if isPerfectSquare(i):
        perfectSquaresList.append(i)

print (perfectSquaresList)
print (findPythTriplet(perfectSquaresList))



