#read an image and display using api

import cv2
import numpy as np
from matplotlib import pyplot as plt

# img = cv2.imread('C:\Users\DELL\Desktop\sem marksheet\IMG-20230206-WA0005.jpg',0)

from fastapi import FastAPI
from fastapi.responses import StreamingResponse
import cv2
import numpy as np
from io import BytesIO

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Welcome to the image display API"}

@app.get("/display-image")
def display_image():
    # Read the image
    img = cv2.imread(r'C:\Users\DELL\Desktop\sem marksheet\IMG-20230206-WA0005.jpg', 0)
    
    # Convert the image to a format that can be streamed
    _, img_encoded = cv2.imencode('.jpg', img)
    img_bytes = BytesIO(img_encoded.tobytes())

    return StreamingResponse(img_bytes, media_type="image/jpg")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)