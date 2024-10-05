from uuid import uuid4
import json

def load_data():
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