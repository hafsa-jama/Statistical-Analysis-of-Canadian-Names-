#!/usr/bin/env python3

import os
import sys
import getopt
import csv
import pandas as pd
from Function_file import *
 
def main ( argv ):

    if len(argv) < 1:
        print ( "Usage: ./NovaScotia.py -i <input file name>" )
        sys.exit(2)
    try:
        (opts, args) = getopt.getopt ( argv,"i:",["input="] )
    except getopt.GetoptError:
        print ( "Usage: ./NovaScotia.py -i <input file name>" )
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print ( "Usage: ./NovaScotia.py -i <input file name>" )
            sys.exit()
        elif opt in ( "-i", "--input"):
            inputFileName = arg
    outputFileName = "NovaScotia_F.csv"

    names    = []
    count  = []
    ranks    = []
    years    = []
    total = 0

    with open ( inputFileName ) as csvDataFile:
        next ( csvDataFile ) 
        csvReader = csv.reader(csvDataFile, delimiter=',')
        for row in csvReader:
            if (row[1]) == 'F' :
                years.append(int(row[0]))

                tempName = row[2].strip()
                tempName = tempName.lower()
                tempName = tempName.upper()
                names.append(tempName)

                count.append(int(row[3]))

                total = total + 1
                ranks.append(total)

        if total > 0 :
            people = {'Year':years,'Name':names,'Count':count}
            people_df = pd.DataFrame(people)
            people_df.sort_values(["Count","Name"], axis = 0, ascending=[False,True], inplace=True)

            rankedPeople_df = people_df.assign(Rank=ranks)
            rankedPeople_df = rankedPeople_df.loc[:, ["Year", "Name", "Count", "Rank"]]

            rankedPeople_df.to_csv(outputFileName, sep=',', index=False, encoding='utf-8')        

if __name__ == "__main__":
    main ( sys.argv[1:] )