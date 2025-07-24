
# RAG Exercise Report

## Objective

This exercise demonstrates how to build a simple Retrieval-Augmented Generation (RAG) system using ChromaDB and Sentence Transformers. The system retrieves relevant FAQ entries from a small set of internal Python development FAQs based on a user query.

---
## Purpose of Each Major Step

- **Initializing ChromaDB**  
  Sets up the vector database that stores and manages the embedded documents for efficient similarity search.

- **Loading the SentenceTransformer model**  
  Loads a pre-trained model that converts text into dense vector representations (embeddings) based on semantic meaning.

- **Embedding the documents**  
  Transforms each FAQ entry into a numerical format that can be compared mathematically for similarity.

- **Adding documents to ChromaDB**  
  Stores each document along with its embedding in the database, making it retrievable during a query.

- **Querying the system**  
  Converts a user's question into an embedding and searches the database to find the most semantically similar document(s).



## Setup and Installation

### Virtual Environment

A Python virtual environment was created to isolate dependencies:

```bash
python -m venv venv
source venv/bin/activate  # For Windows: venv\Scripts\activate
````

### Dependencies Installed

The following Python libraries were installed using pip:

```bash
pip install chromadb sentence-transformers
```

* `chromadb`: Used as an in-memory vector database to store and query embedded documents.
* `sentence-transformers`: Used to convert both documents and queries into dense vector embeddings.

---

## Sample Documents

The following documents were used to simulate internal company FAQs:

```python
sample_docs = [
    "What is Git? Git is a distributed version control system for tracking changes in source code during software development.",
    "How do I create a Python virtual environment? You can create a virtual environment using `python -m venv myenv` or `conda create -n myenv python=3.9`.",
    "What is a FastAPI endpoint? A FastAPI endpoint is a function decorated with an HTTP method (like `@app.get` or `@app.post`) that handles incoming web requests.",
    "Explain Python's `list` data structure. A list in Python is an ordered, mutable collection of items. It allows duplicate members and can contain items of different data types."
]
```

Each document was added to ChromaDB with a unique ID (`doc_0`, `doc_1`, etc.) and embedded using the `all-MiniLM-L6-v2` model.

---

## Querying the RAG System

### Primary Query Example

```python
query_text = "How do I make a virtual environment?"
```

**Top result:**

```
How do I create a Python virtual environment? You can create a virtual environment using `python -m venv myenv` or `conda create -n myenv python=3.9`.
```

**Distance:** 0.89 (example)

The result is a strong match. A lower distance means higher similarity.

---

## Additional Query Examples

### Query 1: "What does actually Git do?"

* **Top result:**

  ```
  What is Git? Git is a distributed version control system for tracking changes in source code during software development.
  ```
* **Distance:** \~0.34

### Query 2: "How do I build an API in Python?"

* **Top result:**

  ```
  What is a FastAPI endpoint? A FastAPI endpoint is a function decorated with an HTTP method (like `@app.get` or `@app.post`) that handles incoming web requests.
  ```
* **Distance:** \~0.34

### Query 3: "Tell me about Python lists."

* **Top result:**

  ```
  Explain Python's `list` data structure. A list in Python is an ordered, mutable collection of items. It allows duplicate members and can contain items of different data types.
  ```
* **Distance:** \~0.25
---

## Conceptual LLM Prompt

For a query like:
**"How do I make a virtual environment?"**

The conceptual prompt that could be sent to an LLM is:

```
Based on the following context, please answer the question.

Context: How do I create a Python virtual environment? You can create a virtual environment using `python -m venv myenv` or `conda create -n myenv python=3.9`.

Question: How do I make a virtual environment?
```

---

## Benefits of RAG vs. Standalone LLM

**Standalone LLM:**

* May fabricate answers (hallucinations).
* Not grounded in current or internal knowledge.

**RAG System:**

* Uses specific, trusted documents as context.
* Improves accuracy and explainability.
* Easily updatable (add documents, no retraining).

---

## Challenges and Resolutions

| Issue                                             | Resolution                                                                                       |
| ------------------------------------------------  | ------------------------------------------------------------------------------------------------ |
| Model and Library download took time on first run | Waited for initial download; subsequent runs were faster.                                        |
| Less relevant results for unseen topics           | Verified behavior by checking distances and experimenting with multiple results (`n_results=3`). |



