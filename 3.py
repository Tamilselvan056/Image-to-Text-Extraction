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
def extract_text_from_image(image_path):
    # Open the image file
    with Image.open(image_path) as img:
        # Use pytesseract to extract text
        extracted_text = pytesseract.image_to_string(img)
    return extracted_text.strip().split('\n')  # Split text into lines

# Function to type out the extracted text word by word with different wait times
def type_extracted_text_word_by_word(text_lines):
    # Define wait times for each line
    wait_times = [1, 1.5, 2]

    # Iterate through each line
    for i, line in enumerate(text_lines):
        words = line.split()  # Split line into words
        for word in words:
            pyautogui.typewrite(word + ' ')  # Type word with space
            time.sleep(0.1)  # Wait between words
        if i < len(wait_times):  # Check if there is a corresponding wait time
            time.sleep(wait_times[i])  # Wait according to the specified time

# Main function to initiate the process
def main():
    # Upload image
    image_path = upload_image()

    # Check if image_path is not empty (user canceled the selection)
    if image_path:
        # Extract text from the uploaded image
        extracted_text_lines = extract_text_from_image(image_path)

        # Type out the extracted text word by word with different wait times
        type_extracted_text_word_by_word(extracted_text_lines)
    else:
        print("No image selected. Exiting...")

if __name__ == "__main__":
    main()
