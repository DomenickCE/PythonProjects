'''Bubble Sort
compairson-based algorithm in which each pair of adjacent elements is compared and the
elements are swapped if they are not in order.'''


def BubbleSort():

    #open file in "in read only mode" to read random numbers
    infile = open ("numbers.txt", "r")

    
    #for numIndex in range(len(infile)):
    numFile =  infile.read()
    #split large single string of numbers into list of singular numbers.
    numFile = numFile.split()
    
    #list before sorting
    print("before",numFile)


    #total number of passes/"bubbles"
    for FirstNum in range(len(numFile)):
        
        
        #number of iterations/checks per bubbles of comparison
        for NextNum in range(0, len(numFile)-FirstNum-1,1):

            #the int() function needs to be used to convert text file strings to int values to be compared.
            #main comparison to determine IF the bubbles needs to be swapped.
            if int(numFile[NextNum]) > int(numFile[NextNum+1]):
                print("before swap:",numFile[NextNum], numFile[NextNum+1])
                
                numFile[NextNum], numFile[NextNum+1] = numFile[NextNum+1], numFile[NextNum]

                print("after swap:",numFile[NextNum], numFile[NextNum+1])

    #list after sorting
    print("after",numFile)
    
    #close file after usage.
    infile.close()
    
            
BubbleSort()     
        
        
        

        

        
    
        
        

        

        






    

    
