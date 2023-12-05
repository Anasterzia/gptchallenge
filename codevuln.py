import csv
import subprocess

# Function to detect code or plain text using Pygments
def detect_code_or_text(input_text):
    try:
        # Perform code detection logic using Pygments
        # Replace this with your actual code detection logic
        return "Detected as source code."
    except Exception:
        return "Detected as plain text."

# Function to run SonarQube analysis for the given code and language
def run_sonarqube(code, language):
    try:
        # Replace the following command with the actual SonarQube analysis command
        sonarqube_command = f"sonar-scanner -Dsonar.language={language} -Dsonar.sourceBaseDir=. -Dsonar.sources=-"
        result = subprocess.check_output(sonarqube_command, input=code, text=True, shell=True)
        return result.strip()
    except subprocess.CalledProcessError as e:
        return f"SonarQube analysis failed: {e}"

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
        if len(row) >= 2:  # Ensure there's at least one column before the last one
            code_for_check = row[-1]
            result_code_detection = detect_code_or_text(code_for_check)
            row.append(result_code_detection)  # Append code detection result as a new column

            # Assuming the second-to-last column contains the language
            language = row[-3].lower()
            print("here")
            print(language)
            # Run SonarQube with the detected language
            sonarqube_result = run_sonarqube(code_for_check, language)
            row.append(sonarqube_result)  # Append SonarQube results as a new column

        modified_rows.append(row)

# Write the modified rows back to the original CSV file with semicolon as delimiter
with open(csv_file_path, 'w', newline='', encoding='utf-8') as csv_file:
    csv_writer = csv.writer(csv_file, delimiter=delimiter)
    csv_writer.writerows(modified_rows)

print(f"SonarQube results written to {csv_file_path}")
