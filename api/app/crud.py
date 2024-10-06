from uuid import uuid4
import json
import os

DATA_FILE = "data/images.json"
IMAGE_DIR = "images/"

def load_data():
  # Check if the file exists and is not empty
  if os.stat(DATA_FILE).st_size == 0:
    return []
  
  # Load image data from the JSON file.
  with open(DATA_FILE, "r") as file:
    try:
      return json.load(file)
    except json.JSONDecodeError:
      return []
  
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
    # Delete an image by its ID.
    data = load_data()
    
    image_to_del = next((i for i in data if i['id'] == image_id), None)
    
    if image_to_del:
      # Delete the physical img file from the file system
      # image_path = os.path.join(IMAGE_DIR, image_to_del['filepath'])
      image_filename = image_to_del['filepath']
      compressed_image_filename = image_to_del['compressed_filepath']
      
      # Track the success of file deletions
      original_deleted = False
      compressed_deleted = False
      
      # Check if image file exists and remove it
      if os.path.exists(image_filename):
        os.remove(image_filename)
        original_deleted = True
        
      # Check if compressed image file exists and remove it
      if os.path.exists(compressed_image_filename):
        os.remove(compressed_image_filename)
        compressed_deleted = True
        
      # Remove the img metadata from the json data
      if original_deleted and compressed_deleted:
        data.remove(image_to_del)
        save_data(data)
      else:
        print("One or both files could not be deleted. Metadata not removed.")
    
    # updated_data = [image for image in data if image["id"] != image_id]
    # save_data(updated_data)
    return {"message": "Image deleted successfully"}