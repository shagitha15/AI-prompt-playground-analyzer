from langchain_core.prompts import PromptTemplate

def run_one_shot(llm, question):

    prompt = PromptTemplate(
        input_variables=["question"],
        template="""
Example:

Q: Why do plants need sunlight?
A: Plants use sunlight for photosynthesis.

Now answer:

Q: {question}
A:
"""
    )

    chain = prompt | llm
    return chain.invoke({"question": question})