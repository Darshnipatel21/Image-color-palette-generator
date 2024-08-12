import os.path

from flask import Flask, render_template, request, redirect, url_for
import numpy as np
from PIL import Image
from scipy.spatial.distance import cdist

app = Flask(__name__)


@app.route('/')
def home():
    return render_template("index.html")


def extract_color(image):
    image_array = np.array(image)
    pixels = image_array.reshape(-1, 3)
    unique_color, count = np.unique(pixels, axis=0, return_counts=True)
    sort_indices = np.argsort(-count)
    sort_color = unique_color[sort_indices]

    top_n = 10
    distinct_colors = [sort_color[0]]

    # Define a delta threshold for visual distinction
    delta_threshold = 70  # You can adjust this value

    # Iterate through the sorted colors to find visually distinct ones
    for color in sort_color[1:]:
        distances = cdist([color], distinct_colors, metric='euclidean')
        if np.all(distances >= delta_threshold):
            distinct_colors.append(color)
        if len(distinct_colors) == top_n:
            break

    hex_code = []
    for i in distinct_colors:
        code = '{:02x}{:02x}{:02x}'.format(i[0],i[1],i[2])
        hex_code.append(f"#{code}")

    return hex_code


@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        image_file = request.files['file']
        filepath = os.path.join("static/images", image_file.filename)
        image = Image.open(image_file)
        image.save(filepath)
        hex_code = extract_color(image)
        return render_template('index.html', image=filepath, hex_code=hex_code)
    return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True)