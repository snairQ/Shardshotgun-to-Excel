import re
import csv
import pandas as pd
import sys
import os

def process_file(file_path):
    # Define the pattern for identifying data rows (excluding lines like '----+------+...')
    data_row_pattern = re.compile(r'^\s*[0-9A-F]{32}\s*\|')

    # Variables to store the extracted headers and data
    headers = []
    data = []

    with open(file_path, 'r') as file:
        for line in file:
            # Remove leading and trailing whitespaces
            line = line.strip()

            # Skip empty lines
            if not line:
                continue

            # Check if the line is a header line
            if '|' in line and line[0].isalpha():
                # Extract and clean headers
                headers = [header.strip() for header in line.split('|')]
            elif data_row_pattern.match(line):
                # Extract and clean data rows
                row = [value.strip() for value in line.split('|')]
                data.append(row)

    return headers, data

# Check if a file path was provided
if len(sys.argv) < 2:
    print("Usage: python shardshotgun_extractor.py <file_path>")
    sys.exit(1)

# Process the file
file_path = sys.argv[1]  # Get the file name from the command line

# Check if the file exists
if not os.path.isfile(file_path):
    print(f"Error: File '{file_path}' not found.")
    sys.exit(1)

# Check if the file is readable
if not os.access(file_path, os.R_OK):
    print(f"Error: File '{file_path}' is not readable.")
    sys.exit(1)

# Check if the file is empty
if os.path.getsize(file_path) == 0:
    print(f"Error: File '{file_path}' is empty.")
    sys.exit(1)

try:
    headers, data = process_file(file_path)
except Exception as e:
    print(f"Error processing file: {e}")
    sys.exit(1)

# Check if data was correctly extracted
if not headers or not data:
    print(f"Error: No data was extracted from file '{file_path}'.")
    sys.exit(1)
    
# Write the data to Excel with headers
df = pd.DataFrame(data, columns=headers)
output_file_name = os.path.splitext(os.path.basename(file_path))[0] + '.xlsx'

try:
    df.to_excel(output_file_name, index=False)
except Exception as e:
    print(f"Error writing to Excel file: {e}")
    sys.exit(1)