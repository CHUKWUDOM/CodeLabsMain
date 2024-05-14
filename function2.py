import pandas as pd


def read_excel():
    # We read data from the two sheets on excel
    sheet_3b = pd.read_excel('C:\\Users\\andyk\\Downloads\\Test Files.xlsx', sheet_name='3B')
    sheet_3c = pd.read_excel('C:\\Users\\andyk\\Downloads\\Test Files.xlsx', sheet_name='3C')

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