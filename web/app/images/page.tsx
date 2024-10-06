"use client";

import React, { useEffect, useState } from "react";

interface Image {
  id: string;
  filename: string;
  filepath: string;
}

const ImageList = () => {
  const [images, setImages] = useState<Image[]>([]);
  const [loading, setLoading] = useState(false);

  // Fetch all images from the API
  const fetchImages = async () => {
    setLoading(true);
    try {
      const response = await fetch("http://localhost:8000/images/", {
        method: "GET",
      });

      if (response.ok) {
        const data: Image[] = await response.json();
        setImages(data);
      } else {
        console.error("Failed to fetch images");
      }
    } catch (error) {
      console.error("Error fetching images:", error);
    }
    setLoading(false);
  };

  // Delete an image by id
  const deleteImage = async (id: string) => {
    const confirmDelete = confirm("Are you sure you want to delete this image?");
    if (!confirmDelete) return;

    try {
      const response = await fetch(`http://localhost:8000/images/${id}`, {
        method: "DELETE",
      });

      if (response.ok) {
        // Remove the deleted image from the state
        setImages(images.filter((image) => image.id !== id));
        alert("Image deleted successfully!");
      } else {
        console.error("Failed to delete image");
      }
    } catch (error) {
      console.error("Error deleting image:", error);
    }
  };

  useEffect(() => {
    fetchImages(); // Fetch images on component mount
  }, []);

  if (loading) {
    return <div className="text-center mt-4">Loading images...</div>;
  }

  return (
    <div className="container mx-auto p-4">
      <h1 className="text-2xl font-bold text-center mb-6">Image Gallery</h1>

      {images.length === 0 ? (
        <p className="text-center">No images available.</p>
      ) : (
        <div className="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 gap-6">
          {images.map((image) => (
            <div key={image.id} className="border p-4 rounded-lg shadow">
              <p className="font-semibold mb-2">{image.filename}</p>
              <img
                src={`http://localhost:8000/images/${image.id}`}
                alt={image.filename}
                className="w-full h-auto object-cover mb-4"
              />
              <div className="flex justify-between">
                <a
                  href={`http://localhost:8000/images/${image.id}`}
                  target="_blank"
                  rel="noopener noreferrer"
                  className="bg-blue-500 text-white py-2 px-4 rounded hover:bg-blue-600"
                >
                  View Image
                </a>
                <button
                  onClick={() => deleteImage(image.id)}
                  className="bg-red-500 text-white py-2 px-4 rounded hover:bg-red-600"
                >
                  Delete
                </button>
              </div>
            </div>
          ))}
        </div>
      )}
    </div>
  );
};

export default ImageList;