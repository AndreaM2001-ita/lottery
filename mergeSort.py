"""
File: testMergeSort.py

Tests the Merge sort algorithm
"""
def mergeSort(lyst):
    # lyst            list to be sorted
    # copyBuffer      temporary space needed during merge

    copyBuffer = [None]*(len(lyst))
    lyst=mergeSortHelper(lyst, copyBuffer, 0, len(lyst)-1)
    return lyst

def mergeSortHelper(lyst, copyBuffer, low, high):
    # lyst            list to be sorted
    # copyBuffer      temporary space needed during merge
    # high, low       bounds of sublist
    # middle          midpoint of sublist
    if low <high:
        middle = (low+high)//2
 
        mergeSortHelper(lyst, copyBuffer, low, middle)

        mergeSortHelper(lyst, copyBuffer, middle+1, high)

        lyst=merge(lyst, copyBuffer, low, middle, high)
 
    return lyst

def merge(lyst, copyBuffer, low, middle, high):
    # lyst            list to be sorted
    # copyBuffer      temporary space needed during merge
    # low             beginning of 1st sorted sublist
    # middle          end of 1st sorted sublist
    # middle +1       beginning of 2nd sorted sublist
    # high            end of 2nd sorted sublist

    #initialize i1 and i2 to the 1st items in each sublist
    i1=low
    i2=middle+1
    #interleave  items from the sublists into the
    #copyBuffer in such a way that order is maintained.
    for i in range(low, high+1):
        if i1>middle:
            copyBuffer[i]=lyst[i2] # 1st sublist exhausted
            i2 +=1
        elif i2>high:
            copyBuffer[i] = lyst[i1] # 2nd sublist exhausted
            i1 +=1
        elif lyst[i1]<lyst[i2]:
            copyBuffer[i] = lyst[i1] # item in 1st sublist
            i1 +=1            
        else:                 # lyst[i1]>=lyst[i2]
            copyBuffer[i] = lyst[i2] # item in 2nd sublist  
            i2 +=1
    for i in range(low, high+1):     # copy sorted items back to         
        lyst[i] = copyBuffer[i]      # proer position in lyst
    return lyst