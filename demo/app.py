
import gradio as gr
from pathlib import Path
import uvicorn

from gradio_motioncanvasplayer import MotionCanvasPlayer

project_path = "/gradio_api/file=demo/public/project-3.17.2.js"


gr.set_static_paths(paths=[Path.cwd().absolute()/"demo/public"])

demo = gr.Interface(
    lambda x:x,
    None,  # interactive version of your component, not relevant for this demo
    MotionCanvasPlayer(project_path, auto=True, quality=0.5, width=1920, height=1080, variables="{}"),  # static version of your component
    clear_btn=None

)

if __name__ == '__main__':
    demo.launch(server_name="0.0.0.0", server_port=7860)