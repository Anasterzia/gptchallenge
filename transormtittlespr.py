import pandas as pd
import nltk
from nltk.stem import WordNetLemmatizer
import re

# Download the WordNet corpus if not already downloaded
nltk.download('wordnet')

# Initialize the WordNet lemmatizer
lemmatizer = WordNetLemmatizer()

# Function to generate patterns for words and their variations
def generate_patterns(word):
    return [f'^{word}$', f'^{word}s?$', f'^{word}ed$', f'^{word}ing$', f'^{word}s$', f'^{word}es$', f'^{word}ly$', f'^{word}ness$', f'^{word}e$',f'^{word}y$', f'^{word}ment$', f'^{word}ation$', f'^{word}less$',f'^{word}ize$', f'^{word}able$', f'^{word}er$',f'^{word}ure$' , f'^{word}ity$' ,f'^{word}gpt$',f'^gpt{word}$' , f'^{word}ate$']

# Dictionary mapping words or phrases to their lemmatized or replaced forms
word_to_replacement = {
    tuple(pattern for word in ['python', 'java', 'c','c++', 'javascript', 'go', 'rust', 'swift', 'kotlin', 'ruby', 'perl', 'lua', 'scala', 'r', 'matlab' , 'html', 'css', 'jsx', 'json', 'graphql', 'xml', 'yaml', 'markdown', 'sql', 'php','laravel','c ++','cpp','sql','mysql','arduino','script','golang'] for pattern in generate_patterns(word)): 'Prog language',
  
    
    tuple(pattern for word in ['add', 'plugin', 'feature', 'new',' generate','creat','build','install','encapsulat','tutorial','guide','writ','instruct','execut','input','module','implement','set','make','compos','need','option','ability','gener','import','setup','download','expand','explor','customiz','extend',' framework','feat','launc','feature'] for pattern in generate_patterns(word)): 'New Feature',
    
    tuple(pattern for word in ['blockchain', 'key', 'password','accesspolicy', 'accessrole', 'access-policy', 'access-role', 'accesspolicy', 'accessrole', 'aes', 'audit', 'authentic', 'authority', 'authoriz', 'biometric', 'blacklist', 'black-list', 'blacklist', 'blacklist', 'cbc', 'certificate', 'checksum', 'cipher', 'clearance', 'confidentiality', 'cookie', 'crc', 'credential', 'crypt', 'csrf', 'decode', 'defensiveprogramming', 'defensive-programming', 'delegation', 'denialofservice', 'denial-of-service', 'diehellman', 'dmz', 'dotfuscator', 'dsa', 'ecdsa', 'encode', 'escrow', 'exploit', 'firewall', 'forge', 'forgery', 'gssapi', 'gss-api', 'gssapi', 'hack', 'hash', 'hmac', 'honeypot', 'honey-pot', 'honeypot', 'inject', 'integrity', 'kerberos', 'ldap', 'login', 'malware', 'md5', 'nonce', 'nss', 'oauth', 'obfuscat', 'openauth', 'open-auth', 'openauth', 'openid', 'owasp', 'password', 'pbkdf2', 'pgp', 'phishing', 'pki', 'privacy', 'privatekey', 'privatekey', 'privatekey', 'privi-lege', 'publickey', 'public-key', 'publickey', 'rbac', 'rc4', 'repudiation', 'rfc2898', 'rfc-2898', 'rfc2898', 'rijndael', 'rootkit', 'rsa', 'salt', 'saml', 'sanitiz','secur', 'sha', 'shell code','shellcode', 'shellcode', 'shibboleth', 'signature', 'signed','signing', 'singsign-on', 'singlesignon', 'single-sign-on', 'smartassembly', 'smart-assembly', 'smartassembly', 'snif', 'spam', 'spnego', 'spoofing', 'spyware', 'ssl', 'sso', 'steganography', 'tampering', 'trojan','trust', 'violat', 'virus', 'whitelist', 'white-list', 'whitelist', 'x509', 'xss', 'verify','configure','risk', 'deepfake','ledger','monitor','configur','fear','lethal','legal',' secur','fake','unexpect','config','permission','validator','backup','websocket','socket','policy','encrypt','proxy'] for pattern in generate_patterns(word)): 'Security',
    
    tuple(pattern for word in ['energy consum', 'energy efficien', 'energy sav', 'save energy', 'power consum', 'power ecien', 'power save', 'save power', 'energy drain', 'energy leak', 'tail energy', 'power efficien', 'high CPU', 'power aware', 'drain', 'no sleep', 'battery life' , 'battery consum', 'renewable energy'] for pattern in generate_patterns(word)): 'Energy',
    
    tuple(pattern for word in ['rewrit', 'restruct','revis', 'reorgani','renew', 'revitaliz','refresh', 'reconstruct','modif', 'amend','upgrade', 'update','transform', 'rectify','rectification','cleanup', 'redesign', 'reengineer','reverse','improve','remove','split','rename','move','reset','integrate',' organize','convert','increase','decrease','rewrite','rephrase','paraphrase','optimize','optimise','decompos','instead','vs','redo','parallel','format','refactor','enhance','chang','edit','migrat','automat','enlarg','custom','resize',' reduction','reformat','refine','reorder','simpl','unsupported'] for pattern in generate_patterns(word)): 'Refactor',
    
        
    tuple(pattern for word in ['gpt','gpt-3','gpt-4','chatgpt','llm','chat-gpt','chat gpt','llama','bart','openai','chatbot','copilot', 'chaptgpt'] for pattern in generate_patterns(word)): 'LLM-ChatGPT',
    
    tuple(pattern for word in ['debug', 'issue','troubleshoot', 'problem','resolve', 'error','patch', 'glitch','fix', 'defect','diagnose', 'anomaly','review', 'inconsistency','testing', 'fault','QA', 'workaround','validation','correct','solve','help','check', 'eliminate','try','catch','test','handle','exception','support','ask','answer','solution','incorrect ','wraperror','syntaxerror','overwrit','uninstall','change','include','convert','stablecode','stable','fail','question','unknown', 'heal','404','worry','bug','conflict','override'] for pattern in generate_patterns(word)): 'Bug Fix'
    
    

    # Add more mappings as needed
    
}

