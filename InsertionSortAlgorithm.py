
def InsertionSort(numFile):

    for i in range(len(numFile)):
        
        #target value to be sorted in the correct position.
        tarVal= int(numFile[i])
        print("Target Value to be sorted:", tarVal)

        # Move elements of numFile[0..i-1], that are 
        # greater than tarVal, to one position ahead 
        # of their current position
        
        precI = i-1
        while precI >=0 and tarVal < int(numFile[precI]):
            print("The value following the Target Value:", numFile[precI], "is", numFile[precI+1])
            numFile[precI+1] = numFile[precI]
            precI -= 1 #precI - 1 = precI
            numFile[precI+1] = tarVal 
  
  
    # Driver code to test above 
    print ("Sorted numFile is: [ ",end="") 
    for i in range(len(numFile)): 
        print(numFile[i],",",end="")
    print("]")

if __name__ == '__main__':
    InsertionSort()     
        



