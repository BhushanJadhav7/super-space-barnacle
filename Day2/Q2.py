#'A'is initialised array 
A=[]
#Number of elements to be added to the array be 'N'
N = int(input("Enter Number of elements to be added to the array: "))

for _ in range(N):
    #Elements to be added to the Array
    element = int(input("Enter Elements to be added to the Array: "))
    #Adding each element to the array
    A.append(element)
#Final Array Output
print("The Final Array is: ",A)


