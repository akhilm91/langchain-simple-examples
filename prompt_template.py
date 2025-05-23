from langchain.chat_models import ChatOpenAI
from langchain.prompts.chat import ChatPromptTemplate
from dotenv import load_dotenv
import os


load_dotenv()
api_key: str = os.getenv("OPENAI_API_KEY")

chat_model: ChatOpenAI = ChatOpenAI(openai_api_key=api_key)

template: str = "You are a helpful assistant that translates {input_language} to {output_language}"
human_template: str = "{text}"

chat_prompt: ChatPromptTemplate = ChatPromptTemplate.from_messages([
    ("system", template),
    ("human", human_template),
])

messages = chat_prompt.format_messages(
    input_language="English",
    output_language="French",
    text="I love programming",
)

result = chat_model.predict_messages(messages=messages)
print(result.content)
