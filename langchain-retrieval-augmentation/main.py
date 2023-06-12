import argparse
import os

from langchain.embeddings import OpenAIEmbeddings
from stages import *
from tqdm.auto import tqdm
from util import ensure_env_vars_exported

STAGE_DOC_STRING = """
    The mode to run this program in . Must be one of:

    - init (perform dataset loading and index creation)
    - upsert (upsert data to created index)
    - query (query data from created index)
    - teardown (cleanup: delete the pinecone index)

"""

parser = argparse.ArgumentParser()
parser.add_argument("-s", "--stage",
                    type=str,
                    help=STAGE_DOC_STRING,
                    choices=['init', 'upsert', 'query', 'teardown'],
                    required=True)
parser.add_argument("-i", "--index-name",
                    type=str,
                    help="Name of the pinecone index to use",
                    default="langchain-retrieveal-augmentation",
                    required=False)
parser.add_argument("-q", "--query",
                    type=str,
                    help="Query to run against the index. Ensure you have already run the init and upsert steps successfully!",
                    default="Who was Alan Turing?",
                    required=False,
                    )


args = parser.parse_args()

PINECONE_INDEX = args.index_name
CURRENT_STAGE = args.stage
QUERY = args.query

# Sanity check that required env vars have been exported, otherwise
# bail out early with a helpful error message explaining to the user
# which env vars are missing
ensure_env_vars_exported()

# Setup required env vars and script variables
BATCH_LIMIT = 100
MODEL_NAME = 'text-embedding-ada-002'
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
PINECONE_API_KEY = os.getenv("PINECONE_API_KEY")
PINECONE_ENVIRONMENT = os.getenv("PINECONE_ENVIRONMENT")

if CURRENT_STAGE == 'init':
    init_stage(PINECONE_INDEX, PINECONE_API_KEY, PINECONE_ENVIRONMENT)
elif CURRENT_STAGE == 'upsert':
    upsert_stage(PINECONE_INDEX, PINECONE_API_KEY,
                 PINECONE_ENVIRONMENT, OPENAI_API_KEY)
elif CURRENT_STAGE == 'query':
    query_stage(PINECONE_INDEX, PINECONE_API_KEY,
                PINECONE_ENVIRONMENT, OPENAI_API_KEY, QUERY)
elif CURRENT_STAGE == 'teardown':
    teardown_stage(PINECONE_INDEX, PINECONE_API_KEY, PINECONE_ENVIRONMENT)
else:
    print(f"Error: bad stage name passed to script: {CURRENT_STAGE}")
