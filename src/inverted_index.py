class InvertedIndex:
    def __init__(self):
        self.term_index = {}
        self.doc_table = {}

    def _tokenize(self, text):
        pass

    def create_index(self, dir, stop_list):
        pass

    def find(self, word, weight, n):
        pass

    def find_from_file(self, word_file, n):
        pass
