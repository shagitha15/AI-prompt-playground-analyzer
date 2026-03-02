import gradio as gr
from langchain_ollama import OllamaLLM

from prompts.zero_shot import run_zero_shot
from prompts.one_shot import run_one_shot
from prompts.few_shot import run_few_shot
from prompts.cot import run_cot
from prompts.react import run_react

from utils.token_counter import token_count


def load_llm(temp):
    return OllamaLLM(model="llama3.2:1b", temperature=temp)


def run_experiment(question, techniques, temperature):

    llm = load_llm(temperature)

    outputs = {}
    tokens = {}

    if "Zero Shot" in techniques:
        result = run_zero_shot(llm, question)
        outputs["Zero Shot"] = result
        tokens["Zero Shot"] = token_count(result)

    if "One Shot" in techniques:
        result = run_one_shot(llm, question)
        outputs["One Shot"] = result
        tokens["One Shot"] = token_count(result)

    if "Few Shot" in techniques:
        result = run_few_shot(llm, question)
        outputs["Few Shot"] = result
        tokens["Few Shot"] = token_count(result)

    if "Chain of Thought" in techniques:
        result = run_cot(llm, question)
        outputs["Chain of Thought"] = result
        tokens["Chain of Thought"] = token_count(result)

    if "ReAct" in techniques:
        result = run_react(llm, question)
        outputs["ReAct"] = result
        tokens["ReAct"] = token_count(result)

    output_text = ""
    token_text = ""

    for k, v in outputs.items():
        output_text += f"\n\n===== {k} =====\n\n{v}"

    for k, v in tokens.items():
        token_text += f"{k}: {v} tokens\n"

    return output_text, token_text


with gr.Blocks() as demo:

    gr.Markdown("# 🤖 AI Prompt Playground Analyzer")

    question = gr.Textbox(
        label="Enter Question",
        placeholder="Example: Why is the sky blue?"
    )

    techniques = gr.CheckboxGroup(
        [
            "Zero Shot",
            "One Shot",
            "Few Shot",
            "Chain of Thought",
            "ReAct"
        ],
        label="Prompt Techniques"
    )

    temperature = gr.Slider(0, 1, value=0.3, step=0.1, label="Temperature")

    run_btn = gr.Button("Run Experiment")

    outputs = gr.Textbox(label="Outputs", lines=20)
    tokens = gr.Textbox(label="Token Usage")

    run_btn.click(
        run_experiment,
        inputs=[question, techniques, temperature],
        outputs=[outputs, tokens]
    )


demo.launch()