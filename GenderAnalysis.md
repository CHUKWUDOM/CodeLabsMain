# Gender Data Analysis README

## Introduction
This repository contains code for analyzing gender data of students stored in an Excel file. The code separates the data based on gender and counts the number of female and male students. Additionally, it saves the separated data into new Excel files.

## Requirements
To run this code, you need the following libraries installed:
- Python (>=3.6)
- openpyxl
- pandas

## Installation
1. Clone this repository to your local machine:
https://github.com/CHUKWUDOM/CodeLabs1
2. Navigate to the project directory
   (_Quinter to give the project directory of the final work here_)
3. Install the required [dependencies](requirements.txt): 
```python
 pip install -r requirements.txt
```
## Usage
1. Set the working directory in the code to the directory where your data file is located:
```python
folder = (Quinter to provide the directory of the data file)
os.chdir(folder)
```
2. Update the path of the input Excel file and the output directory in the code:
```python
class TestFile: # Define a class for the management of test file paths
    xlsx = r"Quinter to give name of the downloaded spreadsheet"

class TestFiles: # Define a class for managing test files
    xlsx = r"C:\CodeLab\TestFiles.xlsx"

output_directory = r"Quinter to give the directory"
```
3. Run the python script
```python
python filename.py # Quinter to give the name of the python file
```
## Output
The code generates the following outputs:   
✓ Separated data of female and male students.   
✓ Total count of female and male students.  
✓ Two Excel files containing separated data of both female and male students.

## License 
This project is licensed under the MIT [License](LICENSE.txt). See the LICENSE file for details.
```python
You can customize it further if necessary!
```

