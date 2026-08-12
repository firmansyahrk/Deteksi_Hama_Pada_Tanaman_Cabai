# utils/detector.py

import torch

model = torch.hub.load(
    "yolov5",
    "custom",
    path="best.pt",
    source="local"
)

def detect(image):

    results = model(image)

    prediction = results.pandas().xyxy[0]

    return results, prediction