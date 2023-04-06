#!/usr/bin/env python3

import os
import sys
import getopt
import csv
import pandas as pd

from topTen import *
from graphs import *
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

    name_df = readNamesGood()

    
    print("\nWelcome to Team Cheetah's CIS2250 Team Project\n")
    user_input = 0
    while user_input != 11:
        print("\n\n Welcome To The Menu \n\n")
        print("1.    Function 1 - Displays shortest name from each province")#Allison
        print("2.    Function 2 - Displays top name for a gender in a province every year")#Hafsa
        print("3.    Function 3 - Comparsion of the first letter in a name from a province in a specific year using a graph")#tanveer
        print("4.    Function 4 - Rank of a name from a province over time")#tanveer
        print("5.    Function 5 - Displays which gender has more names in a particular year")#Ayo
        print("6.    Function 6 - Displays the longest name from each province")#Allison
        print("7.    Function 7 - Displays top 10 names in a province")#Ayo
        print("8.    Function 8 - Displays the ethnicity of the top ten names from each year")#Allison
        print("9.    Exit\n")

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
                                        yearInput = 0
                                        while yearInput == 0:
                                            print("Enter a year between 1980 and 2022")
                                            try:
                                                yearInput = int(input("Enter a year: "))
                                                if yearInput > 1979 and yearInput < 2023:
                                                    shortest (al_m,yearInput)
                                                else:
                                                    print("Incorrect Year")
                                                    yearInput = 0
                                            except ValueError:
                                                print("Error. Please input a valid integer option.")
                                                yearInput = 0

                                    elif gender == 2:
                                        yearInput = 0
                                        while yearInput == 0:
                                            print("Enter a year between 1980 and 2022")
                                            try:
                                                yearInput = int(input("Enter a year: "))
                                                if (yearInput > 1979 and yearInput < 2023):
                                                    shortest (al_f,yearInput)
                                                else:
                                                    print("Incorrect Year")
                                                    yearInput = 0
                                            except ValueError:
                                                print("Error. Please input a valid integer option.")
                                                yearInput = 0
                                    else:
                                        print("Incorrect gender")
                                        gender = 0

                                except ValueError:
                                    print("Error. Please input a valid integer option.")
                                    gender = 0

                        elif province == 2:
                            gender = 0
                            while gender == 0:
                                genderMenu()
                                try:
                                    gender = int(input("Enter gender: "))

                                    if gender == 1:
                                        yearInput = 0
                                        while yearInput == 0:
                                            print("Enter a year between 1922 and 2020")
                                            try:
                                                yearInput = int(input("Enter a year: "))
                                                if yearInput > 1921 and yearInput < 2021:
                                                    shortest (bc_m,yearInput)
                                                else:
                                                    print("Incorrect Year")
                                                    yearInput = 0
                                            except ValueError:
                                                print("Error. Please input a valid integer option.")
                                                yearInput = 0

                                    elif gender == 2:
                                        yearInput = 0
                                        while yearInput == 0:
                                            print("Enter a year between 1922 and 2020")
                                            try:
                                                yearInput = int(input("Enter a year: "))
                                                if (yearInput > 1921 and yearInput < 2021):
                                                    shortest (bc_f,yearInput)
                                                else:
                                                    print("Incorrect Year")
                                                    yearInput = 0
                                            except ValueError:
                                                print("Error. Please input a valid integer option.")
                                                yearInput = 0
                                    else:
                                        print("Incorrect gender")
                                        gender = 0

                                except ValueError:
                                    print("Error. Please input a valid integer option.")
                                    gender = 0

                        elif province == 3:
                            gender = 0
                            while gender == 0:
                                genderMenu()
                                try:
                                    gender = int(input("Enter gender: "))

                                    if gender == 1:
                                        yearInput = 0
                                        while yearInput == 0:
                                            print("Enter a year between 1980 and 2018")
                                            try:
                                                yearInput = int(input("Enter a year: "))
                                                if yearInput > 1979 and yearInput < 2019:
                                                    shortest (nb_m,yearInput)
                                                else:
                                                    print("Incorrect Year")
                                                    yearInput = 0
                                            except ValueError:
                                                print("Error. Please input a valid integer option.")
                                                yearInput = 0

                                    elif gender == 2:
                                        yearInput = 0
                                        while yearInput == 0:
                                            print("Enter a year between 1980 and 2018")
                                            try:
                                                yearInput = int(input("Enter a year: "))
                                                if (yearInput > 1979 and yearInput < 2019):
                                                    shortest (nb_f,yearInput)
                                                else:
                                                    print("Incorrect Year")
                                                    yearInput = 0
                                            except ValueError:
                                                print("Error. Please input a valid integer option.")
                                                yearInput = 0
                                    else:
                                        print("Incorrect gender")
                                        gender = 0

                                except ValueError:
                                    print("Error. Please input a valid integer option.")
                                    gender = 0

                        elif province == 4:
                            gender = 0
                            while gender == 0:
                                genderMenu()
                                try:
                                    gender = int(input("Enter gender: "))

                                    if gender == 1:
                                        yearInput = 0
                                        while yearInput == 0:
                                            print("Enter a year between 1920 and 2022")
                                            try:
                                                yearInput = int(input("Enter a year: "))
                                                if yearInput > 1919 and yearInput < 2023:
                                                    shortest (Ns_m,yearInput)
                                                else:
                                                    print("Incorrect Year")
                                                    yearInput = 0
                                            except ValueError:
                                                print("Error. Please input a valid integer option.")
                                                yearInput = 0

                                    elif gender == 2:
                                        yearInput = 0
                                        while yearInput == 0:
                                            print("Enter a year between 1920 and 2022")
                                            try:
                                                yearInput = int(input("Enter a year: "))
                                                if (yearInput > 1919 and yearInput < 2023):
                                                    shortest (Ns_f,yearInput)
                                                else:
                                                    print("Incorrect Year")
                                                    yearInput = 0
                                            except ValueError:
                                                print("Error. Please input a valid integer option.")
                                                yearInput = 0
                                    else:
                                        print("Incorrect gender")
                                        gender = 0

                                except ValueError:
                                    print("Error. Please input a valid integer option.")
                                    gender = 0
                            
                        else:
                            print("Incorrect province")
                            province = 0
                

                    except ValueError:
                        print("Error. Please input a valid integer option.")
                        province = 0

            elif user_input == 2:
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
                                        top_name_by_year('M', "alberta")

                                    elif gender == 2:
                                        top_name_by_year('F', "alberta")

                                    else:
                                        print("Incorrect gender")
                                        gender = 0
                            

                                except ValueError:
                                    print("Error. Please input a valid integer option.")
                                    gender = 0

                        elif province == 2:
                            gender = 0
                            while gender == 0:
                                genderMenu()
                                try:
                                    gender = int(input("Enter gender: "))

                                    if gender == 1:
                                        top_name_by_year('M', "britishcolumbia")

                                    elif gender == 2:
                                        top_name_by_year('F', "britishcolumbia")

                                    else:
                                        print("Incorrect gender")
                                        gender = 0

                                except ValueError:
                                    print("Error. Please input a valid integer option.")
                                    gender = 0

                        elif province == 3:
                            gender = 0
                            while gender == 0:
                                genderMenu()
                                try:
                                    gender = int(input("Enter gender: "))

                                    if gender == 1:
                                        top_name_by_year('M', "newbrunswick")

                                    elif gender == 2:
                                        top_name_by_year('F', "newbrunswick")

                                    else:
                                        print("Incorrect gender")
                                        gender = 0
                            

                                except ValueError:
                                    print("Error. Please input a valid integer option.")
                                    gender = 0

                        elif province == 4:
                            gender = 0
                            while gender == 0:
                                genderMenu()
                                try:
                                    gender = int(input("Enter gender: "))

                                    if gender == 1:
                                        top_name_by_year('M', "novascotia")

                                    elif gender == 2:
                                        top_name_by_year('F', "novascotia")
                            
                                    else:
                                        print("Incorrect gender")
                                        gender = 0

                                except ValueError:
                                    print("Error. Please input a valid integer option.")
                                    gender = 0

                        else:
                            print("Incorrect province")
                            province = 0
                

                    except ValueError:
                        print("Error. Please input a valid integer option.")
                        province = 0

            elif user_input == 3:
                nameOverAlphabet(2000, Alberta_names_M, Alberta_years_M)

            elif user_input == 4:
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

                                    else:
                                        print("Incorrect gender")
                                        gender = 0
                            

                                except ValueError:
                                    print("Error. Please input a valid integer option.")
                                    gender = 0

                        elif province == 2:
                            gender = 0
                            while gender == 0:
                                genderMenu()
                                try:
                                    gender = int(input("Enter gender: "))

                                    if gender == 1:
                                        username = input("Enter a name: ")
                                        nameOverTime(username, BC_years_M, BC_names_M, BC_ranks_M)

                                    elif gender == 2:
                                        username = input("Enter a name: ")
                                        nameOverTime(username, BC_years_F, BC_names_F, BC_ranks_F)

                                    else:
                                        print("Incorrect gender")
                                        gender = 0

                                except ValueError:
                                    print("Error. Please input a valid integer option.")
                                    gender = 0

                        elif province == 3:
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

                                    else:
                                        print("Incorrect gender")
                                        gender = 0
                            

                                except ValueError:
                                    print("Error. Please input a valid integer option.")
                                    gender = 0

                        elif province == 4:
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
                            
                                    else:
                                        print("Incorrect gender")
                                        gender = 0

                                except ValueError:
                                    print("Error. Please input a valid integer option.")
                                    gender = 0

                        else:
                            print("Incorrect province")
                            province = 0
                

                    except ValueError:
                        print("Error. Please input a valid integer option.")
                        province = 0

            elif user_input == 5:
                province = 0
                while province == 0:
                    provinceMenu()
                    try:
                        province = int(input("Enter province: "))

                        if province == 1:
                            yearInput = 0
                            while yearInput == 0:
                                print("Enter a year between 1980 and 2022")
                                try:
                                    yearInput = int(input("Enter a year: "))
                                    if yearInput > 1979 and yearInput < 2023:
                                        topGender (al_m, al_f, yearInput)
                                    else:
                                        print("Incorrect Year")
                                        yearInput = 0
                                except ValueError:
                                    print("Error. Please input a valid integer option.")
                                    yearInput = 0

                        elif province == 2:
                            yearInput = 0
                            while yearInput == 0:
                                print("Enter a year between 1922 and 2020")
                                try:
                                    yearInput = int(input("Enter a year: "))
                                    if yearInput > 1921 and yearInput < 2021:
                                        topGender (bc_m, bc_f, yearInput)
                                    else:
                                        print("Incorrect Year")
                                        yearInput = 0
                                except ValueError:
                                    print("Error. Please input a valid integer option.")
                                    yearInput = 0

                        elif province == 3:
                            yearInput = 0
                            while yearInput == 0:
                                print("Enter a year between 1980 and 2018")
                                try:
                                    yearInput = int(input("Enter a year: "))
                                    if yearInput > 1979 and yearInput < 2019:
                                        topGender (nb_m, nb_f, yearInput)
                                    else:
                                        print("Incorrect Year")
                                        yearInput = 0
                                except ValueError:
                                    print("Error. Please input a valid integer option.")
                                    yearInput = 0

                        elif province == 4:
                            yearInput = 0
                            while yearInput == 0:
                                print("Enter a year between 1920 and 2022")
                                try:
                                    yearInput = int(input("Enter a year: "))
                                    if yearInput > 1919 and yearInput < 2023:
                                        topGender (Ns_m, Ns_f, yearInput)
                                    else:
                                        print("Incorrect Year")
                                        yearInput = 0
                                except ValueError:
                                    print("Error. Please input a valid integer option.")
                                    yearInput = 0

                        else:
                            print("Incorrect province")
                            province = 0

                    except ValueError:
                        print("Error. Please input a valid integer option.")
                        province = 0

            elif user_input == 6:
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
                                        yearInput = 0
                                        while yearInput == 0:
                                            print("Enter a year between 1980 and 2022")
                                            try:
                                                yearInput = int(input("Enter a year: "))
                                                if yearInput > 1979 and yearInput < 2023:
                                                    longest (al_m,yearInput)
                                                else:
                                                    print("Incorrect Year")
                                                    yearInput = 0
                                            except ValueError:
                                                print("Error. Please input a valid integer option.")
                                                yearInput = 0

                                    elif gender == 2:
                                        yearInput = 0
                                        while yearInput == 0:
                                            print("Enter a year between 1980 and 2022")
                                            try:
                                                yearInput = int(input("Enter a year: "))
                                                if (yearInput > 1979 and yearInput < 2023):
                                                    longest (al_f,yearInput)
                                                else:
                                                    print("Incorrect Year")
                                                    yearInput = 0
                                            except ValueError:
                                                print("Error. Please input a valid integer option.")
                                                yearInput = 0
                                    else:
                                        print("Incorrect gender")
                                        gender = 0

                                except ValueError:
                                    print("Error. Please input a valid integer option.")
                                    gender = 0

                        elif province == 2:
                            gender = 0
                            while gender == 0:
                                genderMenu()
                                try:
                                    gender = int(input("Enter gender: "))

                                    if gender == 1:
                                        yearInput = 0
                                        while yearInput == 0:
                                            print("Enter a year between 1922 and 2020")
                                            try:
                                                yearInput = int(input("Enter a year: "))
                                                if yearInput > 1921 and yearInput < 2021:
                                                    longest (bc_m,yearInput)
                                                else:
                                                    print("Incorrect Year")
                                                    yearInput = 0
                                            except ValueError:
                                                print("Error. Please input a valid integer option.")
                                                yearInput = 0

                                    elif gender == 2:
                                        yearInput = 0
                                        while yearInput == 0:
                                            print("Enter a year between 1922 and 2020")
                                            try:
                                                yearInput = int(input("Enter a year: "))
                                                if (yearInput > 1921 and yearInput < 2021):
                                                    longest (bc_f,yearInput)
                                                else:
                                                    print("Incorrect Year")
                                                    yearInput = 0
                                            except ValueError:
                                                print("Error. Please input a valid integer option.")
                                                yearInput = 0
                                    else:
                                        print("Incorrect gender")
                                        gender = 0

                                except ValueError:
                                    print("Error. Please input a valid integer option.")
                                    gender = 0

                        elif province == 3:
                            gender = 0
                            while gender == 0:
                                genderMenu()
                                try:
                                    gender = int(input("Enter gender: "))

                                    if gender == 1:
                                        yearInput = 0
                                        while yearInput == 0:
                                            print("Enter a year between 1980 and 2018")
                                            try:
                                                yearInput = int(input("Enter a year: "))
                                                if yearInput > 1979 and yearInput < 2019:
                                                    longest (nb_m,yearInput)
                                                else:
                                                    print("Incorrect Year")
                                                    yearInput = 0
                                            except ValueError:
                                                print("Error. Please input a valid integer option.")
                                                yearInput = 0

                                    elif gender == 2:
                                        yearInput = 0
                                        while yearInput == 0:
                                            print("Enter a year between 1980 and 2018")
                                            try:
                                                yearInput = int(input("Enter a year: "))
                                                if (yearInput > 1979 and yearInput < 2019):
                                                    longest (nb_f,yearInput)
                                                else:
                                                    print("Incorrect Year")
                                                    yearInput = 0
                                            except ValueError:
                                                print("Error. Please input a valid integer option.")
                                                yearInput = 0
                                    else:
                                        print("Incorrect gender")
                                        gender = 0

                                except ValueError:
                                    print("Error. Please input a valid integer option.")
                                    gender = 0

                        elif province == 4:
                            gender = 0
                            while gender == 0:
                                genderMenu()
                                try:
                                    gender = int(input("Enter gender: "))

                                    if gender == 1:
                                        yearInput = 0
                                        while yearInput == 0:
                                            print("Enter a year between 1920 and 2022")
                                            try:
                                                yearInput = int(input("Enter a year: "))
                                                if yearInput > 1919 and yearInput < 2023:
                                                    longest (Ns_m,yearInput)
                                                else:
                                                    print("Incorrect Year")
                                                    yearInput = 0
                                            except ValueError:
                                                print("Error. Please input a valid integer option.")
                                                yearInput = 0

                                    elif gender == 2:
                                        yearInput = 0
                                        while yearInput == 0:
                                            print("Enter a year between 1920 and 2022")
                                            try:
                                                yearInput = int(input("Enter a year: "))
                                                if (yearInput > 1919 and yearInput < 2023):
                                                    longest (Ns_f,yearInput)
                                                else:
                                                    print("Incorrect Year")
                                                    yearInput = 0
                                            except ValueError:
                                                print("Error. Please input a valid integer option.")
                                                yearInput = 0
                                    else:
                                        print("Incorrect gender")
                                        gender = 0

                                except ValueError:
                                    print("Error. Please input a valid integer option.")
                                    gender = 0
                            
                        else:
                            print("Incorrect province")
                            province = 0
                

                    except ValueError:
                        print("Error. Please input a valid integer option.")
                        province = 0

            elif user_input == 7:
                province = 0
                while province == 0:
                    provinceMenu()
                    try:
                        province = int(input("Enter province: "))

                        if province == 1:
                            yearInput = 0
                            while yearInput == 0:
                                print("Enter a year between 1980 and 2022")
                                try:
                                    yearInput = int(input("Enter a year: "))
                                    if yearInput > 1979 and yearInput < 2023:
                                        top10All (al_m, al_f, yearInput)
                                    else:
                                        print("Incorrect Year")
                                        yearInput = 0
                                except ValueError:
                                    print("Error. Please input a valid integer option.")
                                    yearInput = 0

                        elif province == 2:
                            yearInput = 0
                            while yearInput == 0:
                                print("Enter a year between 1922 and 2020")
                                try:
                                    yearInput = int(input("Enter a year: "))
                                    if yearInput > 1921 and yearInput < 2021:
                                        top10All (bc_m, bc_f, yearInput)
                                    else:
                                        print("Incorrect Year")
                                        yearInput = 0
                                except ValueError:
                                    print("Error. Please input a valid integer option.")
                                    yearInput = 0

                        elif province == 3:
                            yearInput = 0
                            while yearInput == 0:
                                print("Enter a year between 1980 and 2018")
                                try:
                                    yearInput = int(input("Enter a year: "))
                                    if yearInput > 1979 and yearInput < 2019:
                                        top10All (nb_m, nb_f, yearInput)
                                    else:
                                        print("Incorrect Year")
                                        yearInput = 0
                                except ValueError:
                                    print("Error. Please input a valid integer option.")
                                    yearInput = 0

                        elif province == 4:
                            yearInput = 0
                            while yearInput == 0:
                                print("Enter a year between 1920 and 2022")
                                try:
                                    yearInput = int(input("Enter a year: "))
                                    if yearInput > 1919 and yearInput < 2023:
                                        top10All (Ns_m, Ns_f, yearInput)
                                    else:
                                        print("Incorrect Year")
                                        yearInput = 0
                                except ValueError:
                                    print("Error. Please input a valid integer option.")
                                    yearInput = 0

                        else:
                            print("Incorrect province")
                            province = 0

                    except ValueError:
                        print("Error. Please input a valid integer option.")
                        province = 0

            elif user_input == 8:
                province = 0
                while province == 0:
                    provinceMenu()
                    try:
                        province = int(input("Enter province: "))

                        if province == 1:
                            yearInput = 0
                            while yearInput == 0:
                                print("Enter a year between 1980 and 2022")
                                try:
                                    yearInput = int(input("Enter a year: "))
                                    if yearInput > 1979 and yearInput < 2023:
                                        exploration (al_m,al_f,yearInput,name_df)
                                    else:
                                        print("Incorrect Year")
                                        yearInput = 0
                                except ValueError:
                                    print("Error. Please input a valid integer option.")
                                    yearInput = 0

                        elif province == 2:
                            yearInput = 0
                            while yearInput == 0:
                                print("Enter a year between 1922 and 2020")
                                try:
                                    yearInput = int(input("Enter a year: "))
                                    if yearInput > 1921 and yearInput < 2021:
                                        exploration (bc_m,bc_f,yearInput,name_df)
                                    else:
                                        print("Incorrect Year")
                                        yearInput = 0
                                except ValueError:
                                    print("Error. Please input a valid integer option.")
                                    yearInput = 0

                        elif province == 3:
                            yearInput = 0
                            while yearInput == 0:
                                print("Enter a year between 1980 and 2018")
                                try:
                                    yearInput = int(input("Enter a year: "))
                                    if yearInput > 1979 and yearInput < 2019:
                                        exploration (nb_m,nb_f,yearInput,name_df)
                                    else:
                                        print("Incorrect Year")
                                        yearInput = 0
                                except ValueError:
                                    print("Error. Please input a valid integer option.")
                                    yearInput = 0

                        elif province == 4:
                            yearInput = 0
                            while yearInput == 0:
                                print("Enter a year between 1920 and 2022")
                                try:
                                    yearInput = int(input("Enter a year: "))
                                    if yearInput > 1919 and yearInput < 2023:
                                        exploration (Ns_m,Ns_f,yearInput,name_df)
                                    else:
                                        print("Incorrect Year")
                                        yearInput = 0
                                except ValueError:
                                    print("Error. Please input a valid integer option.")
                                    yearInput = 0

                        else:
                            print("Incorrect province")
                            province = 0

                    except ValueError:
                        print("Error. Please input a valid integer option.")
                        province = 0

            elif user_input == 9:
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