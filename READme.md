# News Research Tool

This is an End-to-End LLM project which takes in a bunch of news article URLs and when prompted, the model retrievs the answer from our aggregate knowledge base.

##Technologies used
-Python, LangChain, OpenAI API and FAISS indexing

## Features
- Makes use of UnstructuresURLLoad to collect and store the unstructured text data from various articles.
- RecursiveCharacterTextSplitter is used to divide the data into chunks to provide a more accurate output while reducing the API cost.
- FAISS with it's IndexFlatL2 (for search using Euclidean distance) is used to index the OpenAI embeddings of the data chunks.

