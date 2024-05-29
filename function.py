import pandas as pd
import csv
import re
import glob
import json
from constraints import *

def read_excel():
    # We read data from the two sheets on excel
    sheet_3b = pd.read_excel('C:\CodeLab\TestFiles.xlsx', sheet_name='3B')
    sheet_3c = pd.read_excel('C:\CodeLab\TestFiles.xlsx', sheet_name='3C')

    # We extract the column named Student name from both sheets
    sheet_3b_names = sheet_3b['Student Name']
    sheet_3c_names = sheet_3c['Student Name']

    # We combine both sheets containing the names into one
    combined = pd.concat([sheet_3b_names, sheet_3c_names], ignore_index=True)

    # We split the name into first and the other names
    split_names = combined.str.split(expand=True)

    combined['First Name'] = split_names[0]  # The first name
    combined['Mid Name'] = split_names[1]    # Middle name
    combined['Second Mid'] = split_names[2]  # Third name
    combined['Last Name'] = split_names[3]   # Last Name

    first_name = combined['First Name']
    mid_name = combined['Mid Name']
    sec_mid_name = combined['Second Mid']
    last_name = combined['Last Name']
    # We get the first letter of the first name
    first_letter = first_name.str[0]

    for first, mid, sec_mid_name,  last in zip(first_letter, mid_name, sec_mid_name, last_name):
        if last is None:
            last = sec_mid_name  # if the last name is not there, the third name becomes the last name

            if sec_mid_name is None:
                last = mid
                # If the person has two names, the middle name which in this case is the second, becomes the last

        print(f"{first.lower()}.{last.lower()}@gmail.com")  # prints out the email


read_excel()

def separate_gender(filename):
    """Separate data based on gender."""
    df = pd.read_excel(filename)  # Read the Excel file

    # Data separation based on gender differences
    female_data = df[df['Gender'] == 'F']
    male_data = df[df['Gender'] == 'M']

    return female_data, male_data

def count_gender(filename):
    """Count the number of female and male students."""
    df = pd.read_excel(filename)
    # Count number of both female and male students
    female_count = df[df['Gender'] == 'F'].shape[0]  # Count female students
    male_count = df[df['Gender'] == 'M'].shape[0]  # Count male students
    return female_count, male_count
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


def list_names_with_special_characters(filename):
    """List names of students with special characters."""
    df = pd.read_excel(filename)  # Read the Excel file

    # Regular expression pattern to find special characters
    special_char_pattern = re.compile(r"[^\w\s]", re.UNICODE)

    # Extract the column named 'Student Name' and find names with special characters
    names_with_special_chars = df[df['Student Name'].str.contains(special_char_pattern, na=False)]

    return names_with_special_chars['Student Name'].tolist()

def save_to_csv(data, filename):
    """Save a list of tuples to a CSV file."""
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        # Write data rows
        writer.writerows(data)

def save_to_tsv(data, filename):
    """Save data to a TSV file."""
    pd.DataFrame(data).to_csv(filename, sep='\t', index=False, header=False)

def load_csv_files(pattern):
    """Load all CSV files matching the given pattern into a list of DataFrames."""
    file_list = glob.glob(pattern)
    return [pd.read_csv(file) for file in file_list]

def merge_dataframes(df_list):
    """Merge a list of DataFrames into a single DataFrame."""
    return pd.concat(df_list, ignore_index=True)

def shuffle_dataframe(df):
    """Shuffle the DataFrame."""
    return df.sample(frac=1).reset_index(drop=True)

def save_dataframe(df, file_name, file_format, sep=','):
    """Save the DataFrame to a file."""
    if file_format == 'csv':
        df.to_csv(file_name, index=False)
    elif file_format == 'tsv':
        df.to_csv(file_name, index=False, sep=sep)
    elif file_format == 'json':
        df.to_json(file_name, orient='records', lines=False)
    elif file_format == 'jsonl':
        df.to_json(file_name, orient='records', lines=True)
    else:
        raise ValueError("Unsupported file format")

def row_to_special_format(row):
    """Convert a DataFrame row to the special JSON format."""
    return {
        "id": str(row.get('id', '')),
        "student_number": str(row.get('student_number', '')),
        "additional_details": [
            {
                "dob": row.get('dob', ''),
                "gender": row.get('gender', ''),
                "special_character": "['yes']" if any(char in str(row.get('Student Name', '')) for char in ["'", "-", "_"]) else "['no']",
                "name_similar": "['no']"  # This is just a placeholder
            }
        ]
    }

def save_special_format(df, json_file, jsonl_file):
    """Save the DataFrame in the special JSON format."""
    special_format_data = [row_to_special_format(row) for _, row in df.iterrows()]
    with open(json_file, 'w') as f:
        json.dump(special_format_data, f, indent=4)
    with open(jsonl_file, 'w') as f:
        for item in special_format_data:
            f.write(json.dumps(item) + "\n")
