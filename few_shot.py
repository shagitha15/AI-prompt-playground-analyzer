from langchain_core.prompts import PromptTemplate

def run_few_shot(llm, question):

    prompt = PromptTemplate(
        input_variables=["question"],
        template="""
Example 1:
Q: Why are leaves green?
A: Chlorophyll reflects green light.

Example 2:
Q: Why is the ocean blue?
A: Water scatters blue wavelengths.

Now answer:

Q: {question}
A:
"""
    )

    chain = prompt | llm
    return chain.invoke({"question": question})