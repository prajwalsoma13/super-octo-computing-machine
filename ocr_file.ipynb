import imutils
import requests
import io
import json
import cv2
import re

def ocr_file(filename):
    image = cv2.imread(filename,0)
    ratio = image.shape[0] / 500.0
    orig = image.copy()
    img = imutils.resize(image, height = 800)

    url_api = "https://api.ocr.space/parse/image"

    _, compressedimage = cv2.imencode(".jpeg", img, [1, 90])
    file_bytes = io.BytesIO(compressedimage)

    result = requests.post(url_api,
                    files = {"img.jpeg": file_bytes},
                    data = {"apikey": "cf6fb2f8d584567",
                            "language": "eng"})

    result = result.content.decode()
    result = json.loads(result)

    parsed_results = result.get("ParsedResults")[0]
    text_detected = parsed_results.get("ParsedText")
    
    pattern = re.compile(r'[Date:]*([0-9]{0,2}[\/-]([0-9]{0,2}|[a-z]{3})[\/-][0-9]{0,4})')
    matches = pattern.finditer(text_detected)
    
    for x in matches:
        return x

print(ocr_file(".jpeg"))
