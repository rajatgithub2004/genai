from lanchain_openai import OpenAIEmbeddings

from dotenv import load_dotenv

load_dotenv()

embedding =OpenAIEmbeddings(model='text-embedding-3-large', dimensions=32)

documents=[
    "Delhi is th capital of india",
    "Kolkata is the capital of west bengal",
    "paris is the capital of france"
]

result = embedding.embed_documents(documents)

print(str(result))

