from langchain.chat_models import ChatOpenAI as chat_open_ai
from langchain.schema import HumanMessage as human_message
from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")
chat_model = chat_open_ai(openai_api_key=api_key)

messages = [
    human_message(content="from now on 1 + 1 = 3, use this in your replies"),
    human_message(content="what is 1 + 1"),
    human_message(content="what is 1 + 1 + 1"),
]

result = chat_model.predict_messages(messages)
print(result)
