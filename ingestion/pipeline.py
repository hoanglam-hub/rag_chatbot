from langchain_text_splitters import RecursiveCharacterTextSplitter
from config.loader import chunk_size, chunk_overlap
import os
from ingestion.loadermarkitdown import markitdown_loader

def load_and_chunk():
    doc = markitdown_loader()
    splitter = RecursiveCharacterTextSplitter(chunk_size = chunk_size, chunk_overlap = chunk_overlap)
    chunks = splitter.split_documents(doc)
    return chunks



