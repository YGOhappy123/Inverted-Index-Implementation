# Inverted Index Implementation
## Student Information
Hà Gia Huy N21DCCN038

Lê Trung Nguyên N21DCCN057

Trần Bình Phương Nhã N21DCCN059     

Trần Đình Toàn N21DCCN086
## Topic Information
As a project, write a program that implements inverted indexes. Your program must contain the following routines:
(a) CreateIndex(Dir, StopList) takes a directory name and a file called StopList (in that directory) as input. It returns an inverted index as output. The DocTable includes all files in the directory Dir, except for the StopList file. The TermTable includes only all words occurring in the directory that start with the letter C (lower- or uppercase).

(b) Find(Word, Weight, N) finds the top N documents in the index associated with the word specified in the input.

(c) Find(WordFile, N) is similar to the above, but there is one difference. Instead of taking a single word as part of the input, it takes a file called WordFile as input. This file has, on each line, a word (string) and a weight (integer). It then attempts to find, using the inverted index, the top N matches for this query.

## Detailed Description of Implementation

This project implements the Inverted Index data structure in Python to enable efficient document search for keywords—specifically, words starting with the letter 'c'—and supports multi-keyword queries with weights.

### 1. Data Structures
- `self.term_index`: A nested dictionary. The outer key is a keyword (token, only those starting with 'c'), the inner key is a document ID, and the value is the number of times the word appears in that document.
- `self.doc_table`: A dictionary mapping doc_id (an auto-increment integer) to the corresponding document filename.

### 2. Preprocessing & Index Construction
- **Tokenization:** Uses regex to convert all text to lowercase and split it into tokens (words).
- **Stopword Removal:** Reads a stopwords file (from the `stop_list` parameter) and builds a set of words to ignore.
- **Indexing Only Words Starting with 'c':** When processing tokens from documents, only those starting with the letter 'c' are stored in the index.
- **Frequency Counting:** For each valid word, its occurrence count is updated per document.

### 3. Single Keyword Search (`find`)
- The `find(word, weight, n)` method takes a keyword, a weight, and the number of top documents to return.
- It computes a score for each document containing the word: score = (frequency of word) × (weight).
- Returns a list of up to n files with the highest scores, along with their filenames and scores.

### 4. Multi-keyword Weighted Search from File (`find_from_file`)
- The function takes a query file, each line containing a word and its weight.
- It reads the file, checks if each word exists in the index, and parses the weights.
- For each document, it computes a total score: the sum of (word frequency × word weight) for all query words.
- Returns a list of up to n files with the highest scores, along with their filenames and scores.

### 5. Error Handling
- If the query file does not exist, the function raises an error.
- If a line in the query file is invalid (wrong format or non-integer weight), that line is skipped.

### 6. Workflow Summary
- The user creates an `InvertedIndex` object and calls `create_index` to build the index from document files.
- For searching, the user calls either `find` (for a single keyword) or `find_from_file` (for a weighted multi-keyword query).
- The result is a ranked list of document filenames according to relevance to the search keywords.

### 7. Key Features
- Efficiently indexes only words that start with a specific character ('c').
- Flexible search: supports both single-keyword and weighted multi-keyword queries.
- Ignores stopwords to improve search precision and reduce noise.

## Features

-   Tokenizes text files and builds an inverted index of words starting with the letter 'c'.
-   Supports search for the most relevant documents based on a single word.
-   Supports weighted multi-word queries from a file.
-   Ignores common stop words provided in a stop list.

## How It Works

1. **Indexing**:

    - Reads all text files from a specified directory (excluding the stop list file).
    - Tokenizes content, ignores stop words, and only indexes words starting with the letter 'c'.
    - Tracks frequency of indexed words in each document.

2. **Searching**:
    - `find(word, n)`: Finds the top `n` documents with the highest count of the specified word.
    - `find_from_file(word_file, n)`: Computes scores for documents based on the frequency of words and their respective weights from the query file.

## Installation Instructions
### Installation

1. Clone this repository

    ```bash
    git clone https:https://github.com/YGOhappy123/Inverted-Index-Implementation.git
    ```

