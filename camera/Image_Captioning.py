import cv2
import requests
import base64
import time
from pathlib import Path
import depthai as dai
from transformers import AutoModelForImageCaptioning, AutoTokenizer
import torch
import torchvision.transforms as transforms
from PIL import Image
import torchtext
import torchvision.models as models
from transformers import HubModel, HubTokenizer
import pyttsx3

# Initialize the TTS engine
engine = pyttsx3.init()

# Set properties (optional)
engine.setProperty('rate', 150)  # Speed of speech
engine.setProperty('volume', 0.9)  # Volume level (0.0 to 1.0)

# Load the image captioning model
model_name = "blip-image-captioning-base"
tokenizer = HubTokenizer.from_pretrained(model_name)
model = HubModel.from_pretrained(model_name)

def main():
    # Create pipeline
    pipeline = dai.Pipeline()

    # Define sources and outputs
    camRgb = pipeline.create(dai.node.ColorCamera)
    xoutRgb = pipeline.create(dai.node.XLinkOut)

    xoutRgb.setStreamName("preview")
    camRgb.preview.link(xoutRgb.input)

    # Properties
    camRgb.setPreviewSize(300, 300)
    camRgb.setResolution(dai.ColorCameraProperties.SensorResolution.THE_1080_P)
    camRgb.setInterleaved(False)
    camRgb.setColorOrder(dai.ColorCameraProperties.ColorOrder.BGR)

    # Connect to device and start pipeline
    with dai.Device(pipeline) as device:
        previewQueue = device.getOutputQueue("preview", 4, False)

        print("Press 'y' and Enter to capture an image and get the caption.")
        while True:
            frame = previewQueue.get().getCvFrame()
            cv2.imshow("Camera Preview", frame)

            key = cv2.waitKey(1) & 0xFF
            if key == ord('y'):
                # Capture an image from the camera
                image_data = cv2.imencode(".jpg", frame)[1].tobytes()

                image = Image.open(image_data)
                
                # Perform necessary preprocessing on the image
                transform = transforms.Compose([
                    transforms.ToPILImage(),
                    transforms.Resize((224, 224)),  # ResNet-152 requires 224x224 input
                    transforms.ToTensor(),
                    transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
                ])
                
                # Convert the image to a PyTorch tensor and normalize it
                image_tensor = transform(image).unsqueeze(0)

                with torch.no_grad():
                    outputs = model.generate(input_ids=image_tensor)
                caption_indices = outputs[0].tolist()

                # Decode the caption indices back to text using the tokenizer
                caption_text = tokenizer.decode(caption_indices, skip_special_tokens=True)

                # Print the predicted output
                print("Predicted Caption: ", caption_text)
                # Speak the text
                engine.say(caption_text)

                # Wait for the speech to finish
                engine.runAndWait()

                # Save the image
                timestamp = int(time.time())
                image_filename = f"captured_image_{timestamp}.jpg"
                cv2.imwrite(image_filename, frame)
                print(f"Image saved as: {image_filename}")

            elif key == ord('q'):
                print("Exiting the program.")
                break

if __name__ == "__main__":
    ca()
