import pytesseract
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
from flask import Flask, render_template, request
from PIL import Image
import pytesseract
from summarizer import summarize_text
import os

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    if 'image' not in request.files:
        return "No file part"
    file = request.files['image']
    if file.filename == '':
        return "No selected file"
    if file:
        path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(path)
        text = pytesseract.image_to_string(Image.open(path))
        summary = summarize_text(text)
        return render_template('result.html', original=text, summary=summary)

if __name__ == '__main__':
    app.run(debug=True)
