from uuid import uuid4
import json
import os

DATA_FILE = "data/images.json"

def load_data():
  # Check if the file exists and is not empty
  if os.stat(DATA_FILE).st_size == 0:
    return []
  
  # Load image data from the JSON file.
  with open(DATA_FILE, "r") as file:
    return json.load(file)
  
def save_data(data):
  # Save updated image data to the JSON file.
  with open(DATA_FILE, "w") as file:
    json.dump(data, file, indent=4)

def save_image(filename, filepath, compressed_filepath):
  # Save image data to the JSON file and return the image data.
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

def get_image(image_id):
    # Get an image by its ID.
    data = load_data()
    for image in data:
        if image["id"] == image_id:
            return image
    return None
  
def get_all_images():
    # Retrieve all images from the JSON file.
    return load_data()

def delete_image(image_id):
    #Delete an image by its ID.
    data = load_data()
    updated_data = [image for image in data if image["id"] != image_id]
    save_data(updated_data)
    return {"message": "Image deleted successfully"}