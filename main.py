# main.py

from function import *
from constraints import *

def main():
    # Read the Excel sheets and extract names
    combined_df = read_excel(EXCEL_FILE, SHEET_NAMES)

    # Generate emails from the extracted names
    emails = generate_emails(combined_df)

    # Separate data based on gender
    female_data, male_data = separate_gender(EXCEL_FILE)

    # Count the number of female and male students
    female_count, male_count = count_gender(EXCEL_FILE)

    # List names with special characters
    names_with_special_chars = list_names_with_special_characters(EXCEL_FILE)

    # Save data to CSV
    save_to_csv(emails, CSV_EMAIL)
    save_to_csv(female_data.values.tolist(), CSV_FEMALE)
    save_to_csv(male_data.values.tolist(), CSV_MALE)
    save_to_csv([[female_count, male_count]], CSV_GENDER_COUNT)
    save_to_csv([names_with_special_chars], CSV_SPECIAL_NAMES)

    # Save the results to new TSV files
    save_to_tsv(emails, EMAIL_TSV)
    save_to_tsv(female_data.values.tolist(), FEMALE_TSV)
    save_to_tsv(male_data.values.tolist(), MALE_TSV)
    save_to_tsv([[female_count, male_count]], GENDER_COUNT_TSV)
    save_to_tsv([names_with_special_chars], SPECIAL_NAMES_TSV)

    # Load CSV files
    df_list = load_csv_files(CSV_FILE_PATTERN)

    # Merge DataFrames
    merged_df = merge_dataframes(df_list)

    # Shuffle DataFrame
    shuffled_df = shuffle_dataframe(merged_df)

    # Save shuffled DataFrame in various formats
    save_dataframe(shuffled_df, MERGED_CSV, 'csv')
    save_dataframe(shuffled_df, MERGED_TSV, 'tsv')
    save_dataframe(shuffled_df, MERGED_JSON, 'json')
    save_dataframe(shuffled_df, MERGED_JSONL, 'jsonl')

if __name__ == "__main__":
    main()
