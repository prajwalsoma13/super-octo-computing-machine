import requests
import json
import logging
import base64

def ocr_file(data):
    api_url = "https://api.ocr.space/parse/image"
    result = requests.post(api_url,
                    data = {"apikey": "cf6fb2f8d68759", 
                            "base64Image": "data:image/png;base64,"+data,
                            "language": "eng"})

    logging.warning(result)
    result = result.content.decode()
    logging.warning(result)
    result = json.loads(result)

    parsed_results = result.get("ParsedResults")[0]
    text_detected = parsed_results.get("ParsedText")

    pattern = re.compile(r'[Date:]*([0-9]{0,2}[\/-]([0-9]{0,2}|[a-z]{3})[\/-][0-9]{0,4})')
    matches = pattern.finditer(text_detected)

    for x in matches:
        return x

