from flask import Flask, render_template, request, send_file
from PIL import Image, ImageDraw, ImageFont
import os

app = Flask(__name__)

# Path to the certificate template and font
TEMPLATE_PATH = r"C:\Users\aarah\OneDrive\Documents\Python programming files\Certificate Genration\Demo Image\Certificate.jpg"
FONT_PATH = r"C:\Users\aarah\OneDrive\Documents\Python programming files\Certificate Genration\Fonts\nasa21\Nasa21.ttf"
OUTPUT_DIR = r"C:\Users\aarah\OneDrive\Documents\Python programming files\Certificate Genration"

# Ensure the output directory exists
if not os.path.exists(OUTPUT_DIR):
    os.makedirs(OUTPUT_DIR)

@app.route('/')
def home():
    # Render the HTML form
    return render_template('form.html')

@app.route('/generate-certificate', methods=['POST'])
def generate_certificate():
    # Get data from the form
    name = request.form['name']

    # Load the certificate template
    certificate = Image.open(TEMPLATE_PATH)
    draw = ImageDraw.Draw(certificate)

    # Define font and size
    font_size = 90
    font = ImageFont.truetype(FONT_PATH, font_size)

    # Define text coordinates (adjust as needed)
    text_position = (175, 627)  # Adjust to match the text area of your certificate

    # Add the user's name to the certificate
    draw.text(text_position, name, fill="black", font=font)

    # Save the certificate
    output_path = os.path.join(OUTPUT_DIR, f"{name}_Certificate.jpg")
    certificate.save(output_path)

    # Send the certificate as a downloadable file
    return send_file(output_path, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
