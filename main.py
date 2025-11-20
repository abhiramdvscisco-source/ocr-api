from fastapi import FastAPI, UploadFile, File
from fastapi.responses import JSONResponse
from PIL import Image
import pytesseract

app = FastAPI()

@app.get("/")
def root():
    return {"message": "OCR API running"}

@app.post("/ocr")
async def ocr_image(file: UploadFile = File(...)):
    print("---- Incoming request ----")
    print("filename:", file.filename)
    print("content_type:", file.content_type)
    print("--------------------------")

    if file.filename is None:
        return {"error": "No file uploaded"}

    img = Image.open(file.file)
    text = pytesseract.image_to_string(img)
    return {"text": text}
