from collections import defaultdict


class InvertedIndex:
    def __init__(self):
        self.term_index = defaultdict(lambda: defaultdict(int))
        self.doc_table = {}

    def _tokenize(self, text):
        '''
        Split a block of text into individual words (tokens).
        '''
        pass

    def create_index(self, dir, stop_list):
        """
        Return a dictionary of terms and their counts in each files.
        """
        pass

    def find(self, word, weight, n):
        '''
        Find the top nth documents that have the highest score.
        Document's score is the PROD(word's frequency in document * weight).
        Return a list of filename and the respective count of the specified word.
        '''
        pass

    def find_from_file(self, word_file, n):
        '''
        Find the top nth documents that have the highest score.
        Document's score is the SUM(PROD(word's frequency in document * word's weight)) for each word in the file.
        Return a list of filename and the respective count of the specified word.
        '''
        pass
