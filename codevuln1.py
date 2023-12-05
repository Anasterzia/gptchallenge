import csv
import subprocess
import tempfile

# Function to run Snyk analysis for the given code and language
def run_snyk(code, language):
    try:
        # Create a temporary directory
        with tempfile.TemporaryDirectory() as temp_dir:
            # Create a temporary file within the directory
            temp_file_path = tempfile.mktemp(suffix=f'.{language}', dir=temp_dir)
            
            # Write the code to the temporary file
            with open(temp_file_path, 'w') as temp_file:
                temp_file.write(code)

            # Replace the following command with the actual Snyk analysis command
            snyk_command = f"snyk code test "

            # Run the Snyk command using subprocess.run
            result = subprocess.run(snyk_command, shell=True, capture_output=True, text=True)

            # Print the standard output and standard error
            print(result.stdout)
            print(result.stderr)

            # Return the result
            return result.stdout.strip()

    except subprocess.CalledProcessError as e:
        # Handle the exception, print the error, and return a default result
        print(f"Snyk analysis failed: {e}")
        return "Snyk analysis failed."

# Example usage:
# Input CSV file path
csv_file_path = input("Enter the path to the CSV file: ")

# Print message indicating the file is being opened
print(f"Opening CSV file: {csv_file_path}")

# Read the first few lines of the file to detect the delimiter
with open(csv_file_path, 'r', newline='', encoding='utf-8') as csv_file:
    dialect = csv.Sniffer().sniff(csv_file.read(1024))

# Use the detected delimiter in csv.reader
with open(csv_file_path, 'r', newline='', encoding='utf-8') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=dialect.delimiter)
    modified_rows = []

    for row in csv_reader:
        if len(row) >= 2:  # Ensure there's at least one column before the last one
            code_for_check = row[-3]
           # result_code_detection = detect_code_or_text(code_for_check)
           # row.append(result_code_detection)  # Append code detection result as a new column

            # Assuming the second-to-last column contains the language
            language = row[-4].lower()
            print("Language:", language)
            print("code:", code_for_check)

            # Run Snyk with the detected language
            snyk_result = run_snyk(code_for_check, language)
            row.append(snyk_result)  # Append Snyk results as a new column

        modified_rows.append(row)

# Write the modified rows back to the original CSV file with the detected delimiter
with open(csv_file_path, 'w', newline='', encoding='utf-8') as csv_file:
    csv_writer = csv.writer(csv_file, delimiter=dialect.delimiter)
    csv_writer.writerows(modified_rows)

print(f"Snyk results written to {csv_file_path}")
