from django.core.files.uploadedfile import SimpleUploadedFile
from PIL import Image
import io
from rest_framework.test import APITestCase, APIClient
from rest_framework.response import Response


class DetectObjectsUnitTest(APITestCase):
    """
    Unit test for the object detection API endpoint.
    This test sends an image to the API and checks whether the detection results are returned correctly.
    """

    def setUp(self) -> None:
        """
        Set up the test case by initializing the API client.
        """
        self.client = APIClient()

    def test_detect_objects_success(self) -> None:
        """
        Test case for successfully detecting objects in an uploaded image.
        """

        # Create a test image (100x100 pixels, RGB format)
        image = Image.new('RGB', (100, 100))
        img_io = io.BytesIO()
        image.save(img_io, format='JPEG')
        img_io.seek(0)

        # Create a SimpleUploadedFile object for the image
        uploaded_file = SimpleUploadedFile('test_image.jpg', img_io.getvalue(), content_type='image/jpeg')

        # Send a POST request with the image file using APIClient
        response: Response = self.client.post('/detect/', {'image': uploaded_file}, format='multipart')

        # Assert that the response status code is 200 (success)
        self.assertEqual(response.status_code, 200)
