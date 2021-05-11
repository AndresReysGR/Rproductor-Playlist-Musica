import speech_recognition as sr
import time
import webbrowser
import playsound
import os
import random
from gtts import gTTS
from time import ctime

r = sr.Recognizer()

def record_audio(ask = False):
    with sr.Microphone() as source: 
        if ask: 
            alexa_speak(ask)         
        audio = r.listen(source)
        voice_data = ''
        try:
            voice_data = r.recognize_google(audio)
        
        except sr.UnknownValueError:
            alexa_speak('Lo siento, no te entendi')
        except sr.UnknownValueError:
            alexa_speak('Lo siento, error de conexion')
        return voice_data

def alexa_speak(audio_string):
    tts = gTTS(text=audio_string, lang='en')
    r = random.randint(1, 1000000)
    audio_file = 'audio-' + str(r) + '.mp3'
    tts.save(audio_file)
    
    playsound.playsound(audio_file)
    print(audio_string)
    os.remove(audio_file)

def respond(voice_data):
    if 'como te llamas' in voice_data:
        alexa_speak('Mi nombre es Chito')
    if 'musica' in voice_data:
        musica = record_audio("¿Que tipo de playlist musical buscas?")
        url = 'https://www.youtube.com/results?search_query=Plylist+Musica' + musica
        alexa_speak('Aqui una playlist de : ' + musica)
        webbrowser.get().open(url)     
    if 'anime' in voice_data:
        anime = record_audio("¿Que anime buscas?")
        url = 'https://www3.animeflv.net/anime/' + anime
        alexa_speak('Aqui esta el anime : ' + anime)
        webbrowser.get().open(url)   
    if 'terminar' in voice_data:
        exit()
    
time.sleep(1)
alexa_speak('¿Como te puedo ayudar?')
while 1:
    voice_data = record_audio()
    respond(voice_data)
