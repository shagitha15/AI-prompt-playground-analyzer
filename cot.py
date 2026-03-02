from langchain_core.prompts import PromptTemplate

def run_cot(llm, question):

    prompt = PromptTemplate(
        input_variables=["question"],
        template="""
Solve the problem step by step.

Question: {question}

Let's think step by step.
"""
    )

    chain = prompt | llm
    return chain.invoke({"question": question})