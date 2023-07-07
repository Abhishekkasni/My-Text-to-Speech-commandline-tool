from gtts import gTTS

import os

def text_to_speech():
    text = input("Enter text to change in voice file -> ")
    language = 'in'
    myobj = gTTS(text=text, lang=language, slow=False)
    myobj.save("speech.mp3")
    os.system("speech.mp3")
    
def main():
    text_to_speech()
main()