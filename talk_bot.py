import speech_recognition as sr
import pyttsx3
from transformers import pipeline
from huggingface_hub import login

# Log into Hugging Face API (if required)
# You can skip this part if you're using a model that's publicly available
login(token='your api key')

# Initialize the speech recognizer, text-to-speech engine, and Hugging Face model
recognizer = sr.Recognizer()
engine = pyttsx3.init()
model = pipeline('text-generation', model='gpt2')  # You can choose any model available on Hugging Face

# Function to listen to user's speech
def listen():
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)
    try:
        print("Recognizing...")
        user_input = recognizer.recognize_google(audio)
        print(f"You said: {user_input}")
        return user_input
    except sr.UnknownValueError:
        print("Sorry, I couldn't understand that.")
        return ""
    except sr.RequestError:
        print("Sorry, there was an issue with the speech recognition service.")
        return ""

# Function to generate a response using Hugging Face model
def get_response(user_input):
    try:
        response = model(user_input, max_length=150, num_return_sequences=1)
        return response[0]['generated_text']
    except Exception as e:
        print(f"Error: {e}")
        return "Sorry, I couldn't process that."

# Function to speak the response
def speak(response):
    engine.say(response)
    engine.runAndWait()

# Main function for the chatbot
def voice_bot():
    print("Bot: Hello! I'm your voice assistant. How can I help you today?")
    speak("Hello! I'm your voice assistant. How can I help you today?")

    while True:
        user_input = listen()
        if user_input.lower() == "quit":
            print("Bot: Goodbye!")
            speak("Goodbye!")
            break
        response = get_response(user_input)
        print(f"Bot: {response}")
        speak(response)

if __name__ == "__main__":
    voice_bot()
