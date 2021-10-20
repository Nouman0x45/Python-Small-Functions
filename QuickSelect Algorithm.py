# Program = Find the required Smallest Element using QuickSort.
# Muhammad Nouman Butt
# (Github : https://github.com/Nouman0x45) (LinkedIn : https://www.linkedin.com/in/nouman0x45/)

# Necessary Variable
A = []

def input_func(A):
    size = int(input("Enter the Array Size: "))
    j = 0
    while j < size:
        temp = input("Enter " + str( j + 1 ) + " number: ")
        try:
            x = int(temp)
            A.append(x)
            j = j+1
        except:
            print("In-Valid Input")

def quickSelect(A,left,right,k):
    
    # If left index is equal to right means There is only 1 
    # element passed in this function adn we will just return it
    if left == right:
        return A[left]

    pivotIndex = partition(A,left,right) # find pivot point

    # if k is equal to pivot means Number is found
    if k == pivotIndex:
        return A[k]

    # if k is less than pivotIndex means Kth number is present is left Partition                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      c
    elif k < pivotIndex:
        right = pivotIndex - 1
        return quickSelect(A,left,right,k)

    # if k is less than pivotIndex means Kth number is present is right Partition
    else:
        left = pivotIndex + 1
        return quickSelect(A,left,right,k)

def partition(A,low,high):

    # pivot (Element to be placed at right position)
    pivot = A[high]

    i = (low - 1) # Index of smaller element and indicates the
                  # right position of pivot found so far

    # If current element is smaller than the pivot
    for j in range(low,high):
        if(A[j] < pivot):
            i += 1              # increment index of smaller element
            A[i], A[j] = A[j], A[i]
    
    A[i+1], A[high] = A[high], A[i+1]
    return (i+1)

input_func(A)
print(A)
k = int(input("Enter k Value: "))
B = quickSelect(A,0,len(A)-1,k -1)
print(B)