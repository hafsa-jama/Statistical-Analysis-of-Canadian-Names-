import os
import sys
import getopt
import csv
import pandas as pd

#which gender has more names 

def topGender (male_df, female_df, year) :
    m_year = male_df.groupby("Year").get_group(year)   #groups the 
    ind_m = (m_year.index)
    count_m = 0
    f_year = female_df.groupby("Year").get_group(year)
    ind_f = (f_year.index)
    count_f = 0

    for x in ind_m:
        count_m = count_m +1

    for x in ind_f:
        count_f = count_f + 1

    if (count_m > count_f):
        print("There are more male names than female names in " + str(year))

    elif(count_m == count_f):
        print("There are the same amounts of male names and female names in " + str(year))

    else:
        print("There are more female names than male names in " + str(year))    




def top10All (male_df, female_df, year):
    m_year = male_df.groupby("Year").get_group(year)   #groups the 
    ind_m = (m_year.index)
    f_year = female_df.groupby("Year").get_group(year)
    ind_f = (f_year.index)

    a = 1
    i = int(ind_f[0])
    j = int(ind_m[0])

    while (a<11):
        print(str(a) + " " + m_year.loc[j, "Name"] + "  \t" + f_year.loc[i, "Name"])
        a = a +1
        i = i+1
        j = j+1