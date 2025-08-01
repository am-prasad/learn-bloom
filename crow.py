# crow.py

import os
from dotenv import load_dotenv
from langchain.chains import LLMChain
from langchain.prompts.chat import ChatPromptTemplate
from langchain_groq import ChatGroq

# ✅ Load environment variables from .env file
load_dotenv()

# 🔐 Set your Groq API key securely
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
if not GROQ_API_KEY:
    raise ValueError("Missing GROQ_API_KEY in environment variables.")
os.environ["GROQ_API_KEY"] = GROQ_API_KEY

# 🧠 Load Groq LLM (LLaMA3 70B)
llm = ChatGroq(
    model_name="llama3-70b-8192"
)

# 📘 Define the Crow-style prompt
template = """You are Crow, an academic assistant for first-year engineering students at JSSSTU, Mysuru.
Your goal is to answer only the specific question asked by the user, using concise, textbook-like language.

Rules:
- Don't provide extra explanation unless asked.
- If the concept can be remembered using a trick or acronym (e.g., VIBGYOR for rainbow colors), include it.
- Never make up content or examples unless you are sure.
- Keep your answer under 80 words unless the question demands more.
- Avoid repetition. Be direct.

Question: {question}
"""

prompt = ChatPromptTemplate.from_template(template)

# 🔗 Build the chain
crow_chain = LLMChain(llm=llm, prompt=prompt, verbose=False)

# 🔁 Function to call from API
def run_crow_chain(query: str) -> str:
    return crow_chain.run(query)
