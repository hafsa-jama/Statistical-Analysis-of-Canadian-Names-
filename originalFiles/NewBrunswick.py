#!/usr/bin/env python3

#   Author: Ayomide Awofisayo
#   Date of last update:jan 20 2023 

# Libraries
import os
import sys
import getopt
import csv
import pandas as pd
 
def main ( argv ):

# checks that the appropiate files have been used to run this program - gives appropiate errors responses

    if len(argv) < 6:
        print ( "Usage: ./names.py -i <input file name> -g <gender> -o <output file name base>" )
        sys.exit(2)
    try:
        (opts, args) = getopt.getopt ( argv,"i:g:o:",["input=","gender=","output="] )
    except getopt.GetoptError:
        print ( "Usage: ./names.py -i <input file name> -g <gender> -o <output file name base>" )
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print ( "Usage: ./names.py -i <input file name> -g <gender> -o <output file name base>" )
            sys.exit()
        elif opt in ( "-i", "--input"):
            inputFileName = arg
        elif opt in ("-g", "--gender"):
            gender = arg
        elif opt in ("-o", "--output"):
            outputFileNameBase = arg
    outputFileName = outputFileNameBase + gender +".csv"

#   declares varriables
#   What is being declared here and why?
#
    names    = []
    numbers  = []
    ranks    = []
    year     = []
    total    = 0

#   opens file and reads lines from it and prints orderd names
#
    with open ( inputFileName ) as csvDataFile:

        # returns next item
        #gender = "M"

        next ( csvDataFile ) 
        csvReader = csv.reader(csvDataFile, delimiter=',')
        for row in csvReader:
            #    counts number of lines and removes new line from read text and appends it arrays
            # goes through one year at a time
            

            if (row[1] == gender) :
                tempName = row[2].strip()
                names.append(tempName)
                numbers.append(int(row[3]))
                year.append(int(row[0]))
                total = total + 1
                ranks.append(total)
        print ( "There are ",total," names in ",gender )

        # total could = 0 if file is empty or the chosen year dosent have recorded data
        #  Why could total == 0?     
        if total > 0 :
            people = {'Year':year,'Name':names,'Count':numbers}
            people_df = pd.DataFrame(people)
        
# sorts in assending order of number then decending alpha order
#           What is this doing?
# prints the ranked list of names
#            people_df.sort_values(["Number","Name"], axis = 0, ascending=[False,True], inplace=True)

            rankedPeople_df = people_df.assign(Rank=ranks)
           # print ( rankedPeople_df )
            #rankedPeople_df = rankedPeople_df.set_index("Rank")
            rankedPeople_df = rankedPeople_df.loc[:, ["Year", "Name", "Count", "Rank"]]
            print(rankedPeople_df[["Year","Name","Count", "Rank"]])
# says its a utf based file - default string length- row names not written
#           What is this doing?
# runs main
            rankedPeople_df.to_csv(outputFileName, sep=',', index=False, encoding='utf-8')

if __name__ == "__main__":
    main ( sys.argv[1:] )

#
#   End of names.py
#
