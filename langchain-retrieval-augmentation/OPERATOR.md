# Setup 

```bash
pip install -r requirements.txt
```

# Run a stage 

This program consists of multiple stages, to make it easier to work with the example: 

* `init`: Initialize the project. This will create the pinecone index, if it doesn't already exist. Note that creating an index may take around 1 minute.
* `upsert`: Pre-process the dataset and create the embeddings and vector store.
* `query`: Query the embeddings and return the results
* `teardown`: Clean up, by deleting the Pinecone index

Run a stage like so: 

```bash 
python main.py --stage init
```
or

```bash
python main.py --stage teardown
```

