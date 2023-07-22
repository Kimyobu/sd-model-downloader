import gradio as gr


def b1(name, age):
    return [['Test', 'Fri2', '/myComputer/Test'], ['Test2', 'Fri3', '/myComputer/Test2']]


with gr.Blocks() as ui:
    with gr.Row():
        name = gr.Textbox(label='Name')
        age = gr.Textbox(label='Age')
        b = gr.Button(value='Add', variant='primary').style(
            full_width=False)
        
    with gr.Row():
        table = gr.List(headers=['File', 'Changed', 'Path'], col_count=3)

    b.click(b1, inputs=[name, age], outputs=[table])

    ui.launch(server_port=7777)
