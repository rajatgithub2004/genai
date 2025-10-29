from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI(model='gpt-4', temprature=0)

result = model.invoke("what is the capital of india")
print(result.content)