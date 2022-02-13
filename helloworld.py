import gradio as gr

def hello_world(txt):
    return f"Hello {txt}"

gr.Interface(
    hello_world,
    "text",
    "text"
).launch()