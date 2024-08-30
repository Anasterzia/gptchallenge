import pandas as pd
import nltk
from nltk.stem import WordNetLemmatizer

# Download the WordNet corpus if not already downloaded
nltk.download('wordnet')

# Initialize the WordNet lemmatizer
lemmatizer = WordNetLemmatizer()

def replace_words(text):
    # Check if the input is a string
    if isinstance(text, str):
        # Tokenize the text into words
        words = nltk.word_tokenize(text)
        
        # Define the list of allowed words
        allowed_words = ['Security', 'LLM-ChatGPT', 'Bug-Fix', 'Refactor', 'Prog-language', 'Energy', 'New-Feature']
        
        # Replace words with their replacements or 'String' if not found in allowed_words
        replaced_text = []
        string_added = False  # Flag to track if 'String' has been added
        for word in words:
            if word in allowed_words:
                replaced_text.append(word)
                string_added = False  # Reset the flag if an allowed word is found
            elif not string_added:
                replaced_text.append('String')
                string_added = True
        
        return ' '.join(replaced_text)
    else:
        # If the input is not a string, return an empty string
        return ''

        
# Read the Excel file
excel_file_path = '/Users/anastassia/Desktop/SYNEDRIA/icsr24/DevGPT2/excels_afterwebsearch/titles.xlsx'
df = pd.read_excel(excel_file_path)

# Apply word replacement to the specified columns
df['CommitMessage'] = df['CommitMessage'].apply(replace_words)
df['Title'] = df['Title'].apply(replace_words)

# Save the modified DataFrame to a new Excel file
output_excel_file_path = '/Users/anastassia/Desktop/SYNEDRIA/icsr24/DevGPT2/excels_afterwebsearch/titlescategory.xlsx'
df.to_excel(output_excel_file_path, index=False)

print(f"Replacements applied and saved to: {output_excel_file_path}")
