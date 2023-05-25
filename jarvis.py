import speech_recognition as sr
import pyttsx3

def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Dinliyorum...")
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)

        try:
            text = r.recognize_google(audio, language="en-EN") # Türkçe olarak tanıma yapmak için "tr-TR" kullanıyoruz
            print("Anlaşılan metin: ", text)
            return text
        except sr.UnknownValueError:
            print("Ses anlaşılamadı.")
        except sr.RequestError as e:
            print("Ses tanıma hizmetine erişilemedi; {0}".format(e))

def speak(text):
    engine = pyttsx3.init()
    engine.setProperty('rate', 150) # Konuşma hızı ayarlanabilir (isteğe bağlı)
    engine.setProperty('volume', 0.8) # Ses düzeyi ayarlanabilir (isteğe bağlı)
    engine.say(text)
    engine.runAndWait()

def assistant():
    while True:
        command = listen()
        if command == "stop":
            break
            
        if "hello" in command:
            response = "hi"
            speak(response)
        elif "what's up" in command:
            response = "I'm fine thanks how about you"
            speak(response)

        else:
            response = "Anladım. Komutunuz: " + command
            speak(response)

assistant()
