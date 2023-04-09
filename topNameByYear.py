import os 

# Hafsa's Functions

def top_name_by_year(gender, province):
    
    # Define the file name based on user input
    # Converts the province input to lowercase and then checks for a match against a lowercase and space-removed version of each province name
    if province.replace(' ', '').lower() == "alberta":
        file_name = f"alberta_{gender.upper()}.csv"
    elif province.replace(' ', '').lower() == "britishcolumbia":
        file_name = f"BritishColumbia_{gender.upper()}.csv"
    elif province.replace(' ', '').lower() == "newbrunswick":
        file_name = f"NewBrunswick_{gender.upper()}.csv"
    elif province.replace(' ', '').lower() == "novascotia":
        file_name = f"NovaScotia_{gender.upper()}.csv"
    else:
        print("Invalid province name. Please try again.")
        return {}

    
    # Open the file containing the baby names data for the specified province and gender
    with open(file_name, 'r') as file:
        # skips the first line of file
        next (file)
        
        # Initialize a dictionary to store the top name for each year
        top_names = {}
        # Iterate over each line in the file
        for line in file:
            # Split the line into a list of values
            year, name, number, rank = line.strip().split(',')
            # Check if the name matches the specified gender
            if gender.lower() in name.lower():
                # Check if the year is already in the dictionary
                if year in top_names:
                    # Check if the current name has a higher frequency than the previous top name
                    if int(number) > int(top_names[year][1]):
                        # Update the top name for the year
                        top_names[year] = (name, number)
                else:
                    # Add the name as the top name for the year
                    top_names[year] = (name, number)
        # Sort the dictionary by year
        top_names = dict(sorted(top_names.items(), key=lambda x: int(x[0])))
    # Return the dictionary of top names
    #return top_names
    print("{:<5} {:<10} {}".format("Year", "Name", "Frequency"))
    for year, (name, freq) in top_names.items():
        print("{:<5} {:<10} {}".format(year, name, freq))

# # asks for user input and stores inside variable
# gender = input("Enter the gender (M/F): ")

# # Check if gender is either M or F
# if gender.upper() not in ["M", "F"]:
#     print("Error. Please make sure to only enter in 'M' or F'")
#     exit()

# # asks for user input and stores inside variable
# print("\nCurrent Provinces - British Columbia, Alberta, New Brunswick, Nova Scotia")
# province = input("Please enter the province: ")



# # calls function and prints result 


