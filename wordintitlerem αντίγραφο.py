import pandas as pd

# Read the CSV file with semicolon delimiter
input_csv_path = "/Users/anastassia/Desktop/wordswork.csv"
output_csv_path = "/Users/anastassia/Desktop/wordswork.csv"  # Note: Same input and output paths

# Read the CSV file with semicolon delimiter
df = pd.read_csv(input_csv_path, delimiter=";")

# Define the patterns to replace
patterns_to_replace = {
    r".*ADD.*": "ADD",
    r".*UPDAT.*": "UPDATE",
    r".*UPGRA.*": "UPDATE",
    r".*INSTALL.*": "INSTALL",
    r".*SOURCE.*": "CODE",
    r".*PUSH.*": "GITHUB",
    r".*PULL.*": "GITHUB",
    r"GIT.*": "GITHUB",
    r"COMMIT.*": "GITHUB",
    r"BRANCH.*": "GITHUB",
    r".*RESPONS.*": "RESPONSE",
    r".*QUESTION.*": "PROMPT",
    r".*ASK.*": "PROMPT",
    r".*ANSWER.*": "RESPONSE",
    r".*ERROR.*": "ERROR",
    r".*ISSUE.*": "ISSUE",
    r".*WEB.*": "WEB",
    r".*LINK.*": "WEB",
    r".*HTTP.*": "WEB",
    r".*FIX.*": "FIX",
    r".*CORRECT.*": "CORRECT",
    r".*SPANISH.*": "SPOKEN LANGUAGE",
    r".*PNG.*": "IMAGE",
    r".*TEST.*": "TEST",
    r".*EXAMP.*": "EXAMPLE",
    r".*DEMO.*": "EXAMPLE",
    r".*TEMPLATE.*": "EXAMPLE",
    r"ELSE.*": "FUNCTION",
    r"IF.*": "FUNCTION",
    r"SET.*": "FUNCTION",
    r"GET.*": "FUNCTION",
    r"RETURN.*": "FUNCTION",
    r".*RUN.*": "EXECUTE",
    r".*EXECUT.*": "EXECUTE",
    r".*AUTO.*": "AUTOMATE",
    r".*SQL.*": "PROGRAMMING LANGUAGE",
    r".*CSS.*": "PROGRAMMING LANGUAGE",
    r".*JS.*": "PROGRAMMING LANGUAGE",
    r".*NPM.*": "THIRD PARTY",
    r".*AWS.*": "THIRD PARTY",
    r".*AI.*": "AI",
    r".*GPT.*": "GPT",
    r".*ENDPOPLUGPLUGPLUGINT.*": "REFACTOR",
    r".*LOAD.*": "LOAD",
    r".*BUILD.*": "CREATE",
    r".*BOT.*": "AI",
    r".*TIME.*": "TIME",
    r".*DATE.*": "TIME",
    r".*CACHE.*": "DATA STORAGE",
    r".*DB.*": "DATA STORAGE",
    r".*BASE.*": "DATA STORAGE",
    r".*STORAGE.*": "DATA STORAGE",
    r".*VISUAL.*": "VISUALISATION",
    r".*FOR.*": "FUNCTION",
    r".*APP.*": "APPLICATION",
    r".*AUTH.*": "AUTHENTICATE",
    r".*MISTAKE.*": "ERROR",
    r".*LL.*": "LLM",
    r".*ELEMENT.*": "MODULE",
    r".*VALID.*": "VALIDATION",
    r"BUTTON": "MODULE",
    r".*FEAT.*": "MODULE",
    #r"IN": "PLUGIN",
    r"PLUGPLUGIN": "PLUGIN",
    r"SENS.*": "SECURITY",
    r"DEFPLUGPLUGPLUGINED": "REFACTOR"

    
    # Add more patterns as needed
}

# List of programming languages to replace as "PROGRAMMING LANGUAGE"
programming_languages = [
   "DESIGN","LOOK"
    # Add more operating systems as needed
]

# Add programming languages to the patterns to replace
for lang in programming_languages:
    patterns_to_replace[f".*{lang}.*"] = "VISUALISATION"

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
