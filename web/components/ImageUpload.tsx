'use client'

import React, { useState } from 'react';
import { useRouter } from "next/navigation";

const ImageUpload = () => {
  const [selectedFile, setSelectedFile] = useState<File | null>(null);
  const [previewUrl, setPreviewUrl] = useState<string | null>(null);
  const [error, setError] = useState("");
  const [loading, setLoading] = useState(false);
  const router = useRouter(); // Use the Next.js router for navigation

  // Handle file selection
  const handleFileChange = (event: React.ChangeEvent<HTMLInputElement>) => {
    if (event.target.files && event.target.files.length > 0) {
      const file = event.target.files[0];
      setSelectedFile(file);

      // Generate a preview URL for the uncompressed image
      const preview = URL.createObjectURL(file);
      setPreviewUrl(preview);
    }
  };

  // Handle form submission (image upload and compression)
  const handleSubmit = async (event: React.FormEvent) => {
    event.preventDefault();
    if (!selectedFile) {
      setError("Please select a file to upload");
      return;
    }

    setLoading(true);

    const formData = new FormData();
    formData.append("file", selectedFile);

    try {
      const response = await fetch("http://localhost:8000/images/", {
        method: "POST",
        body: formData,
      });

      if (response.ok) {
        alert("Image uploaded and compressed successfully!");
        router.push("/images"); // Redirect to gallery after successful upload and compression
      } else {
        setError("Failed to upload or compress the image");
      }
    } catch (err) {
      console.error("Error uploading/compressing image:", err);
      setError("Error uploading/compressing image");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="container mx-auto p-4">
      <h1 className="text-2xl font-bold text-center mb-6">Upload and Compress Image</h1>

      <form onSubmit={handleSubmit} className="flex flex-col items-center">
        <input
          type="file"
          accept="image/*"
          onChange={handleFileChange}
          className="mb-4"
        />

        {previewUrl && (
          <div className="mb-4">
            <h3 className="font-semibold mb-2">Uncompressed Image Preview:</h3>
            <img src={previewUrl} alt="Preview" className="w-64 h-auto object-cover" />
          </div>
        )}

        {error && <p className="text-red-500">{error}</p>}

        <button
          type="submit"
          className={`bg-blue-500 text-white py-2 px-4 rounded hover:bg-blue-600 ${
            loading ? "opacity-50 cursor-not-allowed" : ""
          }`}
          disabled={loading}
        >
          {loading ? "Uploading and Compressing..." : "Upload and Compress Image"}
        </button>
      </form>
    </div>
  );
};

export default ImageUpload;