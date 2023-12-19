# -*- coding: utf-8 -*-

pip install streamlit -q

pip install langchain -q

pip install unstructured -q

pip install tiktoken -q

pip install faiss-cpu -q

!pip install typing-extensions==3.10.0.2-q

!pip show typing_extensions

pip install gradio

pip install openai

import os
import pickle
import time
from langchain import OpenAI
from langchain.chains import RetrievalQAWithSourcesChain
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.document_loaders import UnstructuredURLLoader
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from google.colab import userdata
key=userdata.get('OPENAI_API_KEY')
#os.environ["OPENAI_API_KEY"] = key
!wget -q -O - ipv4.icanhazip.com
import gradio
def main(url1,url2,url3,queryInput):
  urls=[]
  #for i in range(3):
   # url=input(f"enter url {i}")
    #urls.append(url)
  urls_=[url1,url2,url3]

  #Loading the data from URLs
  loaded=UnstructuredURLLoader(urls=urls_)
  loaded_data=loaded.load()

  #Splitting the data into chunks
  text_splitter=RecursiveCharacterTextSplitter(
    separators=['\n\n' , '\n' , '.' , ','],
    chunk_size=1000
  )
  documents = text_splitter.split_documents(loaded_data)

  #creating and saving embeddings to FAISS Index
  embeddings=OpenAIEmbeddings()
  vectorstore_openai=FAISS.from_documents(documents,embeddings)
  vectorstore = FAISS.from_documents(documents, embeddings)
  query=queryInput
  llm = OpenAI(temperature=0.9, max_tokens=500)
  chain = RetrievalQAWithSourcesChain.from_llm(llm=llm, retriever=vectorstore.as_retriever())
  result = chain({"question": query}, return_only_outputs=True)
  ans=result["answer"]
  return ans
interface=gradio.Interface(fn=main ,inputs=['text','text','text','text'],outputs=['text'])
interface.launch(debug=True)
