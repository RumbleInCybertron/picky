from fastapi import FastAPI, UploadFile, File
from app import compress_image
from app import save_image
import os
import shutil

app = FastAPI()

# Allow CORS from the Next.js frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

IMAGE_DIR = "images/"
DATA_FILE = "data/images.json"

# Ensure image directory exists
os.makedirs(IMAGE_DIR, exist_ok=True)

@app.post("/images/")
async def upload_image(file: UploadFile = File(...)):
  filepath = os.path.join(IMAGE_DIR, file.filename)
  with open(filepath, "wb") as buffer:
    shutil.copyfileobj(file.file, buffer)
    
  compressed_filepath = compress_image(filepath)
  image_data = save_image(file.filename, filepath, compressed_filepath)
  return image_data

