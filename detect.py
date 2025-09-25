import cv2
import os

# --- CONFIGURATION ---
# Path to your Haar Cascade XML file (it's in the same folder)
cascade_filepath = 'file.xml' 

# Path to the image you want to test (also in the same folder)
image_filepath = r'C:\Users\sunku\Haar_Project\WhatsApp Image 2025-05-03 at 11.58.04_828f7781.jpg'
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
    print(f"Error: Could not read the image. It might be corrupt or in an unsupported format.")
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

# 6. Save and Display the final image with detections
# ================== NEW PART STARTS HERE ==================

# Save the image with the drawn rectangle to a new file
cv2.imwrite("detection_output.jpg", image)
print("Successfully saved the output image as detection_output.jpg")

# =================== NEW PART ENDS HERE ===================

# Display the final image in a window
cv2.imshow('Detections', image)

# Wait until a key is pressed to close the image window
print("Press any key in the image window to exit.")
cv2.waitKey(0)
cv2.destroyAllWindows()