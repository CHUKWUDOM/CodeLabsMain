## Saving progress
This Python script is designed to process data from Excel files and generate CSV, TSV, and JSON files containing various student information. It includes functions to read Excel sheets, generate emails, separate data based on gender, count the number of female and male students, list names with special characters, and more.

## Installation
1. Clone the repository or download the script files (`main.py`, `functions.py`, `constraints.py`).
2. Ensure you have Python installed on your system (version 3.6 or later).
3. Install the required dependencies by running `pip install pandas`.

## Usage
1. Place your Excel file (`Test Files.xlsx`) in the same directory as the script files.
2. Adjust the sheet names in the `constraints.py` file if necessary.
3. Run the `main.py` script using Python: `python main.py`.
4. The script will process the data and generate the following files:
   - `email.csv`: CSV file containing generated email addresses.
   - `FemaleStudents.tsv` and `MaleStudents.tsv`: TSV files containing data of female and male students, respectively.
   - `StudentsPerGender.csv`: CSV file containing the count of female and male students.
   - `StudentsWithSpecialNames.csv`: CSV file containing names of students with special characters.
   - `merged_shuffled.csv` and `merged_shuffled.tsv`: CSV and TSV files containing merged and shuffled student data.
   - `merged_shuffled.json` and `merged_shuffled.jsonl`: JSON and JSON Lines files containing merged and shuffled student data in JSON format.
   - `special_format.json` and `special_format.jsonl`: JSON and JSON Lines files containing student data in a special JSON format.

## Functionality
### `functions.py`
- `read_excel(file_path, sheet_names)`: Reads specified sheets from an Excel file and extracts student names.
- `generate_emails(combined_df)`: Generates email addresses from the combined DataFrame of student names.
- `separate_gender(filename)`: Separates data based on gender.
- `count_gender(filename)`: Counts the number of female and male students.
- `list_names_with_special_characters(filename)`: Lists names of students with special characters.
- `save_to_csv(data, filename)`: Saves a list of tuples to a CSV file.
- `save_to_tsv(data, filename)`: Saves data to a TSV file.
- `load_csv_files(pattern)`: Loads all CSV files matching the given pattern into a list of DataFrames.
- `merge_dataframes(df_list)`: Merges a list of DataFrames into a single DataFrame.
- `shuffle_dataframe(df)`: Shuffles the DataFrame.
- `save_dataframe(df, file_name, file_format, sep=',')`: Saves the DataFrame to a file in various formats.
- `row_to_special_format(row)`: Converts a DataFrame row to a special JSON format.
- `save_special_format(df, json_file, jsonl_file)`: Saves the DataFrame in the special JSON format.

### `constraints.py`
- Defines paths to input Excel file and output files.
- Defines sheet names, file patterns, and output file names.
