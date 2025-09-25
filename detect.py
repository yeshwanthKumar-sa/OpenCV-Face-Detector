import cv2
import os

# --- CONFIGURATION ---
# The pre-trained model file
cascade_filepath = 'file.xml' 

# IMPORTANT: Change this to the name of the image you want to test.
# This image file must be in the same folder as your script.
# Remember: This model is for HUMAN faces and will not find animals.
image_filepath = 'lion-animal-isolated-photo.jpg' 

# The name of the file that will be saved with the results
output_filename = 'detection_output.jpg'
# ---------------------


# 1. Load the trained cascade classifier from the XML file
if not os.path.exists(cascade_filepath):
    print(f"Error: Cascade file not found at '{cascade_filepath}'")
    exit()

cascade_classifier = cv2.CascadeClassifier(cascade_filepath)
if cascade_classifier.empty():
    print(f"Error: Could not load cascade classifier from '{cascade_filepath}'. The file may be corrupt.")
    exit()

# 2. Load the image
if not os.path.exists(image_filepath):
    print(f"Error: Image file not found at '{image_filepath}'")
    exit()

image = cv2.imread(image_filepath)
if image is None:
    print(f"Error: Could not read the image from '{image_filepath}'. It might be corrupt or an unsupported format.")
    exit()

# 3. Convert the image to grayscale (Haar cascades work on grayscale images)
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# 4. Perform the detection
detected_objects = cascade_classifier.detectMultiScale(
    gray_image,
    scaleFactor=1.1,
    minNeighbors=5,
    minSize=(30, 30)
)

print(f"Found {len(detected_objects)} objects!")

# 5. Draw rectangles around the detected objects on the original color image
for (x, y, w, h) in detected_objects:
    cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)

# 6. Save the final image with detections to a new file
cv2.imwrite(output_filename, image)
print(f"Successfully saved the output image as {output_filename}")

# 7. Display the final image in a window
cv2.imshow('Detections', image)

# Wait until a key is pressed to close the image window
print("Press any key in the image window to exit.")
cv2.waitKey(0)
cv2.destroyAllWindows()