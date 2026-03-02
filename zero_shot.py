from langchain_core.prompts import PromptTemplate

def run_zero_shot(llm, question):

    prompt = PromptTemplate(
        input_variables=["question"],
        template="""
Answer the following question clearly.

Question: {question}

Answer:
"""
    )

    chain = prompt | llm
    return chain.invoke({"question": question})