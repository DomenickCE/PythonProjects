'''where the sorting algorithms are imported and executed'''

from BubbleSortAlgorithm import BubbleSort

def main():

    #open file in "in read only mode" to read random numbers
    infile = open ("numbers.txt", "r")

    
    #for numIndex in range(len(infile)):
    numFile =  infile.read()
    #split large single string of numbers into list of singular numbers.
    numFile = numFile.split()
    
    #list before sorting
    print("Before Sort:",numFile,"\n")


    BubbleSort(numFile)

    

    

    



main()
