from dataclasses import dataclass
from collections import Counter
from .analysis import analyze

@dataclass
class Abstract:
    """Wikipedia abstract"""

    ID: int
    title: str
    abstract: str
    url: str

    @property
    def fulltext(self):
        return " ".join([self.title, self.abstract])

    def analyze(self):
        tokens = analyze(self.fulltext)
        self.term_frequency = Counter(tokens)

    def get_term_frequency(self, term):
        return self.term_frequency.get(term, 0)

    def __str__(self):
        return f"Document(ID={self.ID}, title={self.title})"