# Function to replace words in a given text

def replace_words(text, row_number, column_name):
    # Check if the input is a string
    if isinstance(text, str):
        # Tokenize the text into words
        words = nltk.word_tokenize(text)
        
        # Replace words with their replacements
        replaced_text = []
        for word in words:
            # Check if the word is in any of the word groups
            for word_group, replacement in word_to_replacement.items():
                if any(re.match(pattern, word.lower()) for pattern in word_group):
                    replaced_text.append(replacement)
                    break  # Stop searching for replacements once a match is found
            else:
                # If the word doesn't match any group, lemmatize it
                replaced_text.append(lemmatizer.lemmatize(word))
        
        # Print current row number, column name, and original text
        print(f"Row {row_number}, Column {column_name}: {text}")
        print(f"Replaced text: {' '.join(replaced_text)}")
        
        return ' '.join(replaced_text)
    else:
        # If the input is not a string, return an empty string or handle it based on your requirements
        return ''

# Read the Excel file
excel_file_path = '/Users/anastassia/Desktop/SYNEDRIA/icsr24/DevGPT2/snapshot_20230831/rr_output.xlsx'
df = pd.read_excel(excel_file_path)

# Iterate over each row and apply word replacement to the specified columns
for index, row in df.iterrows():
    for column_name in ['Title', 'Title.1']:  # Specify the column names you want to process
        original_text = row[column_name]
        replaced_text = replace_words(original_text, index + 1, column_name)
        df.at[index, column_name] = replaced_text

# Save the modified DataFrame to a new Excel file
output_excel_file_path = '/Users/anastassia/Desktop/SYNEDRIA/icsr24/DevGPT2/snapshot_20230831/rry_output.xlsx'
df.to_excel(output_excel_file_path, index=False)

print(f"Replacements applied and saved to: {output_excel_file_path}")
