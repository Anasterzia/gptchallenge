import csv
from difflib import SequenceMatcher

def calculate_similarity_and_common_lines(text1, text2):
    # Using SequenceMatcher to get a similarity ratio
    similarity_ratio = SequenceMatcher(None, text1, text2).ratio()

    # Split the texts into lines
    lines1 = set(text1.splitlines())
    lines2 = set(text2.splitlines())

    # Calculate common lines
    common_lines = lines1.intersection(lines2)

    return similarity_ratio, common_lines

# Input CSV file path
csv_file_path = "/Users/anastassia/Desktop/testforwordincolumn.csv"

# Output CSV file path (will overwrite the input file)
output_csv_file_path = csv_file_path

# Columns to compare
column1_index = -2  # Index of the first column (0-based)
column2_index = -1  # Index of the second column (0-based)

# List to store modified rows
rows_with_similarity = []

# Read CSV file line by line and compare columns
with open(csv_file_path, 'r', encoding='utf-8', errors='ignore') as csv_file:
    # Use csv.reader
    csv_reader = csv.reader(csv_file, delimiter=';')

    # Iterate through the rows
    for row in csv_reader:
        # Check if the row has the specified columns
        if len(row) > max(column1_index, column2_index):
            # Get the texts from the specified columns
            text1 = row[column1_index]
            text2 = row[column2_index]
            print("column1_index = 9")
            print(text1)
            print("column1_index = 12")
            print(text2)
            # Calculate similarity and common lines
            similarity, common_lines = calculate_similarity_and_common_lines(text1, text2)

            # Add new columns to the row
            row.append(similarity)
            row.append(len(common_lines))
            row.append(', '.join(common_lines))

            # Append the modified row to the list
            rows_with_similarity.append(row)

# Write the modified rows back to the same CSV file
with open(output_csv_file_path, 'w', newline='', encoding='utf-8') as csv_file:
    # Use csv.writer
    csv_writer = csv.writer(csv_file, delimiter=';')

    # Write the rows with additional columns
    csv_writer.writerows(rows_with_similarity)

print(f"Results written to {output_csv_file_path}")
