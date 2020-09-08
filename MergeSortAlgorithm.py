'''Mergesort is a comparison-based algorithm that focuses on how to merge together two pre-sorted arrays such that the mergedListulting array is also sorted.'''


def MergeSort(numFile):
    print("\n\nMERGE SORT\n")
    
    # Find the middle point and devide it
    middle = len(numFile) // 2

    #slices right half of list
    left_list = numFile[:middle]
    print("pre-sorted: left list:", left_list)

    #slices left half of list
    right_list = numFile[middle:]
    print("pre-sorted: right list:", right_list,"\n")

   
    left_list = HalfSort(left_list)
    right_list = HalfSort(right_list)
    print("sorted: left list:", left_list)
    print("sorted: right list:", right_list)


    HalvesMerge(left_list,right_list)

def HalfSort(listHalf):

    for t in range(len(listHalf)):
        
        for l in range(len(listHalf)-1):

            if int(listHalf[l]) > int(listHalf[l+1]):
                
                listHalf[l],listHalf[l+1] = listHalf[l+1],listHalf[l]
                
    return listHalf
            
def HalvesMerge(left_list,right_list):

    #mergedListulting list when lists are combined
    mergedList = []
    
    #loop conditional ensuring there are numbers in both halves before continueing
    while len(left_list) != 0 and len(right_list) != 0:
        
        #conditional checking if the left_list first indexed value is less than the right.
        #If so then number will be appended to the final list and removed from the left_list.
        if int(left_list[0]) < int(right_list[0]):
            
            mergedList.append(left_list[0])
            left_list.remove(left_list[0])
        #if the conditions above aren't met than appending and deletion will be pushed onto the right half.   
        else:
            mergedList.append(right_list[0])
            right_list.remove(right_list[0])


    print("\nMerged Sorted List:",mergedList,"\n")

if __name__ == '__main__':
    MergeSort()



