import nltk
import re
import spacy
import pandas as pd
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer

nltk.download('punkt')
nltk.download('stopwords')

lemmatizer = nltk.WordNetLemmatizer()
stop_words = set(stopwords.words('english'))

# Read the Excel file (assuming 'your_excel_file.xlsx' is the name of your file)
excel_file_path = '/Users/anastassia/Desktop/SYNEDRIA/icsr24/DevGPT2/snapshot_20230831/uniquetittle.xlsx'
df = pd.read_excel(excel_file_path)

# Check if the DataFrame has at least 13 columns
if len(df.columns) >= 3:
    # Assuming you want to process and modify columns 2, 3, 7, 11, and 12
    text_columns_indices = [2, 4]
    text_columns = df.iloc[:, text_columns_indices]

    # Iterate through each row of the columns and process the text
    for index, row in text_columns.iterrows():
        # Process text for each specified column
        for col_index, col_text in enumerate(row):
            if not pd.isna(col_text):
                standardized_text = str(col_text).lower()
                
                #punctuated_text = re.sub(r'[^\w\s]', '', standardized_text)
                punctuated_text = standardized_text
                tokens = word_tokenize(punctuated_text)

                # spaCy for current column
                nlp = spacy.load('en_core_web_sm')
                doc = nlp(punctuated_text)
                tokens_spacy = [token.text for token in doc]

                # Stopwords removal using NLTK for current column
                filtered_tokens = [token for token in tokens if token.lower() not in stop_words]

                # Lemmatization using spaCy for current column
                sentence = " ".join(filtered_tokens)
                doc = nlp(sentence)
                lemmatized_tokens = [token.lemma_ for token in doc]

                # Replace the original text in the current column with lemmatized tokens
                df.iat[index, text_columns_indices[col_index]] = " ".join(lemmatized_tokens)

    # Save the modified DataFrame to a new Excel file
    output_excel_file_path = 'unique_output.xlsx'
    df.to_excel(output_excel_file_path, index=False)

else:
    print("The DataFrame does not have at least 13 columns.")
