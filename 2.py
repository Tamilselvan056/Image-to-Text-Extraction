import pytesseract
from PIL import Image
import pyautogui
from tkinter import Tk
from tkinter.filedialog import askopenfilename
import time
import random

# Function to upload image and get its path
def upload_image():
    # Create Tkinter window
    Tk().withdraw()  # Hide the Tkinter root window

    # Prompt user to select image file
    image_path = askopenfilename(title="Select an image file",
                                  filetypes=[("Image Files", "*.png; *.jpg; *.jpeg; *.bmp")])

    return image_path

# Function to extract text from image using Tesseract OCR
def extract_text_from_image(image_path):
    # Open the image file
    with Image.open(image_path) as img:
        # Use pytesseract to extract text
        extracted_text = pytesseract.image_to_string(img)
    return extracted_text.strip()

# Function to type out the extracted text slowly like a human
def type_extracted_text_slowly(extracted_text):
    # Define typing speed range (in seconds) to simulate human-like typing
    min_typing_speed = 0.07  # Minimum typing speed (seconds per character)
    max_typing_speed = 1  # Maximum typing speed (seconds per character)
    time.sleep(1.5)
    # Type out the extracted text slowly
    for char in extracted_text:
        # Type the character
        pyautogui.typewrite(char)

        # Randomly adjust typing speed to simulate variation in typing speed
        time.sleep(random.uniform(min_typing_speed, max_typing_speed))

# Main function to initiate the process
def main():
    # Upload image
    image_path = upload_image()

    # Check if image_path is not empty (user canceled the selection)
    if image_path:
        # Extract text from the uploaded image
        extracted_text = extract_text_from_image(image_path)

        # Type out the extracted text slowly
        type_extracted_text_slowly(extracted_text)
    else:
        print("No image selected. Exiting...")

if __name__ == "__main__":
    main()
