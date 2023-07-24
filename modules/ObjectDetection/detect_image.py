import torch
import torchvision
import argparse
import cv2
import detect_utils
from PIL import Image
import matplotlib.pyplot as plt
import numpy as np
from detecting_depth import estimate_depth

class ssdMobNetv3():
    def __init__(self, device):
        self.device = device
        
    def get_model(self):
        # load the model 
        model = torchvision.models.detection.ssdlite320_mobilenet_v3_large(pretrained=True)
        # load the model onto the computation device
        model = model.to(self.device)
        model = model.eval()
        return model

# define the computation device
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
preTrainedModel = ssdMobNetv3(device)
model = preTrainedModel.get_model()

# read the image
image = Image.open('./../Test Images/IMG-8064.jpg')
print(np.asarray(image).shape)
# detect outputs
boxes, classes, labels = detect_utils.predict(image, model, device, 0.5)

# draw bounding boxes
image_ = detect_utils.draw_boxes(boxes, classes, labels, image)

new_image_ = np.zeros_like(image_)
new_image_[:, :, 0] = image_[:, :, 2]
new_image_[:, :, 2] = image_[:, :, 0]
new_image_[:, :, 1] = image_[:, :, 1]
plt.imshow(new_image_)

def findObject(image, obj):
    result = []
    boxes, classes, labels = detect_utils.predict(image, model, device, 0.5)
    # draw bounding boxes
    image_ = detect_utils.draw_boxes(boxes, classes, labels, image)
    depth_output = estimate_depth(image)
    print(depth_output.shape)
    if(obj in classes):
        indices = np.where(np.array(classes) == obj)[0]
        count = len(indices)
        for i in range(count):
            x_obj_centr = int((boxes[indices[i]][0] + boxes[indices[i]][2])/2)
            y_obj_centr = int((boxes[indices[i]][1] + boxes[indices[i]][3])/2)
            print(x_obj_centr, y_obj_centr)
            depth_obj = depth_output[x_obj_centr][y_obj_centr]
            if(x_obj_centr < np.asarray(image).shape[1]/5.0):
                direction = "left"
            elif(x_obj_centr < np.asarray(image).shape[1]/2.0):
                direction = "slight left"
            elif(x_obj_centr < (4*np.asarray(image).shape[1])/5.0):
                direction = "slight right"
            else:
                direction = "right"
            result.append((depth_obj, direction))
    return result, depth_output

res, depth = findObject(image, 'chair')