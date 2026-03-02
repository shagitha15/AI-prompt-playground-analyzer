from langchain_core.prompts import PromptTemplate

def run_react(llm, question):

    prompt = PromptTemplate(
        input_variables=["question"],
        template="""
You are a reasoning assistant.

Question: {question}

Thought:
Action:
Observation:
Final Answer:
"""
    )

    chain = prompt | llm
    return chain.invoke({"question": question})