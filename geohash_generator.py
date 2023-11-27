import pandas as pd
import numpy as np
import geohash

#generates geohashes for the coordinates.
def generate_geohash(df):
    df['Geohash'] = df.apply(lambda row: geohash.encode(row['Latitude'], row['Longitude'], precision=12), axis=1)
    return df[['Latitude', 'Longitude', 'Geohash']]

#initiates a trie , used for shortest unique prefix calculation.
class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False
        self.prefix_count = 0
        
#inserts individual geohash characters to the trie.
def insert_word(root, word):
    node = root
    for char in word:
        if char not in node.children:
            node.children[char] = TrieNode()
        node = node.children[char]
        node.prefix_count += 1
    node.is_end_of_word = True

#calculates shortest unique prefixes for a single geohash
def find_shortest_prefix(root, word):
    node = root
    prefix = ""
    for char in word:
        node = node.children[char]
        prefix += char
        if node.prefix_count == 1:
            break
    return prefix

#generates shortest unique prefix for every geohash one at a time
def find_shortest_prefixes(words):
    root = TrieNode()
    for word in words:
        insert_word(root, word)

    prefixes = [find_shortest_prefix(root, word) for word in words]
    return prefixes


#Modify the file_path based on where the file is stored.
file_path = 'coordinates.csv.gz'

#Read the file and store data onto a pandas dataframe.
try:
    df = pd.read_csv(file_path, compression='gzip',sep=';')
except FileNotFoundError:
    print(f"Error: File '{file_path}' not found in path specified, Please check the file_path.")
    exit()

# Validate the schema by ensuring columns 'Latitude' and 'Longitude' exist
if 'Latitude' not in df.columns or 'Longitude' not in df.columns:
    print("Error: 'Latitude' and 'Longitude' columns are required.")
    exit()

# Filter out rows with invalid coordinates
df = df[(df['Latitude'] >= -90) & (df['Latitude'] <= 90) & (df['Longitude'] >= -180) & (df['Longitude'] <= 180)]

# Deduplication to avoid redundancy
df = df.drop_duplicates(subset=['Latitude', 'Longitude'])

# Generate Geohash for the cleaned DataFrame
df = generate_geohash(df)

#Generate unique prefix for geohashes and store in df 
df['unique_prefix']=find_shortest_prefixes(df['Geohash'].to_numpy())

#store only unique_prefix in a new csv file , use df.to_csv("geohash.csv",sep=';',index=False) if the entire df is needed
df['unique_prefix'].to_csv("geohash.csv",sep=';',index=False)
