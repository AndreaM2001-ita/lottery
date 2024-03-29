"""
File: testSelectionSort.py

Tests the Selection sort algorithm
"""

def selectionSort(lyst):
    i=0
    while i<len(lyst)-1:     # Do n-1 search
        minIndex=i           # index: for the smallest
        j=i+1
        while j<len(lyst):   # start search 
            if lyst[j]<lyst[minIndex]:
                minIndex = j
            j += 1;
        if minIndex != i:
            swap(lyst, minIndex, i)
        i += 1
    return lyst
       

def swap(lyst, i, j):
    """Exchanges the items at positions i and j."""
    # You could say lyst[i], lyst[j] = lyst[j], lyst[i]
    # but the following code shows what is really going on
    temp = lyst[i]
    lyst[i] = lyst[j]
    lyst[j] = temp
