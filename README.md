# OpenCV Face Detector Project

A simple Python script that uses the OpenCV library and a pre-trained Haar Cascade classifier to detect faces in an image and save the result.

---

## Sample Output

Here is an example of the face detector successfully identifying a face in an image:

![Detection Result](detection_output.jpg)

---

## About The Project

This project is a foundational computer vision application built in Python. It demonstrates an end-to-end pipeline for object detection:

1.  Loading a pre-trained machine learning model (Haar Cascade).
2.  Reading an input image from the disk.
3.  Performing pre-processing by converting the image to grayscale.
4.  Running the detection algorithm to find face coordinates.
5.  Visualizing the results by drawing a bounding box on the original image.
6.  Saving the final processed image to a new file.

### Technologies Used
* [Python](https://www.python.org/)
* [OpenCV](https://opencv.org/)
* [Haar Cascade Classifiers](https://en.wikipedia.org/wiki/Viola%E2%80%93Jones_object_detection_framework)

---

## Getting Started

To get a local copy up and running, follow these simple steps.

### Prerequisites

Make sure you have Python installed on your system. You can download it [here](https://www.python.org/downloads/).

### Installation & Usage

1.  **Clone the repository:**
    ```sh
    git clone [https://github.com/yeshwanthKumar-sa/OpenCV-Face-Detector.git](https://github.com/yeshwanthKumar-sa/OpenCV-Face-Detector.git)
    ```
2.  **Navigate into the project directory:**
    ```sh
    cd OpenCV-Face-Detector
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
    Before running, make sure your desired input image is in the project folder and its path is correctly specified inside the `detect.py` script.
    ```sh
    python detect.py
    ```
    The script will display the result in a window and save it as `detection_output.jpg`.
