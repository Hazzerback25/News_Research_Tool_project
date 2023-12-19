# News Research Tool

This is an End-to-End LLM project which takes in a bunch of news article URLs and when prompted, the model retrievs the answer from our aggregate knowledge base.

## Technologies used
-Python, LangChain, OpenAI API and FAISS indexing

## Features
- Makes use of UnstructuresURLLoad to collect and store the unstructured text data from various articles.
- RecursiveCharacterTextSplitter is used to divide the data into chunks to provide a more accurate output while reducing the API cost.
- FAISS with it's IndexFlatL2 (for search using Euclidean distance) is used to index the OpenAI embeddings of the data chunks.

## Output

### [Demo Video](https://youtu.be/f4N4GB4ZCuI)

<img width="973" alt="Screenshot 2023-07-09 at 2 40 27 PM" src="https://github.com/Hazzerback25/News_Research_Tool_project/assets/85587494/360b9a0c-292f-4049-971c-77343ae138cf">
<img width="1336" alt="Screenshot 2023-12-19 at 6 39 28 AM" 
