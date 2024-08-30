
import pandas as pd
from difflib import SequenceMatcher
import nltk
from nltk.tokenize import word_tokenize

# Function to find similar lines and words between two strings
def find_similar_lines_and_words(text1, text2):
    # Tokenize the text into words
    words1 = set(word_tokenize(text1))
    words2 = set(word_tokenize(text2))
    
    # Find common words between the two sets
    common_words = words1.intersection(words2)
    
    # Calculate similarity ratio using SequenceMatcher
    similarity_ratio = SequenceMatcher(None, text1, text2).ratio()
    
    return common_words, similarity_ratio

# Function to count the number of words in a text
def count_words(text):
    return len(word_tokenize(text))

# Read the Excel file
excel_file_path = 'unique_output.xlsx'
df = pd.read_excel(excel_file_path)

# Create new columns to store results
df['Common_Words'] = ''
df['Similarity_Ratio'] = 0.0
df['Words_Count_Column2'] = 0
df['Words_Count_Column4'] = 0

# Iterate over each row and compare columns 2 and 4
for index, row in df.iterrows():
    text1 = str(row.iloc[2])  # Assuming column 2 contains text
    text2 = str(row.iloc[4])  # Assuming column 4 contains text
    
    # Find similar lines and words
    common_words, similarity_ratio = find_similar_lines_and_words(text1, text2)
    
    # Store results in DataFrame
    df.at[index, 'Common_Words'] = ', '.join(common_words)
    df.at[index, 'Similarity_Ratio'] = similarity_ratio
    
    # Count words in each column
    df.at[index, 'Words_Count_Column2'] = count_words(text1)
    df.at[index, 'Words_Count_Column4'] = count_words(text2)

# Save the modified DataFrame to a new Excel file
output_excel_file_path = 'unique_output_with_similarity.xlsx'
df.to_excel(output_excel_file_path, index=False)

print(f"Similarity results saved to: {output_excel_file_path}")
