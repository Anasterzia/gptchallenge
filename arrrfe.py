import csv

# Input CSV file path
csv_file_path = "/Users/anastassia/Desktop/arfmake.csv"

# Output ARFF file path
arff_file_path = "/Users/anastassia/Desktop/arfmake.arff"

# Open the CSV file
with open(csv_file_path, 'r') as csv_file:
    # Read CSV data
    csv_reader = csv.reader(csv_file, delimiter=';')
    data = list(csv_reader)

# Extract attribute names from the header (assuming the first row is the header)
attributes = data[0]

# Remove the header from the data
data = data[1:]

# Open the ARFF file in write mode
with open(arff_file_path, 'w') as arff_file:
    # Write ARFF header
    arff_file.write("@relation your_relation_name\n\n")

    # Write ARFF attributes
    for attribute in attributes:
        arff_file.write(f"@attribute {attribute} string\n")

    # Write ARFF data
    arff_file.write("\n@data\n")
    for row in data:
        # Fill missing values with '?'
        row += ['?'] * (len(attributes) - len(row))
        arff_file.write(','.join(row) + '\n')

print(f"Conversion completed. ARFF file saved at: {arff_file_path}")
