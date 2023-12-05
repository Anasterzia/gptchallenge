import csv
from pygments.lexers import guess_lexer
from pygments.util import ClassNotFound
from guesslang import Guess

# Create an instance of Guess
guess = Guess()

def detect_code_or_text(input_text):
    try:
        lexer = guess_lexer(input_text)
        language = guess.language_name(input_text)
        print(f"Opening CSV file: {language} but lexer said {lexer.name}")
        return language
    except ClassNotFound:
        return "Plain text."

# Example usage:
# Input CSV file path
csv_file_path = input("Enter the path to the CSV file: ")

# Print message indicating the file is being opened
print(f"Opening CSV file: {csv_file_path}")
delimiter = ';'
# Read CSV file line by line and compare columns

with open(csv_file_path, 'r', newline='', encoding='utf-8') as csv_file:
    # Use csv.reader with the specified delimiter
    csv_reader = csv.reader(csv_file, delimiter=delimiter)
    modified_rows = []

    
    for row in csv_reader:
        if len(row) >= 10:  # Ensure the 11th column exists
            textforcheck = row[9]
            result = detect_code_or_text(textforcheck)
            row.append(result)  # Append the result as a new column

        if len(row) >= 2:  # Ensure there's at least one column before the last one
            codeforcheck = row[-2]
            result1 = detect_code_or_text(codeforcheck)
            row.append(result1)  # Append the result as a new column

        modified_rows.append(row)

# Write the modified rows back to the original CSV file with semicolon as delimiter
with open(csv_file_path, 'w', newline='', encoding='utf-8') as csv_file:
    csv_writer = csv.writer(csv_file, delimiter=delimiter)
    csv_writer.writerows(modified_rows)

print(f"Output written to {csv_file_path}")
