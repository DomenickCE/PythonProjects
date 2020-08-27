'''Bubble Sort
compairson-based algorithm in which each pair of adjacent elements is compared and the
elements are swapped if they are not in order.'''


def BubbleSort(numFile):


    #total number of passes/"bubbles"
    for FirstNum in range(len(numFile)):
        
        
        #number of iterations/checks per bubbles of comparison
        for NextNum in range(0, len(numFile)-FirstNum-1,1):

            #the int() function needs to be used to convert text file strings to int values to be compared.
            #main comparison to determine IF the bubbles needs to be swapped.
            if int(numFile[NextNum]) > int(numFile[NextNum+1]):
                
                
                numFile[NextNum], numFile[NextNum+1] = numFile[NextNum+1], numFile[NextNum]


    #list after sorting
    print("After Sort:",numFile)
    

if __name__ == '__main__':
    BubbleSort()     
        
        
        

        

        
    
        
        

        

        






    

    
