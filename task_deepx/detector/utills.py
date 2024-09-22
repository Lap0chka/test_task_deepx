import os
import ssl
from typing import Any, Optional

import torch


def load_model(model_path) -> Optional[Any]:
    """
    Load the YOLOv5 model from the Ultralytics repository.

    Returns:
        Optional[Any]: The loaded model if successful, None otherwise.
    """
    try:
        # Check if the model is already downloaded
        if os.path.exists(model_path):
            model = torch.load(model_path)
            print("Model loaded successfully from local file!")
            return model

        # Create an unverified SSL context to avoid certificate verification errors
        ssl._create_default_https_context = ssl._create_unverified_context
        # Load the model from the Ultralytics repository
        model = torch.hub.load('ultralytics/yolov5', 'yolov5s', pretrained=True)
        torch.save(model, model_path)

        print("Model downloaded and saved successfully!")
        return model

    except Exception as e:
        print(f"Error loading model: {e}")
        return None
