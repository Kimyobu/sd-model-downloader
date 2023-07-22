import modules.scripts as scripts
import gradio as gr

from modules import script_callbacks


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
            submit = gr.Button('Download').style(full_width=False)

        with gr.Row():
            folder = gr.Textbox(
                label='Directory Path', value='embeddings', placeholder='Type your directory here')
            url = gr.Textbox(
                label='Download URL', placeholder="Place model download url here (Not a url of page of model card)")
            submit2 = gr.Button('Download').style(full_width=False)

        with gr.Row():
            output = gr.Text('Status:')

        submit.click(
            sub1,
            inputs=[model_type, model_url],
            outputs=[output]
        )

        submit2.click(
            sub2,
            inputs=[folder, url],
            outputs=[output]
        )

        return [(ui_component, "Model Downloader", "sd_model_downloader_tab")]


def sub1(model_type, model_url):
    model_url = f"\"{model_url}\""
    model_path = f'{scripts.os.getcwd()}/models/{model_type}'
    if not scripts.os.path.exists(model_path):
        scripts.os.makedirs(model_path, exist_ok=True)
    if model_type == 'ControlNet':
        model_path = f'{scripts.os.getcwd()}/extensions/sd-we' + \
            'bui-controlnet/models'
    try:
        scripts.os.system(
            f'aria2c --console-log-level=error -c -x 16 -s 16 -k 1M {model_url} -d {model_path}')
        return [f'Status: Download {model_url} success [{model_path}]']
    except Exception as Error:
        return [f'Error: {Error}']


def sub2(folder, url):
    url = f"\"{url}\""
    folder = f'{scripts.os.getcwd()}/{folder}'
    if not scripts.os.path.exists(folder):
        scripts.os.makedirs(folder, exist_ok=True)
    try:
        scripts.os.system(
            f'aria2c --console-log-level=error -c -x 16 -s 16 -k 1M {url} -d {folder}')
        return [f'Status: Download {url} success [{folder}]']
    except Exception as Error:
        return [f'Error: {Error}']


script_callbacks.on_ui_tabs(on_ui_tabs)
