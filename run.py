import os.path
from download import download_wikipedia_abstracts
from search.timing import timing
from load import  load_documents
from search.index import Index
import pickle
import time

@timing
def index_documents(documents, index):
    for i, document in enumerate(documents):
        index.index_document(document)
        if i % 5000 == 0:
            print(f'Indexed {i} documents', end='\r')
    return index

if __name__ == '__main__':
    if not os.path.exists('data/enwiki-latest-abstract27.xml.gz  '):
        download_wikipedia_abstracts()

    if not os.path.exists('data/my_index.pkl'):
        print(f"Index file not found!. Build index from xml.gz file")
        documents = load_documents()
        index = index_documents(documents, Index())
        # save data to file
        with open('data/my_index.pkl', 'wb') as output:
            pickle.dump(index, output, pickle.HIGHEST_PROTOCOL)
    else:
        print(f"Index file found!. Load pickle data to memory")
        with open('data/my_index.pkl', 'rb') as index_file:
            index = pickle.load(index_file)

    print(f'Index contains {len(index.documents)} documents')
    while True:
        value = input("Please enter a search query:")
        start = time.time()
        results = index.search(value)
        end = time.time()
        execution_time = end - start
        print(f'{len(results)} results. ({execution_time * 1000} milliseconds)')
        for ele in results[:10]:
            print(f"Score: {ele[1]}, {ele[0]}")
        print("")
