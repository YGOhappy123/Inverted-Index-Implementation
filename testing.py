import os
from pprint import pprint
from src.inverted_index import InvertedIndex

current_dir_path = os.path.dirname(__file__)
resources_dir_path = os.path.join(current_dir_path, 'resources')

# Create inverted index for given text files
index = InvertedIndex()
index.create_index(os.path.join(resources_dir_path, 'ex01'), 'stop_list.txt')
pprint(dict(index.doc_table))
pprint(dict(index.term_index))

# Single word search
results = index.find('cats', 4, 3)
print(results)

# Multi-word weighted search from file
results = index.find_from_file(os.path.join(resources_dir_path, 'ex03', 'query.txt'), 5)
print(results)
