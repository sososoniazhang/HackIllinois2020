import cv2
import numpy as np
import torch

def get_frames(filepath, max_frames=1e7, verbose=1000):
    

    vidcap = cv2.VideoCapture(filepath)
    success,image = vidcap.read()
    count = 0

    data = []

    while success and count < max_frames:
        # save frame as JPEG file      
        success, image = vidcap.read()
        data.append(image / 255)
        count += 1
        if verbose != -1 and count%verbose==0:
            print("Loading video %s: %.2f%%" % (filepath, count * 100 / max_frames))


    data = np.array(data)
    data = torch.as_tensor(data)
    return data.permute(0, 3, 1, 2)
