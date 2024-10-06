# Image Management System

This is a full-stack application that provides a RESTful API service for managing images, allowing users to upload, compress, view, and delete images. The back-end is built with FastAPI, and the front-end is developed using Next.js with the app router. The images are stored locally on the file system, and the metadata is stored in a JSON file.
Features

    Upload images and compress them via the FastAPI back end.
    View a gallery of uploaded images.
    Preview uncompressed images before uploading.
    Delete images from the gallery, which removes them from both the JSON database and the local directory.
    Responsive design using Tailwind CSS.

# Tech Stack

    Back-End (api): FastAPI, Python, PIL for image processing
    Front-End (web): Next.js with TypeScript and Tailwind CSS
    Storage: Images stored locally, metadata stored in a JSON file (db.json)
    Docker: Containerized the application for easy deployment

### Project Structure

bash

.
├── api/
│   ├── app/
│   │   ├── main.py              # FastAPI application routes
│   │   ├── crud.py              # CRUD operations for images
│   │   ├── __init__.py          # Package initialization
│   │   ├── utils.py             # Utility functions
│   │   ├── data/
│   │   │   └── images.json      # JSON file for storing image metadata
│   │   ├── images/
│   │   │   └── .jpg/.jpeg       # original and compressed images storage
│   └── Dockerfile               # Dockerfile for FastAPI
│
├── web/
│   ├── app/
│   │   ├── upload/page.tsx      # Next.js upload image page
│   │   ├── images/page.tsx      # Next.js image gallery page
│   │   ├── components/
│   │   │   └── ImageUpload.tsx  # Image upload component
│   ├── Dockerfile               # Dockerfile for Next.js
│   └── tailwind.config.js       # Tailwind CSS configuration
│
├── README.md                    # Project documentation
└── docker-compose.yml           # Docker Compose for orchestrating services

Requirements

    Docker
    Python 3.10 or higher
    Node.js 18 or higher

Installation
1. Clone the repository

### bash

git clone https://github.com/RumbleInCybertron/picky.git
cd picky

### end bash

2. Set up the back end (FastAPI)
Install dependencies

If you are running it locally, create a virtual environment and install the required dependencies:

### bash

cd backend
python -m venv env
source env/bin/activate (MacOS)
.\env\Scripts\Activate.ps1 (Windows)
pip install -r requirements.txt

### end bash

Create necessary directories (Only if not successfully created by API) *This has been tested to work*

Make sure the images/ directory exists for storing images:

bash

mkdir -p api/app/images

If the data/images.json file does not exist, it will be created when the app starts.
Run the back end

### bash

uvicorn app.main:app --reload

### end bash

By default, the API will be available at: http://localhost:8000
3. Set up the front end (Next.js)
Install dependencies

### bash

cd web
npm install

### end bash

Run the front end (web)

### bash

npm run dev

### end bash

The front end will be available at: http://localhost:3000
API Endpoints (Back End)
1. Upload and Compress Image

    POST /images/
    Accepts a file upload and compresses the image.
    The compressed image is saved to the uploads/ directory.

Request Example:

POST /images/

Form Data:

    file: Image file

2. Get All Images

    GET /images/
    Returns metadata for all uploaded images.

Request Example:

GET /images/

3. Get Image by ID

    GET /images/{image_id}
    Returns the actual image by its unique ID.

Request Example:

GET /images/{image_id}

4. Delete Image by ID

    DELETE /images/{image_id}
    Deletes the image from both the JSON file and the local directory.

Request Example:

DELETE /images/{image_id}

Frontend Pages (Next.js)
1. Upload Image Page

    Route: /
    This page allows users to upload an image, preview it before submission, and compress it by sending it to the FastAPI back end.

2. Image Gallery Page

    Route: /images
    This page lists all uploaded images and provides options to delete images.

Docker Setup
Build and Run with Docker

You can run both the FastAPI back end and the Next.js front end in Docker containers using Docker Compose.
1. Build and run the containers

### bash

docker-compose up --build

### end bash

This will start:

    FastAPI at http://localhost:8000
    Next.js at http://localhost:3000

2. Stopping the containers

### bash

docker-compose down

### end bash

Dockerfile for FastAPI (backend/Dockerfile)

dockerfile

# Backend Dockerfile

FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]

Dockerfile for Next.js (frontend/Dockerfile)

dockerfile

# Frontend Dockerfile

FROM node:18-alpine

WORKDIR /app

COPY package.json ./

RUN npm install

COPY . .

EXPOSE 3000

CMD ["npm", "run", "dev"]

Docker Compose (docker-compose.yml)

### yaml

version: "3.9"

services:
  api:
    build: ./api
    ports:
      - "8000:8000"
    volumes:
      - ./api/images:/app/images
      - ./api/data:/app/data
    environment:
      - UPLOAD_DIR=/app/images

  web:
    build: ./web
    ports:
      - "3000:3000"
    depends_on:
      - api

### end yaml

How to Use

    Upload Images: Navigate to http://localhost:3000/, select an image, preview it, and upload it. The image will be sent to the FastAPI back end and compressed.

    View Gallery: Visit http://localhost:3000/images to see all uploaded images. You can view or delete any image from this page.

    Delete Images: Click the "Delete" button next to any image in the gallery to remove it both from the JSON database and the local file system.

License

This project is open-source and licensed under the MIT License.