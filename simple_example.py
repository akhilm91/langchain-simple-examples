from langchain.chat_models import ChatOpenAI as chat_open_ai
from dotenv import load_dotenv
import os


load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")
chat_model = chat_open_ai(openai_api_key = api_key)

result = chat_model.predict("hello world")
print(result)
