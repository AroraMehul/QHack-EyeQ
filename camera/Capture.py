#!/usr/bin/env python3

import cv2
import depthai as dai
import time
import os

# Create pipeline
pipeline = dai.Pipeline()

# Define sources and outputs
camRgb = pipeline.create(dai.node.ColorCamera)
xoutRgb = pipeline.create(dai.node.XLinkOut)

xoutRgb.setStreamName("preview")

# Properties
camRgb.setPreviewSize(300, 300)
camRgb.setResolution(dai.ColorCameraProperties.SensorResolution.THE_1080_P)
camRgb.setInterleaved(False)
camRgb.setColorOrder(dai.ColorCameraProperties.ColorOrder.BGR)

# Linking
camRgb.preview.link(xoutRgb.input)

# Connect to device and start pipeline
with dai.Device(pipeline) as device:

    preview = device.getOutputQueue("preview", 4, False)

    while True:
        # Get the latest frame from the camera
        imgFrame = preview.get()
        frame = imgFrame.getCvFrame()

        # Display the stream
        cv2.imshow("Camera Stream", frame)

        # Wait for user input
        key = cv2.waitKey(1) & 0xFF
        if key == ord('y'):
            # Capture an image and save it
            timestamp = int(time.time())
            image_path = f"captured_image_{timestamp}.jpg"
            cv2.imwrite(image_path, frame)
            print(f"Image saved as {image_path}")
            cv2.imshow("Captured Image", frame)
            cv2.waitKey(2000)  # Show the captured image for 2 seconds
            cv2.destroyWindow("Captured Image")

        if key == ord('q'):
            break

# Release OpenCV resources
cv2.destroyAllWindows()
