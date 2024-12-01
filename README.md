# Image-to-Text Flask App

A simple **Flask** application that allows users to upload images and extract text using Optical Character Recognition (**OCR**). This app is perfect for digitizing printed content, scanned documents, business cards, or any image-based text into machine-readable text.

## Features

- **Image Upload**: Users can easily upload images to extract text.
- **OCR Integration**: Utilizes the **Tesseract OCR** engine to perform text extraction.
- **Easy-to-use**: A user-friendly web interface built with **Flask**.
- **Fast and Accurate**: Reliable text extraction from images in real time.

## Tech Stack

- **Flask**: A lightweight Python web framework for building web applications.
- **Tesseract OCR**: An open-source OCR engine for converting images into editable text.
- **HTML/CSS**: Front-end to create a simple and clean user interface for uploading images and displaying results.

## How to Use

### 1. Clone the Repository

Start by cloning this repository to your local machine:

```bash
git clone https://github.com/usmanyousaaf/image-to-text-flask-app.git
cd image-to-text-flask-app
```

## Install the required Python libraries:

```bash
pip install Flask Pillow pytesseract Flask-Uploads werkzeug clipboard
```

## External Software Requirement
- You also need to install Tesseract OCR on your system for text extraction.

## Download Tesseract OCR from Tesseract at UB Mannheim (for Windows).
```bash
Install Tesseract and note the installation path (e.g., C:\Program Files\Tesseract-OCR).
```
## Set the Tesseract executable path in your app.py:
```bash
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
```
##Running the Application
- Start the Flask app:
```bash
python app.py
```

Access the app: Open your browser and go to http://127.0.0.1:5000/ to use the image-to-text converter.

## Features
- Upload an image using the file upload button or drag-and-drop the image onto the upload area.
- The extracted text from the image will be displayed below the upload button.
- You can copy the extracted text to the clipboard using the "Copy to Clipboard" button.
- The app allows users to upload another image without refreshing the page.

## Project Structure
```bash
image-to-text/
│
├── app.py               # Main Flask application file
├── requirements.txt     # List of required Python libraries
├── static/
│   └── uploads/         # Folder to store uploaded images
├── templates/
│   ├── index.html       # Homepage template
│   └── result.html      # Result page template
└── README.md            # Project documentation

```
<br>

## Look Like 👀 
<img width="846" alt="Screenshot 2024-12-01 at 8 55 15 PM" src="https://github.com/user-attachments/assets/974dca88-9631-45a7-8b19-1b4da349150f">
<br>
<img width="712" alt="Screenshot 2024-12-01 at 8 55 44 PM" src="https://github.com/user-attachments/assets/5c35bd0f-079f-4f7f-b215-7707c3385dbc">


## Contributing
- Contributions are welcome! If you find any bugs or have suggestions for improvements, feel free to fork the repository and submit a pull request.

## Fork the repository.
- Create a new branch for your changes.
- Submit a pull request with a detailed explanation of your changes.

## License
- This project is licensed under the MIT License - see the LICENSE file for details.
