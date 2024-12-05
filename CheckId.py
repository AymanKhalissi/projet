import cv2
import numpy as np

def preprocess_image(image_path):
    """
    Preprocess the image to enhance template matching accuracy.
    - Resize the image to a fixed size.
    - Convert it to grayscale.
    - Apply histogram equalization to normalize brightness and contrast.
    """
    # Load the image
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    
    # Resize the image to a standard size (adjust based on your template dimensions)
    resized = cv2.resize(image, (500, 300))  # Change dimensions as necessary
    
    # Apply histogram equalization for contrast normalization
    equalized = cv2.equalizeHist(resized)
    
    # Apply Gaussian Blur to reduce noise
    blurred = cv2.GaussianBlur(equalized, (5, 5), 0)
    
    return blurred

def is_valid_id_card(input_image_path, template_image_path, threshold=0.8):
    """
    Check if the input image matches the template image using template matching.
    """
    # Preprocess the input image and template image
    input_preprocessed = preprocess_image(input_image_path)
    template_preprocessed = preprocess_image(template_image_path)

    # Resize the template to match the input image size
    template_resized = cv2.resize(template_preprocessed, (input_preprocessed.shape[1], input_preprocessed.shape[0]))

    # Apply template matching
    result = cv2.matchTemplate(input_preprocessed, template_resized, cv2.TM_CCOEFF_NORMED)

    # Get the best match
    _, max_val, _, _ = cv2.minMaxLoc(result)

    print(f"Match Confidence: {max_val}")
    return max_val >= threshold
