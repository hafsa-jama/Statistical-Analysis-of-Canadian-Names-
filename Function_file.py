import os
import sys
import getopt
import csv
import pandas as pd

# Ayomide's Functions

#which gender has more names 

def topGender(male_df, female_df, year):
    # Filter dataframes to get data for a specific year
    m_year = male_df.groupby("Year").get_group(year)
    ind_m = (m_year.index)
    count_m = 0
    f_year = female_df.groupby("Year").get_group(year)
    ind_f = (f_year.index)
    count_f = 0

    # Count the number of male names and female names
    for x in ind_m:
        count_m = count_m + 1

    for x in ind_f:
        count_f = count_f + 1

    # Determine which gender has more names
    if count_m > count_f:
        print("There are more male names than female names in " + str(year))
    elif count_m == count_f:
        print("There are the same amounts of male names and female names in " + str(year))
    else:
        print("There are more female names than male names in " + str(year))


def top10All(male_df, female_df, year):
    # Group male and female dataframes by year and select the groups corresponding to the given year
    m_year = male_df.groupby("Year").get_group(year)
    ind_m = (m_year.index)
    f_year = female_df.groupby("Year").get_group(year)
    ind_f = (f_year.index)

    # Initialize variables for current ranking position and row indices for male and female dataframes
    a = 1
    i = int(ind_f[0])
    j = int(ind_m[0])

    # Loop through top 10 names for given year and print ranking position, male name, and female name
    while (a<11):
        print(str(a) + " " + m_year.loc[j, "Name"] + "  \t" + f_year.loc[i, "Name"])
        a = a +1
        i = i+1
        j = j+1
