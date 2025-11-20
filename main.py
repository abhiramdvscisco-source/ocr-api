from fastapi import FastAPI, UploadFile, File
import pytesseract
from PIL import Image
import io

app = FastAPI()

@app.get("/")
def home():
    return {"status": "ok", "message": "OCR API is running"}

@app.post("/ocr")
async def ocr_image(file: UploadFile = File(...)):
    content = await file.read()
    img = Image.open(io.BytesIO(content))
    text = pytesseract.image_to_string(img)
    return {"text": text}
