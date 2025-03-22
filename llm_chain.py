import os


language = input("Enter target language [Russian]: ").strip() or "Russian"
text = input("Enter text to translate [Putin sucks!]: ").strip() or "Putin sucks!"

env_model_path = os.environ.get("GGUF_MODEL_PATH")

if env_model_path and os.path.isfile(os.path.expanduser(env_model_path)):
    from llm_chain_local_llama import translate_with_llama
    print(translate_with_llama(language, text))

if os.environ.get("OPENAI_API_KEY"):
    from llm_chain_openai_gpt import translate_with_openai_gpt
    print(translate_with_openai_gpt(language, text))
