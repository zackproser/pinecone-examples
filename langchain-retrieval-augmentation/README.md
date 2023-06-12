# Pinecone Langchain Retrieval Augmentation example

![Pinecone langchain retrieval example](../_docs/langchain-retrieval.gif)

## Setup 

```bash
pip install -r requirements.txt
```

## Run a stage 

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

## Run a query 

Once you have successfully run the `init` and `upsert` stages, you can run a query like so:

```bash
python main.py -s query -q "Who be Alan Turing?"
```

You should get output like the following:
```bash
All required environment variables are exported
Stage query running...
Query results: Alan Turing was an English mathematician and computer scientist who was born in Maida Vale, London on June 23, 1912, and died on June 7, 1954. He is considered the founder of modern-day computer science and artificial intelligence. During World War II, he worked for the Government Code and Cypher School (GC&CS) at Bletchley Park, Britain's codebreaking center that produced Ultra intelligence. He helped to break the codes of the Enigma machine, which made the single biggest contribution to the Allied victory in the war against Nazi Germany, possibly saving the lives of an estimated 2 million people, through his effort in shortening World War II. Turing was also a homosexual man and was convicted in 1952 for having sex with a man, which was illegal at that time. He was subjected to chemical castration and died in 1954, possibly by suicide.
```


