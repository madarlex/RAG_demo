# rag/rag_singleton.py
print("Importing FAISS...")

from langchain.vectorstores import FAISS
print("Importing SentenceTransformerEmbeddings...")

from langchain.embeddings import SentenceTransformerEmbeddings
from langchain_huggingface.llms import HuggingFacePipeline
from transformers import AutoTokenizer, pipeline, AutoModelForSeq2SeqLM
import torch
from langchain.chains import RetrievalQA

print("Loading RAG model and vectorstore...")  # Helpful debug print

# Load only once
embedding_model = SentenceTransformerEmbeddings(model_name="all-MiniLM-L6-v2")
vectorstore = FAISS.load_local("vector_store", embedding_model, allow_dangerous_deserialization=True)

model_id = "google/flan-t5-small"
tokenizer = AutoTokenizer.from_pretrained(model_id)
model = AutoModelForSeq2SeqLM.from_pretrained(model_id)

pipe = pipeline("text2text-generation", model=model, tokenizer=tokenizer, max_new_tokens=128)
llm = HuggingFacePipeline(pipeline=pipe)

# Final chain (can be reused)
qa_chain = RetrievalQA.from_chain_type(
    llm=llm,
    retriever=vectorstore.as_retriever(),
    chain_type="map_reduce"
)