2. Ensure Python 3.6+ is installed.

3. Project Structure

-   `InvertedIndex`: Main class handling indexing and searching.
-   `_tokenize(text)`: Tokenizes input text.
-   `create_index(dir, stop_list)`: Builds the index.
-   `find(word, n)`: Finds top documents for a given word.
-   `find_from_file(word_file, n)`: Finds top documents using weighted query from file.

## Instructions For Running The rogram
### Usage

```python
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

```

### Query File Format

The `query.txt` file should contain one word and its weight per line, like:

```text
computer 2
code 3
```

### Development

To start the program, use:

```bash
python testing.py
```

## Inputs
### Input Files

The included doc files available after copying the project are as below:

- ai_description.txt

- car_descriptions.txt

- cat_descriptions.txt

- house_descriptions.txt

- laptop_descriptions.txt

- pets_descriptions.txt

- pizza_descriptions.txt

- vietnam_descriptions.txt

- stop_list.txt

- query.txt

## Outputs
After running the program, the output will be as follows:

```bash
{0: 'ai_description.txt',
 1: 'car_description.txt',
 2: 'cat_description.txt',
 3: 'house_description.txt',
 4: 'laptop_description.txt',
 5: 'pets_description.txt',
 6: 'pizza_description.txt',
 7: 'vietnam_description.txt'}
{'café': defaultdict(<class 'int'>, {4: 1}),
 'called': defaultdict(<class 'int'>, {0: 1, 3: 1, 5: 1}),
 'calming': defaultdict(<class 'int'>, {2: 1}),
 'calmness': defaultdict(<class 'int'>, {5: 1}),
 'can': defaultdict(<class 'int'>, {0: 1, 3: 1, 4: 2, 5: 2, 6: 1}),
 'capable': defaultdict(<class 'int'>, {4: 1}),
 'car': defaultdict(<class 'int'>, {1: 7}),
 'care': defaultdict(<class 'int'>, {3: 1, 5: 2}),
 'carried': defaultdict(<class 'int'>, {4: 1}),
 'cars': defaultdict(<class 'int'>, {0: 1, 1: 1}),
 'cat': defaultdict(<class 'int'>, {2: 6}),
 'cats': defaultdict(<class 'int'>, {2: 4, 5: 2}),
 'challenges': defaultdict(<class 'int'>, {7: 1}),
 'changing': defaultdict(<class 'int'>, {0: 1}),
 'charm': defaultdict(<class 'int'>, {2: 1, 3: 1}),
 'chase': defaultdict(<class 'int'>, {2: 1}),
 'cheese': defaultdict(<class 'int'>, {6: 2}),
 'chi': defaultdict(<class 'int'>, {7: 1}),
 'cities': defaultdict(<class 'int'>, {7: 1}),
 'city': defaultdict(<class 'int'>, {7: 1}),
 'classic': defaultdict(<class 'int'>, {6: 1}),
 'clean': defaultdict(<class 'int'>, {2: 1}),
 'cleanliness': defaultdict(<class 'int'>, {3: 1}),
 'climate': defaultdict(<class 'int'>, {1: 1}),
 'coast': defaultdict(<class 'int'>, {7: 1}),
 'colorful': defaultdict(<class 'int'>, {7: 1}),
 'colors': defaultdict(<class 'int'>, {3: 1, 4: 1}),
 'combination': defaultdict(<class 'int'>, {6: 1}),
 'combines': defaultdict(<class 'int'>, {1: 1, 4: 1}),
 'come': defaultdict(<class 'int'>, {4: 1, 5: 1, 7: 1}),
 'comfort': defaultdict(<class 'int'>, {1: 2, 2: 2, 3: 1, 5: 1}),
 'comfortable': defaultdict(<class 'int'>, {4: 1}),
 'comforting': defaultdict(<class 'int'>, {6: 1}),
 'communication': defaultdict(<class 'int'>, {4: 1}),
 'commute': defaultdict(<class 'int'>, {1: 1}),
 'compact': defaultdict(<class 'int'>, {4: 1}),
 'companion': defaultdict(<class 'int'>, {1: 1, 2: 1, 4: 1}),
 'companions': defaultdict(<class 'int'>, {2: 1, 5: 1}),
 'companionship': defaultdict(<class 'int'>, {5: 1}),
 'complex': defaultdict(<class 'int'>, {0: 1}),
 'computer': defaultdict(<class 'int'>, {0: 1, 4: 1}),
 'concrete': defaultdict(<class 'int'>, {3: 1}),
 'connected': defaultdict(<class 'int'>, {4: 1}),
 'connection': defaultdict(<class 'int'>, {3: 1}),
 'connections': defaultdict(<class 'int'>, {5: 1}),
 'connects': defaultdict(<class 'int'>, {4: 1}),
 'consists': defaultdict(<class 'int'>, {6: 1}),
 'constantly': defaultdict(<class 'int'>, {2: 1}),
 'content': defaultdict(<class 'int'>, {2: 1}),
 'continues': defaultdict(<class 'int'>, {0: 1}),
 'control': defaultdict(<class 'int'>, {1: 2}),
 'controls': defaultdict(<class 'int'>, {1: 1}),
 'convenience': defaultdict(<class 'int'>, {4: 1}),
 'convenient': defaultdict(<class 'int'>, {6: 1}),
 'corner': defaultdict(<class 'int'>, {3: 1}),
 'country': defaultdict(<class 'int'>, {7: 2}),
 'cozy': defaultdict(<class 'int'>, {2: 1}),
 'create': defaultdict(<class 'int'>, {7: 1}),
 'creates': defaultdict(<class 'int'>, {5: 1}),
 'creativity': defaultdict(<class 'int'>, {4: 1, 6: 1}),
 'crisp': defaultdict(<class 'int'>, {4: 1}),
 'crispy': defaultdict(<class 'int'>, {6: 1}),
 'crust': defaultdict(<class 'int'>, {6: 1}),
 'cuisine': defaultdict(<class 'int'>, {7: 1}),
 'culture': defaultdict(<class 'int'>, {3: 1, 7: 2}),
 'curl': defaultdict(<class 'int'>, {2: 1}),
 'curled': defaultdict(<class 'int'>, {2: 1}),
 'cushions': defaultdict(<class 'int'>, {2: 1}),
 'customs': defaultdict(<class 'int'>, {7: 1})}
[('cat_description.txt', 16), ('pets_description.txt', 8)]
[('cat_description.txt', 65), ('car_description.txt', 57), ('laptop_description.txt', 27), ('house_description.txt', 21), ('pets_description.txt', 21)]
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contributors

Thanks to the following people for contributing to this project ✨:

<table>
    <tr>
        <td align="center">
            <a href="https://github.com/YGOhappy123">
                <img 
                    src="https://avatars.githubusercontent.com/u/90592072?v=4"
                    alt="YGOhappy123" width="100px;" height="100px;" 
                    style="border-radius: 4px; background: #fff;"
                /><br />
                <sub><b>YGOhappy123</b></sub>
            </a>
        </td>
        <td align="center">
            <a href="https://github.com/ryuus3igun">
                <img 
                    src="https://avatars.githubusercontent.com/u/126484739?v=4"
                    alt="ryuus3igun" width="100px;" height="100px;"                 
                    style="border-radius: 4px; background: #fff;"
                /><br />
                <sub><b>ryuus3igun</b></sub>
            </a>
        </td>
        <td align="center">
            <a href="https://github.com/DinhToanIT2003">
                <img 
                    src="https://avatars.githubusercontent.com/u/126399422?v=4"
                    alt="DinhToanIT2003" width="100px;" height="100px;"                 
                    style="border-radius: 4px; background: #fff;"
                /><br />
                <sub><b>DinhToanIT2003</b></sub>
            </a>
        </td>
        <td align="center">
            <a href="https://github.com/Nguyen1609">
                <img 
                    src="https://avatars.githubusercontent.com/u/126648891?v=4"
                    alt="Nguyen1609" width="100px;" height="100px;"
                    style="border-radius: 4px; background: #fff;"
                /><br />
                <sub><b>Nguyen1609</b></sub>
            </a>
        </td>
    </tr>
</table>
