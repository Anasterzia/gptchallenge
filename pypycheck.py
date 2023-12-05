import csv
import requests
from bs4 import BeautifulSoup
from difflib import SequenceMatcher
from fuzzywuzzy import fuzz
import Levenshtein

def get_webpage_text(url):
    url = url.lstrip('\ufeff')
    # s    url = url.lstrip('?diff=split')
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    return soup.get_text()

def preprocess_text(text):
    # Remove empty lines
    lines = text.splitlines()
    non_empty_lines = [line for line in lines if line.strip()]
    return ' '.join(non_empty_lines)

def code_similarity(code_block, webpage_text):
    # Using SequenceMatcher to get a similarity ratio
    similarity_ratio = SequenceMatcher(None, code_block, webpage_text).ratio()
    return similarity_ratio

def count_lines_in_webpage22(code_lines, webpage_text):
    print("Number of lines in code_lines:", len(code_lines))
    count = 0
    counter = 0
    for line in code_lines:
        parts = line.split('\x0b')
        for part in parts:
            counter += 1
            print("", counter, ":", part.strip(), "\n")
            if part.strip() in webpage_text:
                count += 1
    
    return count
    
def count_lines_in_webpage(code, webpage_text):
    # Split the code column into lines
    code_lines = code.splitlines()
    
    print("Number of lines in code_lines:", len(code_lines))
    count = 0
    counter = 0

    # Iterate through each line in the code
    for line in code_lines:
        # Split each line by '\x0b'
        parts = line.split('\x0b')
        
        # Iterate through each part
        for part in parts:
            # Remove empty lines from each part
            part_lines = [pl for pl in part.splitlines() if pl.strip()]
            # Iterate through each non-empty line in the part
            for part_line in part_lines:
                counter += 1
                print("", counter, ":", part_line.strip(), "\n")
                
                # Check if the line is found in the webpage text
                if part_line.strip() in webpage_text:
                    count += 1
           
    return count, counter

def levenshtein_distance(text1, text2):
    return Levenshtein.distance(text1, text2)

def fuzzywuzzy_similarity(text1, text2):
    return fuzz.token_sort_ratio(text1, text2)
    
def fuzzywuzzy_similarity1(text1, text2):
    return fuzz.token_set_ratio(text1, text2)
    
def fuzzywuzzy_similarity2(text1, text2):
    return fuzz.partial_ratio(text1, text2)
    

# Input CSV file path
csv_file_path = input("Enter the path to the CSV file: ")
# Output file path
output_file_path = "outputcomm.txt"

# Print message indicating the file is being opened
print(f"Opening CSV file: {csv_file_path}")
delimiter = ';'
# Read CSV file line by line and compare columns
with open(csv_file_path, 'r') as csv_file:
    # Use csv.reader with the specified delimiter
    csv_reader = csv.reader(csv_file, delimiter=delimiter)

    # Iterate through the rows until there are no more rows left
    for row in csv_reader:
        if len(row) >= 1:
            # Extract web URL and code from the row
            web_url = row[0]
            code = row[-1]

            # Print columns url
            print("Columns url:")
            print(web_url)
            print("Columns code:")
            print(code)

            # Fetch webpage text
            webpage_text = get_webpage_text(web_url)

            # Preprocess text to remove new lines and empty lines
            code_lines = code.splitlines()
            code_text = preprocess_text('\n'.join(code_lines))
            webpage_text = preprocess_text(webpage_text)

            # Count lines in the webpage
            #lines_count = count_lines_in_webpage(code_lines, webpage_text)
            lines_count, counter = count_lines_in_webpage(code, webpage_text)


            # Calculate additional similarity metrics
           # levenshtein_dist = levenshtein_distance(code_text, webpage_text)
           # fuzzywuzzy_sim = fuzzywuzzy_similarity(code_text, webpage_text)
            #fuzzywuzzy_sim1 = fuzzywuzzy_similarity1(code_text, webpage_text)
            #fuzzywuzzy_sim2 = fuzzywuzzy_similarity2(code_text, webpage_text)

            # Calculate similarity ratio
            similarity_ratio = code_similarity(code_text, webpage_text)

            # Print every variable
            print("Columns url1:")
            print(web_url)
            with open(output_file_path, 'a') as output_file:
                output_file.write("\nWebpage Text for {}: ;".format(web_url))
                output_file.write("Similarity Ratio: {};".format(similarity_ratio))
                output_file.write("Lines Found in Webpage: {};".format(lines_count))
                output_file.write("Length of Webpage Text: {};".format(len(webpage_text)))
                output_file.write("Length of Code Text: {};".format(counter))
               #output_file.write("Levenshtein Distance: {};".format(levenshtein_dist))
                #output_file.write("Fuzzywuzzy sort Similarity: {};".format(fuzzywuzzy_sim))
                #output_file.write("Fuzzywuzzy set Similarity1: {};".format(fuzzywuzzy_sim1))
                #output_file.write("Fuzzywuzzy partial Similarity2: {};".format(fuzzywuzzy_sim2))
                output_file.write("\n----------------------------------------\n")

print(f"Results written to {output_file_path}")

