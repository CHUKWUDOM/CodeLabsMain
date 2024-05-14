import pandas as pd
import csv
import re
import glob
import json
from constraints import *

def read_excel(file_path, sheet_names):
    """Read specified sheets from an Excel file and extract student names."""
    sheets_data = [pd.read_excel(file_path, sheet_name=sheet) for sheet in sheet_names]

    # Extract the column named 'Student Name' from both sheets and combine them
    combined_names = pd.concat([sheet['Student Name'] for sheet in sheets_data], ignore_index=True)

    # Split the names into first and other names
    split_names = combined_names.str.split(expand=True)

    combined_df = pd.DataFrame()
    combined_df['First Name'] = split_names[0]  # The first name
    combined_df['Mid Name'] = split_names[1]  # Middle name
    combined_df['Second Mid'] = split_names[2]  # Third name
    combined_df['Last Name'] = split_names[3]  # Last Name

    return combined_df

def generate_emails(combined_df):
    """Generate email addresses from the combined DataFrame of student names."""
    first_letter = combined_df['First Name'].str[0]
    mid_name = combined_df['Mid Name']
    sec_mid_name = combined_df['Second Mid']
    last_name = combined_df['Last Name']

    emails = []
    for first, mid, sec_mid, last in zip(first_letter, mid_name, sec_mid_name, last_name):
        if pd.isna(last):
            last = sec_mid if pd.notna(sec_mid) else mid
        email = f"{first.lower()}{last.lower()}@gmail.com"
        emails.append([email])

    return emails

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
