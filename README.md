# Inverted Index Implementation

This project implements a basic inverted index data structure for text files, allowing efficient search for terms and ranked retrieval based on word frequencies and weights.

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

## Installation

Clone this repository and ensure Python 3.6+ is installed.

## Usage

```python
from src.inverted_index import InvertedIndex

# Create inverted index for given text files
index = InvertedIndex()
index.create_index('path/to/documents', 'stopwords.txt')

# Single word search
results = index.find('computer', 5)
print(results)

# Multi-word weighted search from file
results = index.find_from_file('query.txt', 5)
print(results)
```

### Query File Format

The `query.txt` file should contain one word and its weight per line, like:

```text
computer 2
code 3
```

## Project Structure

-   `InvertedIndex`: Main class handling indexing and searching.
-   `_tokenize(text)`: Tokenizes input text.
-   `create_index(dir, stop_list)`: Builds the index.
-   `find(word, n)`: Finds top documents for a given word.
-   `find_from_file(word_file, n)`: Finds top documents using weighted query from file.

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
