import cv2
import requests
import base64
import time
from pathlib import Path
import depthai as dai
# from transformers import AutoModelForImageCaptioning, AutoTokenizer
import torch
import torchvision
from PIL import Image

model = torchvision.models.detection.captioning_showtell(pretrained=True)

# def get_image_caption(image_data):
#     api_url = "https://captionbot.azurewebsites.net/api/messages"
#     headers = {"Content-Type": "application/octet-stream"}

#     response = requests.post(api_url, data=image_data, headers=headers)
#     if response.status_code == 200:
#         caption = response.json()["created"]
#         return caption
#     else:
#         print("Error: Unable to get image caption.")
#         return None

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

                # Convert the image to PyTorch tensor and normalize it
                transform = torchvision.transforms.Compose([
                    torchvision.transforms.ToTensor(),
                    torchvision.transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
                ])
                image_tensor = transform(image).unsqueeze(0)

                # Set the model to evaluation mode
                model.eval()

                # Generate captions for the image
                with torch.no_grad():
                    captions = model.caption_image(image_tensor)

                # Print the generated captions
                for caption in captions:
                    print(caption)
                # # Print the caption to the terminal
                # print("Predicted Caption: ", caption)

                # Save the image
                timestamp = int(time.time())
                image_filename = f"captured_image_{timestamp}.jpg"
                cv2.imwrite(image_filename, frame)
                print(f"Image saved as: {image_filename}")

            elif key == ord('q'):
                print("Exiting the program.")
                break

if __name__ == "__main__":
    main()
