from langchain.chat_models import ChatOpenAI
from langchain.prompts.chat import ChatPromptTemplate
from langchain.schema import BaseOutputParser
from dotenv import load_dotenv
import os


load_dotenv()
api_key: str = os.getenv("OPENAI_API_KEY")

class AnswerOutputParser(BaseOutputParser):
    def parse(self, text: str):
        """Parse the output of an LLM call"""
        return text.strip().split("answer =")

chat_model: ChatOpenAI = ChatOpenAI(openai_api_key=api_key)

template: str = (
    "You are a helpful assistant that solves math problems and shows your work."
    "Output each step then return the answer in the following format: answer = <answer here>."
    "Make sure to output answer in all lowercases and to have exactly one space and one equal sign following it."
)
human_template: str = "{problem}"

chat_prompt: ChatPromptTemplate = ChatPromptTemplate.from_messages([
    ("system", template),
    ("human", human_template),
])

messages = chat_prompt.format_messages(problem="2x^2 - 5x + 3 = 0")
result = chat_model.predict_messages(messages=messages)
parsed = AnswerOutputParser().parse(result.content)
steps, answer = parsed

print(answer)
