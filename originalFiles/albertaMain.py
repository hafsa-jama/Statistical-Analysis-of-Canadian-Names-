#! /usr/bin/env python3
import os
import sys
import getopt
import csv
import pandas as pd
from Function_file import *

def main ( argv ):

#checks that imputs exist and turns them into varriables
    if len(argv) < 3:
        print ( "Usage: ./names.py -i <input file name> -j <file2> " )
        sys.exit(2)
    try:
        (opts, args) = getopt.getopt ( argv,"i:j:",["input=","input2="] )
    except getopt.GetoptError:
        print ( "Usage: ./names.py -i <input file name> -j <file2>  ")
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print ( "Usage: ./names.py -i <input file name> -j <file2> ")
            sys.exit()
        elif opt in ( "-i", "--input"):
            inputFileName = arg
        elif opt in ("-j", "--file2"):
            file2 = arg

#   declares varriables#   What is being declared here and why?
#
    names    = []
    numbers  = []
    ranks    = []
    year     = []
    total    = 0

    namesf    = []
    numbersf  = []
    ranksf    = []
    yearf     = []
    totalf    = 0
#   opens file and reads line by line from it 
#   
    with open ( inputFileName ) as csvDataFile:
        next ( csvDataFile )
        csvReader = csv.reader(csvDataFile, delimiter=',')
        for row in csvReader:
            #    counts number of lines and removes new line from read text and appends it to arrays sepreatly tor male and female
            if row[3] == "Boy":
                ranks.append(int (row[0]))
                tempName = row[1].strip()
                tempName = tempName.upper()
                names.append(tempName)
                numbers.append(int(row[2]))
                year.append(int(row[4]))
                total = total + 1
            if row[3] == "Girl":
                ranksf.append(int (row[0]))
                tempName = row[1].strip()
                tempName = tempName.upper()
                namesf.append(tempName)
                numbersf.append(int(row[2]))
                yearf.append(int(row[4]))
                totalf = totalf + 1

        #opens and reads second file
        with open ( file2 ) as csvDataFile2:
            next ( csvDataFile2 )
            csvReader2 = csv.reader(csvDataFile2, delimiter=',')
            for row in csvReader2:
                #counts entries removes \n and appends to arrays sepreately for male and female
                if row[3] == "Boy":
                    ranks.append(int (row[0]))
                    tempName = row[1].strip()
                    tempName = tempName.upper()
                    names.append(tempName)
                    numbers.append(int(row[2]))
                    year.append(int(row[4]))
                    total = total + 1
                if row[3] == "Girl":
                    ranksf.append(int (row[0]))
                    tempName = row[1].strip()
                    tempName = tempName.upper()
                    namesf.append(tempName)
                    numbersf.append(int(row[2]))
                    yearf.append(int(row[4]))
                    totalf = totalf + 1



        # if total > 0 gather data into a df :
            if total > 0 :
                people = {'Year':year,'Name':names,'Number':numbers,'Rank':ranks}
                people_df = pd.DataFrame(people)
            
            if totalf > 0 :
                peoplef = {'Year':yearf,'Name':namesf,'Number':numbersf,'Rank':ranksf}
                peoplef_df = pd.DataFrame(peoplef)

            #topGender (people_df, peoplef_df, 2015)  
            top10All (people_df, peoplef_df, 2005)  


            
#           turns df into csv
            people_df.to_csv("alberta_M.csv", sep=',', index=False, encoding='utf-8')
            peoplef_df.to_csv("alberta_F.csv", sep=',', index=False, encoding='utf-8')

if __name__ == "__main__":
    main ( sys.argv[1:] )

#
#   End of names.py
#
