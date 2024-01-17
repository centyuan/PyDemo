import chromadb
from typing import Type

chroma_client = chromadb.Client()

# 1.创建一个collection
# collection = chroma_client.create_collection(name="test-chroma")
collection = chroma_client.create_collection(name="test-chroma")

# 使用Chroma默认的all-MiniLM-L6-v2 方式进行embedding
collection.add(
    documents=["This is a document", "This is another document"],
    metadatas=[{"source": "my_source"}, {"source": "my_source"}],
    ids=["id1", "id2"]
)

results = collection.query(
    query_texts=["This is a query document"],
    n_results=2
)
print(results)