#!/usr/bin/env python3

# to run: ./test.py -i BritishColombiaGirls_1922_2021.csv -y 1917 -o ontFemale_ 
import os
import sys
import getopt
import csv
import pandas as pd
 
def main ( argv ):

#
#   What does this section of the code do?
#
    if len(argv) < 6:
        print ( "Usage: ./names.py -i <input file name> -y <year> -o <output file name base>" )
        sys.exit(2)
    try:
        (opts, args) = getopt.getopt ( argv,"i:y:o:",["input=","year=","output="] )
    except getopt.GetoptError:
        print ( "Usage: ./names.py -i <input file name> -y <year> -o <output file name base>" )
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print ( "Usage: ./names.py -i <input file name> -y <year> -o <output file name base>" )
            sys.exit()
        elif opt in ( "-i", "--input"):
            inputFileName = arg
        elif opt in ("-y", "--year"):
            year = int(arg)
        elif opt in ("-o", "--output"):
            outputFileNameBase = arg
    outputFileName = outputFileNameBase+str(year)+".csv"

#
#   What is being declared here and why?
#
    names    = []
    numbers  = []
    ranks    = []
    total    = 0

#
#   What is the overall purpose of this section of code?
#
    with open ( inputFileName ) as csvDataFile:
        #
        # What does next do
        #
        next ( csvDataFile ) 
        csvReader = csv.reader(csvDataFile, delimiter=',')
        for row in csvReader:
            #
            # What is happening here?
            #   - include information about strip() and the purpose
            #     of newranks as opposed to ranks
            #
            if int(row[0]) == year :
                tempName = row[1].strip()
                names.append(tempName)
                numbers.append(int(row[2]))
                total = total + 1
                ranks.append(total)
        print ( "There are ",total," names in ",year )

        #
        #  Why could total == 0?
        #
        if total > 0 :
            people = {'Name':names,'Number':numbers}
            people_df = pd.DataFrame(people)
        
#
#           What is this doing?
#
            people_df.sort_values(["Number","Name"], axis = 0, ascending=[False,True], inplace=True)

            rankedPeople_df = people_df.assign(Rank=ranks)
            print ( rankedPeople_df )

#
#           What is this doing?
#
            rankedPeople_df.to_csv(outputFileName, sep=',', index=False, encoding='utf-8')

if __name__ == "__main__":
    main ( sys.argv[1:] )

#
#   End of names.py
#