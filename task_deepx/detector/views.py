from django.http import JsonResponse
from rest_framework.decorators import api_view
from PIL import Image
import io
from .utills import load_model


@api_view(['POST'])
def detect_objects(request) -> JsonResponse:
    """
    Detect objects in an uploaded image using a pre-loaded YOLOv5 model.
    Returns:
        JsonResponse: A response containing the detection results or an error message.
    """
    model = load_model()
    if model is None:
        return JsonResponse({'error': 'Model not loaded'}, status=500)

    try:
        # Retrieve the uploaded image file
        image_file = request.FILES['image']
        img = Image.open(io.BytesIO(image_file.read()))

        # Perform object detection
        results = model(img)
        predictions = results.pandas().xyxy[0].to_json(orient="records")

        return JsonResponse(predictions, safe=False)

    except KeyError:
        return JsonResponse({'error': 'No image file provided'}, status=400)
    except Exception as e:
        print(f"Error processing image: {e}")
        return JsonResponse({'error': str(e)}, status=500)
