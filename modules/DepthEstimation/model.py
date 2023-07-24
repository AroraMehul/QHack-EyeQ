from transformers import AutoImageProcessor, DPTForDepthEstimation
import torch
import numpy as np
from PIL import Image
import requests
import matplotlib.pyplot as plt
import time

def estimate_depth(img_path, idx):
    """
    This method is used to create a depth map of an image whose path is taken as an input
    This function is also used for saving these depth maps, which are used to create point-clouds
    """
    image_processor = AutoImageProcessor.from_pretrained("Intel/dpt-large")
    model = DPTForDepthEstimation.from_pretrained("Intel/dpt-large")
    img = Image.open(img_path)
    # prepare image for the model
    inputs = image_processor(images=img, return_tensors="pt")
    with torch.no_grad():
        outputs = model(**inputs)
        predicted_depth = outputs.predicted_depth
    # interpolate to original size
    prediction = torch.nn.functional.interpolate(
        predicted_depth.unsqueeze(1),
        size=img.size[::-1],
        mode="bicubic",
        align_corners=False,
    )
    output = prediction.squeeze().cpu().numpy()
    # setting the lower bounds of the depth
    output[output < 0] = 0
    np.save("./../Simulation/1/depth_" + str(idx) + ".npy", depth)