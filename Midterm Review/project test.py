import pandas as pd
import pickle
import string

processed_file_path = "Processed_Country_and_Titles.csv"
positional_index_path = "positional_index.pkl"

def preprocess_text(text):
    if isinstance(text, str):  
        text_cleaned = text.lower().translate(str.maketrans('', '', string.punctuation + '0123456789'))
        tokens = [token.strip() for token in text_cleaned.split() if token.strip()]
        return tokens
    else:
        return []

df = pd.read_csv(processed_file_path, converters={'Titles 1': eval, 'Titles 2': eval, 'Titles 3': eval, 'Titles 4': eval, 'Titles 5': eval})

positional_index = {}

for index, row in df.iterrows():
    for column in ['Titles 1', 'Titles 2', 'Titles 3', 'Titles 4', 'Titles 5']:
        tokens = row[column]
        for pos, token in enumerate(tokens):
            if token not in positional_index:
                positional_index[token] = {}
            if index not in positional_index[token]:
                positional_index[token][index] = []
            positional_index[token][index].append(pos)

with open(positional_index_path, 'wb') as f:
    pickle.dump(positional_index, f)

def preprocess_query(query):
    return preprocess_text(query)

def phrase_search(query, positional_index):
    query_tokens = preprocess_query(query)
    phrase_positions = {}
    if query_tokens[0] not in positional_index:
        return []
    initial_positions = positional_index[query_tokens[0]]
    for doc_id in initial_positions:
        for pos in initial_positions[doc_id]:
            match = True
            current_position = pos
            for token in query_tokens[1:]:
                current_position += 1
                if token not in positional_index or doc_id not in positional_index[token] or current_position not in positional_index[token][doc_id]:
                    match = False
                    break
            if match:
                if doc_id not in phrase_positions:
                    phrase_positions[doc_id] = []
                phrase_positions[doc_id].append(pos)
    return phrase_positions

# Example query for testing
example_query = "climate change"
search_results = phrase_search(example_query, positional_index)

print(search_results)
