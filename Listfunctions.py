# Import necessary libraries
import os
import openpyxl
import pandas as pd

# Setting up the working directory
folder = 'C:\CodeLab'
os.chdir(folder)

# Define a class for the management of test file paths
class TestFile:
    xlsx = r"C:\CodeLab\TestFile.xlsx"

# Create a new Excel workbook for output
output_file = openpyxl.Workbook(TestFile.xlsx)

# Define a function to separate data based on gender
def separate_gender(filename):
    from openpyxl import Workbook
    wb = Workbook(TestFiles.xlsx)
    df = pd.read_excel("C:\CodeLab\TestFiles.xlsx")  # Read the Excel file

    # Data separation based on gender differences
    female_data = df[df['Gender'] == 'F']
    male_data = df[df['Gender'] == 'M']

    return female_data, male_data

# Define a function to count the number of female and male students
def count_gender(filename):
    df = pd.read_excel("C:\CodeLab\TestFiles.xlsx")
    # Count number of both female and male students
    female_count = df[df['Gender'] == 'F'].shape[0]  # Count female students
    male_count = df[df['Gender'] == 'M'].shape[0]  # Count male students
    return female_count, male_count

# Define a function to save data to an Excel file
def save_to_excel(data, filename):
    data.to_excel(filename, index=False)

# Define a class for managing test files
class TestFiles:
    xlsx = r"C:\CodeLab\TestFiles.xlsx"

# Separate data based on gender
female_data, male_data = separate_gender(TestFiles.xlsx)

# Count the number of female and male students
female_count, male_count = count_gender(TestFiles.xlsx)

# Output results
print("Female data: ")
print(female_data)
print("Male data: ")
print(male_data)
print("Total number of female students", female_count)
print("Total number of male students", male_count)

# Ensure the output directory exists
output_directory = r"C:\CodeLab"
os.makedirs(output_directory, exist_ok=True)

# Save the results to new Excel files
female_output_file = os.path.join(output_directory, "FemaleStudents.xlsx")
male_output_file = os.path.join(output_directory, "MaleStudents.xlsx")

save_to_excel(female_data, female_output_file)
save_to_excel(male_data, male_output_file)
