
"""
LangChain + OpenAI app with LangSmith tracing configured through .env.

Required .env variables:
OPENAI_API_KEY=your-openai-api-key
LANGSMITH_API_KEY=your-langsmith-api-key
LANGSMITH_TRACING=true
LANGSMITH_PROJECT=langchain-tracing-practice

Run:
    pip install langchain langchain-openai langsmith python-dotenv
    python traced_app.py
"""

from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

# Step 1: Load environment variables from .env
load_dotenv()


# Step 2: Initialize LangChain ChatOpenAI
llm = ChatOpenAI(
    model="gpt-4o-mini",
)


# Step 3: Define at least 3 different prompts
prompts = [
    "Explain the langsmith tracing feature in LangChain and how it can be used to debug and monitor LLM applications.",

    "What are some best practices for using LangSmith tracing in production applications?",

    "How can LangSmith tracing help in identifying performance bottlenecks in LangChain applications?"
]


# Step 4: Send prompts and print responses
def main():

    for index, prompt in enumerate(prompts, start=1):

        print("\n" + "=" * 70)
        print(f"RUN {index}")
        print(f"PROMPT: {prompt}")
        print("-" * 70)

        response = llm.invoke(prompt)

        print("ANSWER:")
        print(response.content)


# Step 5: Execute application
if __name__ == "__main__":
    main()