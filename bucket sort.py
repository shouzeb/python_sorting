# -*- coding: utf-8 -*-
"""
Created on Thu Feb  6 22:44:15 2020

@author: Shouzeb
"""

def bucket_sort(array):
    largest = max(array)
    length = len(array)
    size = largest/length
 
    buckets = [[] for _ in range(length)]
    for i in range(length):
        j = int(array[i]/size)
        if j != length:
            buckets[j].append(array[i])
        else:
            buckets[length - 1].append(array[i])
 
    for i in range(length):
        insertion_sort(buckets[i])
 
    result = []
    for i in range(length):
        result = result + buckets[i]
 
    return result
 
def insertion_sort(array):
    for i in range(1, len(array)):
        temp = array[i]
        j = i - 1
        while (j >= 0 and temp < array[j]):
            array[j + 1] = array[j]
            j = j - 1
        array[j + 1] = temp
 
 
array = input('Enter the list of (nonnegative) numbers: ').split()
array = [int(x) for x in array]
sorted_list = bucket_sort(array)
print('Sorted list: ', end='')
print(sorted_list)
