import os

from langchain_core.prompts import PromptTemplate
from langchain.llms.llamacpp import LlamaCpp


def translate_with_llama(language, text):
    env_model_path = os.environ.get("GGUF_MODEL_PATH")

    if env_model_path and os.path.isfile(os.path.expanduser(env_model_path)):
        model_path = os.path.expanduser(env_model_path)

    llm = LlamaCpp(
        model_path=model_path,
        temperature=0.7,
        max_tokens=256,
        n_ctx=2048,
        verbose=True,
    )

    prompt = PromptTemplate.from_template("Translate the following from English into {language}: {text}")
    return llm(prompt.format(language=language, text=text))
