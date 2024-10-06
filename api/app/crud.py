from uuid import uuid4
import json
import os

DATA_FILE = "data/images.json"

def load_data():
  # Check if the file exists and is not empty
  if os.stat(DATA_FILE).st_size == 0:
    return []
  
  with open(DATA_FILE, "r") as file:
    return json.load(file)
  
def save_data(data):
  with open(DATA_FILE, "w") as file:
    json.dump(data, file, indent=4)

def save_image(filename, filepath, compressed_filepath):
  data = load_data()
  image_id = str(uuid4())
  image_data = {
    "id": image_id,
    "filename": filename,
    "filepath": filepath,
    "compressed_filepath": compressed_filepath,
  }
  data.append(image_data)
  save_data(data)
  return image_data