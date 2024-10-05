from PIL import Image

def compress_image(filepath: str) -> str:
  compressed_filepath = filepath.replace(".jpg", "_compressed.jpg")
  with Image.open(filepath) as img:
    img = img.convert("RGB")
    img.save(compressed_filepath, "JPEG", quality=50)
  return compressed_filepath