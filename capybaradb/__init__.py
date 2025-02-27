"""
CapybaraDB Python SDK

The official Python library for CapybaraDB - an AI-native database that combines
NoSQL, vector storage, and object storage in a single platform.

This package provides a simple, intuitive interface for:
- Storing documents with embedded text fields (no manual embedding required)
- Performing semantic searches on your data
- Managing collections and databases

Key components:
- CapybaraDB: Main client class for connecting to the service
- EmbText: Special data type for text that will be automatically embedded
- EmbModels: Constants for supported embedding models
- EmbImage: Special data type for images that can be processed by vision models
- VisionModels: Constants for supported vision models

Important Note:
CapybaraDB processes embeddings asynchronously on the server side. When you insert documents
with EmbText or EmbImage fields, there will be a short delay (typically a few seconds) before
these documents become available for semantic search. This is because the embedding generation
happens in the background after the document is stored.

Basic usage:
```python
from capybaradb import CapybaraDB, EmbText
from dotenv import load_dotenv

# Load environment variables (CAPYBARA_API_KEY and CAPYBARA_PROJECT_ID)
load_dotenv()

# Initialize the client
client = CapybaraDB()

# Access a database and collection
collection = client.my_database.my_collection

# Insert a document with embedded text
doc = {
    "title": "Sample Document",
    "content": EmbText("This text will be automatically embedded for semantic search")
}
collection.insert([doc])

# Note: There will be a short delay before the document is available for semantic search
# as embeddings are processed asynchronously on the server side

# Perform semantic search (after embeddings have been processed)
results = collection.query("semantic search")
```

For more information, see the documentation at https://capybaradb.co/docs
"""

from ._client import CapybaraDB
from ._emb_json._emb_text import EmbText
from ._emb_json._emb_models import EmbModels
from ._emb_json._emb_image import EmbImage
from ._emb_json._vision_models import VisionModels
import bson

__all__ = ["CapybaraDB", "EmbText", "EmbModels", "EmbImage", "VisionModels", "bson"]
