import gradio as gr
import requests
import cv2


def make_requests(content, style_url):
    _ , encoded_image = cv2.imencode('.png', content)
    r = requests.post(
        "https://api.deepai.org/api/fast-style-transfer",
        data={'style': style_url},
        files = {'content': encoded_image},
        headers={'api-key': '48392ba2-e96c-4dfe-9cb3-b4bf4059987e'}
    )
    return r.json()["output_url"]

inputs = [
    gr.inputs.Image(source="webcam"),
    gr.inputs.Textbox(lines=1, placeholder="image url", label = "Image Style")
]

gr.Interface(
    fn = make_requests,
    inputs = inputs,
    outputs = gr.outputs.Image(type="file"), 
).launch()


