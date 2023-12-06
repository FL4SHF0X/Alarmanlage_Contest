import pathlib

from fastapi import FastAPI

app = FastAPI()

@app.get('/sperren/{code}')
async def sperren(code):
    datei = pathlib.Path("alarmanlagen_code.txt")
    if not datei.exists():
        datei.write_text(code)

    return {"Antwort": "Alarmanlage scharf"}

@app.post("/entsperren/{code}")
async def entsperren(code):
    datei = pathlib.Path("alarmanlagen_code.txt")
    if code == datei.read_text():
        return {"Antwort": "Alarmanlage entschärft"}
    if not code == datei.read_text():
        return {"Antwort": "Alarm, Alarm"}

