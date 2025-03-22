import getpass
import os

from langchain_core.prompts import ChatPromptTemplate
from langchain.chat_models import init_chat_model


def translate_with_openai_gpt(language, text):
    if not os.environ.get("OPENAI_API_KEY"):
        pass
    else:
        os.environ["OPENAI_API_KEY"] = getpass.getpass("Enter API key for OpenAI: ")

    model = init_chat_model("gpt-4o-mini", model_provider="openai")

    system_template = "Translate the following from English into {language}"

    prompt_template = ChatPromptTemplate.from_messages(
        [("system", system_template), ("user", "{text}")]
    )

    prompt = prompt_template.invoke({"language": language, "text": text})
    return model.invoke(prompt)
