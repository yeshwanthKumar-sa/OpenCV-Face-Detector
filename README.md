# OpenCV Human Face Detector

A Python script that uses the OpenCV library and a pre-trained Haar Cascade classifier to detect human faces in an image and highlight them with bounding boxes.

---

## Sample Output

Here is an example of the script successfully identifying a human face in a test image. The output with the green bounding box is automatically saved by the script.

![Detection Result](detection_output.jpg)

---

## About The Project

This project is a foundational computer vision application built in Python. It demonstrates an end-to-end pipeline for object detection. The script was also tested with images of animals, correctly identifying that no human faces were present, which confirms the specificity of the machine learning model.

The workflow is as follows:
1.  Loads a pre-trained Haar Cascade model (`haarcascade_frontalface_default.xml`) trained to find human faces.
2.  Reads an input image from the disk.
3.  Performs pre-processing by converting the image to grayscale.
4.  Runs the detection algorithm to find the coordinates of any faces.
5.  Visualizes the results by drawing a bounding box on the original image.
6.  Saves the final processed image to a new file named `detection_output.jpg`.

### Technologies Used
* **Python**
* **OpenCV:** For all image processing and detection tasks.
* **Haar Cascade Classifiers:** The classic machine learning model used for object detection.

---

## Getting Started

To get a local copy up and running, follow these simple steps.

### Prerequisites

Make sure you have Python installed on your system. You can download it [here](https://www.python.org/downloads/).

### Installation & Usage

1.  **Clone the repository:**
    ```sh
    git clone [https://github.com/yeshwanthKumar-sa/Haar_Project.git](https://github.com/yeshwanthKumar-sa/Haar_Project.git)
    ```
2.  **Navigate into the project directory:**
    ```sh
    cd Haar_Project
    ```
3.  **Create and activate a virtual environment:**
    ```sh
    # Create the environment
    python -m venv venv

    # Activate on Windows (PowerShell)
    .\venv\Scripts\Activate.ps1
    ```
4.  **Install the required library:**
    ```sh
    pip install opencv-python
    ```
5.  **Run the script:**
    Before running, place your desired input image in the project folder and update the `image_filepath` variable inside the `detect.py` script.
    ```sh
    python detect.py
    ```
    The script will display the result in a window and save it as `detection_output.jpg`.
