from dotenv import load_dotenv
from langchain_groq import ChatGroq
import os


load_dotenv()

llm = ChatGroq(groq_api_key = os.getenv("GROQ_API_KEY"), model_name="llama-3.1-70b-versatile")

if __name__=="__main__":
    res = llm.invoke("What are the two main ingredients in pizza")
    print(res.content)