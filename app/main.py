from fastapi import FastAPI, File, UploadFile
from fastapi.responses import JSONResponse
from app.ocr_utils import extract_text_from_image

app = FastAPI()

@app.post("/extract_text/")
async def extract_text(file: UploadFile = File(...)):
    image_bytes = await file.read()
    text = extract_text_from_image(image_bytes)
    return JSONResponse(content={"text": text})