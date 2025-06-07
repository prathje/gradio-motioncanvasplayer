
import gradio as gr
from gradio_motioncanvasplayer import MotionCanvasPlayer


example = MotionCanvasPlayer().example_value()

with gr.Blocks() as demo:
    with gr.Row():
        MotionCanvasPlayer(label="Blank"),  # blank component
        MotionCanvasPlayer(value=example, label="Populated"),  # populated component


if __name__ == "__main__":
    demo.launch()
