from fastai.vision.all import *
import gradio as gr

# import pathlib
# temp = pathlib.PosixPath
# pathlib.PosixPath = pathlib.WindowsPath

musical_instruments = (
    'Bansuri',
    'Harmonium',
    'Pakhawaz',
    'Santoor',
    'Sarangi',
    'Sarod',
    'Shehnai',
    'Sitar',
    'Tabla',
    'Tanpura'
)



model = load_learner("models/musical-instrument-recognizer-v6.pkl")


def recognize_image(image):
  pred, idx, probs = model.predict(image)
  return dict(zip(musical_instruments, map(float, probs)))



image = gr.Image()
label = gr.Label()
examples = [
    'bansuri.jfif',
    'harmonium.jfif',
    'pakhawaj.jfif',
    'santoor.jfif',
    'sarengi.jfif',
    'sarod.jfif',
    'shehnai.jfif',
    'sitar.jfif',
    'tabla.jfif',
    'tanpura.jfif'
]

iface = gr.Interface(fn=recognize_image, inputs = image, outputs= label, examples = examples)
iface.launch(inline =False, share =True)