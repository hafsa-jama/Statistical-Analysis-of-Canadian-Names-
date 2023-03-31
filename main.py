#!/usr/bin/env python3

import os
import sys
import getopt
import csv
import pandas as pd

from topTen import *
##from graphs import *
from Function_file import *
from topNameByYear import *

def main (argv):

    # function that will from the files and store in lists      
    def read_my_file(name_file,file_years,file_names,file_count,file_ranks):
       with open ( name_file ) as csvDataFile:
        csvReader = csv.reader(csvDataFile)

        # skips the header row
        next (csvReader)
        for row in csvReader:
          file_years.append(int(row[0]))
          file_names.append(row[1])
          file_count.append(int(row[2]))
          file_ranks.append(row[3])


    Alberta_names_M = []
    Alberta_count_M = []
    Alberta_years_M = []
    Alberta_ranks_M = []

    Alberta_names_F = []
    Alberta_count_F = []
    Alberta_years_F = []
    Alberta_ranks_F = []

    BC_names_M = []
    BC_count_M = []
    BC_years_M = []
    BC_ranks_M = []

    BC_names_F = []
    BC_count_F = []
    BC_years_F = []
    BC_ranks_F = []

    NovaScotia_names_M = []
    NovaScotia_count_M = []
    NovaScotia_years_M = []
    NovaScotia_ranks_M = []

    NovaScotia_names_F = []
    NovaScotia_years_F = []
    NovaScotia_count_F = []
    NovaScotia_ranks_F = []

    NewBrunswick_names_M = []
    NewBrunswick_ranks_M = []
    NewBrunswick_years_M = []
    NewBrunswick_count_M = []

    NewBrunswick_names_F = []
    NewBrunswick_ranks_F = []
    NewBrunswick_years_F = []
    NewBrunswick_count_F = []

    fileName_1 = "alberta_M.csv"
    fileName_2 = "alberta_F.csv"
    fileName_3 = "BritishColumbia_M.csv"
    fileName_4 = "BritishColumbia_F.csv"
    fileName_5 = "NewBrunswick_M.csv"
    fileName_6 = "NewBrunswick_F.csv"
    fileName_7 = "NovaScotia_M.csv"
    fileName_8 = "NovaScotia_F.csv"

    
    read_my_file(fileName_1,Alberta_years_M,Alberta_names_M,Alberta_count_M,Alberta_ranks_M)
    read_my_file(fileName_2,Alberta_years_F,Alberta_names_F,Alberta_count_F,Alberta_ranks_F)
    read_my_file(fileName_3,BC_years_M,BC_names_M,BC_count_M,BC_ranks_M)
    read_my_file(fileName_4,BC_years_F,BC_names_F,BC_count_F,BC_ranks_F)
    read_my_file(fileName_5, NewBrunswick_years_M, NewBrunswick_names_M, NewBrunswick_count_M, NewBrunswick_ranks_M)
    read_my_file(fileName_6,NewBrunswick_years_F, NewBrunswick_names_F, NewBrunswick_count_F, NewBrunswick_ranks_F)  
    read_my_file(fileName_7,NovaScotia_years_M,NovaScotia_names_M,NovaScotia_count_M,NovaScotia_ranks_M)
    read_my_file(fileName_8,NovaScotia_years_F,NovaScotia_names_F,NovaScotia_count_F,NovaScotia_ranks_F)

    al_m = read ("alberta_M.csv")
    al_f = read("alberta_F.csv")
    Ns_m = read("NovaScotia_M.csv")
    Ns_f = read("NovaScotia_F.csv")
    nb_m = read("NewBrunswick_M.csv")
    nb_f = read("NewBrunswick_F.csv")
    bc_f = read("BritishColumbia_F.csv")
    bc_m = read("BritishColumbia_M.csv")

    
print("\nWelcome to Team Cheetah's CIS2250 Team Project\n")
user_input = 0
while user_input != 11:
  print("\n\n Welcome To The Menu \n\n")
  print("1.    Function 1 - Displays shortest name from each province")#Allison
  print("2.    Function 3 - Displays most frequently repeated name in a year")#Ayo
  print("3.    Function 4 - Comparsion of the first letter in a name from a province in a specific year using a graph")#tanveer
  print("4.    Function 5 - Rank of a name from a province over time")#tanveer
  print("5.    Function 6 - Displays top 10 names in a province")#Ayo
  print("6.    Function 7 - Displays the longest name from each province")#Allison
  print("8.    Function 8 - Displays which gender has more names in a particular year")#Ayo
  print("9.    Function 9 - Displays top name for a gender in a province every year")#Hafsa
  print("10.   Function 10 - Displays the ethnicity of the top ten names from each year")#Allison



  print("11.   Exit\n")

  try:
    user_input = int(input("Please enter in your choice: "))

    if user_input == 1:
      print("choice 1")
      ## calls function ##

    elif user_input == 2:
      print("choice 2")
      ## calls function ##

    elif user_input == 3:
      print("choice 3")
      ## calls function ## 

    elif user_input == 4:
      print("choice 4")
      ## calls function ##

    elif user_input == 5:
      print("choice 5")
      ## calls function ##

    elif user_input == 6:
      print("choice 6") 
      ## calls function

    elif user_input == 7:
      print("choice 7")

    elif user_input == 8:
      print("choice 8")

    elif user_input == 9:
      print("Choice 9")

    elif user_input == 10:
      print("choice 10")

    elif user_input == 11:
      print("Exiting from menu......")
      break
      
    else:
      print("Error. Please input a valid option.")
      user_input = 0
      
  except ValueError:
    print("Error. Please input a valid integer option.")
    user_input = 0

if __name__ == "__main__":
    main (sys.argv[1:])