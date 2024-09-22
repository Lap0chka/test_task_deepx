import csv
import json
import random
from typing import Any, Dict, List

import requests
import typer
from PIL import Image, ImageDraw

app = typer.Typer()


@app.command()
def detect(source: str = typer.Option(..., "--source", "-s")) -> None:
    """
    Detect objects in the image using a remote detection service.
    Parameters:
        source (str): The file path to the image that needs to be analyzed.
        - An image file 'output.png' with bounding boxes drawn around detected objects.
    """
    url = "http://127.0.0.1:8000/detect/"

    files = {'image': open(source, 'rb')}

    response = requests.post(url, files=files)

    if response.status_code == 200:
        predictions = json.loads(response.json())
        # Save predictions in output.csv
        with open('result/output.csv', 'w', newline='') as csvfile:
            fieldnames = ['xmin', 'ymin', 'xmax', 'ymax', 'confidence', 'class', 'name']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            for pred in predictions:
                writer.writerow({
                    'xmin': pred['xmin'],
                    'ymin': pred['ymin'],
                    'xmax': pred['xmax'],
                    'ymax': pred['ymax'],
                    'confidence': pred['confidence'],
                    'class': pred['class'],
                    'name': pred['name']
                })

        # Display bounding boxes and save in output.png
        img = Image.open(source)
        img_with_boxes = draw_boxes(img, predictions)
        img_with_boxes.save('result/output.png')
        print("Results saved to 'output.csv' and 'output.png'")
    else:
        print("Error:", response.status_code)


def random_color() -> str:
    """Generate a random RGB color in hex format."""
    return f'#{random.randint(0, 0xFFFFFF):06x}'


def draw_boxes(image: Image.Image, predictions: List[Dict[str, Any]]) -> Image.Image:
    """
    Draw bounding boxes on the image based on detection predictions.
    Returns:
        PIL.Image: The image with bounding boxes drawn.
    """
    name = predictions[0]['name']
    color = random_color()
    draw = ImageDraw.Draw(image)
    for pred in predictions:
        bbox = (pred['xmin'], pred['ymin'], pred['xmax'], pred['ymax'])
        label = pred['name']
        score = pred['confidence']
        if name != pred['name']:
            color = random_color()
            name = pred['name']
        draw.rectangle(bbox, outline=color, width=5)
        draw.text((pred['xmin'], pred['ymin'] - 10), f'{label} ({score:.2f})', fill=color)

    return image


if __name__ == "__main__":
    app()
