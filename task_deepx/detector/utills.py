import ssl
import torch
from typing import Optional, Any


def load_model() -> Optional[Any]:
    """
    Load the YOLOv5 model from the Ultralytics repository.

    Returns:
        Optional[Any]: The loaded model if successful, None otherwise.
    """
    try:
        # Create an unverified SSL context to avoid certificate verification errors
        ssl._create_default_https_context = ssl._create_unverified_context
        model = torch.hub.load('ultralytics/yolov5', 'yolov5s', pretrained=True)
        print("Model loaded successfully!")
        return model
    except Exception as e:
        print(f"Error loading model: {e}")
        return None
