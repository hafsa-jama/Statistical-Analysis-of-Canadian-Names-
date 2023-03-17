# To Run: python3 ./britishColumbia.py BritishColombiaBoys_1922_2021.csv BritishColombiaGirls_1922_2021.csv
# Format: year/name/frequency/rank

import csv
import pandas as pd

def main(argv, fn, index):
    
   # initalizes dictonaries to store data read from CSV file
    people = {}
    names = {}
    years = {}
    

    # initalizes variables
    startYear = 1922
    endYear = 2022
    count = 0
    fileName = argv[index] # assigns the value of the command-line argument at the specified index to a variable


    # opens the csv file using encoding
    with open(fileName, encoding='windows-1252') as csvFile:
        # reads the csv file using csv reader 
        reader = csv.reader(csvFile)
        # iterate through each row in csv file
        for row in reader:
            # if the first value of the row is not "Name"
            if row[0] != "Name":
                # reassigns the first value of the row
                name = row[0]
                # new dictionary is created to store the data for the person
                people[name] = {}
                # iterate through the range of years
                for year in range(startYear, endYear):
                    # retrieve the frequency value for the current year and person 
                    frequency = row[year - startYear + 2].replace(',', '')
                    # convert the frequency value to an integer and store it in the dictionary
                    people[name][year] = int(frequency)
                # store the count of the person's name in the names dictionary
                names[name] = count
                count += 1 # increments count by 1

    #  ranks each person in the people dictionary based on their frequency in each year #

    # iterates through each year
    for year in range(startYear, endYear):
      # gets list of people's names sorted by their frequency in the given year
        sortedFrequencyPeople = sorted(
        people.keys(),
         key=lambda x: people[x].get(year, 0), # sort by frequency or 0 if missing
         reverse=True, # sorts in descending order
)
        # assigns the rank to each person based on their frequency in a given year
        for j, person in enumerate(sortedFrequencyPeople, 1):
            people[person]["rank_{}".format(year)] = j

    # writes a new output to a csv file
    with open(fn, "w") as file:
        writer = csv.writer(file)
       # iterates through each year between startYear and endYear
        for year in range(startYear, endYear):
            # creates a list of tuples with each tuple containing the name and rank for each person for the given year
            rankedList = [(name, people[name]["rank_{}".format(year)]) for name in people.keys() if "rank_{}".format(year) in people[name]]
            # sorts the rankedList based on rank
            rankedList.sort(key=lambda x: people[x[0]].get(year, 0), reverse=True)

            # iterates through each person in the rankedList and writes their informatio to the CSV file
            for person in rankedList:
                writer.writerow([year, person[0].title(), names[person[0]], people[person[0]]["rank_{}".format(year)]])


# output files
if __name__ == "__main__":
    import sys
    main(sys.argv, "BritishColumbia_M.csv", 1)
    main(sys.argv, "BritishColumbia_F.csv", 2)

    

