from .analysis import analyze
import math

class Index:
    def __init__(self):
        self.index = {}
        self.documents = {}


    def index_document(self, document):
        if document.ID not in self.documents:
            self.documents[document.ID] = document
            # generate term frequency
            document.analyze()

        tokens = analyze(document.fulltext)
        for token in tokens:
            if token not in self.index:
                self.index[token] = set()

            self.index[token].add(document.ID)


    def _result(self, analyzed_query):
        return [self.index.get(token, set()) for token in analyzed_query]

    def document_frequency(self, token):
        return len(self.index.get(token, set()))

    def inverse_document_frequency(self, token):
        return math.log10(len(self.documents) / self.document_frequency(token))

    def search(self, query, search_type = 'AND', rank = True):
        if search_type not in ('AND', 'OR'):
            return []

        analyzed_query = analyze(query)
        results = self._result(analyzed_query)
        if search_type == 'OR':
            # only one token must be in documents
            documents = [self.documents[doc_id] for doc_id in set.union(*results)]
        else:
            # all token must be in documents
            documents = [self.documents[doc_id] for doc_id in set.intersection(*results)]

        # rank the documents
        if rank:
            return self.rank(analyzed_query, documents)
        return documents

    def rank(self, analyzed_query, documents):
        # sum up term occurence
        results = []
        for document in documents:
            score = 0.0
            for term in analyzed_query:
                tf = document.get_term_frequency(term)
                idf = self.inverse_document_frequency(term)
                score += tf * idf

            results.append((document, score))

        return sorted(results, key=lambda doc: doc[1], reverse=True)
