import os
import sys


def ensure_env_vars_exported():
    """Ensure that all required environment variables are exported
    """
    required_vars = (
        "OPENAI_API_KEY",
        "PINECONE_API_KEY",
        "PINECONE_ENVIRONMENT",
    )

    missing_vars = []
    for var in required_vars:
        if var not in os.environ:
            missing_vars.append(var)
    if len(missing_vars) > 0:
        print(
            f"Missing required environment variables: {', '.join(missing_vars)}")
        sys.exit(1)
    print("All required environment variables are exported")
