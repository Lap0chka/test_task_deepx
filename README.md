TODO

1.	Use any pre-trained computer vision (CV) object detector (YOLOv8 is recommended). 
2.	Create an API service that can be queried to obtain CV module predictions (FastAPI Python framework is recommended). 
3.	Deploy inside a Docker container. 
4.	Create a simple Python client, which: 
a.	Takes path to the image as a parameter (e.g. using Typer; Fire; or simple argparse). 
b.	Sends image data to API service inside Docker container. 
c.	Waits for inference results, or if necessary, makes a second query to get processed results. 
d.	Saves output predictions (bounding boxes with categories) to output.csv file.
e.	Saves processed image to output.png. 
Test Case

1.	Download test image. 
2.	Run “python3 client.py --source zidane.jpg”. 
3.	Check if output.csv contains predictions. 
4.	Check if output.png looks like this (if using YOLOv8). 

Deliveries

●	Dockerfile
●	API service code
●	client.py code
●	Recorded video screencast showcasing the test case execution process (Screencast apps: Kazam; OBS Studio)
