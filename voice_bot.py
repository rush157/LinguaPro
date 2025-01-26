import pyttsx3
import pytesseract
from PIL import Image
from PyPDF2 import PdfReader

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
        reader = PdfReader(file_path)
        text = ""
        for page in reader.pages:
            text += page.extract_text()
        return text.strip()
    except Exception as e:
        return f"Error reading PDF: {e}"

def scan_image(file_path):
    """Extract text from an image using OCR."""
    try:
        image = Image.open(file_path)
        text = pytesseract.image_to_string(image)
        return text.strip()
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
            pdf_path = input("Enter the path to the PDF file: ")
            pdf_text = read_pdf(pdf_path)
            if pdf_text:
                print("\nExtracted Text:\n", pdf_text)
                speak(pdf_text)
            else:
                print("No text extracted from the PDF.")
        elif choice == "3":
            # Scan and speak text from an image
            image_path = input("Enter the path to the image file: ")
            image_text = scan_image(image_path)
            if image_text:
                print("\nExtracted Text:\n", image_text)
                speak(image_text)
            else:
                print("No text extracted from the image.")
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
