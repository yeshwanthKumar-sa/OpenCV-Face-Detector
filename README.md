

# OpenCV Haar Cascade Detector: A Demonstration

This project demonstrates a fundamental concept in machine learning and computer vision: **a model is highly specific to the data it was trained on.**

To show this, the script intentionally uses a pre-trained Haar Cascade model that was trained to detect **human faces** and runs it on an image of a **lion**.

## The Main Demonstration: Why the Lion Was Not Detected

The core of this project is to show what happens when a model is given data it doesn't recognize. The script processes an input image of a lion and produces an output image with the detection results.
## Sample Output

Here is an example of the script successfully identifying a human face in a test image. The output with the green bounding box is automatically saved by the script.

![Detection Result](detection_output.jpg)



```
Found 0 objects!
```
 The model did not fail; it worked perfectly. It correctly determined that there were no human faces in the image, proving that it is specifically looking for the patterns and features of humans it learned during its training.

## How the Code Works

The `detect.py` script performs the following steps:

1.  **Load Model**: Loads the `file.xml` Haar Cascade model.
2.  **Load Image**: Reads the input image (`lion-animal-isolated-photo.jpg`).
3.  **Grayscale Conversion**: Converts the image to grayscale, as the Haar algorithm analyzes intensities, not colors.
4.  **Detect Objects**: The `detectMultiScale` function scans the image to find features matching the pre-trained model.
5.  **Draw & Save**: Draws rectangles for any found objects (in this case, none) and saves the result as `detection_output.jpg`.

## Project Files

  * **`detect.py`**: The main Python script that runs the detection.
  * **`file.xml`**: The pre-trained Haar Cascade model for **frontal human faces**.
  * **`lion-animal-isolated-photo.jpg`**: The sample input image of a lion.
  * **`detection_output.jpg`**: The resulting image, showing no detections.

## Prerequisites

  * Python 3.x
  * OpenCV library for Python (`opencv-python`)

## Setup and Installation

It is highly recommended to use a virtual environment.

1.  **Open a Terminal** in the project folder.

2.  **Create a virtual environment:**

    ```bash
    python -m venv venv
    ```

3.  **Activate the virtual environment:**

    ```bash
    # On Windows
    venv\Scripts\activate

    # On macOS/Linux
    source venv/bin/activate
    ```

    Your terminal prompt should now start with `(venv)`.

4.  **Install OpenCV:**

    ```bash
    pip install opencv-python
    ```

## How to Run

With your virtual environment active, run the script from the terminal:

```bash
python detect.py
```

A window will display the `detection_output.jpg` image. Press any key to close it. The script will also save this file to your project directory.

To test with a different image (e.g., a photo of a person), change this line in `detect.py`:

```python
image_filepath = 'your_human_face_image.jpg' 
```
