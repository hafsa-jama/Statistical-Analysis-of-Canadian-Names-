#!/usr/bin/env python3

import os
import sys
import getopt
import csv
import pandas as pd

def main (argv):
  if len(argv)<9:
    print("Usage : ./names.py -f1 <file input 1> -f2 <file input 2> -f3 <file input 3> -f4 <file input 4> -f5 <file input 5> -f6 <file input 6> -f7 <file input 7> -f8 <file input 8>")
    sys.exit(2)
  try: # to catch any errors that occur 
    (opts, args) = getopt.getopt (argv,"f1:f2:f3:f4:f5:f6:f7:f8")
  except getopt.GetoptError: #if an error occurs it prints this and exits 
        print ("Usage : ./names.py -f1 <file input 1> -f2 <file input 2> -f3 <file input 3> -f4 <file input 4> -f5 <file input 5> -f6 <file input 6> -f7 <file input 7> -f8 <file input 8>")
        sys.exit(2)
  for opt, arg in opts:
    if opt == '-h': ## this is used as an instruction 
            print ( "Usage: ./analysisNames.py -i <input file name> -n <name>" )
            sys.exit()
    elif opt in ( "-f1", "--file input 1 "):
            fileName_1 = arg
    elif opt in ( "-f2", "--file input 2 "):
            fileName_2 = arg
    elif opt in ( "-f3", "--file input 3 "):
            fileName_3 = arg
    elif opt in ( "-f4", "--file input 4 "):
            fileName_4 = arg
    elif opt in ( "-f5", "--file input 5 "):
            fileName_5 = arg
    elif opt in ( "-f6", "--file input 6 "):
            fileName_6 = arg
    elif opt in ( "-f7", "--file input 7 "):
            fileName_7 = arg
    elif opt in ( "-f8", "--file input 8 "):
            fileName_8 = arg
      
    def read_my_file(name_file,file_years,file_names,file_count,file_ranks):#function to read files 
       with open ( name_file ) as csvDataFile:
        csvReader = csv.reader(csvDataFile)
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

    read_my_file(fileName_1,Alberta_years_M,Alberta_names_M,Alberta_count_M,Alberta_ranks_M)
    read_my_file(fileName_2,Alberta_years_F,Alberta_names_F,Alberta_count_F,Alberta_ranks_F)
    read_my_file(fileName_3,BC_years_M,BC_names_M,BC_count_M,BC_ranks_M)
    read_my_file(fileName_4,BC_years_F,BC_names_F,BC_count_F,BC_ranks_F)
    read_my_file(fileName_5, NewBrunswick_years_M, NewBrunswick_names_M, NewBrunswick_count_M, NewBrunswick_ranks_M)
    read_my_file(fileName_6,NewBrunswick_years_F, NewBrunswick_names_F, NewBrunswick_count_F, NewBrunswick_ranks_F)  
    read_my_file(fileName_7,NovaScotia_years_M,NovaScotia_names_M,NovaScotia_count_M,NovaScotia_ranks_M)
    read_my_file(fileName_8,NovaScotia_years_F,NovaScotia_names_F,NovaScotia_count_F,NovaScotia_ranks_F)
print("\nWelcome to Team Cheetah's CIS2250 Team Project\n")
user_input=0
while user_input==0:
  print("Welcome to the menu")
  print("1-Check if the name is present in a province\n")
  print("2-Displays shortest name in each province\n")
  print("3-Displays most frequently repeated name in a year\n")
  print("4-Enter this to leave")
  user_input = int(input("Enter your choice wisely :"))
  if user_input==1:
    print("choice 1")
  
  elif user_input==2:
    print("choice 2")
  elif user_input==3:
    print("choice 3")
    
  elif user_input==4:
    print("hope you enjoyed")
    break
  else:
    print("Please choose again")


if __name__ == "__main__":
    main (sys.argv[1:])