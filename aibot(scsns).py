import pyttsx3
import pytesseract
from PIL import Image
from PyPDF2 import PdfReader
import os

# Initialize TTS engine
tts_engine = pyttsx3.init()
tts_engine.setProperty('rate', 150)  # Adjust speech rate
tts_engine.setProperty('volume', 0.9)  # Set volume (0.0 to 1.0)

# Set Tesseract OCR path (adjust for your system)
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"  # For Windows

# Functions
def speak(text):
    """Convert text to speech."""
    tts_engine.say(text)
    tts_engine.runAndWait()

def read_pdf(file_path):
    """Extract text from a PDF file."""
    try:
        # Normalize the file path to ensure it works across systems
        normalized_path = os.path.normpath(file_path)
        if not os.path.exists(normalized_path):
            return "Error: The specified PDF file does not exist."

        reader = PdfReader(normalized_path)
        text = ""
        for page in reader.pages:
            text += page.extract_text()
        return text.strip() if text.strip() else "Error: No extractable text found in the PDF."
    except Exception as e:
        return f"Error reading PDF: {e}"

def scan_image(file_path):
    """Extract text from an image using OCR."""
    try:
        # Normalize the file path to ensure it works across systems
        normalized_path = os.path.normpath(file_path)
        if not os.path.exists(normalized_path):
            return "Error: The specified image file does not exist."

        image = Image.open(normalized_path)
        text = pytesseract.image_to_string(image)
        return text.strip() if text.strip() else "Error: No extractable text found in the image."
    except Exception as e:
        return f"Error scanning image: {e}"

# Main Program
def main():
    print("Welcome to the AI Voice Bot!")
    speak("Hello! I am your AI voice bot. How can I assist you?")
    
    while True:
        print("\nOptions:")
        print("1. Speak a message")
        print("2. Read a PDF file")
        print("3. Scan an image for text")
        print("4. Exit")
        
        choice = input("Enter your choice (1/2/3/4): ").strip()
        
        if choice == "1":
            # Speak a user-provided message
            user_text = input("Enter the text you want me to speak: ")
            speak(user_text)
        elif choice == "2":
            # Read and speak text from a PDF file
            pdf_path = input("Enter the path to the PDF file: ").strip()
            pdf_path = pdf_path.replace("\\", "/")  # Replace backslashes with forward slashes
            pdf_text = read_pdf(pdf_path)
            print("\nExtracted Text:\n", pdf_text)
            speak(pdf_text)
        elif choice == "3":
            # Scan and speak text from an image
            image_path = input("Enter the path to the image file: ").strip()
            image_path = image_path.replace("\\", "/")  # Replace backslashes with forward slashes
            image_text = scan_image(image_path)
            print("\nExtracted Text:\n", image_text)
            speak(image_text)
        elif choice == "4":
            # Exit the program
            speak("Goodbye! Have a great day!")
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")
            speak("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
