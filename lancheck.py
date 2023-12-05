import csv
from pygments.lexers import guess_lexer
from pygments.util import ClassNotFound

def detect_code_or_text(input_text):
    try:
        lexer = guess_lexer(input_text)
        return "{lexer.name}."
    except ClassNotFound:
        return "Plain text."

# Example usage:
# Input CSV file path
csv_file_path = "/Users/anastassia/Desktop/forthearf.csv"

# Output CSV file path (will overwrite the input file)
output_csv_file_path = csv_file_path

print(f"Opening CSV file: {csv_file_path}")
delimiter = ';'
# Read CSV file line by line and compare columns
with open(csv_file_path, 'r') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=delimiter)
    rows = list(csv_reader)

# Open the original file in write mode to overwrite its content
with open(csv_file_path, 'w', newline='') as csv_file:
    csv_writer = csv.writer(csv_file, delimiter=delimiter)
  
    for row in rows:
        if len(row) > 0:
                code = row[9]
                print("Columns code:")
                print(code)
                codenot=detect_code_or_text(code)
                row.append(codenot)
        csv_writer.writerow(row)

print(f"Results written to {csv_file_path}")

