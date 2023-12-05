import csv
import requests
from bs4 import BeautifulSoup
from difflib import SequenceMatcher
from fuzzywuzzy import fuzz
import Levenshtein

def get_webpage_text(url):
    url = url.lstrip('\ufeff')
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    return soup.get_text()

def preprocess_text(text):
    lines = text.splitlines()
    non_empty_lines = [line for line in lines if line.strip()]
    return ' '.join(non_empty_lines)

def code_similarity(code_block, webpage_text):
    similarity_ratio = SequenceMatcher(None, code_block, webpage_text).ratio()
    return similarity_ratio

def count_lines_in_webpage(code, webpage_text):
    code_lines = code.splitlines()
    count = 0
    counter = 0

    for line in code_lines:
        parts = line.split('\x0b')
        for part in parts:
            counter += 1
            print("", counter, ":", part.strip(), "\n")
            if part.strip() in webpage_text:
                count += 1

    return count, counter

# Input CSV file path
csv_file_path = "/Users/anastassia/Desktop/forthearf.csv"

# Print message indicating the file is being opened
print(f"Opening CSV file: {csv_file_path}")
delimiter = ';'

# Read all rows from the original CSV file
with open(csv_file_path, 'r') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=delimiter)
    rows = list(csv_reader)

# Open the original file in write mode to overwrite its content
with open(csv_file_path, 'w', newline='') as csv_file:
    csv_writer = csv.writer(csv_file, delimiter=delimiter)

    for row in rows:
        if len(row) > 0:
            if "commit" in row[0].lower() or "pull request" in row[0].lower():
                web_url = row[1] + "?diff=split"
                code = row[-3]

                print("Columns url:")
                print(web_url)
                print("Columns code:")
                print(code)

                webpage_text = get_webpage_text(web_url)
                code_lines = code.splitlines()
                code_text = preprocess_text('\n'.join(code_lines))
                webpage_text = preprocess_text(webpage_text)

                lines_count, counter = count_lines_in_webpage(code, webpage_text)
                similarity_ratio = code_similarity(code_text, webpage_text)

                print("Columns url1:")
                print(web_url)

                # Calculate the usage ratio
                usage_ratio = lines_count / counter if counter != 0 else 0

                # Append the additional information to the row
                row.append(lines_count)
                row.append(counter)
                row.append(usage_ratio)  # Add the new column
                
            else:
                 lines_count = 0
                 counter = 0
                 usage_ratio = 0
                 row.append(lines_count)
                 row.append(counter)
                 row.append(usage_ratio)

        # Write the modified row to the CSV file
        csv_writer.writerow(row)

print(f"Results written to {csv_file_path}")
