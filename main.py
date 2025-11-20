from fastapi import FastAPI, UploadFile, File, HTTPException
import numpy as np
import cv2
import pytesseract

app = FastAPI()

@app.get("/")
def root():
    return {"message": "OCR API is running"}

@app.post("/ocr")
async def ocr(file: UploadFile = File(...)):
    if not file.content_type.startswith("image/"):
        raise HTTPException(400, "Please upload an image")

    data = await file.read()
    npimg = np.frombuffer(data, np.uint8)
    img = cv2.imdecode(npimg, cv2.IMREAD_COLOR)

    if img is None:
        raise HTTPException(415, "Could not decode image")

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    text = pytesseract.image_to_string(gray)

    return {"text": text}
