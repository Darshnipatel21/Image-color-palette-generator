# Image Color Palette Generator

This project is a web application that allows users to upload an image and extract its 
dominant colors. The extracted colors are then displayed alongside the uploaded image.

## Features

- Upload an image in JPEG or PNG format.
- Extract the top 10 dominant colors from the image.
- Display the extracted colors in a grid format with their hex codes.

## Technologies Used

- **Flask**: Web framework for Python.
- **Bootstrap**: Front-end framework for styling.
- **PIL (Pillow)**: Python Imaging Library for image processing.
- **NumPy**: Library for numerical operations.
- **SciPy**: Library for scientific and technical computing.

## Installation

1. **Clone the Repository**

   ```bash
   git clone https://github.com/your-username/image-color-palette-generator.git
   cd image-color-palette-generator
   ```
2. **Create a Virtual Environment**
   
   ```bash
   python -m venv venv

3. **Activate the Virtual Environment**
   On Windows:
    ```bash
    venv\Scripts\activate
    ```
   On macOS/Linux:
    ```bash
    source venv/bin/activate
    ```
    
4. **Install the Required Packages**

  ```bash
  pip install -r requirements.txt
  Run the Application
  ```
  ```bash
  python app.py
  ```
The application will start running on http://127.0.0.1:5000/.

**Usage**
  1. Open your web browser and go to http://127.0.0.1:5000/.
  2. Upload an image file using the provided form.
  3. Click on "Extract Colors" to see the dominant colors extracted from the image.
  
**File Structure**
  **app.py:** The main Flask application script.
  **templates/index.html:** The HTML template for the web application.
  **static/images/:** Directory where uploaded images are stored.
  **requirements.txt:** List of Python packages required for the project.
  
**Dependencies**
  - Flask
  - NumPy
  - Pillow
  - SciPy
  - Bootstrap (via CDN)
    
**Contributing**
  If you would like to contribute to this project, please fork the repository and submit a pull request. 
  Make sure to follow the coding standards and include tests for any new features.

**Contact**
  For any questions or feedback, please contact darshni211196@gmail.com
  
