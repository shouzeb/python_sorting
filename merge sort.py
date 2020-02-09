def mergeSort(arrayToSort):
    print("Splitting ",arrayToSort)
    if len(arrayToSort)>1:
        midOfArray = len(arrayToSort)//2
        lefthalfOfArray = arrayToSort[:midOfArray]
        righthalfOfArray = arrayToSort[midOfArray:]
        mergeSort(lefthalfOfArray)
        mergeSort(righthalfOfArray)
        i=j=k=0       
        while i < len(lefthalfOfArray) and j < len(righthalfOfArray):
            if lefthalfOfArray[i] < righthalfOfArray[j]:
                arrayToSort[k]=lefthalfOfArray[i]
                i=i+1
            else:
                arrayToSort[k]=righthalfOfArray[j]
                j=j+1
            k=k+1

        while i < len(lefthalfOfArray):
            arrayToSort[k]=lefthalfOfArray[i]
            i=i+1
            k=k+1

        while j < len(righthalfOfArray):
            arrayToSort[k]=righthalfOfArray[j]
            j=j+1
            k=k+1
    print("Merging ",arrayToSort)

 #unsorted array
arrayToSort = [14,46,43,27,57,41,45,21,70]
#to print sorted array
mergeSort(arrayToSort)
print(arrayToSort)