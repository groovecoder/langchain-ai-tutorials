# llm_chain

## setup
### Install python dependencies
1. `poetry install --no-root`

## run
### OpenAI GPT
1. `export OPENAI_API_KEY="<your OpenAI API Key>"`
2. `poetry run python llm_chain.py`

### Local llama
1. `poetry run huggingface-cli download TheBloke/Mistral-7B-Instruct-v0.1-GGUF <full-path-to-mistral-.guff>"`
2. `export GGUF_MODEL_PATH="<full-path-to-mistral-.GUFF/blobs/{blobID}>"`
3. `poetry run python llm_chain.py`
