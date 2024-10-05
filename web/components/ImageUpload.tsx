'use client'

import React, { useState } from 'react';

const ImageUpload = () => {
  const [selectedFile, setSelectedFile] = useState<File | null>(null);
  const [preview, setPreview] = useState<string | null>(null);
  const [compressedImage, setCompressedImage] = useState<string | null>(null);

  const handleFileChange = (event: React.ChangeEvent<HTMLInputElement>) => {
    const file = event.target.files?.[0];
    if (file) {
      setSelectedFile(file);
      setPreview(URL.createObjectURL(file));
    }
  };

  const handleUpload = async () => {
    if (!selectedFile) return;
    const formData = new FormData();
    formData.append('file', selectedFile);

    const response = await fetch('http://localhost:8000/images/', {
      method: 'POST',
      body: formData,
    });

    const data = await response.json();
    setCompressedImage(`http://localhost:8000/images/${data.id}`);
  };

  return (
    <div>
      <h2 className="text-xl font-bold mb-4 text-center">Upload and Compress Image</h2>
      <input 
        type="file"
        accept="image/*"
        onChange={handleFileChange}
      />
      {preview && <img src={preview} alt="Preview" className="" />}
      <button
        onClick={handleUpload}
      >
        Upload and Compress
      </button>
      {compressedImage && (
        <div>
          <h3></h3>
          <img src={compressedImage} alt="Compressed" className="" />
        </div>
      )}
    </div>
  );
};

export default ImageUpload;