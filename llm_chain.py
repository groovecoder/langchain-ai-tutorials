import getpass
import os

from langchain.chat_models import init_chat_model
from langchain_core.prompts import ChatPromptTemplate

if not os.environ.get("OPENAI_API_KEY"):
    os.environ["OPENAI_API_KEY"] = getpass.getpass("Enter API key for OpenAI: ")

language = input("Enter target language [Russian]: ").strip() or "Russian"
text = input("Enter text to translate [Putin sucks!]: ").strip() or "Putin sucks!"

model = init_chat_model("gpt-4o-mini", model_provider="openai")

system_template = "Translate the following from English into {language}"

prompt_template = ChatPromptTemplate.from_messages(
    [("system", system_template), ("user", "{text}")]
)

prompt = prompt_template.invoke({"language": language, "text": text})

print(prompt)

prompt.to_messages()

response = model.invoke(prompt)
print(response.content)
