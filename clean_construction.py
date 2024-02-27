import re

# Step 1: Read the content of the file
file_path = '/Users/mariiakokina/Documents/chatbot_ai/construction_terms.txt'
with open(file_path, 'r') as file:
    content = file.read()

# Step 2: Find all terms enclosed in double quotes
terms_list = re.findall(r'"(.*?)"', content)

# Step 3: Write the terms back to the file, one term per line
if terms_list:
    with open(file_path, 'w') as file:
        for term in terms_list:
            file.write(f"{term}\n")
