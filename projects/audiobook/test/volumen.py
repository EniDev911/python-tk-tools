# coding:utf-8
 
import pyttsx3
 
 # Inicializar
engine = pyttsx3.init()
 
voices = engine.getProperty('voices')
 # Control de velocidad de voz
rate = engine.getProperty('rate')
print(rate)
 
 # Control de volumen
volume = engine.getProperty('volume')
print(volume)

engine.setProperty('volume', volume-0.25)
 
#engine.setProperty('rate', rate-30)
engine.say('hello world')
engine.say ('Hola, mundo')
 # Leer una vez
engine.runAndWait()
#engine.say('Síntesis de voz')
#engine.say('Puedo hablar chino, Kaisen, Kaisen')
#engine.runAndWait()
 
#engine.say('The quick brown fox jumped over the lazy dog.')
#engine.runAndWait()
 
 # Cambiar idioma - zh_HK
#engine.setProperty('voice', "com.apple.speech.synthesis.voice.sin-ji")
#engine.setProperty('voice', "VoiceGenderMale")
#engine.say ('De la declaración del método, el primer parámetro especifica el nombre del controlador de voz, que está estrechamente relacionado con el sistema operativo en la parte inferior')
 
 # Cambiar idioma - zh_CN
#engine.setProperty('voice', "com.apple.speech.synthesis.voice.ting-ting.premium")
#engine.say ('De la declaración del método, el primer parámetro especifica el nombre del controlador de voz, que está estrechamente relacionado con el sistema operativo en la parte inferior')
 
 # Cambiar idioma - zh_TW
#engine.setProperty('voice', "com.apple.speech.synthesis.voice.mei-jia")
#engine.say ('De la declaración del método, el primer parámetro especifica el nombre del controlador de voz, que está estrechamente relacionado con el sistema operativo en la parte inferior')
#engine.runAndWait()
 
#for voice in voices:
#    print(voice)
#    engine.setProperty("voice",voice.id)
 
 
 
# engine.endLoop()