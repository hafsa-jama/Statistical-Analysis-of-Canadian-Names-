#!/usr/bin/env python3

import os
import sys
import getopt
import csv
import pandas as pd

#reads the namesGood csv into a datafile
def readNamesGood():
    names = []
    reagon = []
    subReagon = []

    with open ( "namesGood.csv" ) as csvDataFile:

        next ( csvDataFile ) 
        csvReader = csv.reader(csvDataFile, delimiter=',')
        #goes through rows in csv and appends contents into list
        for row in csvReader: 
            temp = row[0].strip()
            names.append(temp)
            temp = row[1].strip()
            reagon.append(temp)
            temp = row[2].strip()
            subReagon.append(temp)    

        #list are grouped and turned into a datafile
        people = {'Name':names,'Reagon':reagon,'SubReagon':subReagon}
        people_df = pd.DataFrame(people)
        return people_df #return datafile

#takes in two dataafiles for given provence, chosen year and the datafile with origin of names
def exploration (df,df2,year,names_df):
    europe = 0
    asia = 0
    africa = 0
    total = 0

    M_df = df.groupby("Year").get_group(year) #creates dataframe with spesified year
    M_df = M_df[M_df["Rank"]<101] #takes only ranks below 1-100
    namesM = M_df ['Name'].to_list() #turns into list

    F_df = df2.groupby("Year").get_group(year) #creates dataframe with spesified year
    F_df = F_df[F_df["Rank"]<101] #takes only ranks below 1-100
    namesF = F_df ['Name'].to_list() #turns into list
    namesAll = namesM + namesF #concoctinates list with top 100 names together

    ind = (names_df.index)
    for x in  ind:
       if  (((names_df.loc[x,"Name"]) in namesAll)):
            total = total+1
            if (names_df.loc[x, 'Reagon'] == "Europe"):
                europe = europe +1
            elif(names_df.loc[x, 'Reagon'] == "Asia"):
                asia = asia +1
            else:
                africa = africa +1
    print("Of the names ranked in the top 100 in",year)
    print(round(africa/total*100,2),"%"+" are from Africa")
    print(round(asia/total*100,2), '%' +" are from Asia")
    print(round(europe/total*100,2), '%' +" are from Europe")

def nameLis (df):
    print("in")
    unique = []
    extra = []
    ind = (df.index)
    for x in  ind:
        if  (((df.loc[x, 'Name'])not in unique)and (df.loc[x, 'Rank']<101 )) :
            unique.append (df.loc[x, 'Name'])
            extra.append(x)
    nom_df = pd.DataFrame( {'Name':unique,"extra":extra})
    return nom_df
def namecont (df,df2):
    print("in")
    unique = df2['Name'].to_list()
    extra = df2["extra"].to_list()
    ind = (df.index)
    for x in  ind:
        if (((df.loc[x, 'Name'])not in unique)and (df.loc[x, 'Rank']<101)) :
            unique.append (df.loc[x, 'Name'])
            extra.append(x)
    nom_df = pd.DataFrame( {'Name':unique,"extra":extra})
    return nom_df

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


def read (df):
    inputFileName = df
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
    return people_df
def readBC (df):
    inputFileName = df
    names    = []
    count  = []
    ranks    = []
    year     = []
    total    = 0

    with open ( inputFileName ) as csvDataFile:

        next ( csvDataFile ) 
        csvReader = csv.reader(csvDataFile, delimiter=',')
        for row in csvReader:
            year.append(int(row[1]))
            tempName = row[2].strip()
            names.append(tempName)
            count.append(int(row[3]))
            ranks.append(int(row[0]))
            total = total + 1

        if total > 0 :
            people = {'Year':year,'Name':names,'Number':count,'Rank':ranks}
            people_df = pd.DataFrame(people)
    return people_df


def main (argv):
    al_m = read ("alberta_M.csv")
    al_f = read("alberta_F.csv")
    Ns_m = read("NovaScotia_M.csv")
    Ns_f = read("NovaScotia_F.csv")
    nb_m = read("NewBrunswick_M.csv")
    nb_f = read("NewBrunswick_F.csv")
    bc_f = readBC("BritishColumbia_F.csv")
    bc_m = readBC("BritishColumbia_M.csv")

    name_df = readNamesGood()
    #exploration (bc_m,bc_f,1980,name_df)
    top10(nb_m,1980)





    

if __name__ == "__main__":
    main ( sys.argv[1:] )
