import pytesseract
from PIL import Image
import pyautogui
from tkinter import Tk
from tkinter.filedialog import askopenfilename
import time

# Function to upload image and get its path
def upload_image():
    # Create Tkinter window
    Tk().withdraw()  # Hide the Tkinter root window

    # Prompt user to select image file
    image_path = askopenfilename(title="Select an image file",
                                  filetypes=[("Image Files", "*.png; *.jpg; *.jpeg; *.bmp")])

    return image_path

# Function to extract text from image using Tesseract OCR
def extract_text_from_image(image_path, psm=11):
    # Open the image file
    with Image.open(image_path) as img:
        # Use pytesseract to extract text
        extracted_text = pytesseract.image_to_string(img, config=f"--psm {psm}")
    return extracted_text.strip()
    time.sleep(1)

# Function to type out the extracted text character by character
def type_extracted_text_character_by_character(extracted_text):
    # Type out each character
    for char in extracted_text:
        pyautogui.typewrite(char)
        time.sleep(0.5)  # Optional: Add a small delay between each character

# Main function to initiate the process
def main():
    # Upload image
    image_path = upload_image()

    # Check if image_path is not empty (user canceled the selection)
    if image_path:
        # Extract text from the uploaded image with PSM parameter
        extracted_text = extract_text_from_image(image_path, psm=11)

        # Type out the extracted text character by character
        type_extracted_text_character_by_character(extracted_text)
    else:
        print("No image selected. Exiting...")

if __name__ == "__main__":
    main()
