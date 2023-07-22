import modules.scripts as scripts
import gradio as gr

from modules import shared
from modules import script_callbacks

def on_ui_settings():
    section = ('downloader', "Model Downloader")
    shared.opts.add_option(
        "option1",
        shared.OptionInfo(
            False,
            "option1 description",
            gr.Checkbox,
            {"interactive": True},
            section=section)
    )

script_callbacks.on_ui_settings(on_ui_settings)
