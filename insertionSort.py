"""
File: testInsertionSort.py

Tests the Insertion sort algorithm
"""

def insertionSort(lyst):
    i=1                               # starting point to be inserted
    while i<len(lyst):                # Do n-1 insertion
        itemToInsert = lyst[i]  
        j=i-1
        while j>=0:                   # start search
            if itemToInsert <lyst[j]:
                lyst[j+1] = lyst[j]   #Shift right
                j -= 1
            else:
                break                 # found a index to insert 
        lyst[j+1]= itemToInsert       # insert  
        i += 1

    return lyst