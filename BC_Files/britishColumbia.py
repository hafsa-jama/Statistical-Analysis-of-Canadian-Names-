# To Run: chmod 777 EVERYTHING
#         python3 ./britishColumbia.py BritishColombiaBoys_1922_2021.csv BritishColombiaGirls_1922_2021.csv
# Format: year,name,frequency,rank

import csv

# define a class record to store information about each name
class Record:
    headers = ('name', 'years', 'rank')

    # degine the constructor for the class
    def __init__(self, name):
        self.name = name
        self.years = {} 
        self.rank = {} 

    # define a method to update the rank for a specific year
    def update_record_rank(self, year, rank):
        self.rank[year] = rank

    # define a method to get the years for which there is data for the name
    def get_record_years(self):
        return self.years

    # define a method to get the rank for a specific year
    def get_record_rank(self, year):
        return self.rank[year]

# define a function to sort the frequency of a name for a specific year
def sort_frequency(record, year):
    years = record.years
    if year in years:
        return (-int(years[year]), record.name, ord(record.name[0]))
    else:
        return (0, record.name, ord(record.name[0]))

# main function
def main(input_file, output_file):

    # initalize the varibales for start and end years for the data
    startYear = 1922
    endYear = 2021

    # create a dictionary to store the index of each record by name
    records = []

    # create a dictionary to store the index od each record by name
    record_names = {}

    record_count = 0 # counter for number of records

    # opens the input file
    with open(input_file, encoding="windows-1252") as csvfile:
        # iterate through each row in the CSV file
        reader = csv.reader(csvfile)
        for row in reader:
            if row[0] != "Name":
                # create a new Record object for the name
                record = Record(row[0])

                # store the data for each year for the record
                years = record.years
                for year in range(startYear, endYear):
                    years[year] = row[year - startYear + 2].replace(',', '') 
                records.append(record) # adds the record to the list of records
                record_names[row[0]] = record_count # store the index of the record by name in the dictionary
                record_count += 1 # increment the counter for the number of records

    # iterate through each year in the data
    for year in range(startYear, endYear):
        # sort the records by frequency for the year 
        sorted_frequency_records = sorted(records, key=lambda x: sort_frequency(x, year))

        # updates the rank for each record for the year
        for j, record in enumerate(sorted_frequency_records, 1):
            records[record_names[record.name]].update_record_rank(year, j)

    # opens the output file and uses the CSV writer to write data to the file
    with open(output_file, 'w', newline='') as file:
        writer = csv.writer(file)

        # write the header row
        writer.writerow(['Year', 'Name', 'Count', 'Rank'])

        # iterate through each year in the data
        for year in range(startYear, endYear):
            # creates a list of tuples with each tuple containing the name and rank for each person for the given year
            rankedList = [(person.name, person.get_record_rank(year), int(person.get_record_years().get(year, 0))) for person in records if year in person.rank]
            # sorts the rankedList based on rank
            rankedList.sort(key=lambda x: x[1])

            # iterates through each person in the rankedList and writes their information to the CSV file
            for person in rankedList:
                writer.writerow([year, person[0].upper().replace("_", " "), person[2], person[1]])


# output files
if __name__ == "__main__":
    main("BritishColombiaBoys_1922_2021.csv", "BritishColumbia_M.csv")
    main("BritishColombiaGirls_1922_2021.csv", "BritishColumbia_F.csv")