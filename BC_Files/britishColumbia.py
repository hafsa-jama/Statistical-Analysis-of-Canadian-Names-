# To Run: chmod 777 EVERYTHING
#         python3 ./britishColumbia.py BritishColombiaBoys_1922_2021.csv BritishColombiaGirls_1922_2021.csv
# Format: year,name,frequency,rank

import csv

# define a class record to store information about each name
class Record:
    headers = ('name', 'years', 'rank')

    # define the constructor for the class
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

    # define a method to get the frequency for a specific year
    def get_frequency(self, year):
      return int(self.years.get(year, 0))
    
# define a function to sort the frequency of a name for a specific year
def sort_frequency(record, year):
    years = record.years
    if year in years:
        return (-int(years[year]), record.name, ord(record.name[0]))
    else:
        return (0, record.name, ord(record.name[0]))

# main function 
def main(input_file, output_file):

    # initlaize variables for start at end year
    start_year = 1922
    end_year = 2022

    records = []   # initlaize a list for records
    record_names = {} # iniltaize a dictonary 
    record_count = 0 # counter 

    # reads file
    with open(input_file, encoding="windows-1252") as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            if row[0] != "Name":
                record = Record(row[0])
                years = record.years
                for year in range(start_year, end_year):
                    years[year] = row[year - start_year + 2].replace(',', '')
                records.append(record)
                record_names[row[0]] = record_count
                record_count += 1

    # writes output to new files
    with open(output_file, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Year", "Name", "Count", "Rank"])  

        for year in range(start_year, end_year):
            # sort the records by frequency for the year 
            sorted_frequency_records = sorted(records, key=lambda x: sort_frequency(x, year))

            # updates the rank for each record for the year
            for j, record in enumerate(sorted_frequency_records, 1):
                records[record_names[record.name]].update_record_rank(year, j)

            # Compute the rank for each record based on the number of occurrences in the current year
            temp = -1
            new_rank = 0

            ranked_list = [(record.name, record.get_record_rank(year), record.get_frequency(year)) for record in records if year in record.rank]
            ranked_list.sort(key=lambda x: x[2], reverse=True)
            for record in ranked_list:
                years = records[record_names[record[0]]].get_record_years()
                if temp == -1:
                    temp = years[year]
                    new_rank = 1
                else:
                    if temp != years[year]:
                        temp = years[year]
                        new_rank += 1
                        
                # iterates through each person in the rankedList and writes their information to the CSV file
                if years[year] != '0':
                    writer.writerow([year, record[0].upper(), record[2], new_rank])


# output files
if __name__ == "__main__":
    main("BritishColombiaBoys_1922_2021.csv", "BritishColumbia_M.csv")
    main("BritishColombiaGirls_1922_2021.csv", "BritishColumbia_F.csv")