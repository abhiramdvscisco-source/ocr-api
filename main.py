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
    try:
        img = Image.open(file.file)
        text = pytesseract.image_to_string(img)
        return {"text": text}
    except Exception as e:
        return JSONResponse(status_code=400, content={"error": str(e)})
