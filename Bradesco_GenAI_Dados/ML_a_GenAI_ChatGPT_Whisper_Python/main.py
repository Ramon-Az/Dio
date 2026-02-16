# https://github.com/github-copilot/code_referencing?cursor=1992805ba82c52ada975e0f9dfd3f218

language = "pt-BR"

from IPython.display import Audio, display, Javascript
from google.colab import output
from base64 import b64decode
import os

RECORD = """
Const sleep = time => new Promise(resolve => setTimeout(resolve, time))
Const b2text = blob => new Promise(resolve => {
    const reader = new FileReader()
    reader.onloadend = e => resolve(e.srcElement.result)
    reader.readAsDataURL(blob)
})

var record = time => new Promise(async resolve => {
    const stream = await navigator.mediaDevices.getUserMedia({ audio: true })
    record = new MediaRecorder(stream)
    chunks = []
    record.ondataavailable = e => chunks.push(e.data)
    record.start()
    await sleep(time)
    recorder.onstop = async () => {
        blob = new Blob(chunks)
        text = await b2text(blob)
        resolve(text)
    }
    recorder.stop()
}) 
"""
def record(seconds=5):
    display(Javascript(RECORD))
    js_result = output.eval_js('record(%s)' % (seconds * 1000))
    audio = b64decode(js_result.split(',')[1])
    file_name = 'request_audio.wav'
    with open(file_name, 'wb') as f:
        f.write(audio)
    return f'./data/{file_name}'

recorded_audio = record()
display(Audio(recorded_audio, autoplay=True))