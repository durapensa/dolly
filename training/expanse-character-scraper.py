import re
import json
import wikia

# List of TV character page titles
character_titles = ['Bobbie_Draper_(TV)', 
                    'Naomi_Nagata_(TV)', 
                    'Chrisjen_Avasarala_(TV)'] 

# Function to generate JSON for each character
def generate_character_json(character_title):
    instruction = f"Who is {character_title.replace('_', ' ')}?"
    context = re.sub(r'(?<=\.)\s*[^.]*\.', '', wikia.summary('expanse', character_title), count=2)
    response = "Answer for the response category" # Replace with actual response
    category = "closed_qa"
    
    character_json = {
        "instruction": instruction,
        "context": context,
        "response": response,
        "category": category
    }
    
    return json.dumps(character_json)

# List to store JSON for all characters
characters_json_list = []

# Iterate over character titles and generate JSON for each character
for character_title in character_titles:
    character_json = generate_character_json(character_title)
    characters_json_list.append(character_json)   

# Write JSON to a file
with open('../data/expanse-dushowxa-characters.jsonl', 'w') as f:
    f.write('\n'.join(map(str, characters_json_list)))

print("Characters:",len(characters_json_list),"written to ../data/expanse-dushowxa-characters.jsonl")

