import os
import re
import heapq
from collections import defaultdict


class InvertedIndex:
    def __init__(self):
        self.term_index = defaultdict(lambda: defaultdict(int))
        self.doc_table = {}

    def _tokenize(self, text):
        '''
        Split a block of text into individual words (tokens).
        '''
        return re.findall(r'\b\w+\b', text.lower())

    def create_index(self, dir, stop_list):
        """
        Return a dictionary of terms and their counts in each files.
        """
        stop_words = set()
        with open(os.path.join(dir, stop_list), 'r') as f:
            for line in f:
                stop_words.add(line.strip().lower())

        # Read all other files in directory and track the count of appropriate words
        doc_id = 0
        for filename in os.listdir(dir):
            full_path = os.path.join(dir, filename)
            if not os.path.isfile(full_path) or filename == stop_list:
                continue

            self.doc_table[doc_id] = filename

            with open(full_path, 'r', encoding='utf-8', errors='ignore') as f:
                text = f.read()
                tokens = self._tokenize(text)

                for token in tokens:
                    if token.lower() in stop_words:
                        continue
                    if token.lower().startswith('c'):
                        self.term_index[token.lower()][doc_id] += 1

            doc_id += 1

        return self.term_index

    def find(self, word, weight, n):
        '''
        Find the top nth documents that have the highest score.
        Document's score is the PROD(word's frequency in document * weight).
        Return a list of filename and the respective count of the specified word.
        '''
        word = word.lower()
        if word not in self.term_index:
            return []

        doc_scores = {key: value * weight for key, value in self.term_index[word].items()}
        top_docs = heapq.nlargest(n, doc_scores.items(), key=lambda x: x[1])
        return [(self.doc_table[doc_id], score) for doc_id, score in top_docs]

    def find_from_file(self, word_file, n):
        '''
        Find the top nth documents that have the highest score.
        Document's score is the SUM(PROD(word's frequency in document * word's weight)) for each word in the file.
        Return a list of filename and the respective count of the specified word.
        '''
        if not os.path.isfile(word_file):
            raise FileNotFoundError(f"{word_file} does not exist")

        query_terms = {}
        with open(word_file, 'r') as f:
            for line in f:
                parts = line.strip().split()
                if len(parts) != 2:
                    continue

                word, weight = parts
                word = word.lower()
                if word in self.term_index:
                    try:
                        weight = int(weight)
                        query_terms[word] = weight
                    except ValueError:
                        continue

        doc_scores = defaultdict(int)
        for word, weight in query_terms.items():
            for doc_id, freq in self.term_index[word].items():
                doc_scores[doc_id] += freq * weight

        top_docs = heapq.nlargest(n, doc_scores.items(), key=lambda x: x[1])
        return [(self.doc_table[doc_id], score) for doc_id, score in top_docs]

