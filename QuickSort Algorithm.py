# Program = QuickSort Algorithm
# Muhammad Nouman Butt
# (Github : https://github.com/Nouman0x45) (LinkedIn : https://www.linkedin.com/in/nouman0x45/)

# Necessary Variable
A = []

# This Function Will Take Input from the User.
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

def quickSort(A,low,high):
    if( low < high):
        # pi is partitioning index, arr[pi] is now
        # at right place 

        pi = partition(A, low, high)

        quickSort(A,low, pi -1)
        quickSort(A, pi + 1, high)

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
quickSort(A,0,len(A)-1)
print(A)