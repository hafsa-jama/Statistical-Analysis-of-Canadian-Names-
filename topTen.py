#!/usr/bin/env python3

import os
import sys
import getopt
import csv
import pandas as pd

#need to check if year is valaid first
#prints top 10 names from given file in chosen year
def top10 (info_df,year):
    year_df = info_df.groupby("Year").get_group(year) #creates dataframe with spesified year
    year_df=year_df.set_index("Rank") #sets rank as index
    print(year_df.loc[1:10,["Name"]]) #prints ranks 1-10
    


#longest name from given year
def longest (info_df,year):
    year_df = info_df.groupby("Year").get_group(year) #creates dataframe with spesified year
    ind = (year_df.index)#finds index
    name = ""

    for x in ind: #goes through index
        if (len(year_df.loc[x, 'Name'])>len(name)):#checks in name at ind is longer than previously longest name
            name = year_df.loc[x, 'Name']#saves name

    print("The longest Name is " + name)

    #shortest name from given year
def shortest (info_df,year):
    year_df = info_df.groupby("Year").get_group(year) #creates dataframe with spesified year
    ind = (year_df.index)#finds index
    name = "lotsofwords"
    
    for x in ind: #goes through index
        if (len(year_df.loc[x, 'Name'])<len(name)):#checks in name at ind is shorter than previously shortest name
            name = year_df.loc[x, 'Name']#saves name

    print("The shortest Name is " + name)






def main (argv):
    if len(argv) < 1:
        print ( "Usage: ./names.py -i <input file name>" )
        sys.exit(2)
    try:
        (opts, args) = getopt.getopt ( argv,"i:",["input="] )
    except getopt.GetoptError:
        print ( "Usage: ./names.py -i <input file name>" )
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print ( "Usage: ./names.py -i <input file name> -y <year> -o <output file name base>" )
            sys.exit()
        elif opt in ( "-i", "--input"):
            inputFileName = arg
    names    = []
    count  = []
    ranks    = []
    year     = []
    total    = 0

    with open ( inputFileName ) as csvDataFile:

        next ( csvDataFile ) 
        csvReader = csv.reader(csvDataFile, delimiter=',')
        for row in csvReader:
            year.append(int(row[0]))
            tempName = row[1].strip()
            names.append(tempName)
            count.append(int(row[2]))
            ranks.append(int(row[3]))
            total = total + 1

        if total > 0 :
            people = {'Year':year,'Name':names,'Number':count,'Rank':ranks}
            people_df = pd.DataFrame(people)

            #top10(people_df,2000)
            longest (people_df,1990)
            shortest (people_df,1990)
            #




    

if __name__ == "__main__":
    main ( sys.argv[1:] )