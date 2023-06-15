import speech_recognition as sr
import pyttsx3
import datetime
import locale
import pyjokes

locale.setlocale(locale.LC_TIME, 'es_CL.UTF-8')

from os import system

def transformar_audio_en_texto():
    #alamacenar el recoginizer en una variable
    r = sr.Recognizer()

    # configurar el microfono
    with sr.Microphone() as source:
        system("clear")
        r.adjust_for_ambient_noise(source)
        r.pause_threshold = 0.8
        print("Ya puedes responder : ")
        audio = r.listen(source, timeout=2)

        print("capturando audio...")

        try :
            print("Cargando...")
            audio = r.recognize_google(audio,language='es-CL').lower()
            print("dijiste : "+ audio)

            if audio in ["fecha actual", "dime la fecha", "dime la fecha por favor"]:
                pedir_dia()
            elif audio in ["dime actual", "dime la hora", "dime la hora por favor"]:
                pedir_hora()
            elif audio in ["dime un chiste"]:
                joke = pyjokes.get_joke(language='es')
                responder(joke)
            else:
                responder("nada")


        except sr.UnknownValueError :
            print("No entendi")
            return "Sigo esperando"

        except sr.RequestError :
            #prueba de que no comprendio el audio
            print("No entendi, no hay servicio")
            #devolver error
            return "Sigo esperando"
        except sr.exceptions.WaitTimeoutError :
            print("Esperando demas ")
            return False
        except :
            print("algo salio mal")

def responder (mensaje) :

    engine = pyttsx3.init()
    engine.setProperty("rate", 135)
    engine.setProperty("voice", "spanish")
    engine.say(mensaje)
    engine.runAndWait()
    engine.stop()

def pedir_dia ():
    fecha_actual = datetime.date.today()
    print(fecha_actual)

    nombre_mes = fecha_actual.strftime("%B")
    numero_dia = fecha_actual.strftime("%d")
    nombre_dia = fecha_actual.strftime("%A")
    año = fecha_actual.strftime("%Y")
    print(nombre_dia)

    responder(f'hoy es {nombre_dia} {numero_dia} de {nombre_mes} de {año}')

def pedir_hora ():
    responder(datetime.datetime.now().strftime("%H %M"))

transformar_audio_en_texto()

