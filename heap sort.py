# -*- coding: utf-8 -*-
"""
Created on Mon Feb 10 21:58:50 2020

@author: Shouzeb
"""


# heap Sort In Python

def heap_sort(arr, n, i):
    # Find largest among root and children
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2 
 
    if l < n and arr[i] < arr[l]:
        largest = l
 
    if r < n and arr[largest] < arr[r]:
        largest = r
 
    # If root is not largest, swap with largest and continue heapifying
    if largest != i:
        arr[i],arr[largest] = arr[largest],arr[i]
        heap_sort(arr, n, largest)
 
def heapSort(arr):
    n = len(arr)
 
    # Build max heap
    for i in range(n, 0, -1):
        heap_sort(arr, n, i)
 
    
    for i in range(n-1, 0, -1):
        # swap
        arr[i], arr[0] = arr[0], arr[i]  
        
        #heap_sort root element
        heap_sort(arr, i, 0)
 #unsorted array
arr = [ 12, 11, 13, 5, 6, 7]
print("Unsorted array is",arr)
heapSort(arr)
n = len(arr)
#sorted array
print ("Sorted array is",arr)