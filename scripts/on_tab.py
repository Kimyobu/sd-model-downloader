import gradio as gr
from modules import script_callbacks
from modules.scripts import os
import time

def on_ui_tabs():
    with gr.Blocks(analytics_enabled=False) as ui_component:
        with gr.Row():
            model_type = gr.Dropdown(
                ["adetailer", "deepdanbooru", "karlo", "sam", "VAE-approx", "Codeformer", "ESRGAN", "LDSR",
                    "Stable-diffusion", "ControlNet", "GFPGAN", "Lora", "SwinIR", "deepbooru", "hypernetworks", "LyCORIS", "VAE"],
                label='Model '
            )
            model_url = gr.Textbox(
                label='Model Url', placeholder="Place model download url here (Not a url of page of model card)")
            submit = gr.Button(value='Download', variant='primary').style(
                full_width=False)

        with gr.Row():
            folder = gr.Textbox(
                label='Directory Path', value='embeddings', placeholder='Type your directory here')
            url = gr.Textbox(
                label='Download URL', placeholder="Place model download url here (Not a url of page of model card)")
            submit2 = gr.Button(value='Download', variant='primary').style(
                full_width=False)

        with gr.Row():
            output = gr.Text(label='Output',value='Status:',interactive=False)
            current = gr.List(label='Current List',col_count=3, headers=['File', 'Changed', 'Path'])

        submit.click(
            sub1,
            inputs=[model_type, model_url],
            outputs=[output,current]
        )

        submit2.click(
            sub2,
            inputs=[folder, url],
            outputs=[output,current]
        )

        return [(ui_component, "Model Downloader", "sd_model_downloader_tab")]


def sub1(model_type, model_url):
    uri = f"\"{model_url}\""
    model_path = f'{os.getcwd()}/models/{model_type}'
    if not os.path.exists(model_path):
        os.makedirs(model_path, exist_ok=True)
    if model_type == 'ControlNet':
        model_path = f'{os.getcwd()}/extensions/sd-we' + 'bui-controlnet/models'
    try:
        print(f'Downloading {model_url} to {model_path}')
        o = os.system(f'aria2c --console-log-level=error -c -x 16 -s 16 -k 1M {uri} -d {model_path}')
        if o != 0:
            return 'Failed: Check output in console', []
        else :
            output = []
            for x in os.listdir(model_path):
                p = f'{model_path}/{x}'
                output.append([x,time.ctime(os.path.getmtime(p)),p])
            return f'Status: Download {model_url} success [{model_path}]', output
    except Exception as Error:
        return f'Error: {Error}', []


def sub2(folder, url):
    uri = f"\"{url}\""
    folder = f'{os.getcwd()}/{folder}'
    if not os.path.exists(folder):
        os.makedirs(folder, exist_ok=True)
    try:
        print(f'Downloading {url} to {folder}')
        o = os.system(f'aria2c --console-log-level=error -c -x 16 -s 16 -k 1M {uri} -d {folder}')
        if o != 0:
            return 'Failed: Check output in console', []
        else :
            output = []
            for x in os.listdir(folder):
                p = f'{folder}/{x}'
                output.append([x,time.ctime(os.path.getmtime(p)),p])
            return f'Status: Download {url} success [{folder}]', output
    except Exception as Error:
        return f'Error: {Error}', []


script_callbacks.on_ui_tabs(on_ui_tabs)
