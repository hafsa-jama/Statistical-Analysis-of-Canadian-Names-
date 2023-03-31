#!/usr/bin/env python3

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

    plt.show()
    plt.savefig(f"{username}.png")

def nameOverAlphabet(useryear, names, years, ranks):
    print("func")
    alphabet = {'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z'}
    alphabetNum = {0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0}


    for b in range(len(names)):
        if useryear == years[b]:
            #if
            print("X")

