'''Bubble Sort
compairson-based algorithm in which each pair of adjacent elements is compared and the
elements are swapped if they are not in order.'''


def BubbleSort():

    #open file in "in read only mode" to read random numbers
    infile = open ("numbers.txt", "r")

    
    #for numIndex in range(len(infile)):
    numFile =  infile.read()
    #split massive singular string of numbers into list of singular numbers.
    numFile = numFile.split()

    print(numFile)
    

    for numIndex in range(len(numFile)-1):
        num = numFile[numIndex]
        numAfter = numFile[numIndex+1]

        if num > numAfter:

            num = numFile[numIndex+1]
            numAfter = numFile[numIndex]

    print(numFile)
    

    
            
        
        
        
        

        

        
    
        
        

        

        





    infile.close()

BubbleSort()
    

    
