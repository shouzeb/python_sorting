# -*- coding: utf-8 -*-
"""
Created on Wed Feb  5 21:55:27 2020

@author: Shouzeb
"""

def partitionOfArray(array, beginPoint, endPoint):
    pivotPoint = beginPoint
    for i in range(beginPoint+1, endPoint+1):
        if array[i] <= array[beginPoint]:
            pivotPoint += 1
            array[i], array[pivotPoint] = array[pivotPoint], array[i]
    array[pivotPoint], array[beginPoint] = array[beginPoint], array[pivotPoint]
    return pivotPoint



def quicksortOfArray(array, beginPoint=0, endPoint=None):
    if endPoint is None:
        endPoint = len(array) - 1
    def _quicksort(array, beginPoint, endPoint):
        if beginPoint >= endPoint:
            return
        pivotPoint = partitionOfArray(array, beginPoint, endPoint)
        _quicksort(array, beginPoint, pivotPoint-1)
        _quicksort(array, pivotPoint+1, endPoint)
    return _quicksort(array, beginPoint, endPoint)

 #unsorted array
array = [97, 200, 100, 101, 211, 107]
#to print sorted array
quicksortOfArray(array)
print(array)