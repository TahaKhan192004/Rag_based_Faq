sample_docs = [
    "What is Git? Git is a distributed version control system for tracking changes in source code during software development.",
    "How do I create a Python virtual environment? You can create a virtual environment using `python -m venv myenv` or `conda create -n myenv python=3.9`.",
    "What is a FastAPI endpoint? A FastAPI endpoint is a function decorated with an HTTP method (like `@app.get` or `@app.post`) that handles incoming web requests.",
    "Explain Python's `list` data structure. A list in Python is an ordered, mutable collection of items. It allows duplicate members and can contain items of different data types."
]
import chromadb
from sentence_transformers import SentenceTransformer

# Step 1: Initialize ChromaDB client and collection
client = chromadb.Client()
faq_collection = client.get_or_create_collection(name="python_faqs")

# Step 2: Load Sentence Transformer model
model = SentenceTransformer('all-MiniLM-L6-v2')  # This will download the model on first run

# Step 3: Embed and add documents
for i, doc in enumerate(sample_docs):
    embedding = model.encode(doc).tolist()
    faq_collection.add(documents=[doc], embeddings=[embedding], ids=[f"doc_{i}"])

print("All documents added to ChromaDB successfully!")

# Step 4: Define a query
query_text = "How do I make a virtual environment?"

# Step 5: Embed the query
query_embedding = model.encode(query_text).tolist()

# Step 6: Perform similarity search
results = faq_collection.query(query_embeddings=[query_embedding], n_results=1) # CAN BE 2 OR 3 TOO

# Step 7: Printing results
print("My Query:", query_text)
print("Top Result:", results['documents'][0][0])
print("Similarity Distance:", results['distances'][0][0])


# Step 8: Simulate an augmented generation prompt
retrieved_document = results['documents'][0][0]
llm_prompt = f"Based on the following context, please answer the question.\nContext: {retrieved_document}\n\nQuestion: {query_text}"

print("\nConceptual LLM Prompt:")
print(llm_prompt)

