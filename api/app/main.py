from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from app import compress_image
from app import save_image, get_image, delete_image, get_all_images
import os
import shutil
import json

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

# Ensure directories and json file exist on startup
def initialize_files():
  os.makedirs(IMAGE_DIR, exist_ok=True)
  if not os.path.exists(DATA_FILE):
    os.makedirs(os.path.dirname(DATA_FILE), exist_ok=True)
    with open(DATA_FILE, 'w') as f:
      json.dump([], f)
      
@app.on_event("startup")
async def startup_event():
  initialize_files()

@app.post("/images/")
async def upload_image(file: UploadFile = File(...)):
  filepath = os.path.join(IMAGE_DIR, file.filename)
  with open(filepath, "wb") as buffer:
    shutil.copyfileobj(file.file, buffer)
    
  compressed_filepath = compress_image(filepath)
  image_data = save_image(file.filename, filepath, compressed_filepath)
  return image_data

@app.get("/images/")
async def list_images():
    return get_all_images()

@app.get("/images/{image_id}")
async def download_image(image_id: str):
    image = get_image(image_id)
    if not image:
        raise HTTPException(status_code=404, detail="Image not found")
    return FileResponse(os.path.join(IMAGE_DIR, image["filename"]))

@app.delete("/images/{image_id}")
async def remove_image(image_id: str):
    return delete_image(image_id)