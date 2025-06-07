
import gradio as gr
from pathlib import Path
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
import uvicorn

from gradio_motioncanvasplayer import MotionCanvasPlayer

project_path = "public/project-3.17.2.js"

# create a FastAPI app
app = FastAPI()

# create a static directory to store the static public files
static_dir = Path('./public')
static_dir.mkdir(parents=True, exist_ok=True)

# mount FastAPI StaticFiles server
app.mount("/public", StaticFiles(directory=static_dir), name="public")

example = MotionCanvasPlayer().example_value()

demo = gr.Interface(
    lambda x:x,
    MotionCanvasPlayer(project_path),  # interactive version of your component
    MotionCanvasPlayer(project_path),  # static version of your component
    # examples=[[example]],  # uncomment this line to view the "example version" of your component
)

app = gr.mount_gradio_app(app, demo, path="/")
if __name__ == "__main__":

    # serve the app
    uvicorn.run(app, host="0.0.0.0", port=7860)