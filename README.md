### Building a full-text search engine in Python

####

-   Index 162082 documents from Wikipedia. Each document consists of title, url, and abstract
-   Using `inverted index` as internal data structure for index which is a dictionary where we map all the words in our corpus to the IDs of the documents they occur in.
-   Implement boolean search which will return documents the contain either all words from the query or just one of them
-   Implement relevancy ranking based on `tf-idf` algorithm.

#### Demo

![alt text](https://github.com/hieutran106/python-searchengine/blob/main/public/capture.png?raw=true)
