import pandas as pd

# Read the CSV file with semicolon delimiter
input_csv_path = "/Users/anastassia/Desktop/wordswork.csv"
output_csv_path = "/Users/anastassia/Desktop/wordswork.csv"  # Note: Same input and output paths

# Read the CSV file with semicolon delimiter
df = pd.read_csv(input_csv_path, delimiter=";")

# Define the patterns to replace
patterns_to_replace = {
    r".*USING.*": "USE",
    r".*SECURITY.*": "SECURITY",
 

    
    # Add more patterns as needed
}

# List of programming languages to replace as "PROGRAMMING LANGUAGE"
programming_languages = [
   "AUTHENTICATION"
    # Add more operating systems as needed
]

# Add programming languages to the patterns to replace
for lang in programming_languages:
   patterns_to_replace[f".*{lang}.*"] = "SECURITY"

# Function to replace patterns in a DataFrame
def replace_patterns(df):
    for pattern, replacement in patterns_to_replace.items():
        for column in df.columns:
            df[column] = df[column].str.replace(pattern, replacement, regex=True)
    return df

# Replace patterns in all columns
df = replace_patterns(df)

# Save the modified DataFrame to the same CSV file with semicolon delimiter
df.to_csv(output_csv_path, index=False, sep=";")

print("Replacement completed. The modified CSV is saved at:", output_csv_path)
