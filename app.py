import os
from flask import Flask, request, jsonify
from ocr import ocr_file

app = Flask(__name__)

@app.route("/extract_date", methods=["POST"])
def date_extractor():
	data = request.get_json()
	image_content = data["base_64_image_content"]
	date = ocr_file(image_content)
	print(date)

	if date:
		return jsonify({
			"DATE": "{base_64_image_content"}
			"METHOD" : "POST"
		})

	else:
		return jsonify({
			"DATE": "Null"
		})

@app.route('/')
def index():
	return"<h1>WELCOME<h1>"


if __name__ == "__main__":
	app.run(threaded=True, port=5000)

