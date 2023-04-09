#!/usr/bin/env python3

# Tanveer's Functions

import os
import sys
import getopt
import csv
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def provinceMenu():
    print("\nEnter 1 for Alberta")
    print("Enter 2 for British Columbia")
    print("Enter 3 for New Brunswick")
    print("Enter 4 for Nova Scotia")

def genderMenu():
   print("\nEnter 1 for Male")
   print("Enter 2 for Female")

def nameOverTime(provi, username, years, names, rank):

    newYears = []
    newRank = []

    username = username.lower()

    count = 0

    for a in range(len(names)): # Looks for the year and name inside the lists and puts them into new lists
        if username == (names[a].lower()):
            newYears.append(int(years[a]))
            newRank.append(int(rank[a]))
            count = count + 1

    username = username.capitalize()

    if count == 0: # Error message if name cannot be found
        print("Name could not be found")
        return

    x = np.array(newYears) # Creates a png of the graph
    y = np.array(newRank)

    plt.figure()
    plt.plot(x,y)
    plt.xlabel("Years") # add X-axis label
    plt.ylabel("Rank") # add Y-axis label
    plt.title(f"Rank of {username} over time")

    plt.savefig(f"{provi}{username}.png")
    plt.show()

def nameOverAlphabet(prov, useryear, namesM, namesF, yearsM, yearsF):

    # Values for the x and y axises
    alphabet = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    alphabetNumM = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    alphabetNumF = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    positions = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25]

    for b in range(len(namesM)): # Collect data for men
        if useryear == yearsM[b]:
            if namesM[b][0] == 'A':
                alphabetNumM[0] = alphabetNumM[0] + 1
            elif namesM[b][0] == 'B':
                alphabetNumM[1] = alphabetNumM[1] + 1
            elif namesM[b][0] == 'C':
                alphabetNumM[2] = alphabetNumM[2] + 1
            elif namesM[b][0] == 'D':
                alphabetNumM[3] = alphabetNumM[3] + 1
            elif namesM[b][0] == 'E':
                alphabetNumM[4] = alphabetNumM[4] + 1
            elif namesM[b][0] == 'F':
                alphabetNumM[5] = alphabetNumM[5] + 1
            elif namesM[b][0] == 'G':
                alphabetNumM[6] = alphabetNumM[6] + 1
            elif namesM[b][0] == 'H':
                alphabetNumM[7] = alphabetNumM[7] + 1
            elif namesM[b][0] == 'I':
                alphabetNumM[8] = alphabetNumM[8] + 1
            elif namesM[b][0] == 'J':
                alphabetNumM[9] = alphabetNumM[9] + 1
            elif namesM[b][0] == 'K':
                alphabetNumM[10] = alphabetNumM[10] + 1
            elif namesM[b][0] == 'L':
                alphabetNumM[11] = alphabetNumM[11] + 1
            elif namesM[b][0] == 'M':
                alphabetNumM[12] = alphabetNumM[12] + 1
            elif namesM[b][0] == 'N':
                alphabetNumM[13] = alphabetNumM[13] + 1
            elif namesM[b][0] == 'O':
                alphabetNumM[14] = alphabetNumM[14] + 1
            elif namesM[b][0] == 'P':
                alphabetNumM[15] = alphabetNumM[15] + 1
            elif namesM[b][0] == 'Q':
                alphabetNumM[16] = alphabetNumM[16] + 1
            elif namesM[b][0] == 'R':
                alphabetNumM[17] = alphabetNumM[17] + 1
            elif namesM[b][0] == 'S':
                alphabetNumM[18] = alphabetNumM[18] + 1
            elif namesM[b][0] == 'T':
                alphabetNumM[19] = alphabetNumM[19] + 1
            elif namesM[b][0] == 'U':
                alphabetNumM[20] = alphabetNumM[20] + 1
            elif namesM[b][0] == 'V':
                alphabetNumM[21] = alphabetNumM[21] + 1
            elif namesM[b][0] == 'W':
                alphabetNumM[22] = alphabetNumM[22] + 1
            elif namesM[b][0] == 'X':
                alphabetNumM[23] = alphabetNumM[23] + 1
            elif namesM[b][0] == 'Y':
                alphabetNumM[24] = alphabetNumM[24] + 1
            elif namesM[b][0] == 'Z':
                alphabetNumM[25] = alphabetNumM[25] + 1


    for c in range(len(namesF)): # Collect data for women
        if useryear == yearsF[c]:
            if namesF[c][0] == 'A':
                alphabetNumF[0] = alphabetNumF[0] + 1
            elif namesF[c][0] == 'B':
                alphabetNumF[1] = alphabetNumF[1] + 1
            elif namesF[c][0] == 'C':
                alphabetNumF[2] = alphabetNumF[2] + 1
            elif namesF[c][0] == 'D':
                alphabetNumF[3] = alphabetNumF[3] + 1
            elif namesF[c][0] == 'E':
                alphabetNumF[4] = alphabetNumF[4] + 1
            elif namesF[c][0] == 'F':
                alphabetNumF[5] = alphabetNumF[5] + 1
            elif namesF[c][0] == 'G':
                alphabetNumF[6] = alphabetNumF[6] + 1
            elif namesF[c][0] == 'H':
                alphabetNumF[7] = alphabetNumF[7] + 1
            elif namesF[c][0] == 'I':
                alphabetNumF[8] = alphabetNumF[8] + 1
            elif namesF[c][0] == 'J':
                alphabetNumF[9] = alphabetNumF[9] + 1
            elif namesF[c][0] == 'K':
                alphabetNumF[10] = alphabetNumF[10] + 1
            elif namesF[c][0] == 'L':
                alphabetNumF[11] = alphabetNumF[11] + 1
            elif namesF[c][0] == 'M':
                alphabetNumF[12] = alphabetNumF[12] + 1
            elif namesF[c][0] == 'N':
                alphabetNumF[13] = alphabetNumF[13] + 1
            elif namesF[c][0] == 'O':
                alphabetNumF[14] = alphabetNumF[14] + 1
            elif namesF[c][0] == 'P':
                alphabetNumF[15] = alphabetNumF[15] + 1
            elif namesF[c][0] == 'Q':
                alphabetNumF[16] = alphabetNumF[16] + 1
            elif namesF[c][0] == 'R':
                alphabetNumF[17] = alphabetNumF[17] + 1
            elif namesF[c][0] == 'S':
                alphabetNumF[18] = alphabetNumF[18] + 1
            elif namesF[c][0] == 'T':
                alphabetNumF[19] = alphabetNumF[19] + 1
            elif namesF[c][0] == 'U':
                alphabetNumF[20] = alphabetNumF[20] + 1
            elif namesF[c][0] == 'V':
                alphabetNumF[21] = alphabetNumF[21] + 1
            elif namesF[c][0] == 'W':
                alphabetNumF[22] = alphabetNumF[22] + 1
            elif namesF[c][0] == 'X':
                alphabetNumF[23] = alphabetNumF[23] + 1
            elif namesF[c][0] == 'Y':
                alphabetNumF[24] = alphabetNumF[24] + 1
            elif namesF[c][0] == 'Z':
                alphabetNumF[25] = alphabetNumF[25] + 1

    fig = plt.figure(figsize=(7,5)) # Create a png of the bar graph using the collected data
    
    plt.bar(positions, alphabetNumM, color = 'r')
    plt.bar(positions, alphabetNumF, bottom=alphabetNumM, color='b')
    plt.xlabel("First Letter of Name")
    plt.ylabel("Frequency")
    plt.title(f"Most Popular First Letter of Names in {useryear} for {prov}")
    plt.legend(labels=['Men', 'Women'])
    plt.xticks(positions, alphabet)


    plt.savefig(f"{prov}{useryear}BarGraph.png")
    plt.show()

