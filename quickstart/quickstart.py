import os
import sys

import pinecone

api_key = os.getenv("PINECONE_API_KEY")

if api_key is None:
    print("You must set PINECONE_API_KEY environment variable")
    sys.exit(1)

pinecone_environment = os.getenv("PINECONE_ENVIRONMENT")
if pinecone_environment is None:
    pinecone_environment = "us-west4-gcp-free"
    print(
        f"No PINECONE_ENVIRONMENT set, using default: {pinecone_environment}")


pinecone.init(api_key=api_key,
              environment="us-west4-gcp-free")

NEEDS_CREATE = False

existing_indexes = pinecone.list_indexes()

if len(existing_indexes) == 0:
    NEEDS_CREATE = True

if NEEDS_CREATE:
    print("Found no existing indexes, so creating a 'quickstart' index now...")
    print("Sit tight as this may take around a minute...")
    pinecone.create_index("quickstart", dimension=8, metric='euclidean')
    print("Done!")

index = pinecone.Index("quickstart")

print("Upserting some text vectors to index...")
index.upsert([
    ("A", [0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1]),
    ("B", [0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2]),
    ("C", [0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3]),
    ("D", [0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4]),
    ("E", [0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5])
])

print("Describing index...")
print(index.describe_index_stats())

query_result = index.query(
    vector=[0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3],
    top_k=4,
    include_values=True
)

print(f"Query result: {query_result}")

print("Performing teardown and deleting index...")
pinecone.delete_index("quickstart")
