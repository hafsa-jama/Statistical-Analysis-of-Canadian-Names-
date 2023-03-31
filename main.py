#!/usr/bin/env python3

import os
import sys
import getopt
import csv
import pandas as pd

from graphs import *


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
    #read_my_file(fileName_3,BC_years_M,BC_names_M,BC_count_M,BC_ranks_M)
    #read_my_file(fileName_4,BC_years_F,BC_names_F,BC_count_F,BC_ranks_F)
    read_my_file(fileName_5, NewBrunswick_years_M, NewBrunswick_names_M, NewBrunswick_count_M, NewBrunswick_ranks_M)
    read_my_file(fileName_6,NewBrunswick_years_F, NewBrunswick_names_F, NewBrunswick_count_F, NewBrunswick_ranks_F)  
    read_my_file(fileName_7,NovaScotia_years_M,NovaScotia_names_M,NovaScotia_count_M,NovaScotia_ranks_M)
    read_my_file(fileName_8,NovaScotia_years_F,NovaScotia_names_F,NovaScotia_count_F,NovaScotia_ranks_F)

    
    print("\nWelcome to Team Cheetah's CIS2250 Team Project\n")
    user_input = 0
    while user_input == 0:
        print("\n\n Welcome To The Menu \n\n")
        print("1.   Graph 1 - Creates a line graph of the rank of a given name over time")
        print("2.   Function 2 - Displays shortest name in each province")
        print("3.   Function 3 - Displays most frequently repeated name in a year")
        print("4.   Exit\n")

        try:
            user_input = int(input("Please enter in your choice: "))

            if user_input == 1:
                province = 0
                while province == 0:
                    provinceMenu()
                    try:
                        province = int(input("Enter province: "))

                        if province == 1:
                            gender = 0
                            while gender == 0:
                                genderMenu()
                                try:
                                    gender = int(input("Enter gender: "))

                                    if gender == 1:
                                        username = input("Enter a name: ")
                                        nameOverTime(username, Alberta_years_M, Alberta_names_M, Alberta_ranks_M)

                                    elif gender == 2:
                                        username = input("Enter a name: ")
                                        nameOverTime(username, Alberta_years_F, Alberta_names_F, Alberta_ranks_F)
                            

                                except ValueError:
                                    print("Error. Please input a valid integer option.")
                                    gender = 0

                        if province == 2:
                            gender = 0
                            while gender == 0:
                                genderMenu()
                                try:
                                    gender = int(input("Enter gender: "))

                                    if gender == 1:
                                        username = input("Enter a name: ")
                                        #nameOverTime(username, BC_years_M, BC_names_M, BC_ranks_M)

                                    elif gender == 2:
                                        username = input("Enter a name: ")
                                        #nameOverTime(username, BC_years_F, BC_names_F, BC_ranks_F)
                            

                                except ValueError:
                                    print("Error. Please input a valid integer option.")
                                    gender = 0

                        if province == 3:
                            gender = 0
                            while gender == 0:
                                genderMenu()
                                try:
                                    gender = int(input("Enter gender: "))

                                    if gender == 1:
                                        username = input("Enter a name: ")
                                        nameOverTime(username, NewBrunswick_years_M, NewBrunswick_names_M, NewBrunswick_ranks_M)

                                    elif gender == 2:
                                        username = input("Enter a name: ")
                                        nameOverTime(username, NewBrunswick_years_F, NewBrunswick_names_F, NewBrunswick_ranks_F)
                            

                                except ValueError:
                                    print("Error. Please input a valid integer option.")
                                    gender = 0

                        if province == 4:
                            gender = 0
                            while gender == 0:
                                genderMenu()
                                try:
                                    gender = int(input("Enter gender: "))

                                    if gender == 1:
                                        username = input("Enter a name: ")
                                        nameOverTime(username, NovaScotia_years_M, NovaScotia_names_M, NovaScotia_ranks_M)

                                    elif gender == 2:
                                        username = input("Enter a name: ")
                                        nameOverTime(username, NovaScotia_years_F, NovaScotia_names_F, NovaScotia_ranks_F)
                            

                                except ValueError:
                                    print("Error. Please input a valid integer option.")
                                    gender = 0
                

                    except ValueError:
                        print("Error. Please input a valid integer option.")
                        province = 0

                
        ## calls function ##

            elif user_input == 2:
                name = input("Please enter in a name: ")
                ## calls function ##

            elif user_input == 3:
                print("choice 3")
                ## calls function ## 

            elif user_input == 4:
                print("Exiting from menu...")
                break

            else:
                print("Error. Please input a valid option.")
                user_input = 0
        
        except ValueError:
            print("Error. Please input a valid integer option.")
            user_input = 0



if __name__ == "__main__":
    main (sys.argv[1:])