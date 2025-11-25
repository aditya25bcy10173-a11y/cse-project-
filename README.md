Python Voice Assistant (Simplified Jarvis)
This is a basic, voice-controlled desktop assistant built entirely in Python. It utilizes several popular libraries for handling speech recognition, text-to-speech output, and various web-based functionalities.
 Features
Voice Commands: Responds to voice commands for various tasks.
Time & Date: Tells the current time and greets the user based on the time of day.
Media Playback: Plays music or videos on YouTube using voice commands.
Information Retrieval: Searches Wikipedia and Google for information.
Web Automation: Opens specified websites and sends scheduled WhatsApp messages.
Entertainment: Tells random jokes.
Error Handling: Includes basic error handling for speech recognition and web operations.
 Installation and Setup
1. Prerequisites
You must have Python 3 installed on your system.
2. Required Libraries
Basic imports and extenstions
Command Keyword Example Command Action
time "What is the time" Tells the current time.
play "Jarvis, play Bohemian Rhapsody" Plays the song on YouTube.
tell me about / search "Tell me about space exploration" Searches Wikipedia for a summary.
open website "Open website amazon dot in" Opens the specified website in the default browser.
whatsapp message "Send whatsapp message" Initiates a sequence to send a scheduled message.
joke "Tell me a joke" Tells a random joke.
Youtube "YouTube search cat videos" Opens YouTube with search results.
google search "Google search best python libraries" Opens Google with search results.
exit / goodbye "Jarvis, exit"
3. WhatsApp Functionality
The send_whatsapp_message function relies on a pre-defined dictionary of phone numbers for recipient lookup:
