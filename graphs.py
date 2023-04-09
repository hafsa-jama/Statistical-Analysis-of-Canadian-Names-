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
    print("Enter 1 for Alberta")
    print("Enter 2 for British Columbia")
    print("Enter 3 for New Brunswick")
    print("Enter 4 for Nova Scotia")

def genderMenu():
   print("Enter 1 for Male")
   print("Enter 2 for Female")

def nameOverTime(username, years, names, rank):

    newYears = []
    newRank = []

    username = username.lower()

    count = 0

    for a in range(len(names)):
        if username == (names[a].lower()):
            newYears.append(int(years[a]))
            newRank.append(int(rank[a]))
            count = count + 1

    username = username.capitalize()

    if count == 0:
        print("Name could not be found")
        return

    x = np.array(newYears)
    y = np.array(newRank)

    plt.plot(x,y)
    plt.xlabel("Years") # add X-axis label
    plt.ylabel("Rank") # add Y-axis label
    plt.title(f"Rank of {username} over time")

    plt.savefig(f"{username}.png")
    plt.show()

def nameOverAlphabet(useryear, names, years):

    alphabet = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    alphabetNum = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

    for b in range(len(names)):
        if useryear == years[b]:
            if names[b][0] == 'A':
                alphabetNum[0] = alphabetNum[0] + 1
            elif names[b][0] == 'B':
                alphabetNum[1] = alphabetNum[1] + 1
            elif names[b][0] == 'C':
                alphabetNum[2] = alphabetNum[2] + 1
            elif names[b][0] == 'D':
                alphabetNum[3] = alphabetNum[3] + 1
            elif names[b][0] == 'E':
                alphabetNum[4] = alphabetNum[4] + 1
            elif names[b][0] == 'F':
                alphabetNum[5] = alphabetNum[5] + 1
            elif names[b][0] == 'G':
                alphabetNum[6] = alphabetNum[6] + 1
            elif names[b][0] == 'H':
                alphabetNum[7] = alphabetNum[7] + 1
            elif names[b][0] == 'I':
                alphabetNum[8] = alphabetNum[8] + 1
            elif names[b][0] == 'J':
                alphabetNum[9] = alphabetNum[9] + 1
            elif names[b][0] == 'K':
                alphabetNum[10] = alphabetNum[10] + 1
            elif names[b][0] == 'L':
                alphabetNum[11] = alphabetNum[11] + 1
            elif names[b][0] == 'M':
                alphabetNum[12] = alphabetNum[12] + 1
            elif names[b][0] == 'N':
                alphabetNum[13] = alphabetNum[13] + 1
            elif names[b][0] == 'O':
                alphabetNum[14] = alphabetNum[14] + 1
            elif names[b][0] == 'P':
                alphabetNum[15] = alphabetNum[15] + 1
            elif names[b][0] == 'Q':
                alphabetNum[16] = alphabetNum[16] + 1
            elif names[b][0] == 'R':
                alphabetNum[17] = alphabetNum[17] + 1
            elif names[b][0] == 'S':
                alphabetNum[18] = alphabetNum[18] + 1
            elif names[b][0] == 'T':
                alphabetNum[19] = alphabetNum[19] + 1
            elif names[b][0] == 'U':
                alphabetNum[20] = alphabetNum[20] + 1
            elif names[b][0] == 'V':
                alphabetNum[21] = alphabetNum[21] + 1
            elif names[b][0] == 'W':
                alphabetNum[22] = alphabetNum[22] + 1
            elif names[b][0] == 'X':
                alphabetNum[23] = alphabetNum[23] + 1
            elif names[b][0] == 'Y':
                alphabetNum[24] = alphabetNum[24] + 1
            elif names[b][0] == 'Z':
                alphabetNum[25] = alphabetNum[25] + 1


    fig = plt.figure()
    ax = fig.add_axes([0,0,1,1])
    ax.bar(alphabet,alphabetNum)
    ax.set_xlabel("Alphabet")
    ax.set_ylabel("Count")
    ax.set_ylim(0, max(alphabetNum))
    plt.savefig("barGraph.png")
    plt.show()

