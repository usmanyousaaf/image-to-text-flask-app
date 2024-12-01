from flask import Flask, render_template, request, redirect, url_for
import cv2
import pytesseract
import os

# Initialize Flask app
app = Flask(__name__)
UPLOAD_FOLDER = "static/uploads/"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

# Inform pytesseract where Tesseract is installed
pytesseract.pytesseract.tesseract_cmd = "/usr/local/bin/tesseract"

# Ensure upload folder exists
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

# Home route
@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        if "image" not in request.files:
            return redirect(request.url)
        file = request.files["image"]
        if file.filename == "":
            return redirect(request.url)

        # Save the uploaded file
        if file:
            filepath = os.path.join(app.config["UPLOAD_FOLDER"], file.filename)
            file.save(filepath)
            return render_template("index.html", image_url=filepath)

    return render_template("index.html")

# Process image and extract text
@app.route("/process", methods=["POST"])
def process_image():
    if "image_path" in request.form:
        image_path = request.form["image_path"]
        img = cv2.imread(image_path)
        
        # Check if the image was read successfully
        if img is None:
            error_message = "Error: Unable to read the uploaded image. Please upload a valid image."
            return render_template("index.html", error=error_message)

        # Extract text from the image
        extracted_text = pytesseract.image_to_string(img)

        # Pass extracted text to the result template
        return render_template("index.html", image_url=image_path, text=extracted_text)

    # Handle missing form data case
    error_message = "Error: No image path provided for processing. Please upload an image first."
    return render_template("index.html", error=error_message)

# Run Flask app
if __name__ == "__main__":
    app.run(debug=True)
