import webbrowser
import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import pywhatkit
import pyjokes
import pyaudio

listener = sr.Recognizer()
engine = pyttsx3.init()
engine.setProperty('rate', 200)


def talk(text):
    """Speak the given text aloud."""
    engine.say(text)
    engine.runAndWait()


def wish_me():
    """Greet the user based on the time of day."""
    hour = datetime.datetime.now().hour
    if hour < 12:
        talk("Good morning, sir! Let's start the day with full energy.")
    elif hour < 18:
        talk("Good afternoon, sir! Hope your day is going well.")
    else:
        talk("Good evening, sir! You might want to take some rest after a long day.")


def take_command():
    """Listen for a voice command and return the text."""
    try:
        with sr.Microphone() as source:
            print("Listening...")
            listener.adjust_for_ambient_noise(source)
            audio = listener.listen(source)
            command = listener.recognize_google(audio).lower()
            print(f"You said: {command}\n")
            return command
    except sr.UnknownValueError:
        print("Could not understand audio.")
    except sr.RequestError:
        print("Could not connect to Google API.")
    return None


def open_website(command):
    """Open a website based on user command."""
    try:
        talk("Opening website, sir.")
        site = command.replace("open website", "").strip()
        webbrowser.open(f"https://www.{site}.com")
    except Exception as e:
        talk("Sorry, there was an error opening the website.")
        print(f"Error: {e}")


def send_whatsapp_message():
    """Send a WhatsApp message using pywhatkit."""
    talk("Tell me the recipient's name.")
    recipient = take_command()

    if recipient:
        talk("Tell me the message.")
        msg = take_command()

        talk("Tell me the hour to send the message.")
        hour = int(take_command())

        talk("Tell me the minute.")
        minute = int(take_command())

        phone_numbers = {
            "ankur": "+918709883914",
            "someone": "+91XXXXXXXXXX"  # Replace with a valid number
        }

        if recipient in phone_numbers:
            pywhatkit.sendwhatmsg(phone_numbers[recipient], msg, hour, minute)
            talk("Message sent successfully.")
        else:
            talk("Recipient not found.")
    else:
        talk("Could not recognize recipient's name.")


def run_jarvis():
    """Main function to continuously listen and execute commands."""
    wish_me()

    while True:
        command = take_command()
        if not command:
            continue

        if 'time' in command:
            time = datetime.datetime.now().strftime("%I:%M %p")
            talk(f"The current time is {time}.")




        elif 'play' in command:
            song = command.replace('play', '').strip()
            talk(f'Playing {song}.')
            pywhatkit.playonyt(song)

        elif 'tell me about' in command or 'search' in command:
            query = command.replace("tell me about", "").replace("search", "").strip()
            try:
                results = wikipedia.summary(query, sentences=2)
                talk(f"According to Wikipedia, {results}")
            except wikipedia.exceptions.DisambiguationError:
                talk("There are multiple results. Please be more specific.")
            except wikipedia.exceptions.PageError:
                talk("No information found on Wikipedia.")

        elif 'open website' in command:
            open_website(command)

        elif 'whatsapp message' in command:
            send_whatsapp_message()

        elif 'joke' in command:
            joke = pyjokes.get_joke()
            talk(joke)

        elif 'youtube search' in command:
            search_query = command.replace('youtube search', '').strip()
            webbrowser.open(f"https://www.youtube.com/results?search_query={search_query}")
            talk("Here are your YouTube search results.")

       



        elif 'google search' in command:
            search_query = command.replace('google search', '').strip()
            pywhatkit.search(search_query)
            talk("Here are your Google search results.")

        elif 'exit' in command or 'goodbye' in command:
            talk("Goodbye, have a nice day!")
            break

        else:
            talk("Sorry, I didn't understand. Can you repeat that?")


run_jarvis()
